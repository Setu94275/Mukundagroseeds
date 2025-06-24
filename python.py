import  streamlit as st


# Dummy user database
users = {
    "admin": "admin123",
    "user1": "pass1",
    "user2": "pass2"
}

def main():
    st.button("login now")
    
    
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
col4,col5 = st.columns(2)
with col4 :
    st.text_input("ENTER NAME HARE: ")

with col5 :
    st.text_input("VILLAGE NAME")    

col6,col7 =st.columns(2)


with col6 :
    st.text_input("TALUKA")

with col7:
    st.text_input("DISTRICT")

with col6 :
    st.text_input("STATE")    



classdeta = st.selectbox("HOW MANY YEARS TO CLOSE FARMING :", ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"])


bname = st.text_input("where are you buy pestiside ")

button = st.button("SAVE")

st.success("Thank you for join mukund agro seeds")
   
 
st.write("pleas select pesicide")
    
import streamlit as st

pesticide = st.radio("Pick your pesticide:", ["PENDI", "THAIFLOW", "REJENT", "BLACK AMRUT","GLYPHOSET"])
st.write(f"Selected : {pesticide}")

st.button("conform now")




import streamlit as st
col1,col2,col3= st.columns(3)
with col1 :
    st.header("PENDI")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFRXQN6zeIjNntgBqXgVqeP74Aq5agpfp0pQ&s", width=200)
    
    
    col8,col9,col10 = st.columns(3)
with col8 :
     with st.expander("PENDI PESISIDE INSTRUCTIONS") :
      st.write("""1.PENDI (30%EC)

 USES(વપરાશ )    (નિંદામણ નાશક)

(1) મગફરી , ઘઉં  , કપાસ ,સોયાબીન ,તુવેર  .

(2) વાવેતર પછી 2 દિવસ અંદર  છટકાવ  માટે  જમીન માં ભેજ હોય તે જરરી છે .

(4) એક પંપ (15 લીટર ) માં 80ml થી 100ml  """)   

with col2 :
    st.header("REJENT")
    st.image("https://kissanemart.com/storage/bayer-regent-sc-insecticide-800x800.jpg",width=250)

with col9  :
 with st.expander("REJENT PESISIDE INSTRUCTIONS") :    
    st.write("""Regent insecticides contain fipronil, a phenylpyrazole compound known for its efficacy in controlling various difficult-to-kill pests, including:
Early shoot borer, stem borer, leaf folder, and termites in rice
Green leafhopper and other significant pests in sugarcane and wheat.
Fipronil works primarily through ingestion and contact, causing toxicity by disrupting the insect's nervous system """)

with col3 :
    st.header("BLACK AMRUT")
    st.image("https://agribegri.com/productimage/18963318401729577015.webp",width=200)
    with col10 :
        with st.expander("BLACK AMRUT PESISIDE INSTRUCTION") :
            st.write("""It is a mixture of essential nutrients, soluble carbon and natural growth enhancers, made from Organic and Natural Extracts, which makes it safe and eco-friendly. It improves the production of crops via acting on all stages like Plant Growth, Fruiting, Flowering & Size Improvement.""")
