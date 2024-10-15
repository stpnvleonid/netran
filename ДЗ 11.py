import numpy as npy
import matplotlib.pyplot as mpl
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans

iris = load_iris()
X = iris.data[:, :2]
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

lda = LDA()
lda.fit(X_train, y_train)
y_pred = lda.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Точность модели LDA: {accuracy:.2f}")

if accuracy > 0.7:
    print("Точность выше 0.7 - соответствует критерию.")
else:
    print("Точность не соответствует критерию.")

mpl.figure(figsize=(8, 8))
colors = ['blue', 'green', 'brown']
for i, color in enumerate(colors):
    mpl.scatter(X_test[y_test == i, 0], X_test[y_test == i, 1], color=color, label=f'Class {i} (True)')
    mpl.scatter(X_test[y_pred == i, 0], X_test[y_pred == i, 1], color=color, marker='+', label=f'Class {i} (Predicted)')

class_centers = lda.means_
mpl.scatter(class_centers[:, 0], class_centers[:, 1], color='orange', marker='o', s=100, label='Class Centers')

mpl.title('LDA Classification')
mpl.xlabel('Sepal Length')
mpl.ylabel('Sepal Width')
mpl.legend()
mpl.grid(True)
mpl.show()

num_classes = len(npy.unique(y))
kmeans = KMeans(n_clusters=num_classes, random_state=42)
kmeans.fit(X)

mpl.figure(figsize=(8, 8))
for i in range(num_classes):
    mpl.scatter(X[kmeans.labels_ == i, 0], X[kmeans.labels_ == i, 1], label=f'Cluster {i}')

mpl.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='red', marker='x', s=100, label='Cluster Centers')

mpl.title(f'KMeans Clustering (n_clusters = {num_classes})')
mpl.xlabel('Sepal Length')
mpl.ylabel('Sepal Width')
mpl.legend()
mpl.grid(True)
mpl.show()

print(f"Количество кластеров: {num_classes}, что соответствует целевой переменной.")