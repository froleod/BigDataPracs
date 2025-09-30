import pandas as pd
import numpy as np
from scipy import stats

# Задание 13
bmi_df = pd.read_csv("/Users/lfrolov/Documents/mirea/7sem/BIGDATA/prac3/bmi.csv")

# Две выборки: northwest и southwest
bmi_nw = bmi_df.loc[bmi_df["region"]=="northwest", "bmi"].dropna()
bmi_sw = bmi_df.loc[bmi_df["region"]=="southwest", "bmi"].dropna()

# Проверка нормальности (Shapiro-Wilk)
print("Shapiro-Wilk test for northwest:", stats.shapiro(bmi_nw))
print("Shapiro-Wilk test for southwest:", stats.shapiro(bmi_sw))

# Проверка гомогенности дисперсий (Bartlett)
print("Bartlett test:", stats.bartlett(bmi_nw, bmi_sw))

# Сравнение средних значений (t-test)
t_stat, p_val = stats.ttest_ind(bmi_nw, bmi_sw, equal_var=True)
print("t-test (northwest vs southwest):", t_stat, p_val)


# Задание 14
obs = np.array([97, 98, 109, 95, 97, 104])

chi2_stat, p_val = stats.chisquare(obs)
print("\nChi-square test for dice fairness:")
print("chi2 =", chi2_stat, "p-value =", p_val)


# Задание 15
data = pd.DataFrame({
    'Женат': [89,17,11,43,22,1],
    'Гражданский брак': [80,22,20,35,6,4],
    'Не состоит в отношениях': [35,44,35,6,8,22]
})
data.index = ['Полный рабочий день','Частичная занятость','Временно не работает',
              'На домохозяйстве','На пенсии','Учёба']

chi2, p, dof, expected = stats.chi2_contingency(data)
print("\nChi-square test for independence (marital status vs employment):")
print("chi2 =", chi2, "p-value =", p, "dof =", dof)

if p < 0.05:
    print("Вывод: зависимость есть (семейное положение влияет на занятость)")
else:
    print("Вывод: зависимости не выявлено (семейное положение не влияет на занятость)")
