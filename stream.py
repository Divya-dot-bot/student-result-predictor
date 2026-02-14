import streamlit as st
import joblib
import pandas as pd
model = joblib.load("student_model.pk1")

st.title("Student Result Prediction")

st.write("Enter student details below:")

study_hours = st.number_input("Study Hours", min_value=0.0)
attendance = st.number_input("Attendance (%)", min_value=0.0)
internal_marks = st.number_input("Internal Marks", min_value=0.0)

if st.button("Predict"):

    input_df = pd.DataFrame([{
        "study_hours": study_hours,
        "attendance": attendance,
        "internal_marks": internal_marks
    }])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.success("Student is likely to PASS ✅")
    else:
        st.error("Student is likely to FAIL ❌")

    st.write(f"Confidence: {round(probability * 100, 2)}%")
            


