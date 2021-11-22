# DataVisualization-1
# This is a python script made by @somePythonProgrammer 
# for a WhiteHat Junior project.

import pandas as pd
import plotly_express as px

df = pd.read_csv('008-C103-DataVisualization-1/csv/corona_data.csv')
plot = px.scatter(df, x='date', y='cases', color='country', title='Corona Virus Cases')
plot.show()
