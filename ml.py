import pandas as pd
import streamlit as st
def hobby():
    st.write("Rating my Hobbies")
    df = pd.DataFrame(
    [
       {"Hobby": "Traveling", "Rating": 5, "Accepted?": True},
       {"Hobby": "Karaoke", "Rating": 5, "Accepted?": True},
       {"Hobby": "Fishing", "Rating": 5, "Accepted?": True},
    ]
    )
    edited_df = st.data_editor(df)

    best_hobby = edited_df.loc[edited_df["Rating"].idxmax()]["Hobby"]
    st.markdown(f"My best hobby is **{best_hobby}**.")