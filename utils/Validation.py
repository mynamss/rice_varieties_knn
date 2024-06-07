import streamlit as st

# Fungsi untuk validasi input
def validate_inputs(area, perimeter, major_axis, minor_axis, eccentricity, convex_area, extent):
    # Daftar nama input yang kosong
    empty_fields = []
    warning_message = ""
    
    if not area:
        empty_fields.append("Area")
    if not perimeter:
        empty_fields.append("Perimeter")
    if not major_axis:
        empty_fields.append("Major Axis")
    if not minor_axis:
        empty_fields.append("Minor Axis")
    if not eccentricity:
        empty_fields.append("Eccentricity")
    if not convex_area:
        empty_fields.append("Convex Area")
    if not extent:
        empty_fields.append("Extent")
    
    # Jika ada input yang kosong
    if empty_fields:
        if len(empty_fields) == 1:
            # st.warning(f"{empty_fields[0]} tidak boleh kosong")
            warning_message = f"{empty_fields[0]} tidak boleh kosong"
        elif len(empty_fields) == 2:
            # st.warning(f"{empty_fields[0]} dan {empty_fields[1]} tidak boleh kosong")
            warning_message = f"{empty_fields[0]} dan {empty_fields[1]} tidak boleh kosong"
        else:
            # Menggabungkan semua nama input yang kosong dengan koma, kecuali yang terakhir dengan 'dan'
            warning_message = ', '.join(empty_fields[:-1]) + f", dan {empty_fields[-1]} tidak boleh kosong"
            # st.warning(warning_message)
        return False,  warning_message
    
    return True, warning_message