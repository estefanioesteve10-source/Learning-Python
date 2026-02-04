import numpy as np
import pickle
import os
import tarfile

# 1. Função para extrair o arquivo baixado
def carregar_cifar_puro(caminho_arquivo):
    # Descompacta o .tar.gz se ainda não foi feito
    if not os.path.exists('cifar-10-batches-py'):
        with tarfile.open(caminho_arquivo, 'r:gz') as tar:
            tar.extractall()

    # O CIFAR-10 é dividido em "batches". Vamos carregar apenas o primeiro.
    with open('cifar-10-batches-py/data_batch_1', 'rb') as f:
        dict_dados = pickle.load(f, encoding='bytes')

    x_train = dict_dados[b'data'].astype("float32")
    y_train = np.array(dict_dados[b'labels'])

    # Carregar o batch de teste
    with open('cifar-10-batches-py/test_batch', 'rb') as f:
        dict_teste = pickle.load(f, encoding='bytes')

    x_test = dict_teste[b'data'].astype("float32")
    y_test = np.array(dict_teste[b'labels'])

    return x_train, y_train, x_test, y_test

# 2. Carregar os dados
# Certifique-se de que o nome do arquivo abaixo é o mesmo que você baixou
arquivo_baixado = 'cifar-10-python.tar.gz'
x_train_all, y_train_all, x_test_all, y_test_all = carregar_cifar_puro(arquivo_baixado)

# Reduzindo para 5000 imagens de treino e 5 de teste (para ser rápido)
x_train = x_train_all[:5000]
y_train = y_train_all[:5000]
x_test = x_test_all[:5]
y_test = y_test_all[:5]

# 3. Função kNN (Distância L2) - Pura Matemática NumPy
def predizer_knn(imagem_teste, base_treino, etiquetas_treino):
    # Subtração -> Quadrado -> Soma -> Raiz (L2)
    # axis=1 significa que somamos os pixels de cada imagem separadamente
    distancias = np.sqrt(np.sum((base_treino - imagem_teste)**2, axis=1))

    # Pega o índice da menor distância
    indice_vencedor = np.argmin(distancias)
    return etiquetas_treino[indice_vencedor]

# 4. Resultados
classes = ['aviao', 'carro', 'passaro', 'gato', 'veado', 'cao', 'sapo', 'cavalo', 'navio', 'caminhao']

print("\n--- Resultados kNN (Sem bibliotecas de IA) ---")
for i in range(5):
    pred = predizer_knn(x_test[i], x_train, y_train)
    print(f"Teste {i}: Previsto: {classes[pred]} | Real: {classes[y_test[i]]}")