"""This code uses several libraries to implement a voice search feature. When the voice_search() function is called, it listens for the user's voice input using a microphone, and then tries to recognize the input and convert it to text using the recognize_google() method from the speech_recognition library.

If the recognition is successful, the voice_search() function opens a new tab in the default web browser and performs a search for the specified text using the webbrowser.open_new_tab() method. If the recognition fails, the function plays an error message using the gTTS and mixer libraries.

The process_input() function tokenizes the user's input using the AutoTokenizer class from the transformers library, and then uses the pre-trained AutoModelWithLMHead class to generate a response to the user's input.

The text_input() function simply gets the user's input using a text input field, and then opens a new tab in the default web browser to search for the specified text."""

# Import necessary libraries
import streamlit as st
from gtts import gTTS
from pygame import mixer
import speech_recognition as sr
import webbrowser


from transformers import AutoModelWithLMHead, AutoTokenizer

# Load the pre-trained NLP model and tokenizer
model = AutoModelWithLMHead.from_pretrained("bert-base-uncased")
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Set up the recognition object
r = sr.Recognizer()

# Define the function that handles the voice search
def voice_search():
  with sr.Microphone() as source:
    # Listen for the user's voice
    audio = r.listen(source)

    # Try to recognize the user's voice and convert it to text
    try:
      text = r.recognize_google(audio)

      # Open a new tab in the default web browser and search for the specified text
      webbrowser.open_new_tab(f"https://www.google.com/search?q={text}")
    except:
      # If the recognition failed, play an error message
      error_message = gTTS("Sorry, I didn't understand that. Please try again.")
      mixer.init()
      mixer.music.load(error_message)
      mixer.music.play()
 
# Define a function that processes the user's input and provides a response
def process_input(input_text):
  # Tokenize the input text
  input_tokens = tokenizer.tokenize(input_text)

  # Use the pre-trained NLP model to generate a response
  response_tokens = model.generate(input_tokens, max_length=64, do_sample=True)


# Define a function that handles the text input
def text_input():
  # Get the user's input
  text = st.text_input("Enter your search query:")

  # Open a new tab in the default web browser and search for the specified text
  webbrowser.open_new_tab(f"https://www.google.com/search?q={text}")

# Set up the streamlit app
st.title("Voice Search App")
st.write("Press the button below and say the word or phrase you want to search for on Google, or enter it directly into the text box.")

# Add a button that the user can click to start the voice search
if st.button("Start Voice Search"):
  voice_search()

# Add a text input field that the user can use to enter their search query directly
st.text_input("Enter your search query:")

# Add a button that the user can click to start the text search
if st.button("Start Text Search"):
  text_input()

# Add a checkbox that the user can use to toggle between different search engines
search_engine = st.sidebar.selectbox("Select search engine:", ["Google", "Bing", "DuckDuckGo"])
if search_engine == "Google":
  search_engine_url = "https://www.google.com/search?q="
elif search_engine == "Bing":
  search_engine_url = "https://www.bing.com/search?q="
else:
  search_engine_url = "https://duckduckgo.com/?q="

# Modify the voice_search() and text_input() functions to use the selected search engine
def voice_search():
  with sr.Microphone() as source:
    # Listen for the user's voice
    audio = r.listen(source)

    # Try to recognize the user's voice and convert it to text
    try:
      text = r.recognize_google(audio)

        # Open a new tab in the default web browser and search for the specified text
      webbrowser.open_new_tab(f"{search_engine_url}{text}")
    except:
      # If the recognition failed, play an error message
      error_message = gTTS("Sorry, I didn't understand that. Please try again.")
      mixer.init()
      mixer.music.load(error_message)
      mixer.music.play()

    def text_input():
      # Get the user's input
      text = st.text_input("Enter your search query:")

      # Open a new tab in the default web browser and search for the specified text
      webbrowser.open_new_tab(f"{search_engine_url}{text}")
