import random
import os
import requests
from flask import Flask, render_template, abort, request
from itertools import chain

from QuoteEngine import Ingestor
from MemeEngine import MemeEngine


app = Flask(__name__, template_folder="templates")

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

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

    images_path = "./_data/photos/dog/"
    images_files = os.listdir(images_path)

    imgs = []
    for file in images_files:
        try:
            imgs.append(os.path.join(images_path, file))
        except ValueError as error:
            print(f"ValueError: {error}")

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    img_url: str = request.form.get("image_url")
    req = requests.get(img_url)
    tmp = f'./tmp/{random.randint(0, 100000000)}.jpg'

    with open(tmp, 'wb') as open_file:
        open_file.write(req.content)
        body = request.form['body']
        author = request.form['author']
        path = meme.make_meme(tmp, body, author)
        os.remove(tmp)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
