import pandas as pd
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import itertools
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/lfrolov/Documents/mirea/7sem/BIGDATA/prac4/insurance.csv")
# print("Размерность:", df.shape)
# print(df.head())

# Проверка пропусков
# print("Пропуски:\n", df.isna().sum())

# Список уникальных регионов
print("Уникальные регионы:", df['region'].unique())

# Выбираем колонку BMI
df_bmi = df[['bmi','region','sex','age','children','smoker','charges']].copy()


# 3.1 One-way ANOVA через SciPy (влиение region на BMI)
groups = [group['bmi'].values for name, group in df_bmi.groupby('region')]
f_stat, p_val = stats.f_oneway(*groups)
print("\n3.1 One-way ANOVA (SciPy): F =", f_stat, "p =", p_val)


# 3.2 One-way ANOVA через statsmodels anova_lm()
model = ols('bmi ~ C(region)', data=df_bmi).fit()
anova_results = anova_lm(model)
print("\n3.2")
print(anova_results)


# 3.3 Перебор всех пар t-критерием Стьюдента + поправка Бонферрони

regions = df_bmi['region'].unique()
alpha = 0.05
pairs = list(itertools.combinations(regions, 2))
m = len(pairs)
alpha_bonf = alpha / m
print("\n3.3 Parwise t-tests, Bonferroni alpha:", alpha_bonf)

results = []
for (r1, r2) in pairs:
    g1 = df_bmi[df_bmi['region']==r1]['bmi']
    g2 = df_bmi[df_bmi['region']==r2]['bmi']
    t_stat, p_val = stats.ttest_ind(g1, g2, equal_var=False)  # Welch by default safer
    results.append((r1, r2, t_stat, p_val, p_val < alpha_bonf))
for res in results:
    print(res)


# 3.4 Пост-хок тест Тьюки и график
tukey = pairwise_tukeyhsd(endog=df_bmi['bmi'], groups=df_bmi['region'], alpha=0.05)
print("\n3.4 Пост-хок тест Тьюки")
print(tukey.summary())
# график
tukey.plot_simultaneous()
plt.title("Tukey HSD: BMI by region")
plt.show()


# 3.5 Двухфакторный ANOVA: влияние region и sex на BMI
model2 = ols('bmi ~ C(region) + C(sex) + C(region):C(sex)', data=df_bmi).fit()
anova_results2 = anova_lm(model2)
print("\n3.5 Двухфакторный ANOVA: влияние region и sex на BMI")
print(anova_results2)


# 3.6 Пост-хок тесты Тьюки для двухфакторного анализа (по факторам/уровням)
df_bmi['region_sex'] = df_bmi['region'] + "_" + df_bmi['sex']
tukey2 = pairwise_tukeyhsd(endog=df_bmi['bmi'], groups=df_bmi['region_sex'], alpha=0.05)
print("\n 3.6 Пост-хок тесты Тьюки для двухфакторного анализа")
print(tukey2.summary())
tukey2.plot_simultaneous()
plt.title("Tukey HSD: BMI by region and sex combinations")
plt.show()