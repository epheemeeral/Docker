import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

# Генерация данных по теме Social Media
data = {
    'post_id': range(1, 101),
    'likes': [random.randint(0, 1000) for _ in range(100)],
    'reposts': [random.randint(0, 200) for _ in range(100)],
    'text_length': [random.randint(10, 500) for _ in range(100)],
    'sentiment': [random.choice(['positive', 'negative']) for _ in range(100)]
}
df = pd.DataFrame(data)
df['engagement'] = df['likes'] + df['reposts']

# Визуализация
plt.figure(figsize=(10, 6))
sns.barplot(x='sentiment', y='engagement', data=df, palette='viridis')
plt.title('Engagement Analysis (Variant 17)')
plt.savefig('/app/result.png')
print("Анализ выполнен, график сохранен как result.png")
