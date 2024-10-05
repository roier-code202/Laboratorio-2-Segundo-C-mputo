import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("C:\\Users\\roger\\Documents\\Progra 3\\spotify.csv")


df.columns = df.columns.str.strip()


def is_valid_date(year, month, day):
    if month == 2:  
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  
            return day <= 29
        return day <= 28
    if month in [4, 6, 9, 11]: 
        return day <= 30
    return day <= 31  


def safe_date(row):
    year, month, day = row['released_year'], row['released_month'], row['released_day']
    if is_valid_date(year, month, day):
        return pd.Timestamp(year=year, month=month, day=day)
    return pd.NaT  


df['release_date'] = df.apply(safe_date, axis=1)


print(f"Valores nulos en 'release_date': {df['release_date'].isnull().sum()}")
print(f"Valores nulos en 'streams': {df['streams'].isnull().sum()}")


canciones_a_comparar = [
    'Seven (feat. Latto) (Explicit Ver.)', 
    'LALA', 
    'vampire', 
    'Cruel Summer', 
    'WHERE SHE GOES', 
    'Ella Baila Sola', 
    'Columbia'
]


canciones = df[df['track_name'].isin(canciones_a_comparar)]


print(f"Nulos en 'streams': {canciones['streams'].isnull().sum()}")
print(f"Valores cero en 'streams': {len(canciones[canciones['streams'] == 0])}")


canciones['streams'] = pd.to_numeric(canciones['streams'], errors='coerce')


plt.figure(figsize=(10, 6))


canciones_sorted = canciones.sort_values(by='release_date')


plt.bar(canciones_sorted['track_name'], canciones_sorted['streams'], color='skyblue')


plt.xlabel('Canciones')
plt.ylabel('Reproducciones (en millones)')
plt.title('Reproducciones de Canciones en Spotify')


plt.xticks(rotation=45, ha='right')


plt.tight_layout() 
plt.show()

