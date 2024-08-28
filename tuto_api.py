import streamlit as st

st.image("https://ygdata.ch/portfolio-details-pages/media/JobJob.png", width = 100)
st.title("JobJob !")

st.divider()

st.markdown("#### Elevate your job search experience with this interactive app !")

st.divider()

st.markdown("### Get your API key 🔑 :  [SerpApi.com](https://serpapi.com/)")

row1_left, row1_right = st.columns(2)
row2_left, row2_right = st.columns(2)
row3_left, row3_right = st.columns(2)
row4_left, row4_right = st.columns(2)

row1_left.container(height=200).markdown("1. Create an account")
row1_right.container(height=200).image("media/API_step_1.jpg")

row2_left.container(height=200).markdown("2. Select **Api Key** on left tab")
row2_right.container(height=200).image("media/API_step_2.jpg")

row3_left.container(height=200).markdown("3. Copy to the clipboard")
row3_right.container(height=200).image("media/API_step_3.jpg")

row4_left.container(height=200).markdown(
    """4. Go to **Get your job 🚀** and past
    
    **Enjoy 100 free requests !**"""
)

row4_right.container(height=200).image("media/API_step_4.jpg")
