import os
import random
import argparse
from itertools import chain

from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel
from MemeEngine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given a path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        path = './_data/DogQuotes/'
        quote_files = os.listdir(path)

        quotes = []
        for file in quote_files:
            try:
                quotes.append(Ingestor.parse(os.path.join(path, file)))
            except ValueError as error:
                print(f"ValueError: {error}")

        # flatten the list of quotes after all files are parsed
        quotes = list(chain(*quotes))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Make a meme from pict path and quote')
    # path - path to an image file
    parser.add_argument('--path', type=str)
    # body - quote body to add to the image
    parser.add_argument('--body', type=str)
    # author - quote author to add to the image
    parser.add_argument('--author', type=str)
    args = parser.parse_args()
    print(f'Your meme was saved at {generate_meme(args.path, args.body, args.author)}')
