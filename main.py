import yt_dlp

def download_video(url, path):
    ydl_opts = {
        'outtmpl': f'{path}/%(title)s.%(ext)s',  # Save the video with title as filename
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_playlist(playlist_url, path):
    ydl_opts = {
        'outtmpl': f'{path}/%(playlist_title)s/%(title)s.%(ext)s',  # Save videos in a directory with the playlist title
        'noplaylist': False,  # Ensure that a full playlist is downloaded
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

def menu():
    print("YouTube Downloader")
    print("1. Download a Single Video")
    print("2. Download a Playlist")
    print("3. Exit")

    while True:
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            video_url = input("Enter YouTube video URL: ")
            download_path = input("Enter path to save the video (leave empty for current directory): ") or "."
            download_video(video_url, download_path)
            print("Video downloaded successfully.")
        
        elif choice == '2':
            playlist_url = input("Enter YouTube playlist URL: ")
            download_path = input("Enter path to save the playlist (leave empty for current directory): ") or "."
            download_playlist(playlist_url, download_path)
            print("Playlist downloaded successfully.")
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
