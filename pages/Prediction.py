import streamlit as st
import pandas as pd
import joblib

st.title('Prediction')
# model = joblib.load('model.joblib')

if 'df' in st.session_state:
    if 'model' in st.session_state:
        model = st.session_state['model']
        st.write(model)
        df = st.session_state['df']
        target = 'rent amount (R$)'
        cols = df.drop(target, axis=1).columns
        x = pd.DataFrame(columns=cols)
        for col in cols:
            if pd.api.types.is_numeric_dtype(df[col]):
                x.loc[0, col] = st.sidebar.number_input(col, value=round(df[col].mean()), step=1)
            else:
                x.loc[0, col] = st.sidebar.selectbox(col, df[col].unique())
        st.write(x)
        y = model.predict(x)
        st.write(f'Predicted rent amount: {y[0]: .02f} R$')
    else:
        st.write('Model not found')
