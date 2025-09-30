import pandas as pd
import numpy as np

# Задание 9. Загрузка данных
df = pd.read_csv("/Users/lfrolov/Documents/mirea/7sem/BIGDATA/prac3/ECDCCases.csv")


# Задание 10. Работа с пропусками
# Считаем количество пропусков в процентах
missing_percent = df.isna().mean() * 100
print("\nПропуски в процентах:\n", missing_percent.sort_values(ascending=False))

# Удаляем два признака с наибольшим количеством пропусков
cols_to_drop = missing_percent.sort_values(ascending=False).head(2).index
df = df.drop(columns=cols_to_drop)
print("\nУдалили признаки:", list(cols_to_drop))

# Для оставшихся: категориальные -> 'other', числовые -> медиана
for col in df.columns:
    if df[col].dtype == "object":  # категориальный
        df[col] = df[col].fillna("other")
    else:  # числовой
        df[col] = df[col].fillna(df[col].median())

# Проверяем, что пропусков больше нет
print("\nПропуски после обработки:\n", df.isna().sum().sum())

# Задание 11. Статистика и выбросы
print("\nСтатистика по данным:\n", df.describe(include="all"))

# Выбросы можно искать по размаху (IQR)
numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    outliers = df[(df[col] < q1 - 1.5*iqr) | (df[col] > q3 + 1.5*iqr)]
    print(f"Признак {col}: выбросов {outliers.shape[0]}")

# Для каких стран число смертей в день превысило 3000
if "deaths" in df.columns:
    df_high = df[df["deaths"] > 3000]
    print("\nСтраны с >3000 смертей в день:")
    print(df_high.groupby("countriesAndTerritories")["dateRep"].count())

# Задание 12. Дубликаты
duplicates = df.duplicated().sum()
print("Размерность до удаления дубликатов:", df.shape)

print("\nКоличество дубликатов:", duplicates)

df = df.drop_duplicates()
print("Размерность после удаления дубликатов:", df.shape)
