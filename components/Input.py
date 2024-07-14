import streamlit as st
import pandas as pd

# local module
from utils import loading_animation, validate_inputs, load_range

def form_input():
    
    # Get range input  
    RANGE, df_range = load_range()
    
    # form
    with st.form(key="input_form"):
        col1, col2 = st.columns([1,1])
        
        with col1: 
            area =  st.number_input(
                "Area (px)",
                min_value= RANGE['Area'][0], 
                max_value= RANGE['Area'][1],
                value=None, 
                step=0.1, 
                format="%.8f", 
                placeholder=f"{RANGE['Area'][0]} - {RANGE['Area'][1]}",
            )
            
            perimeter =  st.number_input(
                "Perimeter (px)", 
                min_value= RANGE["Perimeter"][0], 
                max_value= RANGE["Perimeter"][1],
                value=None, 
                step=0.1, 
                format="%.8f", 
                placeholder=f"{RANGE['Perimeter'][0]} - {RANGE['Perimeter'][1]}",
            )
            
            major_axis =  st.number_input(
                "Major Axis (px)",
                min_value= RANGE["Major Axis Length"][0], 
                max_value= RANGE["Major Axis Length"][1],
                value=None, 
                step=0.1, 
                format="%.8f", 
                placeholder=f"{RANGE['Major Axis Length'][0]} - {RANGE['Major Axis Length'][1]}",
            )

        with col2:
            minor_axis =  st.number_input(
                "Minor Axis (px)",
                min_value= RANGE["Minor Axis Length"][0], 
                max_value= RANGE["Minor Axis Length"][1], 
                value=None, 
                step=0.1, 
                format="%.8f", 
                placeholder=f"{RANGE['Minor Axis Length'][0]} - {RANGE['Minor Axis Length'][1]}",
            )

            eccentricity =  st.number_input(
                "Eccentricity (px)",
                min_value= RANGE["Eccentricity"][0], 
                max_value= RANGE["Eccentricity"][1], 
                value=None, 
                step=0.1, 
                format="%.8f", 
                placeholder=f"{RANGE['Eccentricity'][0]} - {RANGE['Eccentricity'][1]}",
            )

            convex_area =  st.number_input(
                "Convex Area (px)",
                min_value= RANGE["Convex Area"][0], 
                max_value= RANGE["Convex Area"][1], 
                value=None, 
                step=0.1, 
                format="%.8f", 
                placeholder=f"{RANGE['Convex Area'][0]} - {RANGE['Convex Area'][1]}",
            )

        extent =  st.number_input(
        "Extent (px)",
        min_value= RANGE["Extent"][0], 
        max_value= RANGE["Extent"][1], 
        value=None, 
        step=0.1, 
        format="%.8f", 
        placeholder=f"{RANGE['Extent'][0]} - {RANGE['Extent'][1]}",
        )
        
        submit_button = st.form_submit_button(
            label="Hasil Klasifikasi", 
            type="primary",
        )
        
        form_df = None
        if submit_button:
            is_valid, warning_message = validate_inputs(area, perimeter, major_axis, minor_axis, eccentricity, convex_area, extent)
            
            if is_valid:
                loading_animation()

                raw_data = {
                    "Area": area,
                    "Perimeter": perimeter,
                    "Major_Axis_Length": major_axis,
                    "Minor_Axis_Length": minor_axis,
                    "Eccentricity": eccentricity,
                    "Convex_Area": convex_area,
                    "Extent": extent
                    }
                
                # convert input to DF
                form_df = pd.DataFrame([raw_data])
                
            else :
                st.warning(warning_message)
                
    return form_df