from os import path
import pandas as pd
from serpapi import GoogleSearch
import datetime
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import unidecode


# Set title
st.title("🔎 JobJob 🚀")
st.write("### Let's find your dream job ! Exciting, isn't it?")

st.sidebar.write("Enter your filters")

# Ask about request needed
search_term = unidecode.unidecode(
    st.sidebar.text_input("Job you're looking for :", "Data Analyst").lower()
)
search_location = unidecode.unidecode(
    st.sidebar.text_input(
        "Location you're looking for :", "Geneva, Switzerland"
    ).lower()
)
# Add 2 cols
left_col, right_col = st.sidebar.columns(2)

# Left side
domain_country = unidecode.unidecode(
    left_col.text_input("Country code :", "ch").lower()
)

# Right side
results_number = right_col.number_input(
    "Maximum results :", min_value=1, max_value=500, value=70
)

search_radius = st.sidebar.slider(
    "Maximum radius ( km ) :", min_value=1, max_value=500, value=20
)

words_toban = st.sidebar.text_input(
    'Techno to ban ( split by " , " ) :', "C,Go,JavaScript"
)

api_key = st.sidebar.text_input(
    "API key from SerpApi 🔑 :", "A1bcD23eF4ghij56APIKEYA1bcD23eF4ghij56"
)

# Passmode for developpers
if api_key == "ImJesus":
    api_key = open("../API keys/serpapi.txt", "r").read()

# Select only post of the day
today_post = st.sidebar.checkbox("Today's posts only")
agreed = "date_posted:today" if today_post else ""

# Select all techno to drop
banned_word = (
    []
    if words_toban in ["C,Go,JavaScript", ""]
    else words_toban.replace(" ", "").split(",")
)


# Run only if the button is clicked
if st.sidebar.button("Let's GO !"):

    # ---------------------------------------------
    # START SCRAPING PART

    # Create a text element and let the reader know the data is loading.
    data_load_state = st.text("Loading data...")

    # Scraping part
    for num in range(int(results_number / 10)):

        if num == 0:
            next_page_token = ""
        else:
            next_page_token = results.get("serpapi_pagination", {}).get(
                "next_page_token", ""
            )

        start = num
        params = {
            "api_key": api_key,
            "device": "desktop",
            "engine": "google_jobs",
            # "google_domain": "google.com",
            "q": search_term.lower(),  # Lowercase forced
            # "hl": "en", # Language parameter can return No result
            "gl": domain_country.lower(),  # Domain of country, Lowercase forced
            "lrad": search_radius,
            "location": search_location,
            "chips": agreed,
            "next_page_token": next_page_token,
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        # Check if the last search page (i.e., no results)
        try:
            if results["error"] == "Google hasn't returned any results for this query.":
                st.write(f"{results["error"]}")
                break

        except KeyError:
            # Create dataframe of 10 pulled results
            jobs = results["jobs_results"]
            jobs = pd.DataFrame(jobs)
            jobs = pd.concat(
                [pd.DataFrame(jobs), pd.json_normalize(jobs["detected_extensions"])],
                axis=1,
            )
            jobs["date_time"] = datetime.datetime.now(datetime.UTC).strftime(
                "%d-%m-%Y %H:%M"
            )  # Request time add

            # Concat dataframe
            if start == 0:
                jobs_all = jobs
            else:
                jobs_all = pd.concat([jobs_all, jobs])

            jobs_all["search_term"] = search_term
            jobs_all["search_location"] = search_location

        else:
            continue

    # END SCRAPING PART
    # ---------------------------------------------

    # If no results found, inform the reader
    try:
        if results["error"] == "Google hasn't returned any results for this query.":
            st.write("Change parameters.")

    # Elif there are some results, cleaning
    except KeyError:
        # Notify the reader that the data was successfully loaded
        data_load_state.text("Success: Data Loaded!")

        # ---------------------------------------------
        # START of CLEANING PART

        # Drop the useless columns
        to_drop = [
            "detected_extensions",
            "extensions",
            "apply_options",
            "job_id",
            "thumbnail",
            "search_term",
            "search_location",
        ]

        # Looking if each col exist, then delete
        for col in to_drop:
            if col in jobs_all.columns:
                jobs_all.drop(columns=[col], inplace=True)

        # Drop the duplicates offers
        jobs_all.drop_duplicates(subset="description", inplace=True)

        # Drop offers with specifics words (technology)
        def find_words(sentence, words):
            """
            Input : sentence and list of words banned
            Output : True or False check
            Do : normalize text and compare each word of the sentence with the words banned
            """
            for word in words:
                if word.lower() in sentence.lower():
                    return False
                else:
                    return True

        # Count of total rows (with banned_words filter)
        total_rows = jobs_all.shape[0]

        # Filter the offers with banned words
        if banned_word != []:
            jobs_all = jobs_all[
                jobs_all["description"].apply(lambda a: find_words(a, banned_word))
            ]

        # Count of filtred rows (without banned_words)
        rows_deleted = total_rows - jobs_all.shape[0]

        # END of CLEANING PART
        # ---------------------------------------------

        # Notify the data was successfully loaded
        data_load_state.text("Success: Data Loaded!")

        # Notify the rows keeped
        st.write(
            f"Total row(s) : {jobs_all.shape[0]}. Deleted row(s) due to banned words selected : {rows_deleted}."
        )

        # Show the dataframe
        st.dataframe(jobs_all)

        # Show stats from graph
        fig = px.histogram(jobs_all, x="location", color="via")
        st.plotly_chart(fig)

    try:
        st.dataframe(jobs_all)
    except:
        data_load_state.text("Can't run : Check your API key 🔑")
