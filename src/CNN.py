# Importando bibliotecas necessárias
import tensorflow as tf
from keras.preprocessing import image
from tensorflow.keras.callbacks import ModelCheckpoint
from matplotlib import pyplot as plt
import numpy as np
import cv2
import os

# Obtendo o diretório de trabalho padrão
default_path = os.getcwd()

# Definindo caminhos para os diretórios do conjunto de dados
dataset_path = os.path.join(default_path, 'DATASET')
test_path = os.path.join(dataset_path, 'test')
training_path = os.path.join(dataset_path, 'training')
validation_path = os.path.join(dataset_path, 'validation')

# Carregando conjuntos de dados de imagens
test_dataset = tf.keras.utils.image_dataset_from_directory(
    test_path,
    image_size=(180, 180),
    batch_size=12
)

training_dataset = tf.keras.utils.image_dataset_from_directory(
    training_path,
    image_size=(180, 180),
    batch_size=12
)

validation_dataset = tf.keras.utils.image_dataset_from_directory(
    validation_path,
    image_size=(180, 180),
    batch_size=12
)

# Definindo otimização de leitura de dados para melhor desempenho
AUTOTUNE = tf.data.AUTOTUNE
training_dataset = training_dataset.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
validation_dataset = validation_dataset.cache().prefetch(buffer_size=AUTOTUNE)

# Configurando a data augmentation para as imagens
data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal", input_shape=(180, 180, 3)),
    tf.keras.layers.RandomRotation(0.1),
    tf.keras.layers.RandomZoom(0.2)
])

# Criando o modelo de rede neural
model = tf.keras.Sequential([
    data_augmentation,
    tf.keras.layers.Rescaling(1./255),

    tf.keras.layers.Conv2D(16, kernel_size=(3, 3), activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPool2D(pool_size=(3, 3)),

    tf.keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPool2D(pool_size=(3, 3)),

    tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPool2D(pool_size=(3, 3)),

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(2, activation="sigmoid")
])

# Compilando o modelo
model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    optimizer='adam',
    metrics=['accuracy']
)

# Treinando o modelo e salvando checkpoints
epochs = 100
callback = [
    ModelCheckpoint(
        filepath="version",
        save_best_only=True,
        monitor="val_loss",
        save_format="tf"
    )
]
history = model.fit(
    training_dataset,
    epochs=epochs,
    validation_data=validation_dataset,
    callbacks=callback
)

# Exibindo informações do modelo
model.summary()

# Carregando o modelo treinado e avaliando-o
model = tf.keras.models.load_model("version")
test_loss, test_acc = model.evaluate(test_dataset)

# Plotando gráfico com os resultados
names = ['Perda', 'Precisão']
values = [(test_loss * 100), (test_acc * 100)]
colors = ['red', 'blue']

plt.figure(figsize=(15, 2))
plt.barh(names, values, color=colors)
plt.title('Teste do Modelo')

for index, value in enumerate(values):
    plt.text(value, index, str(f'{value:.2f}%'))
plt.show()

# Obtendo informações de precisão e perda ao longo das épocas
accuracy = history.history["accuracy"]
val_accuracy = history.history["val_accuracy"]

loss = history.history["loss"]
val_loss = history.history["val_loss"]

epochs = range(0, len(accuracy))

# Plotando gráficos de precisão e perda
plt.figure()

plt.subplot(121)
plt.plot(epochs, accuracy, color='red', label="Precisão do treino")
plt.plot(epochs, val_accuracy, color='blue', label='Precisão da validação')
plt.xlabel('Épocas')
plt.ylabel('Taxas de precisão (%)')
plt.title('Taxas de precisão')
plt.grid(True)
plt.legend()

plt.subplot(122)
plt.plot(epochs, loss, color='red', label="Perda no treino")
plt.plot(epochs, val_loss, color='blue', label="Perda na validação")
plt.xlabel('Épocas')
plt.ylabel('Taxa de erro (%)')
plt.title('Taxas de Erro')
plt.grid(True)
plt.legend()

plt.subplots_adjust(top=1.0, right=2.0)
plt.show()

# Função para exibir uma única imagem
def showSingleImage(img, title, size):
    fig, axis = plt.subplots(figsize=size)
    axis.imshow(img, 'gray')
    axis.set_title(title, fontdict={'fontsize': 20, 'fontweight': 'medium'})
    plt.show()

# Carregando uma imagem e exibindo-a
img_name = "..\\DATASET\\validation\\no_deforestation\\imagem_020.png"
def_img = cv2.imread(img_name)
def_img = cv2.cvtColor(def_img, cv2.COLOR_BGR2RGB)
showSingleImage(def_img, "Teste de mesa", (12, 8))

# Carregando a mesma imagem para previsão com o modelo
def_img = image.load_img(img_name, target_size=(180, 180))
x = image.img_to_array(def_img)
x = np.expand_dims(x, axis=0)
pred = (model.predict(x) > 0.5).astype('int32')[0][0]

# Exibindo o resultado da previsão
if pred == 1:
    print(f'Desmatado: {model.predict(x)}')
else:
    print(f'Não desmatado: {model.predict(x)}')
