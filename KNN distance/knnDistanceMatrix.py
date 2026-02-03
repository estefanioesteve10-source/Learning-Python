import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from keras.datasets import cifar10

# 1. Baixar o dataset (o Keras faz o download automático)
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# 2. Pré-processamento: Reduzir o tamanho para o kNN não demorar horas
# Vamos usar apenas 5000 imagens de treino e 500 de teste
x_train = x_train[:5000].reshape(5000, 3072) # 32x32x3 = 3072 pixels
y_train = y_train[:5000].ravel()
x_test = x_test[:500].reshape(500, 3072)
y_test = y_test[:500].ravel()

# 3. Criar e treinar o modelo kNN (k=3)
# Aqui você está aplicando a Distância L2 que o professor citou
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)

# 4. Fazer previsões
y_pred = knn.predict(x_test)

# 5. Ver o resultado
print(f"Acurácia do kNN: {accuracy_score(y_test, y_pred) * 100:.2f}%")