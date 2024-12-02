#########################
## OpenAI in Streamlit ##
#########################

# Importing Libraries
import streamlit as st
from openai import OpenAI
import os

# Setting up OpenAI

# Mac terminal: export OPENAI_API_KEY=""
# Windows PS: setx OPENAI_API_KEY "your_api_key_here"
key = ''
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

client = OpenAI(api_key=key)

# Streamlit App

st.title('OpenAI Chef Assistant')

st.write("This app will generate for you a dish you'll love from a country of your choosing.")

# We will start with a side bar to ask the user for a genre

country = st.sidebar.selectbox(
    'Select a country:', 
    ['USA', 'Mexico', 'Germany', 'France', 'Italy', 'Japan', 'South Korea', 'India', 'Egypt', 'Russia']
)

# We will then ask the user for an artist

similar_dish = st.sidebar.text_input('What kind of food do you like?', 'dishes with tomatoes')

# Now we need a place to display the lyrics

lyrics = st.empty()

# Now we need a button to generate the lyrics

if st.sidebar.button('Generate Recipe'):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a master chef."},
            {
                "role": "user",
                "content": f"Generate the full recipe from the country of {country}. Make it similar to or include {similar_dish}."
            }
        ]
    )
    lyrics.write(completion.choices[0].message.content)

# Check it out: https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps#build-a-chatgpt-like-app