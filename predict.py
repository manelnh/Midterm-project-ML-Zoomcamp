import pickle
from fastapi import FastAPI
from pydantic import BaseModel

with open("rf_model.bin", "rb") as f_in:
    dv, model = pickle.load(f_in)

class PatientData(BaseModel):
    age: int
    sex: str
    chestpaintype: str
    restingbp: int
    cholesterol: int
    fastingbs: int
    restingecg: str
    maxhr: int
    exerciseangina: str
    oldpeak: float
    st_slope: str

# Pydantic model for the outgoing prediction response
class PredictionResponse(BaseModel):
    heartdisease_probability: float
    heart_disease: bool

app = FastAPI()


@app.post("/predict", response_model=PredictionResponse)
async def predict(patient: PatientData) -> PredictionResponse:
        patient_dict = patient.dict()
        X = dv.transform([patient_dict])
        prob = model.predict_proba(X)[0, 1]
        heartdisease = prob >= 0.5
        return {
            "heartdisease_probability": float(prob),
            "heart_disease": bool(heartdisease) }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}      