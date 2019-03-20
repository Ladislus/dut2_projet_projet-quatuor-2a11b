from base64 import *

def make_blob(filename):
    extension = ""
    cur_file = filename.split("/")[-1]
    if ("." in cur_file[1:]):
        extension = filename.split(".")[-1]
    else:
        extension = "null"
#    file = open(filename, "r")
#    print(file)
#    data = file.read()
#    encoded_data = b64encode(data.encode("utf-8"))
    # print(filename)
    with open(filename, "rb") as current_file:
        encoded_string = b64encode(current_file.read())
        # print(encoded_string)
    return (encoded_string, extension)

# def from_blob(blob, entension):
#     if extension == "null":
# 	with open("output") as output_file:
#
#     with open("output" +


# print(make_blob("/home/abid/.bashrc"))
# print(make_blob("./test1.jpg"))
# print(make_blob("./test.png"))
# print(make_blob("./DarkSideOfTheRainbow.png"))



def make_file(filename, blob):
    data, ext = blob
    print(ext)
    if ext is "null":
        print("sans Ext")
        fh = open(filename, "wb")
    else:
        print("avec Ext")
        fh = open(filename+'.'+ext, "wb")
    fh.write(b64decode(data))
    fh.close()



make_file("test_bashrc",make_blob("/home/abid/.bashrc"))
make_file("test_image",make_blob("./test1.jpg"))
