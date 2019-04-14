from PIL import Image, ImageFilter



def image_data(path, dims=(128,128), max_images=-1):

    import os
    labels =[]
    values =[]
    i=0
    for filename in os.listdir(path):
        for filename2 in os.listdir(path +"/"+filename):
            labels.append(filename)
            im = Image.open(path + "/" + "/" +filename + "/" + filename2)
            pixels = list(im.resize(dims).getdata())
            values.append(pixels)
            i+=1
            if max_images > -1 and i > max_images:
                break
        if max_images > -1 and i > max_images:
            break
        print(filename)
    data_base = (labels,values)

    print(data_base)
    return data_base

images, labels = image_data("PeopleArt/JPEGImages", max_images=10)

# def image_to_data_set(path):
#     im = Image.open('PeopleArt\JPEGImages\Academicism')
#     import os
#
#     for filename in os.listdir('PeopleArt/JPEGImages'):
#         if filename.endswith(".jpg") or filename.endswith(".py"):
#             # print(os.path.join(directory, filename))
#             print("PIMP")
#             continue
#         else:
#             continue
# image_to_data_set('sag')
