import streamlit as st
import random

# Game categories and words
categories = {
    "Alphabet": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
    "Parts of the Body": ["Head", "Arm", "Leg", "Foot", "Hand", "Eye", "Ear", "Mouth", "Nose", "Knee"],
    "Animals": ["Cat", "Dog", "Elephant", "Lion", "Tiger", "Bear", "Giraffe", "Zebra", "Monkey", "Panda"],
    "Fruits": ["Apple", "Banana", "Orange", "Grapes", "Mango", "Cherry", "Peach", "Pineapple", "Strawberry", "Watermelon"],
    "Shapes": ["Circle", "Square", "Triangle", "Rectangle", "Oval", "Hexagon", "Pentagon", "Octagon", "Diamond", "Star"]
}

# Initialize game state
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question' not in st.session_state:
    st.session_state.question = ""
if 'category' not in st.session_state:
    st.session_state.category = ""

def new_question():
    """Generate a new question from a random category"""
    st.session_state.category = random.choice(list(categories.keys()))
    st.session_state.question = random.choice(categories[st.session_state.category])

def check_answer(user_answer):
    """Check if the user's answer is correct"""
    if user_answer.strip().lower() == st.session_state.question.lower():
        st.session_state.score += 1
        return True
    return False

# Set the page configuration
st.set_page_config(page_title="Letter Work Game", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f5;
        color: #333;
    }
    .sidebar .sidebar-content {
        background-color: #4a90e2;
        color: white;
    }
    .stButton>button {
        background-color: #5cb85c;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #4cae4c;
    }
    .stTextInput>div>input {
        border: 2px solid #4a90e2;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app layout
st.title("Letter Work Game for Kids")
st.sidebar.title("Categories")
st.sidebar.write("Select a category to start the game!")

# Select category
selected_category = st.sidebar.selectbox("Choose a category", list(categories.keys()))

if st.button("Start Game"):
    new_question()

# Display current question
if st.session_state.question:
    st.write(f"### Category: {st.session_state.category}")
    st.write(f"What is the word related to the letter: **{st.session_state.question[0]}**?")

    user_answer = st.text_input("Your Answer:")

    if st.button("Submit"):
        if check_answer(user_answer):
            st.success("Correct! 🎉")
        else:
            st.error(f"Wrong! The correct answer was: **{st.session_state.question}**")

    st.write(f"**Current Score: {st.session_state.score}**")

# Reset button
if st.button("Reset Game"):
    st.session_state.score = 0
    st.session_state.question = ""
    st.session_state.category = ""
    st.success("Game reset! Choose a category to start again.")
