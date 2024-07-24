import streamlit as st

def calculate_bmi(height, weight):
    bmi = round(weight / (height/100) ** 2, 2)
    return bmi

st.title("BMI Calculator")

height = st.number_input('Enter your height (cm)', value = 170.0)

weight = st.number_input('Enter your weight (kg)', value = 70.0)

calculate_but = st.button('Calculate BMI')

if calculate_but == True:
    bmi = calculate_bmi(height, weight)

    st.write(f'Your BMI: {bmi}')
    if bmi < 18.5:
        st.write('Underweight')
    elif 18.5 <= bmi < 24.9:
        st.write('Normal weight')
    elif 25 <= bmi < 29.9:
        st.write('Overweight')
    elif bmi >= 30:
        st.write('Obese')