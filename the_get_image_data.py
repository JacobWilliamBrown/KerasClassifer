def image_data(path):
    images = []
    labels = []
    import os

    for label_string in os.listdir(path):
        for file_name in os.listdir(path+"/"+label_string):
            from PIL import Image
            next_image = Image.open(path+"/"+label_string+"/"+file_name)
            images.append(next_image)
            labels.append(label_string)
            # next_image.show()
    return (images, labels)


# Resizing code.
ima, lab = image_data("PeopleArt/JPEGImages")
ima[0].resize((128, 128)).show()
print(lab[0])
