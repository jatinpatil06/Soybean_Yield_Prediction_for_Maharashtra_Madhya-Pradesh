from fastapi import FastAPI, HTTPException
from .schemas import YieldInput
from .predict import predict_yield
import logging
logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title = "Soybean Yield Prediction API"
)

@app.get("/")
def health():
    return {"status" : "App is running fine"}

@app.post("/predict")
def predict_yield_route(input : YieldInput):
    try:
        prediction = predict_yield(input.dict())
        return {"predicted_yield" : float(prediction)} 
    except Exception as e:
        raise HTTPException(status_code=400, detail= str(e))