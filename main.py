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

# plt.figure(figsize=(10, 6))
# plt.scatter(data['LEO'], data['FullMass'])
# plt.title('Распределение полезной нагрузки НОО')
# plt.xlabel('FullMass')
# plt.ylabel('LEO')
# plt.grid()
# plt.show()

overview_headers = ['Fuel', 'Country', 'Class', 'Purpose', 'Activity']
for header in overview_headers:
    print(f'Заголовок: {header}')
    unique_values = data[header].value_counts()
    print(unique_values)
    print()

