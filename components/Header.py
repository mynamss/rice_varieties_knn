import streamlit as st

def header():    
        # st.image('https://img.icons8.com/color-glass/100/grains-of-rice.png')
        st.set_page_config("RiceClassify", "🌾")
        
        st.markdown("<h1 style='text-align: center;'>RiceClassify</h1>", unsafe_allow_html=True)
        
        st.markdown('''
                <p style='text-align: justify;'>
                Hai 👋, Selamat Datang di <strong>RiceClassify!</strong>
                <i>Website</i> yang dapat membantumu mengklasifikasikan beras ke dalam 2 varietas (<i><strong>Cammeo</strong></i> dan <i><strong>Osmancik</strong></i>) dengan mudah. Untuk menggunakannya, caranya cukup mudah, ikuti tutorial berikut ini ya...<br>
                <ol>
                        <li>Untuk memulai, klik tombol <strong>Klasifikasi</strong> di bawah ini.
                        <li>Pada halaman <strong>Klasifikasi</strong>, <i>input</i> nilai setiap <i>form</i> sesuai rentang yang telah ditentukan.
                        <li>Terakhir, klik tombol <strong>Hasil Klasifikasi</strong> dan ... Simsalabim, Model akan mengolah inputanmu dan akan menunjukkan hasil klasifikasinya</li>
                </ol>
                </p>
                ''', 
                unsafe_allow_html=True
                )
        st.warning('''
                Cukup mudah bukan ? Selamat Mencoba✨
                '''
                )