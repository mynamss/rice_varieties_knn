import streamlit as st
import pandas as pd

# local module
from utils import loading_animation, validate_inputs

# def on_submit(**datas):
#   st.write("Submited", datas)

def form_input():
  # form
  with st.form(key="input_form"):
      col1, col2 = st.columns([1,1])
    
      with col1: 
          area =  st.number_input(
              "Area (px)",
              min_value=0.0, 
              value=None, 
              step=0.1, 
              format="%.8f", 
              placeholder="0.0",
          )
          
          perimeter =  st.number_input(
              "Perimeter (px)", 
              min_value=0.0, 
              value=None, 
              step=0.1, 
              format="%.8f", 
              placeholder="0.0",
          )
          
          major_axis =  st.number_input(
              "Major Axis (px)",
              min_value=0.0, 
              value=None, 
              step=0.1, 
              format="%.8f", 
              placeholder="0.0",
          )

      with col2:
          minor_axis =  st.number_input(
              "Minor Axis (px)",
              min_value=0.0, 
              value=None, 
              step=0.1, 
              format="%.8f", 
              placeholder="0.0",
          )

          eccentricity =  st.number_input(
              "Eccentricity (px)",
              min_value=0.0, 
              value=None, 
              step=0.1, 
              format="%.8f", 
              placeholder="0.0",
          )

          convex_area =  st.number_input(
              "Convex Area (px)",
              min_value=0.0, 
              value=None, 
              step=0.1, 
              format="%.8f", 
              placeholder="0.0",
          )

      extent =  st.number_input(
      "Extent (px)",
      min_value=0.0, 
      value=None, 
      step=0.1, 
      format="%.8f", 
      placeholder="0.0",
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