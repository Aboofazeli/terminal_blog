import uuid
from models.post import Post
import datetime
from database import Database


class Blog:
    def __init__(self, author, title, description, id=None):
        self.author=author
        self.title=title
        self.description=description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title= input('enter the title')
        content = input('enter content')
        date = input('Enter data in the format (ddmmyyyy)')
        if date == '':
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y")
        post=Post(title=title, author=self.author, content=content, date=date, blog_id=self.id)
        post.save_to_mongo()

    def json(self):
        return {'author': self.author, 'title': self.title, 'description':self.description, 'id': self.id}

    def save_to_mongo(self):
        Database.insert(collection='blogs', data=self.json())

    def get_posts(self):
        return Post.from_blog(self.id)

    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs',
                                      query={'id': id})
        return cls(author=blog_data['author'],
                   title=blog_data['title'],
                   description=blog_data['description'],
                   id=blog_data['id'])


