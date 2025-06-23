import  streamlit as st


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


import streamlit as st

# Page configuration
st.set_page_config(page_title="Product Page", layout="centered")

# Product Information
product = {
    "name": "pendi " ,
    "price": 250 ,
    "description": 

    "image_url": "https://via.placeholder.com/300x200.png?text=Wireless+Headphones"
}

# Display product image
st.image(product["image_url"], use_column_width=True)

# Display product name and price
st.title(product["name"])
st.subheader(f"{product['price']}")

# Product description
st.write(product["description"])

# Buy Now button
if st.button("🛒 Buy Now"):
    st.success("Thank you for your purchase! (This is a mock action.)")






