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
        image_name = image.filename[:-4]

        img = Image.open(image)

        # convert to small image
        small_img = img.resize((block_size, block_size), Image.BILINEAR)

        # resize to output size
        res = small_img.resize(img.size, Image.NEAREST)

        # Save output image
        filename = f'{image_name}_{block_size}x{block_size}.png'
        res.save('static/images/' + filename)

        return render_template('result.html', img=img)
    return render_template('generator.html', form=form)
