# Importing Libraries
import wget
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

# Reading Data
train_dir = wget.download("https://s3.amazonaws.com/hr-testcases/399/assets/trainingdata.txt")
datafile = open(train_dir, "r")
data = []

for line in datafile:
    data.append([float(i) for i in line.strip().split(',')])

df = pd.DataFrame(data, columns=['time', 'battery'])

# Visualization
fig, ax = plt.subplots()
ax.scatter(x= df.time, y=df.battery)
ax.set_xlabel("Time Charged in Hours")
ax.set_ylabel("Battery Lasted in Hours")
plt.show()

# Since there is a ceiling effect at 8 hour, I'll remove them and fit a model
df = df[df.battery<8]

X = df.time.values.reshape(df.time.shape[0],1)
y = df.battery.values.reshape(df.battery.shape[0],1)

model = linear_model.LinearRegression()
model.fit(X, y)

# prediction
timeCharged = float(input().strip())
result = model.predict([[timeCharged]])

for i in result: 
    if i[0] > 8:
        print (8.0)
    else:
        print (np.round(i[0],2))

        
        
## Hackerrank
# Importing Libraries
import numpy as np
import pandas as pd
from sklearn import linear_model

df = pd.read_csv('trainingdata.txt', header=None)
df.columns = ['time', 'battery']

# Since there is a ceiling effect at 8 hour, I'll remove them and fit a model
df = df[df.battery<8]

X = df.time.values.reshape(df.time.shape[0],1)
y = df.battery.values.reshape(df.battery.shape[0],1)

model = linear_model.LinearRegression()
model.fit(X, y)

# prediction

timeCharged = float(input().strip())
result = model.predict([[timeCharged]])

for i in result: 
    if i[0] > 8:
        print (8.0)
    else:
        print (np.round(i[0],2))

