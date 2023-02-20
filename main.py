from tkinter import *
from pytube import YouTube

class YoutubeDownloader:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('450x300')
        self.root.title("Youtube Video Downloader")
        self.link = StringVar()
        self.filename = StringVar()

        self.create_widgets()

    def create_widgets(self):
        Label(self.root, text='Youtube Video Downloader', font='arial 15 bold').pack()

        Label(self.root, text='Paste Link Here:', font='arial 13 bold').place(x=160, y=40)
        self.link_entry = Entry(self.root, width=45, textvariable=self.link)
        self.link_entry.place(x=50, y=90)

        self.download_button = Button(self.root, text='Download', font='arial 15 bold', padx=2, command=self.download_video)
        self.download_button.place(x=180, y=150)

    def download_video(self):
        try:
            url = YouTube(str(self.link.get()))
            video = url.streams.get_highest_resolution()
            video.download()
            Label(self.root, text='Downloaded', font='arial 15').place(x=180, y=210)
        except Exception as e:
            Label(self.root, text=f'Error: {e}', font='arial 13').place(x=180, y=210)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    downloader = YoutubeDownloader()
    downloader.run()
