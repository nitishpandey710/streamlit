import streamlit as st 

st.title("Nitish Book Poll App")

# Two columns for book options
col1, col2 = st.columns(2)

with col1:
   st.header("The Alchemist")
   st.image("https://m.media-amazon.com/images/I/71aFt4+OTOL.jpg", width=120)
   vote1 = st.button("Vote The Alchemist")
   
with col2:
   st.header("1984")
   st.image("https://m.media-amazon.com/images/I/71kxa1-0mfL.jpg", width=120)
   vote2 = st.button("Vote 1984")

# Voting result
if vote1:
   st.success("Thanks for voting *The Alchemist*!")
elif vote2:
   st.success("Thanks for voting *1984*!")

# Sidebar
name = st.sidebar.text_input("Enter Your Name")
book = st.sidebar.selectbox("Choose your Favorite Book", 
                            ["The Alchemist", "1984", "Harry Potter", "Pride and Prejudice"])

if name:
    st.write(f" Welcome {name}, your favorite book is **{book}**!")

# Expander for book reading tips
with st.expander("Show Reading Tips"):
     st.write("""
     1. Find a quiet place to read.  
     2. Keep a notebook for thoughts and quotes.  
     3. Read at least 20 minutes daily.  
     """)

# Markdown styling
st.markdown("### Welcome to the Book App ")
st.markdown("> *A reader lives a thousand lives before he dies.*")
