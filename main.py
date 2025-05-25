from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/predict")
def predict(
    feature1: float = Form(...),
    feature2: float = Form(...)
):
    prediction = feature1 + feature2
    return {"prediction": prediction}
