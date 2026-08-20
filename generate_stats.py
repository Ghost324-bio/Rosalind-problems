import os
import json
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# 1. Подсчет текущего количества задач
categories = {
    'Python Village': 'src/Python_Village',
    'Bioinformatics Stronghold': 'src/Bioinformatic_Stronghold',
    'Bioinformatics Armory': 'src/Bioinformatic_Armory',
    'Algorithmic Heights': 'src/Algorithmic_Heights'
}

total_solved = 0
for path in categories.values():
    if os.path.exists(path):
        total_solved += len([f for f in os.listdir(path) if f.endswith('.py')])

# 2. Работа с файлом истории
os.makedirs('assets', exist_ok=True)
history_file = 'assets/history.json'

if os.path.exists(history_file):
    with open(history_file, 'r', encoding='utf-8') as f:
        history = json.load(f)
else:
    history = {}

# Записываем или обновляем значение на сегодняшнее число
today = datetime.now().strftime('%Y-%m-%d')
history[today] = total_solved

with open(history_file, 'w', encoding='utf-8') as f:
    json.dump(history, f, indent=4)

# 3. Подготовка данных для графика
df = pd.DataFrame(list(history.items()), columns=['Date', 'Solved'])
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# 4. Отрисовка линейного графика
plt.figure(figsize=(9, 4.5), dpi=150)
plt.style.use('dark_background')

# Линия и точки
plt.plot(df['Date'], df['Solved'], marker='o', color='#2ea44f', linewidth=2.5, markersize=6, label='Tasks Solved')
plt.fill_between(df['Date'], df['Solved'], color='#2ea44f', alpha=0.2)  # Заливка под графиком

# Оформление
plt.title(f'Overall Progress Over Time (Total: {total_solved})', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Date', fontsize=10)
plt.ylabel('Total Solved Tasks', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.3)
plt.gcf().autofmt_xdate()  # Авто-наклон дат по оси X
plt.tight_layout()

plt.savefig('assets/progress_timeline.png', transparent=True)
