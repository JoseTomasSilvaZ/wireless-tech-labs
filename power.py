import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/measures.csv')  

plt.figure(figsize=(10, 6))
plt.bar(df['Number'], df['Power'], color='blue')

plt.title('Mediciones de potencia')
plt.xlabel('Medición (número)')
plt.ylabel('Power (dBm)')
plt.xticks(df['Number'])

plt.show()
