from kivy.animation import Animation
from kivy.core.window import Window

from kivymd.uix.carousel import MDCarousel


class SlideAnimatior:
    """
    Used for inheritance by those screens classes that use Carousel.
    Animates the transparency of the slides when switching/moving.
    """

    _cursor_pos_x = 0

    def get_direction_swipe(self, progress_value: float) -> str:
        if self._cursor_pos_x > progress_value:
            direction = "left"
        else:
            direction = "right"
        return direction

    def do_animation_slide_content(self, carousel: MDCarousel, progress_value: float):
        """
        Called when the user swipes on the screen (the moment the slides move).
        Animates the transparency of slides.
        """

        direction = self.get_direction_swipe(progress_value)
        self._cursor_pos_x = progress_value
        offset_value = max(min(abs(progress_value) / Window.width, 1), 0)

        if direction == "left":
            # Current slide.
            carousel.current_slide.opacity = 1 - offset_value
            # Next slide.
            if carousel.next_slide:
                carousel.next_slide.opacity = offset_value
            # Previous slide.
            if carousel.previous_slide:
                carousel.previous_slide.opacity = 1 + offset_value
        elif direction == "right":
            # Current slide.
            carousel.current_slide.opacity = 1 - offset_value
            # # Next slide.
            if carousel.next_slide:
                carousel.next_slide.opacity = offset_value
            # Previous slide.
            if carousel.previous_slide:
                carousel.previous_slide.opacity = 0 + offset_value

    def on_index(self, index: int) -> None:
        """
        Called when slides stop (after swipe). Animates screen switching dots.
        """

        for instance_dot in self.ids.dots.children:
            if instance_dot.index == index:
                Animation(md_bg_color=self.theme_cls.primary_color, d=0.2).start(
                    instance_dot
                )
            else:
                Animation(
                    md_bg_color=self.theme_cls.disabled_hint_text_color, d=0.2
                ).start(instance_dot)
