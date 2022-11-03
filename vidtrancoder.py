#! /usr/bin/env python3

from moviepy.editor import *
import moviepy.video.fx.all as vfx
import os
import json
import time
from digital_ocean_space import upload_to_space


class VideoTranscoder:
    def vidcoder(self):
        print("[+] Video Transcoder Bot Has Started")
        # self.filename = []
        with open('/root/vidtranscoder/fn.json') as f:
            self.stored_fn = json.load(f)

        while True:
            with open('/root/vidtranscoder/config.json') as f:
                self.configs = json.load(f)
            try:
                for self.dir in self.configs['dirs']:
                    
                    for self.f in os.listdir(self.dir):
                        if self.f.endswith(".mp4") or self.f.endswith(".avi") or self.f.endswith(".mov") or self.f.endswith(".mkv"):
                            file = [f for f in self.configs['dirs'][self.dir] if not "{}_{}".format(f, self.f) in self.stored_fn]
                            # print(self.f)
                            if file:
                                try:
                                    self.clip = VideoFileClip(self.dir + "/" + self.f)
                                except:
                                    pass
                                

                                # print(self.clip.size)
                                # print(self.clip.w)
                                # print(self.clip.h)

                                # if self.i.size[0] * self.i.size[1] > arbitary_large_limit:
                                #     raise ImageIsToBigError("image size exceeds limit")
                                self.fn, self.fext = os.path.splitext(self.f)

                                try:
                                    self.clip.save_frame("{}/{}.jpg".format(self.configs['stored_images_dir'], self.fn))
                                    upload_to_space('{}/{}.jpg'.format(self.configs['stored_images_dir'], self.fn), 'images/{}.jpg'.format(self.fn,))
                                    self.remove = self.configs['dirs'][self.dir]
                                    if self.clip.h >= 1080:
                                        self.resize()
                                    elif self.clip.h >= 720:
                                        try:
                                            self.remove.remove(1080)
                                        except:
                                            pass
                                        self.resize()
                                    elif self.clip.h >= 480:
                                        try:
                                            self.remove.remove(1080)
                                            self.remove.remove(720)
                                        except:
                                            pass
                                        self.resize()
                                    elif self.clip.h >= 240:
                                        try:
                                            self.remove.remove(1080)
                                            self.remove.remove(720)
                                            self.remove.remove(480)
                                        except:
                                            pass
                                        self.resize()

                                except:
                                    pass
                            else:
                                continue


            except KeyboardInterrupt:
                print("[-] Image Resizer Bot Terminated")

    def resize(self):
        for width, height in zip(self.configs['dirs'][self.dir]["width"], self.configs['dirs'][self.dir]["height"]):
            if not os.path.exists('{}/{}/{}{}'.format(self.dir, height, self.fn, self.fext)) and not "{}_{}".format(height, self.f) in self.stored_fn:

                # self.new_width = int(height / self.clip.h * self.clip.w)
                
                try:
                    os.mkdir(self.configs['stored_videos_dir'] + "/" + str(height))
                except:
                    pass

                try:
                    self.vid_folder = '{}/{}'.format(self.configs['stored_videos_dir'], height)
                    if os.path.exists(self.vid_folder):
                        clip_resized = self.clip.fx( vfx.resize, (width, height) )
                        clip_resized.write_videofile('{}/{}/{}{}'.format(self.configs['stored_videos_dir'], height, self.fn, self.fext))
                        try:
                            upload_to_space('{}/{}/{}{}'.format(self.configs['stored_videos_dir'], height, self.fn, self.fext), 'videos/{}/{}{}'.format(height, self.fn, self.fext), width=width, height=height)
                        except:
                            pass

                        self.stored_fn.append("{}_{}".format(height, self.f))
                        print(self.fn + " Resized into " + str(height) + " folder!")
                    else:
                        print(self.fn + " Could not be resized")
                        # return
                except:
                    pass
            elif os.path.exists('{}/{}/{}{}'.format(self.configs['stored_videos_dir'], height, self.fn, self.fext)) and not "{}_{}".format(height, self.f) in self.stored_fn:
                self.stored_fn.append("{}_{}".format(height, self.f))
                print("[+] " + "{}_{}".format(height, self.f) + " Saved")
            else:
                # print(fn + " already exist")
                continue

        with open('/root/vidtranscoder/fn.json', 'w', encoding='utf-8') as outfile:
            json.dump(self.stored_fn, outfile, ensure_ascii=False, indent=4)

    # def thumb_main_resize(self):
    #     pass


if __name__ == '__main__':
    # imgsizer()
    v = VideoTranscoder()
    v.vidcoder()
