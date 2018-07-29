from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import itertools

file = r'Loans.csv'
df = pd.read_csv(file)

loanParameters = ['Network', 'Product', 'Month']

loanData = []

networkData = []

productData = []

monthData = []

parameterCombinations = list(itertools.combinations(loanParameters, 2))

for column in df:
    if column == 'Network':
        networkData.append(df[column])
    elif column == 'Product':
        productData.append(df[column])
    elif column == 'Date':
        monthData.append(df[column])

    loanData.append(df[column])

print(networkData)
print(productData)
print(monthData)



