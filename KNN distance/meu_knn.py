import numpy as np
import torch
import torchvision
import torchvision.datasets as datasets

# 1. Carregar os dados (isso vai criar uma pasta 'data' no seu PC)
print("Baixando CIFAR-10... aguarde.")
train_data = datasets.CIFAR10(root='./data', train=True, download=True)
test_data = datasets.CIFAR10(root='./data', train=False, download=True)

# 2. Transformar as imagens em matrizes NumPy "achatadas"
# x_train terá 5000 imagens de 3072 pixels cada (32x32x3)
x_train = train_data.data[:5000].reshape(5000, -1).astype("float32")
y_train = np.array(train_data.targets[:5000])

# Vamos pegar 5 imagens de teste para comparar
x_test = test_data.data[:5].reshape(5, -1).astype("float32")
y_test = np.array(test_data.targets[:5])

# 3. A mesma função de predição que você já entendeu
def predizer(imagem_teste, base_treino):
    # L2: Raiz da soma dos quadrados das diferenças
    distancias = np.sqrt(np.sum(np.square(base_treino - imagem_teste), axis=1))
    return np.argmin(distancias)

# 4. Resultados
classes = ['aviao', 'carro', 'passaro', 'gato', 'veado', 'cao', 'sapo', 'cavalo', 'navio', 'caminhao']

print("\n--- Comparando imagens com kNN (L2) ---")
for i in range(5):
    idx = predizer(x_test[i], x_train)
    print(f"Teste {i}: Previsto: {classes[y_train[idx]]} | Real: {classes[y_test[i]]}")