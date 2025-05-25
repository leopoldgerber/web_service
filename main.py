from fastapi import FastAPI, Form
import pandas as pd
import os

app = FastAPI()


@app.post("/new")
def new(
    feature1: float = Form(...),
    feature2: float = Form(...)
):
    prediction = feature1 + feature2
    return {"prediction": prediction}


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
