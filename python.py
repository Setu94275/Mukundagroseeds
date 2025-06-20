import  streamlit as st

st.title ("MUKUND AGRO SEEDS")

st.subheader("RANASAN")

name = st. text_input("ENTER NAME HARE: ") 
dname = st.text_input(" VILLAGE")
sname = st.text_input("DISTRICT")
classdeta = st.selectbox("HOW MANY YEARS TO CLOSE FARMING :", ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"])


bname = st.text_input("where are you buy pestiside ")

button = st.button("SAVE")
if button : 
    st.markdown(f"""
                NAME : {name} 
                
               
                 VILLAGE : {dname} 
                
        
                DISTRICT : {sname}


                 FARMER : {classdeta}


                PESTICIDE : {bname}""")
    