import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="CardioGuardian",
                   layout="wide",
                   page_icon="🧑‍⚕️")


# loading the saved model

heart_disease_model = pickle.load(open('saved_model/heart_disease_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Heart Disease Prediction System',

                           ['CardioGuardian'],
                           menu_icon='hospital-fill',
                           icons=['heart'],
                           default_index=0)



# Heart Disease Prediction Page
if selected == 'CardioGuardian':

    # page title
    st.title('CardioGuardian')

    col1, col2, col3 = st.columns(3)

    with col1:
#        age = st.text_input('Age')
        age = st.number_input("Age in years", min_value=0, max_value=120, value=30) 

    with col2:
 #       sex = st.text_input('Gender')
        gender_options= {"Male": 0, "Female": 1} 
        gender_options= {"Male": 0, "Female": 1} 
        sex = st.selectbox ("Gender", list (gender_options.keys()))
        gender = gender_options[sex]

    with col3:
#        cp = st.text_input('Chest Pain types')
        cp = st.number_input("Chest Pain types", min_value=0, max_value=3, value=2) 

    with col1:
#        trestbps = st.text_input('Resting Blood Pressure')
        trestbps = st.number_input("Resting Blood Pressure", min_value=0, max_value=200, value=120) 

    with col2:
#        chol = st.text_input('Serum Cholestoral in mg/dl')
        chol = st.number_input("Patient's Cholesterol Levels", min_value=0, max_value=500, value=245)

    with col3:
#        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        fbs = st.number_input("Fasting Blood Sugar", min_value=0, max_value=1, value=0) 

    with col1:
#        restecg = st.text_input('Resting Electrocardiographic results')
        restecg = st.number_input("Resting Electrocardiographic results", min_value=0, max_value=1, value=0) 

    with col2:
#        thalach = st.text_input('Maximum Heart Rate achieved')
        thalach = st.number_input("Maximum Heart Rate achieved", min_value=0, max_value=220, value=155)        

    with col3:
#        exang = st.text_input('Exercise Induced Angina')
        exang = st.number_input("Exercise Induced Angina", min_value=0, max_value=1, value=0)        

    with col1:
#        oldpeak = st.text_input('ST depression induced by exercise')
        oldpeak = st.number_input("ST depression induced by exercise", min_value=0, max_value=8, value=3)

    with col2:
#        slope = st.text_input('Slope of the peak exercise ST segment')
        slope = st.number_input("Slope of the peak exercise ST segment", min_value=0, max_value=3, value=1)

    with col3:
#        ca = st.text_input('Major vessels colored by flourosopy')
        ca = st.number_input("Major vessels colored by flourosopy", min_value=0, max_value=4, value=2)

    with col1:
#        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        thal = st.number_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect", min_value=0, max_value=4, value=2)

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [int(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having a heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

