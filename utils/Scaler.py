from pathlib import Path

# local module
from .Helper import load_model
import settings

model_path = Path(settings.SCALER_MODEL)

def robust_scaler_transform(data):
    
    robust_model = load_model(model_path)
    
    scaled_data = robust_model.transform(data)

    return scaled_data