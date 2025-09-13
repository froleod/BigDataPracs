# tsne_visualization.py
import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import fetch_openml
import time

def run_tsne_visualization():
    """Визуализация данных с помощью t-SNE (Задание 6)"""
    print("\n" + "=" * 50)
    print("ЗАДАНИЕ 6: Визуализация многомерных данных (t-SNE)")
    print("=" * 50)

    # Загрузка MNIST
    print("Загрузка MNIST... (это может занять несколько минут)")
    mnist = fetch_openml('mnist_784', version=1, as_frame=False, parser='auto')
    X_mnist, y_mnist = mnist['data'], mnist['target'].astype(int)

    # Подвыборка для экономии времени
    sample_size = 3000
    np.random.seed(42)
    sample_idx = np.random.permutation(len(X_mnist))[:sample_size]
    X_mnist_sample = X_mnist[sample_idx]
    y_mnist_sample = y_mnist[sample_idx]
    X_mnist_scaled = StandardScaler().fit_transform(X_mnist_sample)

    perplexities = [5, 30, 100]
    tsne_results = {}

    for perplexity in perplexities:
        print(f"Выполняется t-SNE с perplexity={perplexity}...")
        start_time = time.time()
        tsne = TSNE(n_components=2, perplexity=perplexity, random_state=42, n_iter=1000)
        X_tsne = tsne.fit_transform(X_mnist_scaled)
        exec_time = time.time() - start_time
        tsne_results[perplexity] = (X_tsne, exec_time)
        print(f"Время выполнения: {exec_time:.2f} секунд.")

    # Визуализация результатов
    plt.figure(figsize=(18, 5))
    for i, (perplexity, (X_tsne, exec_time)) in enumerate(tsne_results.items()):
        plt.subplot(1, len(perplexities), i + 1)
        scatter = plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y_mnist_sample, cmap='Spectral', s=10, alpha=0.7)
        plt.colorbar(scatter, boundaries=np.arange(11) - 0.5).set_ticks(np.arange(10))
        plt.title(f't-SNE, perplexity={perplexity}\nTime: {exec_time:.2f}s')
        plt.axis('off')

    plt.tight_layout()
    plt.savefig('tsne_comparison.png', dpi=150, bbox_inches='tight')
    print("Графики t-SNE сохранены в файл 'tsne_comparison.png'")
    plt.close()

if __name__ == "__main__":
    run_tsne_visualization()