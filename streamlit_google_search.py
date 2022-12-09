# Import necessary libraries
import streamlit as st
from gtts import gTTS
from pygame import mixer
import speech_recognition as sr
import webbrowser

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
