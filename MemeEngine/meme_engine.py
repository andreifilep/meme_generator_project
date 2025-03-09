"""Module is responsible for manipulating and drawing text onto images."""

import os.path
import random
from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """Class generates memes and saves to given directory."""

    def __init__(self,
                 out_dir: str = '',
                 in_path: str = None,
                 quote_text: str = '',
                 quote_author: str = '',
                 font_path: str = None,
                 font_text=None,
                 font_author=None,
                 width: int = None,
                 quote_position=None,
                 ):
        """Set up parameters."""
        self.out_dir = out_dir
        self.in_path = in_path
        self.quote_text = quote_text
        self.quote_author = quote_author
        self.img = None
        self.font_path = font_path
        self.font_text = font_text
        self.font_author = font_author
        self.width = width
        self.quote_position = quote_position
        self.fill = (255, 255, 0)

        if os.path.exists(self.out_dir):
            pass
        else:
            os.makedirs(self.out_dir)

    def load_image(self, in_path: str) -> None:
        """Load image from given path."""
        self.img = Image.open(in_path)

    def resize_image(self, width: int) -> None:
        """Resize image maintaining original aspect ratio."""
        orig_width, orig_height = self.img.size

        if orig_width is not None:
            ratio = width / float(orig_width)
            height = int(ratio * float(orig_height))
            self.img = self.img.resize((width, height))
            self.quote_position = random.choice(range(30, height - 50))

    def set_font(self) -> None:
        """Set font type and size.

        Set font to LeckerliOne-Regular.
        Set body font dimension to 28.
        Set author font dimension to 20.
        """
        # Select font type, size, color and text position
        self.font_path = "./_data/fonts/LeckerliOne-Regular.ttf"
        self.font_text = ImageFont.truetype(self.font_path, 28)
        self.font_author = ImageFont.truetype(self.font_path, 20)

    def save_image(self):
        """Save image to given path."""
        file_path = os.path.abspath(
            os.path.join(
                self.out_dir,
                f'{random.randint(0,100000000)}.jpg'
            ))

        self.img.save(file_path)
        return file_path

    def make_meme(self, in_path: str, text: str, author: str, width: int = 500) -> str:
        """Create meme and save.

        :param str. in_path: Path to the image
        :param str. text: quote text
        :param str. author: quote author
        :param int width: meme width

        :return: str. meme path
        """
        self.load_image(in_path)
        self.resize_image(width)
        self.set_font()
        self.width = width

        # Superimpose text on image
        meme = ImageDraw.Draw(self.img)
        meme.text((30, self.quote_position), text, self.fill, self.font_text)
        meme.text(
            (360,
             self.quote_position + 30),
            author, self.fill,
            self.font_author
        )

        # save meme
        return self.save_image()
