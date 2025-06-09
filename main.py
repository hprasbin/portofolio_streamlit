import streamlit as st

st.set_page_config(page_title = "My Portfolio")

st.title("My Portfolio")
st.header("Data Science Enthusiast")

st.sidebar.title ("Navigation")
page = st.sidebar.radio ("Pages", 
                         ["My Profile", "Project",
                          "Hobby", "Contact"])

if page == "My Profile":
    import profile
    profile.shows()
elif page == "Contact":
    import contact
    contact.contact()
elif page == "Project":
    import project
    project.project()
else:
    import ml
    ml.hobby()