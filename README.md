# Archive
for 林炜倩 Marlene Lin /TeaPP

### Description

A flask blog deployed as a python web app on heroku with its postgres databse. (previously deployed on azure-see CS50 Final)

Intended to be used as a personal archive for study notes, movie/music/literature/cooking reviews, project ideas, random thoughts etc.


## Site

Please view on laptop/PC for best display.

```
pacific-escarpment-25858.herokuapp.com/home
```


### Design

Users: allow user registration, login/out, and password reset with email verification.
Once login, users can update their account information (change username, password, or profile picture).
(Nav: Register, login, logout, account)

Posting: View posts made by all users in descending order sorted by time posted.
Once login, users can create, update, or delete posts with WYSIWYG editor.
(Only post ontent supports utf-8 collation.)
(Nav: Posts)

Event collect: drop-down lists compiling event-related information.
(Nav: egg)

Gallery: photos display with auto slide-view.
(Nav: blinks)

Site owner information: Self-introduction and contact information.
(The Pack, Intro)


## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Web framework and related modules
* [Heroku](https://www.heroku.com) - App Deployment and postgres database
* [Bootstrap](https://getbootstrap.com/) - Styling
* [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) - Template formatting
* [wtforms](https://wtforms.readthedocs.io/en/2.3.x/) - Forms


## Versions/dependencies

Python：3.7
Flask==1.1.2
Jinja2==2.11.2
requests==2.9.1
Werkzeug==1.0.1
markdown
wtforms
flask_wtf
flask_login
itsdangerous
datetime
flask_sqlalchemy
gunicorn
flask_bcrypt
flask_mail
Pillow
email_validator
psycopg2


### Pending updates

1. Posts sort and search functionality.
2. Registration email verification
3. Post text editor background change

### Acknowledgments

* Flask blog tutorial: Corey MSchafer on youtube.
* Site background picture: @yamawava on ins.


