import numpy as np
import plotly.express as px
import csv

def getDataSource(path):
    iceCreamSales=[]
    temp=[]
    with open(path) as f:
        read=csv.DictReader(f) 
        for row in read:
            iceCreamSales.append(float(row["Ice-cream Sales"]))
            temp.append(float(row["Temperature"]))
    return{"x":temp,"y":iceCreamSales}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between ice-cream sales and temperature is: ",correlation[0,1])

def setup():
    path="./data/iceCream.csv"
    dataSource=getDataSource(path)
    findCorrelation(dataSource)

setup()