import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("C:\\Users\\roger\\Documents\\Progra 3\\PremierLeagueSeason2024.csv")


df.columns = df.columns.str.strip()

print(df.head())


nuevos_datos = {
    'team': ['Manchester City', 'Manchester City', 'Liverpool', 'Liverpool', 'Arsenal', 'Arsenal', 
             'Manchester United', 'Manchester United', 'Chelsea', 'Chelsea'],
    'goals_scored': [45, 54, 40, 38, 30, 35, 25, 27, 20, 15],
    'goals_conceded': [10, 15, 25, 30, 15, 20, 30, 35, 10, 12],
    'wins': [15, 18, 12, 10, 8, 12, 6, 8, 5, 3],
    'draws': [3, 4, 6, 4, 2, 3, 2, 2, 2, 1],
    'losses': [2, 1, 3, 5, 4, 3, 5, 5, 3, 6],
    'points': [48, 54, 42, 36, 26, 36, 20, 24, 17, 11],
    'goal_difference': [35, 39, 15, 8, 11, 15, -5, -7, 10, 3],
    'rank': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
}


df_nuevos = pd.DataFrame(nuevos_datos)


df = pd.concat([df, df_nuevos], ignore_index=True)


equipos_a_comparar = ['Manchester City', 'Liverpool', 'Arsenal', 'Manchester United', 'Chelsea']


equipos = df[df['team'].isin(equipos_a_comparar)]


print("Equipos seleccionados para graficar:")
print(equipos[['team', 'rank', 'points']])

for equipo in equipos_a_comparar:
    equipo_data = equipos[equipos['team'] == equipo]
    if len(equipo_data) < 2:
        print(f"Advertencia: {equipo} solo tiene {len(equipo_data)} registro(s). No se puede graficar una línea.")


df['rank'] = pd.to_numeric(df['rank'], errors='coerce')
df['points'] = pd.to_numeric(df['points'], errors='coerce')


plt.figure(figsize=(10, 6))


for equipo in equipos_a_comparar:
    equipo_data = equipos[equipos['team'] == equipo]
    

    if not equipo_data.empty:
        
        plt.plot(equipo_data['rank'], equipo_data['points'], label=equipo, marker='o', linestyle='-', linewidth=2)


plt.xlabel('Posición en la Tabla')
plt.ylabel('Puntos Acumulados')
plt.title('Comparación de Puntos en Premier League 2024')


plt.xlim(equipos['rank'].min() - 1, equipos['rank'].max() + 1)
plt.ylim(0, df['points'].max() + 10)  


plt.xticks(rotation=45)


plt.legend()


plt.tight_layout()  
plt.show()
