import streamlit as st
import pandas as pd

# local module
from components import form_input, display_result
from utils import validate_inputs, loading_animation, robust_scaler_transform, knn_classify

# init
st.set_page_config("RiceClassify - Klasifikasi", "🌾")


def main():
    # condition flag
    page_loaded = False
    
    # title
    st.markdown('''
                <h1 style='text-align: center;'>Klasifikasi Varietas Beras Menggunakan Algoritma KNN</h1>
                ''',
                unsafe_allow_html=True
            )
    # split column
    col1, col2 = st.columns([0.6, 0.1])

    with col2:
            btn_home = st.button("⬅️ Home", key="home")
    
    if btn_home:
        st.switch_page("Main.py")    
    
    st.info('''
        ➡️ Masukkan nilai untuk setiap _form_ (satuan _pixel_)
        '''
    )
    
    # set flag to True
    page_loaded = True
    if page_loaded:
        # get dat from input
        form_df = form_input()
        
        if form_df is not None and not form_df.empty:
            # scaling
            scaled_data = robust_scaler_transform(form_df)
            
            # st.write(scaled_data)
                
            # classify    
            result = knn_classify(scaled_data)
                
            # show result 
            display_result(form_df, scaled_data, result)
        else: 
            st.empty()
            
    
if __name__ == "__main__":
    main()