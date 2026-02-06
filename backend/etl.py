import pandas as pd
from database import engine

def load_csv_to_db():
    patients = pd.read_csv("../data/patients.csv")
    admissions = pd.read_csv("../data/admissions.csv")
    doctors = pd.read_csv("../data/doctors.csv")
    billing = pd.read_csv("../data/billing.csv")

    patients.to_sql("patients", engine, if_exists="replace", index=False)
    admissions.to_sql("admissions", engine, if_exists="replace", index=False)
    doctors.to_sql("doctors", engine, if_exists="replace", index=False)
    billing.to_sql("billing", engine, if_exists="replace", index=False)
print("ETL Completed")
