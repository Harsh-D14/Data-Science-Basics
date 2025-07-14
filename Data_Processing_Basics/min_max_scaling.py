import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
#Sample Dataset
data = {
    'age':[22,25,47,52,46],
    'salary':[25000,27000,90000,110000,85000]
}
df = pd.DataFrame(data)
print("Original Data:\n",df)

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df)

df_minmax = pd.DataFrame(scaled_data,columns=['scaled_age','scaled_salary'])

print("\nAfter MinMax Scaling:\n", df_minmax)

std_scaler = StandardScaler()
std_data = std_scaler.fit_transform(df)

df_std = pd.DataFrame(std_data,columns=['std_age','std_salary'])

print("\nAfter Standard Scaling:\n", df_std)



