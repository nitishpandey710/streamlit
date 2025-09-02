import streamlit as st

# Title and headers
st.title("Hello Book App")
st.subheader("Powered with Streamlit")
st.text("Welcome to your First Interactive Book App")
st.write("Choose your favorite book to read:")

# Dropdown for book selection
book = st.selectbox(
    "Your Favorite Book:",
    ["The Alchemist", "1984", "To Kill a Mockingbird", "Pride and Prejudice", "Harry Potter"]
)

# Display the choice
st.write(f"You chose **{book}**. Great pick!")

# Success message
st.success("Your book is ready to read. Enjoy your journey!")
