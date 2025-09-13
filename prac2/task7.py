# umap_visualization_fixed.py
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_wine
import time
import sys

# Проверка доступности UMAP
try:
    from umap import UMAP

    print("UMAP импортирован успешно")
except ImportError:
    print("UMAP не найден. Установленные пакеты:")
    import pkg_resources

    installed_packages = pkg_resources.working_set
    for package in installed_packages:
        print(f"{package.key}=={package.version}")
    sys.exit(1)


def run_umap_visualization():
    """Визуализация данных с помощью UMAP (Задание 7)"""
    print("\n" + "=" * 50)
    print("ЗАДАНИЕ 7: Визуализация многомерных данных (UMAP)")
    print("=" * 50)

    # Используем Wine dataset (быстрее и проще)
    print("Загрузка датасета Wine...")
    wine = load_wine()
    X, y = wine.data, wine.target

    # Нормализация
    X_scaled = StandardScaler().fit_transform(X)

    n_neighbors_list = [5, 15, 30]
    min_dist_list = [0.1, 0.5]
    umap_results = {}

    for n_neighbors in n_neighbors_list:
        for min_dist in min_dist_list:
            print(f"Выполняется UMAP с n_neighbors={n_neighbors}, min_dist={min_dist}...")
            start_time = time.time()
            reducer = UMAP(n_neighbors=n_neighbors, min_dist=min_dist, random_state=42)
            X_umap = reducer.fit_transform(X_scaled)
            exec_time = time.time() - start_time
            umap_results[(n_neighbors, min_dist)] = (X_umap, exec_time)
            print(f"Время выполнения: {exec_time:.2f} секунд.")

    # Визуализация результатов
    fig, axes = plt.subplots(len(min_dist_list), len(n_neighbors_list), figsize=(15, 8))

    for i, min_dist in enumerate(min_dist_list):
        for j, n_neighbors in enumerate(n_neighbors_list):
            X_umap, exec_time = umap_results[(n_neighbors, min_dist)]

            # Обработка разных конфигураций subplots
            if len(min_dist_list) > 1 and len(n_neighbors_list) > 1:
                ax = axes[i, j]
            elif len(min_dist_list) > 1:
                ax = axes[i]
            elif len(n_neighbors_list) > 1:
                ax = axes[j]
            else:
                ax = axes

            scatter = ax.scatter(X_umap[:, 0], X_umap[:, 1], c=y, cmap='Spectral', s=50, alpha=0.8)
            ax.set_title(f'n_neighbors={n_neighbors}, min_dist={min_dist}\nTime: {exec_time:.2f}s')

            # Добавляем colorbar только для последнего графика
            if i == len(min_dist_list) - 1 and j == len(n_neighbors_list) - 1:
                plt.colorbar(scatter, ax=ax)

    plt.tight_layout()
    plt.savefig('umap_comparison.png', dpi=150, bbox_inches='tight')
    print("Графики UMAP сохранены в файл 'umap_comparison.png'")
    plt.show()


if __name__ == "__main__":
    run_umap_visualization()