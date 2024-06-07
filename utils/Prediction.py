from pathlib import Path
import pandas as pd
import streamlit as st
import numpy as np

# local module
from .Helper import load_model
import settings

model_path = Path(settings.DETECTION_MODEL)

def knn_classify(data):
    data_df = np.array(data)
    
    knn_model = load_model(model_path)
    
    # result
    result = knn_model.predict(data_df)
    
    return result