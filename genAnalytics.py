import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, time

from sklearn.preprocessing import StandardScaler
from pandas_profiling import ProfileReport

def generate_report():
    df_sales= pd.read_csv('april.csv')
    df_sales.pop("Purchase Address")

    profile = ProfileReport(df_sales)
    profile.to_file("templates/generated_report.html")
    xstat = print("Success")
