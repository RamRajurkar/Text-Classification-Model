import requests
import streamlit as st
import pandas as pd
import os

API_URL = "https://api-inference.huggingface.co/models/SamLowe/roberta-base-go_emotions"
headers = {"Authorization": os.getenv('API_KEY')}

st.write("## Welcome to Text Classification ML model !")
text = st.text_input("Enter the Text: ")
button_pressed = st.button("Submit")

if button_pressed:
    with st.spinner("Loading..."):
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": f"{text}",
        })

        # Check if the output is a list and not empty
        if isinstance(output, list) and output:
            st.subheader("Result: ")
            # Convert the output into a DataFrame
            df = pd.DataFrame(output[0], columns=['label', 'score'])
            st.dataframe(df)
        else:
            st.write("No results found")
