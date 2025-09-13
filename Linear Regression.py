# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 15:56:10 2025

@author: Axel
"""

import csv
filename = "test.csv"
filename2 = "train.csv"

import pandas as pd
from sklearn.linear_model import LinearRegression

# Leer datos de entrenamiento
train = pd.read_csv("train.csv")

X = train[["x"]]   # variable independiente (2D)
y = train["y"]     # variable dependiente

# Crear y entrenar modelo
model = LinearRegression()
model.fit(X, y)

print("Coeficiente (pendiente):", model.coef_[0])
print("Intercepto:", model.intercept_)
