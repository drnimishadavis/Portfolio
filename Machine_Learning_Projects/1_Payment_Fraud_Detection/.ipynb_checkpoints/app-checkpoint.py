import joblib
import pandas as pd
import numpy as np
import streamlit as st
import os

rf_model = joblib.load('randomforestmodel.pkl')
label_encoder = joblib.load('label_encoder.pkl')
scaler = joblib.load('X_Scaled.pkl')

type_mapping = {
    'PAYMENT': 0,
    'TRANSFER': 1,
    'CASH_OUT': 2,
    'DEBIT': 3,
    'CASH_IN': 4
}

reverse_type_mapping = {v: k for k, v in type_mapping.items()}

def predict_fraud(step, type_, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest):
    input_data = {
        'step': [step],
        'type': [type_],  
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest]
    }
    input_df = pd.DataFrame(input_data)

    input_df['type'] = input_df['type'].map(type_mapping)

    input_scaled = scaler.transform(input_df)

    prediction = rf_model.predict(input_scaled)

    transaction_type_label = reverse_type_mapping[input_df['type'][0]]

    if prediction[0] == 1:
        return f"🚨 Fraudulent Transaction Detected! Type: {transaction_type_label}."
    else:
        return f"✅ Transaction is Legitimate. Type: {transaction_type_label}."

def main():
    st.markdown(
        f"""
        <style>
        body {{
            background-color: #FFCCE5 !important;  /* Light rose background */
            color: #333333;
            font-family: 'Arial', sans-serif;
        }}
        
        .block-container {{
            background-color: rgba(255, 255, 255, 0.9);
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0px 15px 25px rgba(0, 0, 0, 0.1);
            width: 600px;
            margin: 0 auto;
            text-align: center;
        }}
        
        h1 {{
            font-size: 2rem;
            color: #333333;
            font-weight: bold;
        }}
        
        .stButton button {{
            background-color: #1877F2;
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            padding: 14px 0;
            cursor: pointer;
            width: 100%;
            transition: background-color 0.3s ease;
        }}
        
        .stButton button:hover {{
            background-color: #155db6;
        }}
        
        .stRadio label, .stNumberInput label {{
            color: #555555;
            font-weight: 600;
        }}
        
        .stSuccess {{
            background-color: #28a745;
            color: white;
            padding: 10px;
            font-weight: bold;
            border-radius: 5px;
        }}
        
        .stWarning {{
            background-color: #FFDD57;
            color: #9F6000;
            padding: 10px;
            font-weight: bold;
            border-radius: 5px;
        }}
        </style>
        """, unsafe_allow_html=True
    )
    
    st.title("Payment Fraud Detection")

    col1, col2 = st.columns([2, 2])

    with st.form(key='transaction_form', clear_on_submit=True):
        with col1:
            step = st.number_input("Step (1-9)", min_value=0.0, max_value=9.0, value=None, placeholder="Enter a value between 1-9")
            type_ = st.radio("Transaction Type", ['CASH_IN', 'CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER'])
            amount = st.number_input("Amount", min_value=0.0, max_value=1000000.0, value=None, placeholder="Enter the amount")
        
        with col2:
            oldbalanceOrg = st.number_input("Old Balance of Sender", min_value=0.0, max_value=1000000.0, value=None, placeholder="Enter the old balance for Sender")
            newbalanceOrig = st.number_input("New Balance of Sender", min_value=0.0, max_value=1000000.0, value=None, placeholder="Enter the new balance for Sender")
            oldbalanceDest = st.number_input("Old Balance of Recipient", min_value=0.0, max_value=1000000.0, value=None, placeholder="Enter the old balance for Recipient")
            newbalanceDest = st.number_input("New Balance of Recipient", min_value=0.0, max_value=1000000.0, value=None, placeholder="Enter the new balance for Recipient")

        submit_button = st.form_submit_button(label="Predict")

    if submit_button:
        if any([step is None or amount is None or oldbalanceOrg is None or newbalanceOrig is None or oldbalanceDest is None or newbalanceDest is None]):
            st.warning("⚠️ Please ensure all fields contain valid numeric values.")
        else:
            result = predict_fraud(step, type_, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest)
            
            if "Fraudulent" in result:
                st.markdown(f"<div class='stWarning'>{result}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='stSuccess'>{result}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
