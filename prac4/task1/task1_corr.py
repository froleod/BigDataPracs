import numpy as np
from scipy import stats

# данные
street = np.array([80, 98, 75, 91, 78])
garage = np.array([100, 82, 105, 89, 102])

# коэффициент Пирсона
r, p = stats.pearsonr(street, garage)


print(f"Pearson r = {r:.4f}, p-value = {p:.4f}")
# сильная отрицательная корреляция