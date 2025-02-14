import os
import pickle  # pre-trained models to load
import streamlit as st  # For my web app
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks', layout='wide')

# Load models
diabetes_model = pickle.load(open(r"C:\Users\Admin\Desktop\ML Project\training_models\diabetes_model.sav", 'rb'))
heart_model = pickle.load(open(r"C:\Users\Admin\Desktop\ML Project\training_models\heart_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"C:\Users\Admin\Desktop\ML Project\training_models\parkinsons_model.sav", 'rb'))

# Display user name on top right
st.markdown("""
    <div style="position: absolute; top: 10px; right: 20px; font-size: 20px; font-weight: bold;">
        Mayank Mishra
    </div>
""", unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu('Prediction of disease outbreak system',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Disease Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input("Number of pregnancies:")
    with col2:
        Glucose = st.text_input("Glucose level:")
    with col3:
        Blood_pressure = st.text_input("Blood Pressure value:")
    with col1:
        Skin_thickness = st.text_input("Skin Thickness value:")
    with col2:
        Insulin = st.text_input("Insulin level:")
    with col3:
        BMI = st.text_input("BMI value:")
    with col1:
        Diabetes_pedigree_function = st.text_input("Diabetes Pedigree Function value:")
    with col2:
        Age = st.text_input("Age of the person:")

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [float(x) for x in [Pregnancies, Glucose, Blood_pressure, Skin_thickness, Insulin, BMI, Diabetes_pedigree_function, Age]]
        diab_prediction = diabetes_model.predict([user_input])
        diab_diagnosis = "The person is diabetic" if diab_prediction[0] == 1 else "The person is not diabetic"
    st.success(diab_diagnosis)

if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input("Age of the person:")
    with col2:
        sex = st.text_input("Gender of the person:")
    with col3:
        cp = st.text_input("Type of chest pain:")
    with col1:
        trestbps = st.text_input("Resting blood pressure:")
    with col2:
        chol = st.text_input("Cholesterol value:")
    with col3:
        fbs = st.text_input("Blood Sugar level:")
    with col1:
        restecg = st.text_input("Resting electrocardiographic results:")
    with col2:
        thalach = st.text_input("Highest heart rate:")
    with col3:
        exang = st.text_input("Exercise-induced Angina:")
    with col1:
        oldpeak = st.text_input("ST depression induced value:")
    with col2:
        slope = st.text_input("Slope of the peak:")
    with col3:
        ca = st.text_input("Number of major blood vessels:")
    with col1:
        thal = st.text_input("Thalassemia type:")

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [float(x) for x in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        heart_prediction = heart_model.predict([user_input])
        heart_diagnosis = "The person has heart disease." if heart_prediction[0] == 1 else "The person has no heart disease."
    st.success(heart_diagnosis)

if selected == 'Parkinsons Disease Prediction':
    st.title('Parkinsons Prediction using ML')
    col1, col2, col3 = st.columns(3)
    fields = ["Fo", "Fhi", "Flo", "Jitter_percent", "Jitter_abs", "RAP", "PPQ", "Jitter_DDP", "Shimmer", "Shimmer_dB",
              "APQ3", "APQ5", "APQ", "DDA", "NHR", "HNR", "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"]
    user_inputs = {}
    for i, field in enumerate(fields):
        with [col1, col2, col3][i % 3]:
            user_inputs[field] = st.text_input(field.replace("_", " ") + ":")

    parkin_diagnosis = ''
    if st.button('Parkinsons Disease Test Result'):
        user_input = [float(user_inputs[field]) for field in fields]
        parkin_prediction = parkinsons_model.predict([user_input])
        parkin_diagnosis = "The person has parkinsons" if parkin_prediction[0] == 1 else "The person does not have parkinsons"
    st.success(parkin_diagnosis)
