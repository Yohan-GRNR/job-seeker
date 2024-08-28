import streamlit as st

tuto_api_page = st.Page(
    "tuto_api.py", title="Get your API key 🔑", icon=":material/looks_one:"
)
app_page = st.Page(
    "job-seeker-streamlit.py", title="Get your job 🚀", icon=":material/looks_two:"
)
about_page = st.Page("about.py", title="About the app 📚", icon=":material/looks_3:")

pg = st.navigation([tuto_api_page, app_page, about_page])
st.set_page_config(
    page_title="🔎 JobJob 🚀",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://github.com/Yohan-GRNR/Job-Seeker",
        "Report a bug": "https://www.linkedin.com/in/yohan-grenier/",
        "About": "# Let's find my dream job ! Exciting, isn't it?",
    },
)
pg.run()
