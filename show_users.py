from app import app, db, User

with app.app_context():
    users = User.query.all()
    print('قائمة أسماء المستخدمين:')
    for user in users:
        print(user.username) 