def image_data(path):

    import os

    for filename in os.listdir(path):
        print(filename)

    # import PIL
    # next_image = Image.open(path)
    # next_image.show()
image_data("PeopleArt/JPEGImages")
