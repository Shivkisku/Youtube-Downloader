# Youtube-Downloader

This program is a simple graphical user interface (GUI) that allows the user to download YouTube videos by entering their links into an input field and clicking a "Download" button.

The program is written in Python and uses the tkinter library for creating the GUI, as well as the pytube library for downloading the videos.

The YoutubeDownloader class encapsulates the main window and its widgets, and includes a method for handling the download process. The download process includes error handling with a try/except block to catch any exceptions that may occur during the download process.

When the user clicks the "Download" button, the download_video method is called and attempts to download the video specified by the link in the input field. If the download is successful, a "Downloaded" message is displayed on the GUI. If an error occurs during the download process, an error message is displayed on the GUI instead.



