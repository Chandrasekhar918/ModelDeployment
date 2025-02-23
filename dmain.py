from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel



app = FastAPI()


with open("C:/Users/bansekha/OneDrive - Capgemini/Desktop/ML Practice/Log_Reg.pkl",'rb') as file:
    model = pickle.load(file)

with open("C:/Users/bansekha/OneDrive - Capgemini/Desktop/ML Practice/scaler.pkl",'rb') as file2:
    scaler = pickle.load(file2)

# Define request body format
class InputData(BaseModel):
    age: int
    estimated_salary: float

# Define prediction endpoint
@app.post("/predict/")
def predict(data: InputData):
    # Convert input to NumPy array
    input_data = np.array([[data.age, data.estimated_salary]])

    # Apply scaling
    input_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(input_scaled)

    # Return response
    return {"prediction": int(prediction[0])}
