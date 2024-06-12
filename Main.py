import streamlit as st

# local module
from components import header

def main():
    
    # Header
    header()
    
    # split column
    col1, col2 = st.columns([0.4, 0.6])

    with col2:
            btn_classif = st.button("Klasifikasi", key="Hai")
            
    # author
    st.markdown('''
            <p style='text-align: center;'>🚀 Dibuat oleh <a href="https://www.github.com/mynamss">Nunung Ali Maulana</a></p>
            ''',
            unsafe_allow_html=True
            )
    
    if btn_classif:
        st.switch_page("pages/Classification.py")

    
# Run main()
if __name__ == '__main__':
    main()