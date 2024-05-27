import pandas as pd
from models import CompanyRecord

CSV_FILE = 'company_records.csv'

def initialize_database():
    try:
        pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["name", "role", "package", "shortlisted", "given_interview", "final_result"])
        df.to_csv(CSV_FILE, index=False)

def add_record(record: CompanyRecord):
    df = pd.read_csv(CSV_FILE)
    df = df.append(record.to_dict(), ignore_index=True)
    df.to_csv(CSV_FILE, index=False)

def get_records():
    df = pd.read_csv(CSV_FILE)
    return df

def update_record(name, updated_record: CompanyRecord):
    df = pd.read_csv(CSV_FILE)
    df.loc[df['name'] == name, :] = pd.Series(updated_record.to_dict())
    df.to_csv(CSV_FILE, index=False)
