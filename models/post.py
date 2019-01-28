from database import Database
import datetime
import uuid


class Post:
    def __init__(self, title, author, content, blog_id, date=datetime.datetime.utcnow(), id=None):
        self.title = title
        self.author = author
        self.date_created = date
        self.content = content
        self.blog_id = blog_id
        self.id = uuid.uuid4().hex if id is None else id

    def save_to_mongo(self):
        Database.insert(collection='posts', data=self.json())

    def json(self):
        return {'author': self.author,
                'title': self.title,
                'content': self.content,
                'blog_id':self.blog_id,
                'date_created': self.date_created,
                'id': self.id}

    @staticmethod
    def from_mongo(id):
        post_data = Database.find_one(collection='posts', query={'id': id})
        return post_data

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]



