import streamlit as st

# Set title
st.image("https://ygdata.ch/portfolio-details-pages/media/JobJob.png", width=100)
st.title("JobJob !")

st.divider()

st.markdown(
    """
    - version : 0.8  
    - public : all  
    - API used : Google Jobs API + Locations API from Serpapi
    """
)
st.markdown(
    """
    ### ✨ Future:  
    - Add location suggest  
    - I'd like to use a generic API key to simplify access to the app. But this isn't free.
    """
)


st.markdown(
    """
    ### 🤝 Contributing  
    Contributions are welcome! Please create a pull request or open an issue for any improvements or bug fixes.
    """
)


st.markdown(
    """
    ### 📜 License  
    This project is licensed under the MIT License. See the [Github repo file](https://github.com/Yohan-GRNR/Job-Seeker) for details.
    """
)
