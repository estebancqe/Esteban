import reflex as rx
from collections import Counter

class CarouselState(rx.State):
    current_image: int = 0
    images: list[str] = [
        "/cafetera_horizontal_1080_web.JPG",
        "/cogador_horizontal_1080_web.JPG",
        "/escritorio_cerrado_1080_web.JPG",
        "/mueble_sala_horizontal_1080_web.JPG",
        "/estudio_con_homenaje_1080_web.JPG",
    ]
    
    def next_image(self):
        if self.current_image < len(self.images) - 1:
            self.current_image += 1
    
    def prev_image(self):
        if self.current_image > 0:
            self.current_image -= 1
            
    def on_swipe(self, event_data: dict):
        if event_data.get("dir") == "Left":
            self.next_image()
        elif event_data.get("dir") == "Right":
            self.prev_image()