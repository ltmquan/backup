from game_objects import GameObject
from renderer.image_renderer import ImageRenderer


class RightBorder(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.renderer = ImageRenderer("image/map/image/1.png")