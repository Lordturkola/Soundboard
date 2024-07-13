import sys, os
from os.path import dirname
current_dir = os.path.abspath(os.path.curdir)
MEDIA_DIR = os.path.join(dirname(dirname(current_dir)), "media")
print(MEDIA_DIR)
sys.path.append(os.path.join(current_dir,"model"))
sys.path.append(os.path.join(current_dir,"interfaces"))

print(sys.path)
print(current_dir)
from iMediaPipelineItem import IMediaPipelineItem
from mediaItem import MediaItem
from pytube import YouTube
from pytube import helpers

class FetchMedia(IMediaPipelineItem):
    media_download_folder = MEDIA_DIR
    
    def __init__(self, mediaItem:MediaItem) -> None:
        self.validate(mediaItem)
        self.mediaItem = mediaItem
        
    def validate(mediaItem:MediaItem)->None:
        if mediaItem.videourl == None:
            raise IOError(f"{__class__}, missing media to process")
    
    def process(self) -> MediaItem:
        videoObj = YouTube(self.mediaItem.videoUrl)
        helpers.target_directory("../Media")
        videoObj.streams.filter(progressive = True, file_extension = "mp4").order_by('resolution').desc().first().download("")
       self.mediaItem.file_path = videoObj.
            
if __name__ == "__main__":
    print(sys.path)
