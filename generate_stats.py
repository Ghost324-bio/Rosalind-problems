import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Сбор данных (подсчет файлов в папках src/...)
categories = {
    'Python Village': 'src/Python_Village',
    'Bioinformatics Stronghold': 'src/Bioinformatic_Stronghold',
    'Bioinformatics Armory': 'src/Bioinformatic_Armory',
    'Algorithmic Heights': 'src/Algorithmic_Heights'
}

data = {}
total_solved = 0

for category, path in categories.items():
    if os.path.exists(path):
        count = len([f for f in os.listdir(path) if f.endswith('.py')])
        data[category] = count
        total_solved += count
    else:
        data[category] = 0

# Создаем DataFrame и сортируем (для горизонтальных столбцов лучше сортировать ascending)
df = pd.DataFrame(list(data.items()), columns=['Category', 'Solved'])
df = df.sort_values(by='Solved', ascending=True) 

# 2. Отрисовка гистограммы (ГОРИЗОНТАЛЬНЫХ СТОЛБЦОВ)
plt.figure(figsize=(10, 5), dpi=150)
plt.style.use('dark_background') # Тёмная тема

# Цветовая палитра
colors = plt.colormaps['viridis'](np.linspace(0.2, 0.9, len(df)))

# Рисуем столбцы (barh = bar horizontal)
bars = plt.barh(df['Category'], df['Solved'], color=colors, edgecolor='none')

# Заголовок с общим числом задач
plt.title(f'Rosalind Problems Solved: {total_solved}', fontsize=16, fontweight='bold', pad=20)

# Полностью убираем оси и сетку (для чистоты)
plt.gca().get_xaxis().set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().set_xticks([])

# Убираем деления и настраиваем шрифт категорий
plt.tick_params(axis='y', length=0, labelsize=12)

# Добавляем актуальные числа на каждый столбец
for bar in bars:
    width = bar.get_width()
    # Числа появляются справа от столбца (+0.3 отступа)
    plt.text(width + 0.3, 
             bar.get_y() + bar.get_height()/2, 
             f'{int(width)}', 
             va='center', 
             ha='left', 
             color='white', 
             fontweight='bold', 
             fontsize=11)

plt.tight_layout()

# 3. Сохранение картинки (убедитесь в правильности имени файла)
os.makedirs('assets', exist_ok=True)
plt.savefig('assets/stats_histogram.png', transparent=True, bbox_inches='tight', pad_inches=0.1)
