class MediaItem:
    def __init__(self, videourl, start_time, end_time, key_bindning, file_path) -> None:
        self.video_url = videourl
        self.start_time = start_time
        self.end_time = end_time
        self.key_bindning = key_bindning
        self.file_path = file_path
