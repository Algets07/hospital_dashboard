from fastapi import FastAPI
import pandas as pd
from database import engine

app = FastAPI()

@app.get("/kpi/alos")
def average_length_of_stay():
    query = """
    SELECT AVG(DATEDIFF(discharge_date, admit_date)) AS alos
    FROM admissions
    WHERE discharge_date IS NOT NULL
    """
    df = pd.read_sql(query, engine)
    return {"Average_Length_of_Stay": round(df.iloc[0]["alos"], 2)}

@app.get("/kpi/bed-occupancy")
def bed_occupancy():
    query = """
    SELECT department, COUNT(*) AS admitted
    FROM admissions
    WHERE discharge_date IS NULL
    GROUP BY department
    """
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")

@app.get("/kpi/readmission-rate")
def readmission_rate():
    query = """
    SELECT 
    (COUNT(*) / (SELECT COUNT(*) FROM admissions)) * 100 AS rate
    FROM admissions
    WHERE outcome = 'Readmitted'
    """
    df = pd.read_sql(query, engine)
    return {"Readmission_Rate_%": round(df.iloc[0]["rate"], 2)}

@app.get("/kpi/doctor-utilization")
def doctor_utilization():
    query = """
    SELECT doctor_id,
    (booked_hours / total_hours) * 100 AS utilization
    FROM doctors
    """
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")
