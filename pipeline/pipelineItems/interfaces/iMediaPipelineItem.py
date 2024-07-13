import sys, os

current_dir = os.path.abspath(os.path.pardir)
sys.path.append(os.path.join(current_dir,"model"))
#fkn why is import so fkn hard, why is it líke thiss jesu maddafkakkng christ
from mediaItem import MediaItem
    
class IMediaPipelineItem:    
    def validate(mediaItem:MediaItem)->None:
        raise NotImplementedError()
    def process()->MediaItem:
        raise NotImplementedError()
    
if __name__ == "__main__":
    print(sys.path)