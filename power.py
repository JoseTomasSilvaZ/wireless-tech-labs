import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/measures.csv')  

fig = plt.figure(figsize=(10, 6))
plt.bar(df['Number'], df['Power'], color='blue')

plt.title('Mediciones de potencia')
plt.xlabel('Medición')
plt.ylabel('Power (dBm)')
plt.xticks(df['Number'])


plt.savefig('./images/power.png')
plt.show()

