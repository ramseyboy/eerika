#!/usr/bin/env python3
import os
import PIL
from PIL import Image


class Resizer():

    def __init__(self, dirname):
        self._resized_dir_name = "resized/"
        self._dirname = dirname
        self._img_counter = {'total': 0, 'success': 0, 'failed': 0}

    def process_images(self):
        if os.path.isdir(self._dirname):
            for filename in os.listdir(self._dirname):
                if os.path.isfile(self._dirname + "/" + filename):
                    self.resize_image(self._dirname + "/" + filename)
        else:
            self.resize_image(self._dirname)
        print("Of", self._img_counter['total'], "image(s):", self._img_counter['failed'],
        "failed and", self._img_counter['success'],  "passed")

    def resize_image(self, filename):
        try:
            self._img_counter['total'] = self._img_counter['total'] + 1   

            img = Image.open(filename)
            basewidth = 300
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
            if not os.path.exists(os.path.join(self._dirname, self._resized_dir_name)):
                os.mkdir(os.path.join(self._dirname, self._resized_dir_name))

            resizedFilename = '{0}'.format(os.path.basename(filename))

            if os.path.exists(resizedFilename):
                os.remove(resizedFilename)

            img.save(os.path.join(self._dirname, self._resized_dir_name, resizedFilename))

            self._img_counter['success'] = self._img_counter['success'] + 1
        except IOError as e:
            self._img_counter['failed'] = self._img_counter['failed'] + 1           
            print(e)

if __name__ == '__main__':      
    r = Resizer("photos")
    r.process_images()
