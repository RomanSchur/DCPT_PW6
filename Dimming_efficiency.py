import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

files = {
    "Контроль": "Без_фільтрів.csv",
    "Сонцезахисне скло": "Сонцезахисне_скло.csv",
    "Пластикова плівка": "Пластикова_плівка.csv",
    "Лист А4": "Лист_а4.csv",
    "Тканина": "Тканини.csv"
}

results = []
plt.figure(figsize=(12, 7))

for label, filename in files.items():
    try:
        df = pd.read_csv(filename)

        col = 'Luma' if 'Luma' in df.columns else df.columns[1]
        time_col = 't' if 't' in df.columns else df.columns[0]

        mean_val = df[col].mean()
        std_val = df[col].std()

        results.append({
            "Матеріал": label,
            "Середня яскравість": round(mean_val, 4),
            "Шум (std)": round(std_val, 6)
        })
        mask = df[time_col] <= 9
        plt.plot(df[time_col][mask], df[col][mask], label=label, linewidth=1.5)

    except Exception as e:
        print(f"Помилка при обробці файлу {filename}: {e}")

summary_df = pd.DataFrame(results)

control_val = summary_df.loc[summary_df['Матеріал'] == 'Контроль', 'Середня яскравість'].values[0]
summary_df['Ефективність (%)'] = (1 - (summary_df['Середня яскравість'] / control_val)) * 100

print(summary_df[['Матеріал', 'Середня яскравість', 'Ефективність (%)']])

plt.title('Порівняльний графік освітленості (Практична робота №6)', fontsize=14)
plt.xlabel('Час (с)', fontsize=12)
plt.ylabel('Яскравість (відносні одиниці)', fontsize=12)
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
