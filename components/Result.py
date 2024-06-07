import streamlit as st
import pandas as pd

# local
from settings import COLUMNS


def display_result(raw_data_df, scaled_data, result):
    rice_type = ''
    
    if result[0] == 0:
        rice_type = "Cammeo"
    else:
        rice_type = "Osmancik"
    
    with st.expander(label="Hasil Klasifikasi:", expanded=True):
        st.success(f'''Berdasarkan nilai yang kamu masukkan, hasil yang didapat adalah varietas beras ***{rice_type}***''')
        
        st.markdown("Input awal:")
        st.dataframe(raw_data_df)
        
        scaled_df = pd.DataFrame(data=scaled_data, columns=COLUMNS)
        
        st.markdown("Hasil scaling:")
        st.dataframe(scaled_df)