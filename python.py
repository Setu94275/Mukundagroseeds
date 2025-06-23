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







