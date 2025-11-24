import pandas as pd
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler

# 1
wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)

print("Размерность:", df.shape)
print(df.head())

# Масштабирование
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# 2
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np

K_range = range(2, 11)
inertias = []
sil_scores = []

for k in K_range:
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = km.fit_predict(X_scaled)
    inertias.append(km.inertia_)
    sil_scores.append(silhouette_score(X_scaled, labels))

# Метод локтя
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(list(K_range), inertias, '-o')
plt.xlabel('k')
plt.ylabel('inertia (SSE)')
plt.title('Elbow method')

# Метод силуэта
plt.subplot(1,2,2)
plt.plot(list(K_range), sil_scores, '-o')
plt.xlabel('k')
plt.ylabel('mean silhouette score')
plt.title('Silhouette score vs k')
plt.show()

#
# for k, s in zip(K_range, sil_scores):
#     print(f"k={k}  silhouette={s:.4f}")


k_opt = 3
kmeans = KMeans(n_clusters=k_opt, n_init=20, random_state=42)
labels_km = kmeans.fit_predict(X_scaled)
centers = kmeans.cluster_centers_
print("Inertia:", kmeans.inertia_)
print("Silhouette (kmeans):", silhouette_score(X_scaled, labels_km))


# 3
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import matplotlib.pyplot as plt

Z = linkage(X_scaled, method='ward')

plt.figure(figsize=(12,6))
dendrogram(Z, truncate_mode='level', p=5, leaf_rotation=90., leaf_font_size=10.)
plt.title("Дендрограмма (ward) — усечённая")
plt.xlabel("Объекты")
plt.ylabel("Расстояние")
plt.show()

k_h = 3
labels_h = fcluster(Z, k_h, criterion='maxclust')
from sklearn.metrics import silhouette_score
print("Silhouette (hierarchical):", silhouette_score(X_scaled, labels_h))

# 4
from sklearn.neighbors import NearestNeighbors
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# параметры
min_samples = 5
nbrs = NearestNeighbors(n_neighbors=min_samples).fit(X_scaled)
distances, indices = nbrs.kneighbors(X_scaled)

k_distances = np.sort(distances[:, -1])

plt.figure(figsize=(8,4))
plt.plot(k_distances)
plt.ylabel(f"{min_samples}-distance")
plt.xlabel("sorted points")
plt.title("k-distance plot (для подбора eps)")
plt.show()


eps = 2.3
db = DBSCAN(eps=eps, min_samples=min_samples)
labels_db = db.fit_predict(X_scaled)
unique_labels = np.unique(labels_db)
print("Unique labels (DBSCAN):", unique_labels)
print("Num noise points:", np.sum(labels_db == -1))
# silhouette на ненулевых кластерах:
mask = labels_db != -1
if len(np.unique(labels_db[mask])) > 1:
    print("Silhouette DBSCAN:", silhouette_score(X_scaled[mask], labels_db[mask]))
else:
    print("Silhouette DBSCAN: Невычислимо (мало кластеров)")


# 5
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

tsne = TSNE(n_components=2, perplexity=30, random_state=42, n_iter=1000)
X_tsne = tsne.fit_transform(X_scaled)

fig, axes = plt.subplots(1, 3, figsize=(18,5))
axes[0].scatter(X_tsne[:,0], X_tsne[:,1], c=labels_km, cmap='tab10', s=10)
axes[0].set_title("KMeans (k=%d)" % k_opt)

axes[1].scatter(X_tsne[:,0], X_tsne[:,1], c=labels_h, cmap='tab10', s=10)
axes[1].set_title("Hierarchical (k=%d)" % k_h)

axes[2].scatter(X_tsne[:,0], X_tsne[:,1], c=labels_db, cmap='tab10', s=10)
axes[2].set_title("DBSCAN (eps=%.2f)" % eps)
plt.show()
