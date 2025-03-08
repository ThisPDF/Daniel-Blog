from flask import Flask, render_template
from jinja2 import Template
import requests
import json

try:
    response = requests.get('https://api.npoint.io/674f5423f73deab1e9a7')
    response.raise_for_status()  # Raise an error for bad status codes
    data = response.json()
    for post in data:
        print(post['title'])
        print(post['body'])
        print(post['image_url'])
        print('\n')
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html' , data=data)
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/post/<int:id>')
def post(id):  # ✅ Accept the id parameter
    # Find the specific post by ID
    selected_post = next((item for item in data if item["id"] == id), None)

    if selected_post is None:
        return "Post not found", 404  # Handle case when post is not found

    return render_template('post.html', post=selected_post)


if __name__ == '__main__':
    app.run(debug=True)