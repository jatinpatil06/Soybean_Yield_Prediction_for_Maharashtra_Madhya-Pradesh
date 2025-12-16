import joblib
def load_model():
    model = joblib.load(r"artifacts/soybean_yield_pipeline.joblib")
    return model