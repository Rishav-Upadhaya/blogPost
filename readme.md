# BlogPost

BlogPost is a project based on Backend Development created using Django. It lets users log in, create blogs, read other blogs, and delete their own blogs.

## Features

1. **User Authentication**
2. **Create Blog Posts**
3. **Read Blogs**
4. **Delete Blogs**

## Installation

### Prerequisites

- Python 3.10.4
- Django 4.2.7

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Python, Django.

### Steps

1. Clone the repository:

```bash
git clone https://github.com/Rishav-Upadhaya/blogPost.git
cd BlogPost
```

2. Install Dependencies:

```bash
pip install python 3.10.4
pip install Django 4.2.7
```

3. Apply Database MIgrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Run Development Server:

```bash
python manage.py runserver
```

5. Open application server:

```bash
http://127.0.0.1:8000/
```

## Usage

1. Register as a new user or log in with existing credentials.
2. Create new blog by filling in the required details.
3. View a list of all blog posts on the home page.
4. Click on a blog to view its details.
5. Delete your own blog if needed.

## Future Developments

1. Using DRF and creating API's that could get other user blogs as well.
2. Add a commenting feature for blogs.
3. Allow users to edit their existing blogs.
4. Implement advanced search functionality.
5. Add tags or categories for blogs.
