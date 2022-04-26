from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField, IntegerField
from wtforms.validators import NumberRange

class LoadImgForm(FlaskForm):
    image = FileField('Load Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    block_size = IntegerField('Block size', validators=[NumberRange(min=2, max=80)])
    submit = SubmitField('Submit')


