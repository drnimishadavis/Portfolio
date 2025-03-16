import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os

# Load trained model and scaler
gb_model = joblib.load('gbmodel.pkl')
scaler = joblib.load('X_Scaled.pkl')  # Ensure you have a scaler saved

# Define feature columns based on dataset
feature_columns = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 'France', 'Germany', 'Spain', 'Female', 'Male', 'Mem__no__Products', 'Cred_Bal_Sal', 'Bal_sal', 'Tenure_Age', 'Age_Tenure_product']

def predict_classification(features):
    input_df = pd.DataFrame([features], columns=feature_columns)
    input_scaled = scaler.transform(input_df)
    prediction = gb_model.predict(input_scaled)
    return prediction[0]

def main():
    st.markdown(
        """
        <style>
        body {
            background-color: #F0F2F6;
            font-family: 'Arial', sans-serif;
        }
        .stButton button {
            background-color: #1877F2;
            color: white;
            border-radius: 10px;
            padding: 12px;
        }
        .stSuccess {
            background-color: #28a745;
            color: white;
            padding: 10px;
            border-radius: 5px;
        }
        .stWarning {
            background-color: #FFDD57;
            color: #9F6000;
            padding: 10px;
            border-radius: 5px;
        }
        </style>
        """, unsafe_allow_html=True
    )
    
    st.title("Customer Churn Prediction")
    
    col1, col2 = st.columns(2)
    
    with st.form(key='classification_form', clear_on_submit=True):
        with col1:
            CreditScore = st.number_input("Credit Score", min_value=0.0, max_value=1000.0)
            Age = st.number_input("Age", min_value=18.0, max_value=100.0)
            Tenure = st.number_input("Tenure", min_value=0.0, max_value=50.0)
            Balance = st.number_input("Balance", min_value=0.0, max_value=1000000.0)
            NumOfProducts = st.number_input("Number of Products", min_value=1, max_value=4)
            HasCrCard = st.radio("Has Credit Card", [0, 1])
        
        with col2:
            IsActiveMember = st.radio("Is Active Member", [0, 1])
            EstimatedSalary = st.number_input("Estimated Salary", min_value=0.0, max_value=1000000.0)
            France = st.radio("Is from France?", [0, 1])
            Germany = st.radio("Is from Germany?", [0, 1])
            Spain = st.radio("Is from Spain?", [0, 1])
            Female = st.radio("Is Female?", [0, 1])
            Male = st.radio("Is Male?", [0, 1])
        
        Mem_no_Products = NumOfProducts - 1
        Cred_Bal_Sal = CreditScore * Balance * EstimatedSalary
        Bal_sal = Balance * EstimatedSalary
        Tenure_Age = Tenure * Age
        Age_Tenure_product = Age * Tenure * NumOfProducts
        
        features = [CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, France, Germany, Spain, Female, Male, Mem_no_Products, Cred_Bal_Sal, Bal_sal, Tenure_Age, Age_Tenure_product]
        
        submit_button = st.form_submit_button(label="Predict")
    
    if submit_button:
        if any(v is None for v in features):
            st.warning("⚠️ Please fill in all input fields.")
        else:
            result = predict_classification(features)
            if result == 1:
                st.markdown(f"<div class='stWarning'>🚨 Customer Likely to Exit</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='stSuccess'>✅ Customer Likely to Stay</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()