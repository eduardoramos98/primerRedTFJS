import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt



fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_label)= fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat','Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# train_images.shape
# plt.figure()
# plt.imshow(train_images[0])
# plt.colorbar()
# plt.grid(False)
# plt.show()

train_images=train_images/255.0
test_images=test_images/255.0

# plt.figure(figsize=(10,10))
# for i in range(25):
#     plt.subplot(5,5,i+1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.grid(False)
#     plt.imshow(train_images[i], cmap=plt.cm.binary,)
#     plt.xlabel(class_names[train_labels[i]])
# plt.show()

model =  keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),  #Transforma el formato de un arreglo bidimencional(de 28*28 pixeles) a un arreglo unidimensional 784px
    keras.layers.Dense(128, activation='relu'),  #capa 1 tiene 128 nodos o neuronas
    keras.layers.Dense(10, activation= 'softmax')    #capa2 tiene 10 nodos softmax que devuelven un arreglo 10 probabilidades que seman a 1 

])
#lOSS FUCTION: mide que tan exacto es el modelo durante el entrenamiento.
#OPTIMIZER: esto es como el modelo se actuliza basado en el set de datos que ve y la funcion de perdida
#METRICS: se usan para monitorear los pasos de entrenamiento y pruebas

print("Compilado el modelo")
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=10)

test_loss, test_acc = model.evaluate(test_images, test_label, verbose=2)
print('\nTest accuacy: ', test_acc)

prediccion = model.predict(test_images)
prediccion[0]

#Articulo con mayor nivel de confianza
np.argmax(prediccion[0])

def mostrarImg(i, arreglo_pred, true_label, img):
    arreglo_pred, true_label, img = arreglo_pred, true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    
    plt.imshow(img, cmap=plt.cm.binary)
    
    predicted_label=np.argmax(arreglo_pred)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color='red'
    plt.xlabel("{}{:2.0f}%({})".format(class_names[predicted_label], 100*np.max(arreglo_pred),class_names[true_label]),color=color)
    
def plot_value_array(i, prediction_array, true_label):
    prediction_array, true_label = prediction_array, true_label[i]
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    thisplot = plt.bar(range(10), prediction_array, color="#777777")
    plt.ylim([0,1])
    predicted_label = np.argmax(prediction_array)
        
    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')
    
num_row = 5
num_cols = 3

num_images = num_row*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_row))
for i in range (num_images):
    plt.subplot(num_row, 2*num_cols, 2*i+1)
    mostrarImg(i, prediccion[i], test_label, test_images)
    plt.subplot(num_row, 2*num_cols, 2*i+2)
    plot_value_array(i, prediccion[i], test_label)
plt.tight_layout()
plt.show()



#https://www.tensorflow.org/tutorials/keras/classification?hl=es-419