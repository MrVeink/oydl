# main.py
#
# Copyright 2025 Joona Holkko
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import tkinter as tk
from tkinter import ttk, messagebox
from yt_dlp import YoutubeDL

def download_video():
    link = entry.get()
    if not link:
        messagebox.showerror("Error", "Please enter a valid YouTube link.")
        return

    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        messagebox.showinfo("Success", "Video download completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def download_audio():
    link = entry.get()
    if not link:
        messagebox.showerror("Error", "Please enter a valid YouTube link.")
        return

    selected_codec = codec_combobox.get()

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': selected_codec,
        }],
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        messagebox.showinfo("Success", "Audio download completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("OYDL - Media Downloader")
root.resizable(False, False)
root.configure(bg='#2d2d2d')

style = ttk.Style()
style.theme_use('alt')

style.configure('TFrame', background='#2d2d2d')
style.configure('TLabel', background='#2d2d2d', foreground='#ffffff', font=('Helvetica', 12))
style.configure('TEntry', fieldbackground='#3d3d3d', foreground='#ffffff', font=('Helvetica', 10))
style.configure('TButton', background='#3d3d3d', foreground='#ffffff', font=('Helvetica', 12, 'bold'))
style.configure('TCombobox', fieldbackground='#3d3d3d', foreground='#000000', font=('Helvetica', 10))
style.map('TButton', background=[('active', '#4d4d4d')])

frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

label = ttk.Label(frame, text="Enter YouTube Link:")
label.pack(pady=(0, 10))

entry = ttk.Entry(frame, width=50)
entry.pack(pady=(0, 10))

# Dropdown for codec selection
codec_label = ttk.Label(frame, text="Select Audio Codec:")
codec_label.pack(pady=(10, 0))

codecs = ['mp3', 'opus', 'flac', 'm4a', 'wav']
codec_combobox = ttk.Combobox(frame, values=codecs, state="readonly")
codec_combobox.current(0)  # Set default to mp3
codec_combobox.pack(pady=(0, 10))

video_button = ttk.Button(frame, text="Download Video", command=download_video)
video_button.pack(pady=5)

audio_button = ttk.Button(frame, text="Download Audio", command=download_audio)
audio_button.pack(pady=5)

root.mainloop()
