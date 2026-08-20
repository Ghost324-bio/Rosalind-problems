import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Сбор данных (подсчет файлов в папках)
# Убедитесь, что пути соответствуют вашей структуре папок
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
        # Считаем только файлы .py
        count = len([f for f in os.listdir(path) if f.endswith('.py')])
        data[category] = count
        total_solved += count
    else:
        # Если папки нет, ставим 0
        data[category] = 0

# Создаем DataFrame и сортируем по убыванию для barh
df = pd.DataFrame(list(data.items()), columns=['Category', 'Solved'])
df = df.sort_values(by='Solved', ascending=True) 

# 2. Отрисовка гистограммы в Matplotlib
plt.figure(figsize=(10, 5), dpi=150)
plt.style.use('dark_background') # Тёмная тема под GitHub

# Цветовая палитра
colors = plt.colormaps['viridis'](np.linspace(0.2, 0.9, len(df)))

# Рисуем горизонтальные столбцы
bars = plt.barh(df['Category'], df['Solved'], color=colors, edgecolor='none')

# Оформление заголовка
plt.title(f'Rosalind Problems Solved: {total_solved}', fontsize=16, fontweight='bold', pad=20)

# Убираем оси
plt.gca().get_xaxis().set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().set_xticks([])

# Убираем деления (ticks) на оси Y
plt.tick_params(axis='y', length=0, labelsize=12)

# Добавляем числа на столбцы
for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.3, # Отступ от столбца
             bar.get_y() + bar.get_height()/2, # Центр столбца по вертикали
             f'{int(width)}', 
             va='center', 
             ha='left', 
             color='white', 
             fontweight='bold', 
             fontsize=11)

plt.tight_layout()

# 3. Сохранение картинки
# Сохраняем с прозрачным фоном, чтобы он вписывался в темную тему
os.makedirs('assets', exist_ok=True)
plt.savefig('assets/stats_histogram.png', transparent=True, bbox_inches='tight', pad_inches=0.1)
