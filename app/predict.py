import pandas as pd
from .model import load_model

model = load_model()

def predict_yield(data : dict) -> float:
    X = pd.DataFrame([data])
    X.rename(columns={
            "nitrogen": "Nitrogen(N)",
            "phosphorous": "Phosphorous(P)",
            "potassium": "Potassium(K)",
            "soil_type": "Soil Type",
            "soil_depth": "Soil Depth"
        }, inplace=True)
    prediction = model.predict(X)[0]
    return float(prediction)