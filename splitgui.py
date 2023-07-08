import os
import math
from tkinter import filedialog, Tk, Label, Button, Entry
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip

def getVideoLength(fileName):
    clip = VideoFileClip(fileName)
    return clip.duration

def getSliceCount(fileName, split_duration):
    length = getVideoLength(fileName)
    return math.ceil(length / split_duration)

def split_video(input_filename, output_dir, split_duration):
    sliceCount = getSliceCount(input_filename, split_duration)
    output_files = []
    for i in range(sliceCount):
        output_filename = os.path.join(output_dir, os.path.splitext(os.path.basename(input_filename))[0] + '_%02d.mp4' % i)
        ffmpeg_extract_subclip(input_filename, i*split_duration, min((i+1)*split_duration, getVideoLength(input_filename)), targetname=output_filename)
        output_files.append(output_filename)
    return output_files

class VideoSplitterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Video Splitter")

        self.label = Label(master, text="Select a video file:")
        self.label.pack()

        self.duration_label = Label(master, text="Enter the duration of the splits in seconds:")
        self.duration_label.pack()
        
        self.duration_entry = Entry(master)
        self.duration_entry.pack()

        self.select_button = Button(master, text="Open", command=self.select_file)
        self.select_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def select_file(self):
        input_filename = filedialog.askopenfilename()
        output_dir = filedialog.askdirectory()
        duration = int(self.duration_entry.get())
        output_files = split_video(input_filename, output_dir, duration)
        print("Video split successfully. The output files are located at:")
        for output_file in output_files:
            print(output_file)

root = Tk()
gui = VideoSplitterGUI(root)
root.mainloop()
