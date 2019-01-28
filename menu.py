from database import Database
from models.post import Post
from models.blog import Blog

class Menu:
    def __init__(self):
        self.user = input('Enter your author name:')
        self.user_blog = None
        if self._user_has_account():
            print('Welcome back {}'.format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog=Database.find_one('blogs', {'author':self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True

        else:
            return False

    def _prompt_user_for_account(self):
        title = input('Enter title:')
        description=input('Enter description')
        blog = Blog(title=title, description=description, author=self.user)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_server(self):
        read_or_write = input('Do you want to read (R) or write (W)')

        if read_or_write == 'R':
            self._list_blogs()
            self._view_blogs()
            pass
        elif read_or_write == 'W':
            self.user_blog.new_post()
        else:
            print("Thank you for blogging!")

    def _list_blogs(self):
        blogs = Database.find(collection='blogs', query={})
        for blog in blogs:
            print("Id {}, title {} , Author {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blogs(self):
        blog_to_see = input("Enter the ID of the blog you'd like to read: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:

            print("Date: {}, title: {}\n\n{}".format(post['date_created'], post['title'], post['content']))


