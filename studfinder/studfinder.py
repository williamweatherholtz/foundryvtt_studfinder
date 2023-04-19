import cv2
import json

class Studfinder:
    def __init__(self, image_fn: str):
        self.pois = None        
        pass
    
    def get_studs(self):
        # get POI
        # search for flat walls using a hough accumulator
        
        # search for elliptical walls using a hough accumulator
        
        # search for walls with CNNs
        
        # some walls have thickness.  so we're interested in POI between sets of parallel (or concentric) POI
        pass
    
    def save(self, fn):
        pass
    
    def poi_to_foundryvttwalls(self):
        pass

if __name__ == '__main__':
    fn = 'Meadow-Ruins-battle-map-Day-3672433009.jpg'
    sf = Studfinder(fn)
    