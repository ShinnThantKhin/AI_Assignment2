import streamlit as st
import joblib

#load model
model = joblib.load('model.pkl')

#streamlit app
st.title('What would be your Credit Score Level?')

name = st.text_input('Enter your name','')

age = st.number_input('Enter your age', min_value=0, max_value=100, value=20, step=1)

Gender = st.radio("Select your Gender", ("Male", "Female"))
if Gender=="Male":
    gender=0
else:
    gender=1
        
education = st.radio("Select your Education Status",("Bachelor's Degree", "Master's Degree", "Doctorate", "High School Diploma",  "Associate's Degree"))
if education == "Bachelor's Degree":
    edu=1
elif education=="Master's Degree":
    edu=2
elif education == "Doctorate":
    edu=3
elif education == "High School Diploma":
    edu=4
else:
    edu=5
        
income = st.number_input('Enter your income', min_value=0, max_value=99999999999, value=100000, step=1)

marital = st.radio("Select your Marital Status",("Single","Married"))
if marital == "Single":
    m = 0
else:
    m = 1
        
children = st.number_input("Enter number of children you have", min_value=0, max_value=15, value=0, step=1)

house = st.radio("Select your Home Ownership", ("Owned","Rented"))
if house == "Owned":
    own=1
else:
    own=0
    
btn = st.button("GO")
if btn:
    data=[age,gender,income,edu,m,children,own]
    result=model.predict([data])
    
    if result==1:
        st.success(f"**{name}, Your Credit Score is High!**")
    elif result==2:
        st.success(f"**{name}, Your Credit Score is Average!**")
    else:
        st.success(f"**{name}, Your Credit Score is Low!**")
        
        
        

    







