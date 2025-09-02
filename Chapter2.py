import streamlit as st

st.title("Book Selector App")

# Button
if st.button("Get Book"):
    st.success("Your Book is being fetched")

# Checkbox
add_summary = st.checkbox("Need a Short Summary?")
if add_summary:
    st.write(" A short summary will be shown with your book.")

# Radio button
book_format = st.radio("Pick your Book Format:", ["Hardcover", "Paperback", "E-Book"])
st.write(f"Selected Format: **{book_format}**")

# Selectbox
genre = st.selectbox("Choose Genre:", ["Fiction", "Science", "History", "Fantasy"])
st.write(f"Selected Genre: **{genre}**")

# Slider
reading_time = st.slider("Reading Time (Hours per day)", 0, 10, 2)
st.write(f"Planned Reading Time: **{reading_time} hours/day**")

# Number input
books_count = st.number_input("How many books do you want to read this month?", min_value=1, max_value=20, step=1)
st.write(f"Selected Number of Books: **{books_count}**")

# Text input
name = st.text_input("Enter Your Name")
if name:
    st.write(f"Welcome, {name}! Your reading journey begins.")

# Date input
dob = st.date_input("Select your Date of Birth")
st.write(f"Your Date of Birth is: **{dob}**")
