import plotly.figure_factory as pf
import pandas as pd
import csv

df=pd.read_csv("HWdata.csv")
fig=pf.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"],show_hist=False)
fig.show()