import pickle
import streamlit as st

model = pickle.load(open('estimasi_kalori_fastfood.sav', 'rb'))

st.title('Estimasi kalori berdasarkan jumlah fat')

cal_fat = st.number_input('Input kalori')
total_fat  = st.number_input('Input total fat')
sat_fat = st.number_input('Input sat fat')
trans_fat= st.number_input('Input trans fat')
cholesterol = st.number_input('Input kolesterol')
sodium = st.number_input('Input sodium')
total_carb = st.number_input('Input total carbon')
fiber = st.number_input('Input fiber')
sugar = st.number_input('Input gula')
protein = st.number_input('Input protein')
calcium = st.number_input('input kalsium')

prediksi = ''
if st.button('Estimasi kalori berdasarkan jumlah fat'):
    prediksi = model.predict(
        [[cal_fat, total_fat, sat_fat,trans_fat, cholesterol, sodium, total_carb, fiber, sugar,protein, calcium]]
    )
    st.write('Estimasi kalori berdasarkan jumlah fat : ', prediksi)