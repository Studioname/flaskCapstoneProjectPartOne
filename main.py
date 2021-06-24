from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)


def get_blog_data():
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    response = requests.get(blog_url)
    data = response.json()
    return data

@app.route('/')
def home():
    blog_posts = get_blog_data()
    return render_template("index.html", posts=blog_posts)

@app.route('/post/<int:post_id>')
def get_post(post_id):
    blog_posts = get_blog_data()
    for post in blog_posts:
        if post["id"] == post_id:
            instance_of_post_class = Post(post)
    return render_template("post.html", post_object=instance_of_post_class)

if __name__ == "__main__":
    app.run(debug=True)
