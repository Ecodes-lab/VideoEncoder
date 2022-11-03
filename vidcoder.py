# import argparse
# import configparser
# import os
# import cv2
# import numpy as np
from moviepy.editor import *
import moviepy.video.fx.all as vfx


clip = VideoFileClip("/root/videos/file_5df3e762980db.mp4")
clip_resized = clip.fx( vfx.resize, (1280,720) )
clip_resized.write_videofile("/root/vidtranscoder/videos/output2.mp4")

#! /usr/bin/env python3

import PIL
from PIL import Image
import os
import json
import time
import argparse



class ImgSizer:
    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-s", "--size", dest="size", help="Specify a Size")
        parser.add_argument("-q", "--quality", dest="quality", help="Specify the quality")
        parser.add_argument("-r", "--recompress", dest="recompress", help="Recompress Images")
        options = parser.parse_args()

        if not options.size:
            parser.error("[-] Specify a size --help for more details")
        elif not options.quality:
            parser.error("[-] Specify a quality --help for more details")
        elif options.recompress and not options.recompress == "1" and not options.recompress == "0":
            parser.error("[-] Specify a correct value for -r or --recompress, --help for more details")

        return options


    def imgsizer(self, size, quality, recompress=None):
        print("[+] Image Resizer Bot Has Started")
        try:
            self.dir = os.getcwd().replace("\\", "/")
            for f in os.listdir(self.dir):
                if f.endswith(".jpg") or f.endswith(".jpeg ") or f.endswith(".png") or f.endswith(".gif"):
                    Image.MAX_IMAGE_PIXELS = None
                    try:
                        self.i = Image.open(self.dir + "/" + f)
                    except:
                        pass
                    self.fn, self.fext = os.path.splitext(f)
                    try:
                        # if self.fn.endswith('thumb'):
                        if self.i.size[0] >= int(size):
                            self.resize(size, quality, recompress)


                        # elif fn.replace("thumb", ""):
                        #     # if fn.endswith('thumb'):
                        #     filename.append(fn)
                        #     if fn not in old_fn:
                        #         if i.size[0] >= 1600:
                        #             new_height = int(size / i.width * i.height)
                        #
                        #             try:
                        #                 os.mkdir(dir + "/" + str(size))
                        #             except:
                        #                 pass
                        #
                        #             try:
                        #                 img_folder = '{}/{}'.format(dir, size)
                        #                 if os.path.exists(img_folder):
                        #                     # PIL.Image.ANTIALIAS
                        #
                        #                     i.thumbnail((size, new_height))
                        #                     i.save('{}/{}/{}{}'.format(dir, size, fn, fext), optimize=True,
                        #                            quality=50)
                        #                     print("Image Resized!")
                        #                 else:
                        #                     print("Image Could Not Be Resized")
                        #             except:
                        #                 pass


                    except:
                        pass

        except:
            pass

    def resize(self, size, quality, recompress):
        if recompress == "1":
            self.new_height = int(int(size) / self.i.width * self.i.height)

            try:
                os.mkdir(self.dir + "/" + str(size))
            except:
                pass

            try:
                self.img_folder = '{}/{}'.format(self.dir, size)
                if os.path.exists(self.img_folder):
                    self.i.thumbnail((int(size), self.new_height))
                    self.i.save('{}/{}/{}{}'.format(self.dir, size, self.fn, self.fext), optimize=True,
                                quality=int(quality))
                    # with open('fn.json', 'w', encoding='utf-8') as outfile:
                    #     stored_fn.apend(fn)
                    #     json.dump(stored_fn, outfile, ensure_ascii=False, indent=4)
                    print(self.fn + " Resized into " + str(size) + " folder!")
                else:
                    print(self.fn + " Could not be resized")
                    # return
            except:
                pass
        elif not os.path.exists('{}/{}/{}{}'.format(self.dir, size, self.fn, self.fext)):

            self.new_height = int(int(size) / self.i.width * self.i.height)

            try:
                os.mkdir(self.dir + "/" + str(size))
            except:
                pass

            try:
                self.img_folder = '{}/{}'.format(self.dir, size)
                if os.path.exists(self.img_folder):
                    self.i.thumbnail((int(size), self.new_height))
                    self.i.save('{}/{}/{}{}'.format(self.dir, size, self.fn, self.fext), optimize=True,
                           quality=int(quality))
                    # with open('fn.json', 'w', encoding='utf-8') as outfile:
                    #     stored_fn.apend(fn)
                    #     json.dump(stored_fn, outfile, ensure_ascii=False, indent=4)
                    print(self.fn + " Resized into " + str(size) + " folder!")
                else:
                    print(self.fn + " Could not be resized")
                    # return
            except:
                pass
        else:
            print(self.fn + " already exist")
            # continue

if __name__ == '__main__':
    # while True:
    i = ImgSizer()
    image = i.get_args()
    i.imgsizer(image.size, image.quality, image.recompress)


