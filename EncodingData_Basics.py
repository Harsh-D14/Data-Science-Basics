import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Step 1: Creating a sample DataFrame
df = pd.DataFrame({
    'gender':['Male','Female','Female','Male'],
    'city':['Chennai','Bengaluru','Mumbai','Bengaluru'],
    'priority':['High','Medium','Low','High']
})

print('Data before Encoding')
print(df)

#Step 2: One-hot encoding for priorities
df = pd.get_dummies(df, columns=['priority'])

#Step 2: Label Encoding for gender
df['gender'] = df['gender'].map({'Male':'M', 'Female':'F'})

#Step 3: Label Encoding for City Codes
df['city']=df['city'].map({'Chennai':600,'Bengaluru':500,'Mumbai':400})

#Step 4: Print the final encoded values
print(df)