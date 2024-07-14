import streamlit as st
from settings import COLUMNS
from  utils import load_range

RANGE, df_range = load_range()

def header():    
        # st.image('https://img.icons8.com/color-glass/100/grains-of-rice.png')
        st.set_page_config("RiceClassify", "🌾")
        
        st.markdown("<h1 style='text-align: center;'>RiceClassify</h1>", unsafe_allow_html=True)
        
        st.markdown('''
                <p style='text-align: justify;'>
                Hai 👋, Selamat Datang di <strong>RiceClassify!</strong>
                <i>Website</i> yang dapat membantumu mengklasifikasikan beras ke dalam 2 varietas (<i><strong>Cammeo</strong></i> dan <i><strong>Osmancik</strong></i>) dengan mudah. Untuk menggunakannya, caranya cukup mudah, ikuti tutorial berikut ini ya...<br>
                <ol>
                        <li>Untuk mulai, klik tombol <strong>Klasifikasi</strong> di bawah ini.
                        <li>Di halaman <strong>Klasifikasi</strong>, <i>input</i> nilai setiap <i>form</i> sesuai rentang yang telah ditentukan.
                        <li>Terakhir, klik tombol <strong>'Hasil Klasifikasi'</strong> dan ... Simsalabim, Model akan mengolah inputanmu dan akan menunjukkan hasil klasifikasinya</li>
                        <li>Oya, pastikan inputanmu satuannya piksel 📐 dan rentangnya sesuai tabel di bawah ini ya 😉 </li>
                </ol>
                </p>
                ''', 
                unsafe_allow_html=True
                )
        
        st.table(df_range)
        st.warning('''
                Cukup mudah bukan ? Selamat Mencoba✨
                '''
                )