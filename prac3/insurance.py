# insurance_analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import math

# Задание 1. Загрузка данных
df = pd.read_csv("/Users/lfrolov/Documents/mirea/7sem/BIGDATA/prac3/insurance.csv")

# Задание 2. Первичный анализ
print("Информация о данных:")
print("\nПервые строки:\n", df.head())
print("\nОписание числовых признаков:\n", df.describe())

# Задание 3. Гистограммы числовых признаков
numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    plt.figure(figsize=(6, 4))
    sns.histplot(df[col], bins=30, kde=True)
    plt.title(f"Histogram of {col}")
    plt.show()

# Задание 4. Среднее, медиана, мода, размах, дисперсия, ст. отклонение, IQR
for col in ["bmi", "charges"]:
    s = df[col].dropna()
    mean = s.mean()
    median = s.median()
    mode = s.mode().iloc[0] if not s.mode().empty else np.nan
    range_val = s.max() - s.min()
    var = s.var(ddof=1)
    std = s.std(ddof=1)
    iqr = s.quantile(0.75) - s.quantile(0.25)
    print(f"\n{col}:")
    print(f"  Среднее: {mean:.2f}")
    print(f"  Медиана: {median:.2f}")
    print(f"  Мода: {mode:.2f}")
    print(f"  Размах: {range_val:.2f}")
    print(f"  Дисперсия: {var:.2f}")
    print(f"  Стандартное отклонение: {std:.2f}")
    print(f"  IQR: {iqr:.2f}")

    # график с тремя линиями
    plt.figure(figsize=(6, 4))
    sns.histplot(s, bins=30, kde=False)
    plt.axvline(mean, color="red", linestyle="-", label=f"mean={mean:.2f}")
    plt.axvline(median, color="green", linestyle="--", label=f"median={median:.2f}")
    plt.axvline(mode, color="blue", linestyle=":", label=f"mode={mode:.2f}")
    plt.legend()
    plt.title(f"{col} distribution with mean/median/mode")
    plt.show()

# Задание 5. Boxplot для числовых признаков
# Boxplot для age, bmi, children
plt.figure(figsize=(10, 5))
df[["age", "bmi", "children"]].boxplot()
plt.title("Boxplots for age, bmi, children")
plt.show()

# Boxplot для charges
plt.figure(figsize=(6, 5))
df[["charges"]].boxplot()
plt.title("Boxplot for charges")
plt.show()


# Задание 6. ЦПТ (распределение выборочных средних)
def clt_experiment(series, n, n_samples=300, random_state=0):
    np.random.seed(random_state)
    arr = series.dropna().values
    means = []
    for _ in range(n_samples):
        sample = np.random.choice(arr, size=n, replace=True)
        means.append(sample.mean())
    return np.array(means)


series = df["charges"]
for n in [5, 30, 100]:
    means = clt_experiment(series, n=n, n_samples=300)
    print(f"\nЦПТ для n={n}: среднее={means.mean():.2f}, std={means.std(ddof=1):.2f}")
    plt.figure(figsize=(6, 4))
    sns.histplot(means, bins=30, kde=True)
    plt.title(f"Distribution of sample means (n={n})")
    plt.show()


# Задание 7. Доверительные интервалы (95% и 99%)
def t_confidence_interval(data, alpha=0.05):
    x = np.array(data.dropna())
    n = len(x)
    mean = x.mean()
    se = x.std(ddof=1) / math.sqrt(n)
    t_crit = stats.t.ppf(1 - alpha / 2, df=n - 1)
    return mean - t_crit * se, mean + t_crit * se


for alpha in [0.05, 0.01]:
    ci = t_confidence_interval(df["charges"], alpha=alpha)
    print(f"\nДоверительный интервал {(1 - alpha) * 100:.0f}% для charges: {ci}")

# Задание 8. Проверка нормальности charges и bmi
for col in ["bmi", "charges"]:
    s = df[col].dropna()
    # стандартизация для KS
    s_std = (s - s.mean()) / s.std(ddof=0)
    ks_stat, ks_p = stats.kstest(s_std, "norm")
    sh_stat, sh_p = stats.shapiro(s) if len(s) <= 5000 else (None, None)
    print(f"\nПроверка нормальности {col}:")
    print(f"  KS-test p={ks_p}")

    # Q-Q plot
    plt.figure(figsize=(5, 4))
    stats.probplot(s, dist="norm", plot=plt)
    plt.title(f"Q-Q plot: {col}")
    plt.show()
