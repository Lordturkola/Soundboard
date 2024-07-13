from mediaItem import MediaItem


class MediaBuilder:
    def __init__(self, rawMediaItem) -> None:
        self.media_item = self.extract_data(rawMediaItem)

    def process(self):
        for stage in self.pipeline:
            stage()
        # done building object
        return self.media_item

    def extract_data(self, rawItem):
        parameters = rawItem.strip().split()
        newMediaItem = MediaItem()
        time_interval = []
        for parameter in parameters:
            if parameter.contains("http"):
                newMediaItem.videourl = parameter
            if parameter.contains(":"):
                if len(time_interval[0]) == 0:
                    time_interval[0] = parameter
                elif len(time_interval) == 1:
                    time_interval[1] = parameter
            if len(parameter) == 1:
                newMediaItem.key_binding = parameter

        time_interval.sort(reverse=True)
        newMediaItem.start_time = time_interval[0]
        newMediaItem.end_time = time_interval[1]

        return newMediaItem

    def fetch_url_video(self, url):
        try:
            # try to save file with generic name
            pass
        except:
            # add a digit to it if conflict
            pass

    def convert_media_to_mp4(file_path):
        pass

    def trim_media(start_time, end_time, file_path):
        pass
