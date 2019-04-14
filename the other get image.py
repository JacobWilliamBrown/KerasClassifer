from PIL import Image, ImageFilter



def image_data(path):

    import os
    labels =[]
    values =[]
    for filename in os.listdir(path):
        for filename2 in os.listdir(path +"/"+filename):
            labels.append(filename)
            im = Image.open(path + "/" + "/" +filename + "/" + filename2)
            pixels = list(im.getdata())
            values.append(pixels)
        print(filename)
    data_base = (labels,values)

    print(data_base)

image_data("PeopleArt/JPEGImages")

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