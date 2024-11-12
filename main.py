from typing import Optional
from models import LoginFeatures
from anomaly import detect_anomaly  
from fastapi import FastAPI,HTTPException

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Anomaly Detection API! Developed by Jemimah Twaki"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/predict/")
async def predict(features: LoginFeatures):
    try:
        # Preprocess the input features
        processed_features = features.preprocess()
        # Call the prediction function (ensure `detect_anomaly` uses the processed input)
        result = detect_anomaly(processed_features)
        return {"anomaly_detected": result["anomaly_detected"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)