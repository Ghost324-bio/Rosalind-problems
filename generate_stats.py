import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Сбор данных
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

df = pd.DataFrame(list(data.items()), columns=['Category', 'Solved'])
df = df.sort_values(by='Solved', ascending=True)

# 2. Настройка стиля и сплошного фона
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(9, 4.5), dpi=150)

# Задаем сплошной темный фон (в стиле темы GitHub)
dark_bg = '#0d1117'
fig.patch.set_facecolor(dark_bg)
ax.set_facecolor(dark_bg)

# Цветовая гамма столбцов
colors = plt.colormaps['viridis'](np.linspace(0.3, 0.85, len(df)))

# Рисуем столбцы
bars = ax.barh(df['Category'], df['Solved'], color=colors, height=0.55, edgecolor='none')

# Заголовок
ax.set_title(f'Rosalind Progress: {total_solved} Tasks Solved', 
             fontsize=15, fontweight='bold', pad=18, color='#ffffff')

# Настройка граница и осей
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.get_xaxis().set_visible(False)

ax.tick_params(axis='y', length=0, labelsize=11, labelcolor='#e6edf3')

# Устанавливаем запас по оси X, чтобы числа не вылезали за край
max_val = max(df['Solved'].max(), 1)
ax.set_xlim(0, max_val + max(2, max_val * 0.2))

# Подписи значений на столбцах
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.2, 
            bar.get_y() + bar.get_height()/2, 
            f'{int(width)}', 
            va='center', 
            ha='left', 
            color='#ffffff', 
            fontweight='bold', 
            fontsize=11)

plt.tight_layout()

# 3. Сохранение без прозрачности (facecolor сохраняет темный фон)
os.makedirs('assets', exist_ok=True)
plt.savefig('assets/my_stats.png', facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight', pad_inches=0.2)
