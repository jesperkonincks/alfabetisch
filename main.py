import streamlit as st
import openai
import os
from PIL import Image

openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_blog_post(keywords):
    prompt = f"schrijf een zoekmachine geoptimaliseerde tekst voor een webpagina van circa 300 woorden met de volgende zoekwoorden: {', '.join(keywords)}"
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

image = Image.open("logo-slate.webp")

# Custom CSS
def custom_css():
    st.markdown(
        """
        <style>
            .title {
                font-family: 'Montserrat', sans-serif;
                font-weight: bold;
                font-size: 36px;
                color: #2c3e50;
            }
            .input-label {
                font-family: 'Montserrat', sans-serif;
                font-weight: bold;
                font-size: 16px;
                color: #2c3e50;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

st.image(image)
st.markdown("<p class='input-label'> Vul hier termen in waar de blog post over moet gaan. </p>", unsafe_allow_html=True)
user_input = st.text_input("Termen (Gescheiden met een komma)")
submit_button = st.button("Blog post maken")

if submit_button and user_input:
    keywords = [keyword.strip() for keyword in user_input.split(',')]
    blog_post = generate_blog_post(keywords)
    st.write("Gegenereerde blog post:")
    st.text_area("Bewerk jouw blog post:", value=blog_post, height=600)
else:
    st.write("Er zijn geen geldige termen ingevuld.")