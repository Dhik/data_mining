import numpy as np

X = np.array([[1,1],
    [4,1],
    [1,2],
    [3,4],
    [5,4],])
import pandas as pd 
    
df = pd.DataFrame()
for i in range(0, len(X)):
  for j in range(0, len(X)):
    df.loc[i,j]=0
df
smallest = 100
point1 = 0
point2 = 0
for i in range(0, len(X)):
  for j in range(i, len(X)):
    df.loc[i,j] = ((abs(X[i][0]-X[j][0]))+(abs(X[i][1]-X[j][1])))
    if df.loc[i,j] != 0:
      if df.loc[i,j] < smallest:
        smallest = df.loc[i,j]
    df.loc[j,i] = df.loc[i,j]

for i in range(0, len(X)):
  for j in range(i, len(X)):
    if df.loc[i,j] == smallest:
      col = j
      row = i

print(row, col)
del df[col]
df
# print(Y)
# print(smallest)
limit=len(X)
df = df.rename(columns={0: limit}, index={0: limit})
df.drop([col])