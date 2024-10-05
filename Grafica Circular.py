import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("C:\\Users\\roger\\Documents\\Progra 3\\DELL_daily_data.csv")


df.columns = df.columns.str.strip()


df['Close'] = pd.to_numeric(df['Close'], errors='coerce')


ultimos_dias = df.tail(10)


plt.figure(figsize=(8, 8))
plt.pie(ultimos_dias['Close'], labels=ultimos_dias['Date'], autopct='%1.1f%%', startangle=140)


plt.title('Proporción de Precios de Cierre de DELL en los Últimos 10 Días', pad=20)


plt.axis('equal')  
plt.show()
