import tkinter as tk
from tkinter import messagebox
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# ---------- Dataset Path ----------
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR.parent / "data" / "cleaned_data.csv"

print("Dashboard Folder:", BASE_DIR)
print("Dataset Path:", DATA_PATH)
print("File Exists:", DATA_PATH.exists())


# ---------- Load Data ----------
def load_data():
    try:
        return pd.read_csv(DATA_PATH)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load dataset:\n{e}")
        return None


# ---------- Patient Summary ----------
def summary():
    df = load_data()
    if df is None:
        return

    msg = (
        f"Total Patients : {len(df)}\n"
        f"Average Age : {df['Age'].mean():.1f}\n"
        f"Average Bill : {df['Hospital_Bill'].mean():.2f}\n"
        f"Maximum Bill : {df['Hospital_Bill'].max()}\n"
        f"Minimum Bill : {df['Hospital_Bill'].min()}"
    )

    messagebox.showinfo("Patient Summary", msg)


# ---------- Age Distribution ----------
def age_distribution():
    df = load_data()
    if df is None:
        return

    plt.figure(figsize=(7,5))
    plt.hist(df["Age"], bins=10)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Patients")
    plt.show()


# ---------- Gender Distribution ----------
def gender_distribution():
    df = load_data()
    if df is None:
        return

    gender = df["Gender"].value_counts()

    plt.figure(figsize=(6,4))
    plt.bar(gender.index, gender.values)
    plt.title("Gender Distribution")
    plt.xlabel("Gender")
    plt.ylabel("Patients")
    plt.show()


# ---------- Disease Distribution ----------
def disease_distribution():
    df = load_data()
    if df is None:
        return

    disease = df["Disease"].value_counts()

    plt.figure(figsize=(8,5))
    plt.bar(disease.index, disease.values)
    plt.xticks(rotation=45)
    plt.title("Disease Distribution")
    plt.xlabel("Disease")
    plt.ylabel("Patients")
    plt.tight_layout()
    plt.show()


# ---------- Treatment Outcomes ----------
def treatment_outcomes():
    df = load_data()
    if df is None:
        return

    outcome = df["Outcome"].value_counts()

    plt.figure(figsize=(6,6))
    plt.pie(outcome.values,
            labels=outcome.index,
            autopct="%1.1f%%")
    plt.title("Treatment Outcomes")
    plt.show()


# ---------- Hospital Bills ----------
def hospital_bill():
    df = load_data()
    if df is None:
        return

    plt.figure(figsize=(7,5))
    plt.hist(df["Hospital_Bill"], bins=10)
    plt.title("Hospital Bill Distribution")
    plt.xlabel("Hospital Bill")
    plt.ylabel("Patients")
    plt.show()


# ---------- Tkinter Window ----------
root = tk.Tk()
root.title("Hospital Patient Data Overview")
root.geometry("420x520")

tk.Label(
    root,
    text="Hospital Patient Data Overview",
    font=("Arial",16,"bold")
).pack(pady=15)

tk.Button(root,text="Patient Summary",width=30,command=summary).pack(pady=5)

tk.Button(root,text="Age Distribution",width=30,command=age_distribution).pack(pady=5)

tk.Button(root,text="Gender Distribution",width=30,command=gender_distribution).pack(pady=5)

tk.Button(root,text="Disease Distribution",width=30,command=disease_distribution).pack(pady=5)

tk.Button(root,text="Treatment Outcomes",width=30,command=treatment_outcomes).pack(pady=5)

tk.Button(root,text="Hospital Bill Distribution",width=30,command=hospital_bill).pack(pady=5)

tk.Button(root,text="Exit",width=30,command=root.destroy).pack(pady=20)

root.mainloop()