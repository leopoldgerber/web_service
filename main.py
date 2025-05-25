import os
import numpy as np
import pandas as pd
from joblib import load
from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/predict")
def predict(
    feature1: float = Form(...),
    feature4: float = Form(...)
):
    return {"prediction": feature1 + feature4}


@app.post("/filter-by-client")
def filter_by_client(client_id: int = Form(...)):
    file_path = os.path.join("data", "dataset.xlsx")

    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        return {"error": "Файл не найден"}
    except Exception as e:
        return {"error": str(e)}

    if "client_id" not in df.columns:
        return {"error": "Нет колонки 'client_id'"}

    filtered = df[df["client_id"] == client_id]
    return {"client_id": client_id, "matching_rows": len(filtered)}


@app.post("/predict-model")
def predict_model(
    x1: float = Form(...),
    x2: float = Form(...)
):
    model_path = os.path.join("models", "model.joblib")

    try:
        model = load(model_path)
    except FileNotFoundError:
        return {"error": "Модель не найдена по пути models/model.joblib"}
    except Exception as e:
        return {"error": f"Ошибка загрузки модели: {str(e)}"}

    # Подготовка данных: сконвертировать в форму (1, 2)
    input_data = np.array([[x1, x2]])

    try:
        prediction = model.predict(input_data)
    except Exception as e:
        return {"error": f"Ошибка при предсказании: {str(e)}"}

    return {"prediction": float(prediction[0])}
