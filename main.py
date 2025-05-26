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

overview_headers = ['Fuel', 'Country', 'Class', 'Purpose', 'Activity']

# Определяем количество подграфиков
num_headers = len(overview_headers)
num_cols = 2  # Количество столбцов
num_rows = (num_headers + num_cols - 1) // num_cols  # Количество строк

fig, axs = plt.subplots(num_rows, num_cols, figsize=(10, 3 * num_rows))  # Определяем размер фигуры

# Превращаем axs в одномерный массив для удобства
axs = axs.flatten()

for i, header in enumerate(overview_headers):
    print(f'Заголовок: {header}')
    unique_values = data[header].value_counts()
    print(unique_values)
    print()

    axs[i].bar(unique_values.index, unique_values.values)
    axs[i].set_title(f'Распределение по {header}')
    axs[i].set_xlabel(header)
    axs[i].set_ylabel('Количество')
    axs[i].tick_params(axis='x', rotation=45)  # Поворот подписей по оси X для читаемости

# Убираем пустые подграфики, если есть
for j in range(i + 1, num_rows * num_cols):
    fig.delaxes(axs[j])

plt.tight_layout()  # Автоматическая подгонка подграфиков
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x=data['Activity'], y=data['SuccessRate'], data=data)

# Настройка заголовка и меток
plt.title('Сравнение надежности старых и новых ракет')
plt.xlabel('Тип ракеты')
plt.ylabel('Надежность (%)')

# Показать график
plt.tight_layout()
plt.show()

filtered_data = data[data['Activity'] == 'нет']
plt.figure(figsize=(10, 6))
sns.boxplot(x=filtered_data['Class'], y=filtered_data['ActiveYears'], data=filtered_data)

# Настройка заголовка и меток
plt.title('Сравнение надежности старых и новых ракет')
plt.xlabel('Тип ракеты')
plt.ylabel('Надежность (%)')

# Показать график
plt.tight_layout()
plt.show()

correlation = filtered_data['SuccessRate'].corr(filtered_data['SuccessRate'])
print(f'Коэффициент корреляции между ActiveYears и SuccessRate: {correlation:.2f}')

plt.figure(figsize=(10, 6))
sns.scatterplot(x='ActiveYears', y='SuccessRate', data=filtered_data)

# Настройка заголовка и меток
plt.title('Корреляция между активными годами и надежностью')
plt.xlabel('Активные годы')
plt.ylabel('Надежность')

# Добавление линии регрессии
sns.regplot(x='ActiveYears', y='SuccessRate', data=filtered_data, scatter=False, color='red')

# Показать график
plt.tight_layout()
plt.show()

correlation = filtered_data['LEO'].corr(filtered_data['FullMass'])
print(f'Коэффициент корреляции между LEO и FullMass: {correlation:.2f}')

plt.figure(figsize=(10, 6))
sns.scatterplot(x='LEO', y='FullMass', data=filtered_data)

# Настройка заголовка и меток
plt.title('Корреляция между LEO и FullMass')
plt.xlabel('LEO')
plt.ylabel('FullMass')

# Добавление линии регрессии
sns.regplot(x='LEO', y='FullMass', data=filtered_data, scatter=False, color='red')

# Показать график
plt.tight_layout()
plt.show()
