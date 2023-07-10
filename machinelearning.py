# -*- coding: utf-8 -*-
"""MachineLearning

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YhFig6mcqhUl3yKcn6ajeyGjGyADHoZK

Five Personality Traits(OCEAN)


*   Openness to experience (invite/curious vs. consistent/cautious)
*   Conscientiousness (efficient/organized vs. easy-going/carless)
*   Extroversion (outgoin/energetic vs. solitary/reserved)
*   Agreeableness (friendly/compassionate vs. challenging/detached)
*   Neuroticism (sensitive/nervous vs. secure/confident)

Importing the libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from io import open
pd.options.display.max_columns=150

"""Loading the Dataset"""

data = pd.read_csv('data-final.csv', sep='\t')

"""Checking the Dataset"""

data.head()

"""Removing irrelevant attributes"""

data.drop(data.columns[50:110], axis=1, inplace=True)

"""Checking the data again"""

data.head()

"""Analyzing Statistics of the dataset"""

pd.options.display.float_format="{:.2f}".format
data.describe()

"""Checking the count of records per value"""

data['EXT1'].value_counts()

"""Selecting the total number of records with zero value"""

data[(data==0.00).all(axis=1)].describe()

"""Cleaning the DataFrame with only records greater than zero."""

data = data[(data > 0.00).all(axis=1)]

"""Checking the count of records per value."""

data["EXT1"].value_counts()

!pip install yellowbrick

"""Machine Learning Libraries"""

from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer

"""Instantiating the KMeans method and the Visualizer"""

kmeans = KMeans()
visualizer = KElbowVisualizer(kmeans, k=(2,10))

"""Selecting a random sample of data with 5000 observations."""

data_sample = data.sample(n=5000, random_state=1)

"""Running the test."""

visualizer.fit(data_sample)
visualizer.poof()

"""**Grouping the participants into 5 clusters**

Assigning the records to their respective groups
"""

kmeans = KMeans(n_clusters=5)
k_fit = kmeans.fit(data)

"""Inserting the cluster labels into the dataframe"""

predicoes = k_fit.labels_
data['Clusters'] = predicoes

"""Checking the data"""

data.head()

"""**Analyzing the groups**

What is the number of observations in each group?
"""

data["Clusters"].value_counts()

"""Grouping the records by clusters"""

data.groupby('Clusters').mean()

"""**Calculating the mean of each question group to check for a pattern**.

Selecting the columns for each group
"""

col_list = list(data)
ext = col_list[0:10]
est = col_list[10:20]
agr = col_list[20:30]
csn = col_list[30:40]
opn = col_list[40:50]

"""Summing the values of each group"""

data_soma = pd.DataFrame()
data_soma['extroversion'] = data[ext].sum(axis=1)/10
data_soma['neurotic'] = data[est].sum(axis=1)/10
data_soma['agreeable'] = data[agr].sum(axis=1)/10
data_soma['conscientious'] = data[csn].sum(axis=1)/10
data_soma['open'] = data[opn].sum(axis=1)/10
data_soma['clusters'] = predicoes

"""Displaying the average value per group"""

data_soma.groupby('clusters').mean()

"""Visualizing the averages per group"""

data_clusters = data_soma.groupby('clusters').mean()

plt.figure(figsize=(22,3))
for i in range(0, 5):
    plt.subplot(1,5,i+1)
    plt.bar(data_clusters.columns, data_clusters.iloc[:, i], color='blue', alpha=0.2)
    plt.plot(data_clusters.columns, data_clusters.iloc[:, i], color='red')
    plt.title('Grupo ' + str(i))
    plt.xticks(rotation=45)
    plt.ylim(0,4);

"""Installing the Gradio library"""

!pip install gradio

import gradio as gr

dicio_questions = open("questions.txt").read().split("\n")

"""Checking the data."""

dicio_questions

"""Criando a interface e a função predict."""

questions = []
for q in dicio_questions:
  q = str(q)
  questions.append(q[q.find("\t"):].lstrip())

questions

"""Creating the dynamic inputs to pass to Gradio"""

inputs_questions = []
for q in questions:
  obj_input = gr.inputs.Slider(minimum=1,maximum=5,step=1,default=3,label=q)
  inputs_questions.append(obj_input)

"""Checking the inputs"""

inputs_questions

"""Creating the interface and the predict function."""

def predict(*outputs_questions):
    outputs_questions = np.array(outputs_questions).reshape(1, -1)
    return k_fit.predict(outputs_questions)

iface = gr.Interface(
                    fn = predict,
                    title = "Big Five Personality",
                    description = "Sistema para detecção de traços de personalidade.",
                    inputs = inputs_questions,
                    outputs="text")
iface.launch(share=True)
