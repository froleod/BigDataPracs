import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler


def load_and_preprocess_data():
    """Загрузка и предобработка данных"""
    print("=" * 50)
    print("ЗАДАНИЕ 1 и 2: Загрузка и предобработка данных")
    print("=" * 50)

    # Загрузка датасета Wine
    data_bunch = load_wine()
    data = pd.DataFrame(data_bunch.data, columns=data_bunch.feature_names)
    data['target'] = data_bunch.target
    data['target_name'] = pd.Categorical.from_codes(data_bunch.target, data_bunch.target_names)

    # Вывод информации о данных
    print("Информация о датасете:")
    print(data.info())
    print("\nПервые 5 строк датасета:")
    print(data.head())
    print("\nПроверка на пропуски:")
    print(data.isnull().sum())

    # Нормализация данных
    features = data_bunch.feature_names
    X = data[features].values
    X_scaled = StandardScaler().fit_transform(X)
    y = data['target'].values

    return data, X_scaled, y, features


if __name__ == "__main__":
    data, X_scaled, y, features = load_and_preprocess_data()