import os
from conf.path import WEBPICTURE_PATH


class Tool(object):
    def __init__(self):
        self.filelist = os.listdir(WEBPICTURE_PATH)

    def error_picture(self):
        picture = []
        for item in self.filelist:
            if item.endswith('.jpg'):
                picture.append((item,))
        return picture

    def clear_picture(self):
        list(map(os.remove, map(lambda file: WEBPICTURE_PATH + file, self.filelist)))
