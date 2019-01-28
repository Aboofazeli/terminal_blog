from database import Database
from menu import Menu

#mongo
#use fullstack
#db.posts.insert({})
#db['posts'].findOne()
#db['posts'].find()
Database.initialize()
menu = Menu()

menu.run_server()

