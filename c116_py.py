# -*- coding: utf-8 -*-
"""C116.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xWEL_iv10N3_WXAA6lkcPbrnwPUNbBGq
"""

from google.colab import files
data_to_load = files.upload()

import pandas as pd;
import plotly.express as px;
from sklearn.linear_model import LogisticRegression;
from sklearn.metrics import accuracy_score;
import numpy as np;

data = pd.read_csv('Admission_Predict.csv');

score = data['TOEFL Score'].tolist();
chance = data['Chance of admit'].tolist();

fig = px.scatter(data, x = score, y = chance);

m, c = np.polyfit(score, chance, 1);

Y = [];
for x in score:
    y_value = m * x + c;
    if y_value < 0.5:
        Y.append(0);
    else:
        Y.append(1);

accuracy = accuracy_score(chance, Y);
print(accuracy);

