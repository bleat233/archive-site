# flask-blog
For HarvardX CS50 Final.

### Project Description

A flask-blog deployed as a python web app using Azure App Service and mySQL database.

Intended to be an internet trash site for personal use. Potentially dumping: study notes, movie/music/literature reviews, fanfiction idea, random thoughts etc.


## Site

Please view on laptop/PC for best display.

```
http://bleat2333.azurewebsites.net.
```
The passphrase can currently be circumvent by adding/home after the url. Due to ongoing work, the site might not be deployed at the time you visit it.


### Design

Users: allow user registration, login/out, and password reset with email verification.
Once login, users can update their account information (change username, password, or profile picture).
(Nav: Register, login, logout, account)

Blogging: View posts made by all users in descending order sorted by time posted.
Once login, users can create, update, or delete posts with WYSIWYG editor.
(Only post ontent supports utf-8 collation.)
(Nav: Post, Ashes)

Hobby page: drop-down lists compiling hobby-related information.
(Nav: egg)

Gallery: photos display with auto slide-view.
(Nav: blinks)

Site owner information: Self-introduction and contact information.
(The Pack, Intro)


## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Web framework and related modules
* [Azure](https://azure.microsoft.com/en-us/) - App Deployment
* [MySQL](https://www.mysql.com/) - Database (set up under Azure)
* [Bootstrap](https://getbootstrap.com/) - Styling
* [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) - Template formatting
* [wtforms](https://wtforms.readthedocs.io/en/2.3.x/) - Forms


## Versions

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
pymysql
flask_bcrypt
flask_mail
Pillow
email_validator


### Pending updates

1. Posts sort and search functionality.
2. Registtration email verification
3. Post text editor background change
4. Site passphrase_required decorator


### Authors

* **Weiqian Lin** - for CS50x 2020 Final Project / web track


### Acknowledgments

* Flask blog tutorial: Corey MSchafer on youtube.
* Cover: template for bootstrap by @mdo
* Site background picture: @yamawava on ins.


