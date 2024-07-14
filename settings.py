from pathlib import Path
import sys

# Get the absolute path of the current file
FILE = Path(__file__).resolve()
# Get the parent directory of the current file
ROOT = FILE.parent
# Add the root path to the sys.path list if it is not already there
if ROOT not in sys.path:
    sys.path.append(str(ROOT))
# Get the relative path of the root directory with respect to the current working directory
ROOT = ROOT.relative_to(Path.cwd())

# ML Model config
MODEL_DIR = ROOT/ 'model'
DETECTION_MODEL = MODEL_DIR / 'knn_best_model.pkl'
SCALER_MODEL = MODEL_DIR/ 'robust_scaler_model.pkl'

# Model Type
DETECTION = "KNN_MODEL"
SCALER = "ROBUST_MODEL"


COLUMNS = ["Area", "Perimeter", "Major_Axis_Length", "Minor_Axis_Length", "Eccentricity", "Convex_Area", "Extent"] 


