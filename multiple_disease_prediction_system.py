import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading all the trained models of the prediction problems
diabetes_disease_model = pickle.load(open('C:/Users/othma/Bureau/saved models/diabetes_disease_model.sav','rb'))
heart_disease_model = pickle.load(open('C:/Users/othma/Bureau/saved models/heart_disease_model.sav','rb'))
parkinson_disease_model = pickle.load(open('C:/Users/othma/Bureau/saved models/parkinson_disease_model.sav','rb'))

# Sidebar navigation
with st.sidebar:
    selected = option_menu(menu_title='Mulitple disease prediction system',
                           options=['Diabetes disease prediction',
                                    'Heart disease prediction',
                                    'Parkinson disease prediction'],
                           default_index=0,
                           icons=['activity', 'heart', 'person'])

# The diabetes disease prediction page
if selected == 'Diabetes disease prediction':
    # Giving a title to the page
    st.title('Diabetes disease prediction')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Pregnancies')
    with col2:
        Glucose = st.number_input('Glucose')
    with col3:
        BloodPressure = st.number_input('BloodPressure')

    with col1:
        SkinThickness = st.number_input('SkinThickness')
    with col2:
        Insulin = st.number_input('Insulin')
    with col3:
        BMI = st.number_input('BMI')

    with col1:
        DiabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction')
    with col2:
        Age = st.number_input('Age')

    # Code used for prediction
    diabetes_disease_diagnosis = ''
    if st.button('Diabetes disease Prediction result'):
        diabetes_disease_prediction = diabetes_disease_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if diabetes_disease_prediction[0] == 1:
            diabetes_disease_diagnosis = 'This person is diabetic!'
        else:
            diabetes_disease_diagnosis = 'This person is not diabetic!'
    st.success(diabetes_disease_diagnosis)

if selected == 'Heart disease prediction':
    # Giving a title to the heart disease prediction page
    st.title('Heart disease prediction')

    # Getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        age = st.number_input('Age')
    with col2:
        sex = st.number_input('Sex')
    with col3:
        cp = st.number_input('Cp')
    with col4:
        trestbps = st.number_input('Trestbps')

    with col1:
        chol = st.number_input('Chol')
    with col2:
        fbs = st.number_input('Fbs')
    with col3:
        restecg = st.number_input('Restecg')
    with col4:
        thalach = st.number_input('Thalach')

    with col1:
        exang = st.number_input('Exang')
    with col2:
        oldpeak = st.number_input('Oldpeak')
    with col3:
        slope = st.number_input('Slope')
    with col4:
        ca = st.number_input('Ca')

    with col1:
        thal = st.number_input('Thal')

    # code used for prediction
    heart_disease_diagnosis = ''
    if st.button('Heart disease prediction result'):
        heart_disease_prediction = heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if heart_disease_prediction[0] == 1:
            heart_disease_diagnosis = 'This person has a heart disease!'
        else:
            heart_disease_diagnosis = "This person hasn't a heart disease!"
    st.success(heart_disease_diagnosis)

if selected == 'Parkinson disease prediction':
    # Giving a title to the page
    st.title('Parkinson disease prediction')

    # Getting the input data from the user
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        name = st.number_input('name')
    with col2:
        fo = st.number_input('MDVP: Fo(Hz)')
    with col3:
        fhi = st.number_input('MDVP: Fhi(Hz')
    with col4:
        flo = st.number_input('MDVP: Flo(Hz)')
    with col5:
        jitter_percent = st.number_input('MDVP: Jitter( %)')

    with col1:
        jitter_abs = st.number_input('MDVP: Jitter(Abs)')
    with col2:
        ppq = st.number_input('MDVP: PPQ')
    with col3:
        ddp = st.number_input('Jitter: DDP')
    with col4:
        shimmer = st.number_input('MDVP: Shimmer')
    with col5:
        shimmer_db = st.number_input('MDVP: Shimmer(dB)')

    with col1:
        apq3 = st.number_input('Shimmer: APQ3')
    with col2:
        apq5 = st.number_input('Shimmer: APQ5')
    with col3:
        apq = st.number_input('MDVP: APQ')
    with col4:
        dda = st.number_input('Shimmer: DDA')
    with col5:
        nhr = st.number_input('NHR')

    with col1:
        hnr = st.number_input('HNR')
    with col2:
        rpde = st.number_input('RPDE')
    with col3:
        dfa = st.number_input('DFA')
    with col4:
        spread1 = st.number_input('spread1')
    with col5:
        spread2 = st.number_input('spread2')

    with col1:
        d2 = st.number_input('d2')
    with col2:
        ppe = st.number_input('PPE')

    ## code used for prediction
    parkinson_disease_diagnosis = ''
    if st.button('Parkinson disease prediction result'):
        parkinson_disease_prediction = parkinson_disease_model.predict([[name,fo,fhi,flo,jitter_percent,jitter_abs,ppq,ddp,shimmer,shimmer_db,apq3,apq5,apq,dda,nhr,hnr,rpde,dfa,spread1,spread2,d2,ppe]])
        if parkinson_disease_prediction[0] == 1:
            parkinson_disease_diagnosis = 'This person has a parkinson disease!'
        else:
            parkinson_disease_diagnosis = "This person hasn't a parkinson disease!"
    st.success(parkinson_disease_diagnosis)
