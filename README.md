# Flask Blog Project - Day 57 of Python Bootcamp 📝

A simple blog application built with Flask, Jinja templating, and external API integration as part of my Python bootcamp journey.

## 📁 Project Structure

```
blog-project/
├── main.py                 # 🐍 Flask application
├── templates/              # 📄 HTML templates
│   ├── index.html         # 🏠 Homepage with all blog posts
│   └── post.html          # 📖 Individual blog post page
└── static/
    └── css/
        └── styles.css     # 🎨 Pre-written CSS styles
```

## 🚀 Features

- **Flask Web Framework** - Lightweight Python web framework
- **Jinja2 Templating** - Dynamic HTML rendering
- **REST API Integration** - Fetches blog data from external API
- **Responsive Design** - Clean and modern UI
- **Dynamic Routing** - Individual pages for each blog post

## 🛠️ Technologies Used

- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) **Python** - Backend logic
- ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) **Flask** - Web framework
- ![Jinja](https://img.shields.io/badge/Jinja-B41717?style=for-the-badge&logo=jinja&logoColor=white) **Jinja2** - Templating engine
- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) **HTML5** - Markup
- ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) **CSS3** - Styling
- ![REST API](https://img.shields.io/badge/REST_API-FF6C37?style=for-the-badge&logo=json&logoColor=white) **REST API** - External data source

## 📋 Prerequisites

- Python 3.x
- Flask
- Requests library

## 🎯 Learning Objectives

This project was developed as **Day 57** of my Python Bootcamp with focus on:

- ✅ **Flask Framework** - Building web applications
- ✅ **Jinja Templating** - Dynamic content rendering
- ✅ **API Integration** - Consuming external data
- ✅ **Routing** - Creating multiple endpoints
- ✅ **Template Inheritance** - Reusable HTML components

## 📊 API Integration

The application fetches blog data from:
```
https://api.npoint.io/c790b4d5cab58020d391
```

## 🎨 Pages

### 🏠 Homepage (`/`)
- Displays all blog posts in cards
- Each card shows title and subtitle
- "Read" button links to individual posts

### 📖 Blog Post (`/post/<id>`)
- Shows complete blog post content
- Dynamic routing based on post ID
- Displays title, subtitle, and body content

## 🔧 Code Overview

### Main Application (`main.py`)
```python
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Fetches and displays all blog posts
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", all_data=response)

@app.route("/post/<int:num>")
def post(num):
    # Displays individual blog post
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    selected_post = next((post for post in response if post["id"] == num), None)
    return render_template("post.html", post=selected_post)
```

## 🌟 Key Features Implemented

- **Dynamic Content Rendering** with Jinja2
- **API Data Fetching** and processing
- **Clean Separation** of concerns (templates, static files)
- **Error Handling** for missing posts
- **Professional Styling** with pre-written CSS

## 📝 Note

The CSS styles were provided as part of the bootcamp curriculum, allowing focus on backend Flask development and Jinja templating concepts rather than frontend styling.
