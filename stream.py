import streamlit as st
import requests

st.title("student result prediction")
st.write("enter student details below:")
study_hours=st.number_input("study_hours", min_value=0.0)
attendance=st.number_input("Attendance(%)", min_value=0.0)
internal_marks=st.number_input("internal_marks", min_value=0.0)

if st.button("predict"):
    data={
        "study_hours": study_hours,
        "attendance": attendance,
        "internal_marks": internal_marks
    }
    response=requests.post(
        "http://127.0.0.1:8000/predict",
        json=data
    )
    if response.status_code==200:
        result=response.json()
        prediction=result["prediction"]
        confidence=result.get("confidence", None)
        if prediction==1:
            st.success("student is likely to pass")
        else:
            st.error("student is likely to fail")
        if confidence is not None:
            st.write(f"confidence:{round(confidence*100, 2)}%")
    else:
        st.error("error connecting to api")            

