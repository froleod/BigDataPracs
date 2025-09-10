from sklearn.datasets import fetch_california_housing

california_housing = fetch_california_housing(as_frame=True)
data = california_housing.frame

# 8. Использовать метод info()
print("8. Информация о датафрейме:")
data.info()
print("\n" + "="*50 + "\n")

# 9. Узнать, есть ли пропущенные значения
print("9. Пропущенные значения:")
print(data.isna().sum())
print("\n" + "="*50 + "\n")

# 10. Вывести записи, где средний возраст домов > 50 лет и население > 2500
print("10. Дома старше 50 лет и население > 2500:")
filtered_data = data.loc[(data['HouseAge'] > 50) & (data['Population'] > 2500)]
print(filtered_data)
print("\n" + "="*50 + "\n")

# 11. Максимальное и минимальное значения медианной стоимости дома
med_house_val = data['MedHouseVal']
print("11. Медианная стоимость домов:")
print(f"Максимальная: {med_house_val.max():.3f} млн долларов")
print(f"Минимальная: {med_house_val.min():.3f} млн долларов")
print("\n" + "="*50 + "\n")

# 12. Использовать apply() для вывода названия признака и его среднего значения
print("12. Средние значения признаков:")
def print_mean(series):
    print(f"{series.name}: {series.mean():.3f}")

data.apply(print_mean) # Фролов ЛД ИКБО-20-22