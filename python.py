import  streamlit as st
col11,col12= st.columns(2)
with col11:
      st.image("https://i.pinimg.com/736x/21/9a/c0/219ac0de0c997ac3b03cd2f7d75e6a50.jpg",width=150)


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

if st.button("complet your profile"):
    
    st.text_input("ENTER NAME HARE:")
    st.text_input("VILLAGE NAME") 
    st.text_input("TALUKA") 
    st.text_input("DISTRICT")
    st.text_input("STATE")
    st.selectbox("(HOW MANY YEARS TO CLOSE FARMING :", ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"])
    st.text_input("WHERE YOU BUY PESTICIDE")
    button = st.button("SAVE")
    st.success=(" TAHNKS FOR SHARE YOUR DITAILS")

   
 
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
    
col8,col9,col10 =st.columns(3)    


#PENDI
    
with col8 :
     with st.expander("PENDI PESISIDE INSTRUCTIONS") :
      st.write("""1.PENDI (30%EC)

 USES(વપરાશ )    (નિંદામણ નાશક)

(1) મગફરી , ઘઉં  , કપાસ ,સોયાબીન ,તુવેર  .

(2) વાવેતર પછી 2 દિવસ અંદર  છટકાવ  માટે  જમીન માં ભેજ હોય તે જરરી છે .

(4) એક પંપ (15 લીટર ) માં 80ml થી 100ml  """)   
      


 

#rejent


with col2 :
    st.header("REJENT")
    st.image("https://kissanemart.com/storage/bayer-regent-sc-insecticide-800x800.jpg",width=250)

with col9  :
 with st.expander("REJENT PESISIDE INSTRUCTIONS") :    
    st.write("""Regent insecticides contain fipronil, a phenylpyrazole compound known for its efficacy in controlling various difficult-to-kill pests, including:
Early shoot borer, stem borer, leaf folder, and termites in rice
Green leafhopper and other significant pests in sugarcane and wheat.
Fipronil works primarily through ingestion and contact, causing toxicity by disrupting the insect's nervous system """)


#BALCK AMRUT



with col3 :
    st.header("BLACK AMRUT")
    st.image("https://agribegri.com/productimage/18963318401729577015.webp",width=200)
    with col10 :
        with st.expander("BLACK AMRUT PESISIDE INSTRUCTION") :
            st.write("""It is a mixture of essential nutrients, soluble carbon and natural growth enhancers, made from Organic and Natural Extracts, which makes it safe and eco-friendly. It improves the production of crops via acting on all stages like Plant Growth, Fruiting, Flowering & Size Improvement.""")

            

   
   
   
  