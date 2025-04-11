import streamlit as st
import requests

# API Endpoint
API_URL = "api url"

st.title("Named Entity Recognition (NER) API Demo")
st.write("Enter a sentence and see the extracted named entities!")

# Text input
user_input = st.text_area("Enter text here:", "Apple is looking at buying U.K. startup for $1 billion.")

if st.button("Analyze"):
    if len(user_input) > 1000:
        st.error("Text is too long, please make it less than 1000 charchtars")
    else:

        if user_input.strip():
            # Send request to API
            response = requests.post(API_URL, json={"text": user_input})
            if response.status_code == 200:
                entities = response.json().get("entities", [])
                if entities:
                    st.subheader("Named Entities:")
                    for entity in entities:
                        st.write(f"**{entity['text']}** ({entity['label']})")
                else:
                    st.write("No named entities found.")
            else:
                st.error("Error: Could not connect to API.")
        else:
            st.warning("Please enter some text.")

