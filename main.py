import streamlit as st
import langchain_helper
import random


st.title("🍽️Restaurant Name & Menu Generator")

cuisines = ["Italian","Middle Eastern","Japanese","Mexican","Indian","French","Chinese","Thai","Turkish","Greek","Surprise me!"]
cuisine = st.sidebar.selectbox("🍲 Pick a cuisine", cuisines)

if cuisine == "Surprise me!":
    cuisine = random.choice(cuisines[:-1]) 

st.sidebar.write(f"✨ Selected Cuisine: **{cuisine}**")

if st.sidebar.button("Generate Restaurant"):
    with st.spinner("Cooking up some ideas... 🍳"):
        response = langchain_helper.generate_restauant_name_and_items(cuisine)

    st.subheader(f"🏪 Restaurant Name: **{response['restaurant_name'].strip()}**")

    st.write("📜 **Menu Items**")
    menu_items = [item.strip() for item in response['menu'].split("\n") if item.strip()]

    for item in menu_items:
        st.markdown(f"- {item}")
