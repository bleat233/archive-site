from flask import url_for
import os
import binascii
from PIL import Image
from flask_mail import Message
from main import mail
from flask import current_app


def save_picture(form_picture):
    random_hex = bytes.decode(binascii.b2a_hex(os.urandom(6)))
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='timshellin@outlook.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, please visit the link:
    {url_for('reset_token',token=token, _external=True)}
    The link will be valid for 30 minutes after the email is sent to you.
    If you did not intend to reset your password, please ignore this email.    
    '''
    mail.send(msg)

