import os
import matplotlib.pyplot as plt
import pandas as pd

# 1. Сбор данных (подсчет файлов в папках)
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
        # Считаем только файлы с решениями .py
        count = len([f for f in os.listdir(path) if f.endswith('.py')])
        data[category] = count
        total_solved += count
    else:
        data[category] = 0

df = pd.DataFrame(list(data.items()), columns=['Category', 'Solved'])

# 2. Отрисовка гистограммы в Matplotlib
plt.figure(figsize=(9, 4.5), dpi=150)
plt.style.use('dark_background')  # Тёмная тема под стиль GitHub

bars = plt.barh(df['Category'], df['Solved'], color='#2ea44f', edgecolor='white', linewidth=0.8)

# Настройки заголовка и осей
plt.title(f'Rosalind Progress: {total_solved} Tasks Solved', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Number of Solved Problems', fontsize=10)
plt.xlim(0, max(df['Solved'].max() + 3, 10))
plt.gca().invert_yaxis()  # Верхняя категория вверху

# Подписи значений на барах
for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.2, bar.get_y() + bar.get_height()/2, f'{int(width)}', 
             va='center', ha='left', color='white', fontweight='bold', fontsize=10)

plt.tight_layout()

# 3. Сохранение картинки
os.makedirs('assets', exist_ok=True)
plt.savefig('assets/stats.png', transparent=True)
