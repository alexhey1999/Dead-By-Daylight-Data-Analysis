import streamlink
import subprocess as sp
import cv2
import numpy as np
from dotenv import load_dotenv,find_dotenv
import time
import os
from screen_capping import Screen
from run import main
from database_handling import Database

FFMPEG_BIN = "ffmpeg.exe"

def get_streamer_list():
    with open(os.getenv("STREAMER_LIST")) as file:
        data = file.read()
        data = data.split('\n')
    return data


def twitch_process():
    streamer_list = get_streamer_list()
    DatabaseHandler = Database()
    while True:
        for streamer in streamer_list:
            try:
                del screen
            except:
                pass
            screen = Screen(1920, 1080)
            streams = streamlink.streams(f"https://www.twitch.tv/{streamer}")
            if streams == {}:
                continue
            else:
                correct_resolution = False
                resolution = 0
                for i in streams.keys():
                    raw_resolution = i.split("p")[0]
                    if raw_resolution == "1080":
                        correct_resolution = True
                        resolution = i
                        break
                    
                if correct_resolution:
                    stream_url = streams[resolution].url
                    pipe = sp.Popen([ FFMPEG_BIN, "-i", stream_url,
                    "-loglevel", "quiet", # no text output
                    "-an",   # disable audio
                    "-f", "image2pipe",
                    "-pix_fmt", "bgr24",
                    "-vcodec", "rawvideo", "-"],
                    stdin = sp.PIPE, stdout = sp.PIPE)
                    raw_image = pipe.stdout.read(1920*1080*3) # read 432*240*3 bytes (= 1 frame)
                    image =  np.fromstring(raw_image, dtype='uint8').reshape((1080,1920,3))
                    image,filename = screen.test_endscreen_image(image)
                    print(f"Running -> {streamer}")
                    if filename == None:
                        continue
                    else:
                        main(image, filename, screen, DatabaseHandler)
                        print(f"Data-Added -> {filename}, {streamer}")
                else:
                    continue
                
                
if __name__ == '__main__':
    load_dotenv(find_dotenv())
    twitch_process()