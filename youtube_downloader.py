# pip install pytube
import sys
from pytube import YouTube
from sys import argv


def download_youtube_video(video_url):
    try:
        yt = YouTube(video_url)
        print(f"Title: {yt.title}")

        # Get the video stream with a specified resolution (e.g., 720p)
        yd = yt.streams.filter(res="720p").first()
        # yd = yt.streams.get_by_resolution(720)

        # path for your download
        output_path = 'C:\\Users\\prince\\Desktop\\vd'
        # Download the video to the specified output path
        yd.download(output_path)
        print("Video downloaded successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: python your_script.py <YouTube Video URL> <Output Directory>")
    else:
        # link for your download
        video_url = sys.argv[1]
        download_youtube_video(video_url)
