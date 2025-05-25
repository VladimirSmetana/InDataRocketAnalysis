import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Чтение CSV файла
file_path = 'data.csv'  # Укажите путь к вашему файлу
data = pd.read_csv(file_path, sep=';', decimal=',', skipinitialspace=True)

# Просмотр первых 5 строк данных
print(data.head())

# Основная информация о данных
print(data.info())

# Статистическое описание
print(data.describe())