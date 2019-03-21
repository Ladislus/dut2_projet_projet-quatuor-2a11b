from .views import *
from base64 import *


def make_blob(filename):
    extension = ""
    cur_file = filename.split("/")[-1]
    if ("." in cur_file[1:]):
        extension = filename.split(".")[-1]
    else:
        extension = "null"
    with open(filename, "rb") as current_file:
        encoded_string = b64encode(current_file.read())
    return (encoded_string, extension)

def make_file(filename, blob):
    data, ext = blob
    if ext is "null":
        fh = open(filename, "wb")
    else:
        fh = open(filename+'.'+ext, "wb")
    fh.write(b64decode(data))
    fh.close()
