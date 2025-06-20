import  streamlit as st

import streamlit as st

# Dummy user database
users = {
    "admin": "admin123",
    "user1": "pass1",
    "user2": "pass2"
}

def main():
  

    st.sidebar.header("User Login")

    # Login form
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type='password')

    if st.sidebar.button("Login"):
        if username in users and users[username] == password:
            st.success(f"Welcome {username} 👋")
            st.write("You are successfully logged in!")
            # Add more content below after login
        else:
            st.error("Invalid username or password ❌")

if __name__ == "__main__":
    main()


st.title ("MUKUND AGRO SEEDS")

st.subheader("RANASAN")

name = st. text_input("ENTER NAME HARE: ") 
dname = st.text_input(" VILLAGE")
sname = st.text_input("DISTRICT")
classdeta = st.selectbox("HOW MANY YEARS TO CLOSE FARMING :", ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"])




button = st.button("SAVE")
if button : 
    st.markdown(f"""
                NAME : {name} 
                
               
                 VILLAGE : {dname} 
                
        
                DISTRICT : {sname}


                 FARMER : {classdeta}


                                    """)
# products_app.py
import streamlit as st

st.set_page_config(page_title="Pesticide Products", layout="wide")

products = [
    {"name": "PENDI", "price": 250, "image_url": ""},
    {"name": "THAIOFLOW", "price": 180, "image_url": "https://example.com/b.jpg"},
    {"name": "REJENTS", "price": 300, "image_url": "https://example.com/c.jpg"},
]

st.title("🌱 Pesticide Products")

cols = st.columns(3)
for col, p in zip(cols, products):
    with col:
        st.image(p["image_url"], width=200)
        st.subheader(p["name"])
        st.caption(f"Price: ₹{p['price']}")
        st.button("Add to cart", key=p["add now"])


import streamlit as st

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None: "C:\Users\Setu\Downloads\MUKUND AGRO.png"
    st.image(uploaded_file, caption=f"Uploaded: {uploaded_file.name}")






