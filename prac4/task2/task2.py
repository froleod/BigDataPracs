import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("/Users/lfrolov/Documents/mirea/7sem/BIGDATA/prac4/insurance.csv")
print(df.info())
print(df.head())

# Пропуски
print("Пропуски:\n", df.isna().sum())

# Кодирование категориальных
df['sex_male'] = (df['sex']=='male').astype(int)
df['smoker_yes'] = (df['smoker']=='yes').astype(int)
df = pd.get_dummies(df, columns=['region'], drop_first=True)

# выбор числовых
numeric_cols = ['age','bmi','children','sex_male','smoker_yes'] + [c for c in df.columns if c.startswith('region_')]
print("Колонки для регрессии:", numeric_cols)


# 2.1 corr_matrix
target = 'charges'
corrs = df[numeric_cols + [target]].corr()
print(corrs[target].sort_values(ascending=False))

plt.figure(figsize=(8,6))
sns.heatmap(corrs, annot=True, fmt=".2f", cmap='coolwarm')
plt.title("Корреляционная матрица (numeric + target)")
plt.show()


# 2.2 manual_regression
# выберем X = bmi, y = charges
X = df['bmi'].values
y = df['charges'].values
n = len(X)

# 1) аналитическое решение
x_mean = X.mean()
y_mean = y.mean()
beta1 = np.sum((X - x_mean)*(y - y_mean)) / np.sum((X - x_mean)**2)
beta0 = y_mean - beta1 * x_mean
print("OLS analytic: beta0 =", beta0, "beta1 =", beta1)

y_pred_ols = beta0 + beta1 * X
mse_ols = np.mean((y - y_pred_ols)**2)
print("MSE (OLS):", mse_ols)

# 2) градиентный спуск (простая реализация)
lr = 1e-6        # шаг обучения: подобрать по масштабу y (charges большие)
beta0_g = 0.0
beta1_g = 0.0
epochs = 20000

for epoch in range(epochs):
    y_pred = beta0_g + beta1_g * X
    error = y_pred - y
    grad_b0 = (2/n) * error.sum()
    grad_b1 = (2/n) * (error * X).sum()
    beta0_g -= lr * grad_b0
    beta1_g -= lr * grad_b1
    if epoch % 5000 == 0:
        print(epoch, "beta0_g", beta0_g, "beta1_g", beta1_g)

y_pred_gd = beta0_g + beta1_g * X
mse_gd = np.mean((y - y_pred_gd)**2)
print("Gradient Descent: beta0 =", beta0_g, "beta1 =", beta1_g, "MSE =", mse_gd)


# 2.3 plot_reg

plt.figure(figsize=(7,5))
plt.scatter(X, y, alpha=0.4, label='data')
# OLS line
xs = np.linspace(X.min(), X.max(), 100)
plt.plot(xs, beta0 + beta1*xs, color='red', label='Модель sklearn')
# GD line
plt.plot(xs, beta0_g + beta1_g*xs, color='green', linestyle='--', label='Вручную')
plt.xlabel('bmi')
plt.ylabel('charges')
plt.title('Simple linear regression: charges ~ bmi')
plt.legend()
plt.show()