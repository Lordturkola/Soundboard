from mediaItem import MediaItem
from pipelineItems import fetchMedia

class MediaBuilder:
    def __init__(self, rawMediaItem) -> None:
        self.media_item = self.extract_data(rawMediaItem)
        self.pipeline = [fetchMedia.FetchMedia.process, ]
    def process(self):
        mediaItem = fetchMedia(self.media_item)
        
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
