from sys import path

from init import app, db


if __name__ == '__main__':
    app.run(debug=True)
'''
    if not path.exists('StoreVisitTransaction/' + 'OnlineShop'):
        db.create_all(app=app)
'''

