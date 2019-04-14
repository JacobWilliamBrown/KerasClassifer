from PIL import Image, ImageFilter

import tensorflow as tf

def image_data(path, dims=(128,128), max_images=-1):
    import os
    labels =[]
    label_meanings = []
    values =[]
    i=0
    current_label = 0;
    num_labels = len(os.listdir(path))
    for filename in os.listdir(path):
        label_meanings.append(filename)
        for filename2 in os.listdir(path +"/"+filename):
            label = [0] * num_labels
            label[current_label] = 1
            labels.append(label)
            im = Image.open(path + "/" + "/" +filename + "/" + filename2)
            pixels = list(im.resize(dims).getdata())
            values.append(pixels)
            i+=1
            if max_images > -1 and i > max_images:
                break
        if max_images > -1 and i > max_images:
            break
        current_label += 1
    data_base = (labels,values, label_meanings)
    return data_base
def learn_model(images, labels, label_meaning):
    inputs = tf.keras.Input(shape=(3,128, 128))
    x = tf.keras.layers.Dense(4, activation=tf.nn.relu)(inputs)
    outputs = tf.keras.layers.Dense(5, activation=tf.nn.softmax)(x)
    model = tf.keras.Model(inputs=inputs, outputs=outputs)


images, labels, labels_value = image_data("PeopleArt/JPEGImages", max_images=10)

