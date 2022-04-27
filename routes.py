from app import app
from flask import render_template, redirect, url_for
from PIL import Image

from forms import *

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/generator', methods=['GET', 'POST'])
def generator():
    form = LoadImgForm()
    if form.validate_on_submit():
        image = form.image.data
        block_size = form.block_size.data
        image_name, image_format = image.filename[:-4], image.filename[-4:]

        img = Image.open(image)

        # convert to small image
        small_img = img.resize((block_size, block_size), Image.BILINEAR)

        # resize to output size
        res = small_img.resize(img.size, Image.NEAREST)

        # Save output image
        filename = f'{image_name}_{block_size}x{block_size}{image_format}'
        img_path = 'images/' + filename
        res.save('static/' + img_path)

        return render_template('result.html', img_path=img_path)
    return render_template('generator.html', form=form)

