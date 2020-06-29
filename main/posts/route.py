from flask import Blueprint, render_template, url_for, redirect, flash, request, abort, Markup
from main.posts.form import PostForm
from main.Model import Post
from flask_login import current_user, login_required
from main import db

posts = Blueprint('posts', __name__)


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    image_file = url_for('static', filename='profile_pics/' + post.author.image_file)
    return render_template('post.html', title=post.title, post=post, image_file=image_file)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your posts has been update!', 'success')
        return redirect(url_for('posts.post', post_id=post_id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update posts', form=form, lengend='Update Post', post=post)


@posts.route("/post/<int:post_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your posts has been deleted!', 'success')
    return redirect(url_for('main.ashes'))


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('your posts has been created successfully,', 'success')
        return redirect(url_for('main.ashes'))
    flash('invalid data', 'warning')
    return render_template('create_post.html', title='New Post', lengend='New Post', form=form)

