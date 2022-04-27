from app import app, db, celery
from flask import render_template, redirect, url_for, request
from PIL import Image
import os

from forms import *
from models import *

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

        pic = Picture(name=filename, path=img_path)
        db.session.add(pic)
        db.session.commit()

        return render_template('result.html', pic=pic)
    return render_template('generator.html', form=form)

@app.route('/download/<int:pic_id>')
def download(pic_id):
    pic = Picture.query.get(pic_id)
    pic.downloaded = True
    db.session.commit()
    return ''

#In terminal: flask shell
#celery -A app.celery worker --loglevel=info --pool=eventlet

#On WSL(Redis): sudo service redis-server start
#redis-cli
@celery.task
def add(x, y):
    return x+y

