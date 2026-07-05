# Hospital Patient Data Overview

## Project Description

This project analyzes hospital patient records using Python. It performs
Exploratory Data Analysis (EDA) to identify patient demographics,
admission reasons, treatment outcomes, hospital bills, and length of
stay. A simple Tkinter GUI is included to visualize the analysis.

## Project Structure

``` text
Hospital_Patient_Data_Overview/
├── data/
│   ├── raw_data.csv
│   └── cleaned_data.csv
├── notebooks/
│   └── analysis.ipynb
├── visualizations/
│   └── dashboard.py
├── README.md
├── requirements.txt
└── report.pdf
```

## Technologies Used

-   Python
-   Pandas
-   NumPy
-   Matplotlib
-   Tkinter
-   Jupyter Notebook

## Installation

``` bash
pip install -r requirements.txt
```

## Run

Notebook:

``` text
notebooks/analysis.ipynb
```

Dashboard:

``` bash
cd visualizations
python dashboard.py
```

## Features

-   Data Cleaning
-   Exploratory Data Analysis (EDA)
-   Patient Summary
-   Age Distribution
-   Gender Distribution
-   Disease Analysis
-   Treatment Outcomes
-   Hospital Bill Analysis

## Dataset

The dataset includes Patient ID, Age, Gender, Disease, Admission Type,
Admission Date, Discharge Date, Length of Stay, Treatment, Outcome, and
Hospital Bill.

## Conclusion

This project demonstrates basic hospital data analysis using Python,
Matplotlib, and Tkinter.
