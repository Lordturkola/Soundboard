import sys, os

current_dir = os.path.abspath(__file__)
current_dir = os.path.dirname(current_dir)
print(f"curr {current_dir}")
sys.path.append(os.path.join(current_dir, "model"))
sys.path.append(os.path.join(current_dir, "interfaces"))

from iMediaPipelineItem import IMediaPipelineItem
from mediaItem import MediaItem
from yt_dlp import YoutubeDL, utils

mediadir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEDIA_DIR = os.path.join(mediadir, "media")
print(MEDIA_DIR)


class FetchMedia(IMediaPipelineItem):

    def validate(mediaItem: MediaItem) -> None:
        if mediaItem.video_url == None:
            raise IOError(f"{__class__}, url required")
        if mediaItem.key_bindning == None:
            raise IOError(f"{__class__}, keybinding required")
        if len(mediaItem.key_bindning) != 1:
            raise IOError(f"{__class__}, invalid key bindning")

    def process(mediaItem: MediaItem) -> MediaItem:
        print(
            f"{__name__}: {mediaItem.key_bindning} {mediaItem.video_url} {mediaItem.start_time} {mediaItem.end_time}"
        )
        FetchMedia.validate(mediaItem)
        media_folder = os.path.join(MEDIA_DIR, mediaItem.key_bindning)
        print(media_folder)
        if not os.path.exists(media_folder):
            os.mkdir(media_folder)
        filepath = os.path.join(
            media_folder,
            f"media_file_{mediaItem.key_bindning}_",
        )

        options = {
            "download_ranges": utils.download_range_func(
                [], [[mediaItem.start_time, mediaItem.end_time]]
            ),
            "outtmpl": filepath + "%(format_id)s.%(ext)s",
            "overwrites": True,
        }
        with YoutubeDL(params=options) as ytdl:
            error_code = ytdl.download(mediaItem.video_url)

        print(os.listdir(media_folder))
        mediaItem.file_path = os.path.join(media_folder, os.listdir(media_folder)[0])

        print("fetch media success")
        return mediaItem


if __name__ == "__main__":
    mediaItem = FetchMedia.process(
        MediaItem(
            video_url="https://www.youtube.com/watch?v=B1xXjF5M8R4&ab_channel=ItsBSD",
            start_time=14,
            end_time=15,
            file_path=None,
            key_bindning="x",
        )
    )
    print(mediaItem.file_path)
