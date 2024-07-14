import pickle
import time
import streamlit as st
import os
from dotenv import load_dotenv
import pandas as pd

def load_model(model_path):
    """
    Loads a ML, Scaler, etc Model from the specified model_path.

    Parameters:
        model_path (str): The path to the ML model file.

    Returns:
        ML Object detection model.
    """
    
    model = pickle.load(open(model_path, 'rb'))
    return model


def loading_animation():
    start_load = st.empty()
    start_load.text('Starting a classification...')

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Predict {i+1}%')
        bar.progress(i + 1)
        time.sleep(0.02)
  
    start_load.empty()
    # latest_iteration.empty()
    
def load_range():
    
    load_dotenv()
    
    def parse_range(min_key, max_key):
        return float(os.getenv(min_key)), float(os.getenv(max_key))
    
    RANGE = {
        'Area': parse_range('AREA_MIN', 'AREA_MAX'),
        'Perimeter': parse_range('PERIMETER_MIN', 'PERIMETER_MAX'),
        'Major Axis Length': parse_range('MAJOR_AXIS_LENGTH_MIN', 'MAJOR_AXIS_LENGTH_MAX'),
        'Minor Axis Length': parse_range('MINOR_AXIS_LENGTH_MIN', 'MINOR_AXIS_LENGTH_MAX'),
        'Eccentricity': parse_range('ECCENTRICITY_MIN', 'ECCENTRICITY_MAX'),
        'Convex Area': parse_range('CONVEX_AREA_MIN', 'CONVEX_AREA_MAX'),
        'Extent': parse_range('EXTENT_MIN', 'EXTENT_MAX')
    }
    
    # create DataFrame
    data = [(key, value[0], value[1]) for key, value in RANGE.items()]
    df_range = pd.DataFrame(data, columns=["Input Form", "Min (px)", "Max (px)"])

    return RANGE, df_range
