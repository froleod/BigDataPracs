import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/lfrolov/Documents/mirea/7sem/BIGDATA/prac5/heart.csv")

print("Размерность данных:", df.shape)
print("Типы признаков:")
print(df.dtypes)
print("\nПервые строки:")
print(df.head())

# Проверим пропуски
print("\nКоличество пропусков в каждом столбце:")
print(df.isna().sum())


# ----- 2

sns.countplot(x='target', data=df, palette='pastel')
plt.title('Распределение классов (наличие болезни сердца)')
plt.xlabel('Наличие болезни (0 = нет, 1 = есть)')
plt.ylabel('Количество пациентов')
plt.show()

print(df['target'].value_counts(normalize=True))


# ----- 3

from sklearn.model_selection import train_test_split

X = df.drop(columns='target')
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

print("Размер обучающей выборки:", X_train.shape)
print("Размер тестовой выборки:", X_test.shape)


# ------- 4
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report

# Масштабируем данные (нужно для SVM и KNN)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
    'Логистическая регрессия': LogisticRegression(max_iter=500),
    'SVM': SVC(kernel='rbf', C=1, gamma='scale'),
    'KNN': KNeighborsClassifier(n_neighbors=5)
}

for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    cm = confusion_matrix(y_test, y_pred)
    print(f"\n{name}")
    print("Матрица ошибок:\n", cm)
    print("Отчёт классификации:\n", classification_report(y_test, y_pred))
