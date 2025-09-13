# matplotlib_plots.py
import matplotlib.pyplot as plt
import pandas as pd


def create_line_plots(data, features):
    """Создание линейных графиков (Задание 5)"""
    print("\n" + "=" * 50)
    print("ЗАДАНИЕ 5: Построение линейных графиков")
    print("=" * 50)

    plt.figure(figsize=(12, 6))

    # Берем первый класс и первые 3 признака
    class_0_data = data[data['target'] == 0]
    class_0_data_sorted = class_0_data.sort_values(by=features[0])
    features_to_plot = features[1:4]  # Берем следующие 3 признака

    for feature in features_to_plot:
        plt.plot(class_0_data_sorted[features[0]],
                 class_0_data_sorted[feature],
                 marker='o',
                 label=feature,
                 linewidth=2,
                 color='crimson',
                 markerfacecolor='white',
                 markeredgecolor='black',
                 markeredgewidth=2)

    plt.title(f'Зависимость признаков от "{features[0]}" (Класс 0)')
    plt.xlabel(features[0])
    plt.ylabel('Значение признака')
    plt.legend()
    plt.grid(True, color='mistyrose', linewidth=2)

    plt.savefig('matplotlib_line_plot.png', dpi=150, bbox_inches='tight')
    print("Линейный график сохранен в файл 'matplotlib_line_plot.png'")
    plt.close()


if __name__ == "__main__":
    from data_loading import load_and_preprocess_data

    data, X_scaled, y, features = load_and_preprocess_data()
    create_line_plots(data, features)