import pickle
import time
import streamlit as st

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
    
  