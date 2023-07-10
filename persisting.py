from models import User, Comment
from main import session




kashif = User(
    username= 'kashif',
    email_address = 'kashif214@gmail.com',
    comments = [
        Comment(text= 'Hello World'),
        Comment(text= 'I have learn Python SqlAlchemy Database')
    ]
)

majid = User(
    username= 'Majid',
    email_address = 'majid@gmail.com',
    comments = [
        Comment(text = "Hay Developer"),
        Comment(text= 'I want to learn Pythono')
    ]
)

ehsan = User(
    username= 'Ehsan',
    email_address = 'ehsan214@gmail.com',
    comments = [
        Comment(text= 'Hi, How are you'),
        Comment(text = 'Please Subscribe our channel')
    ]
)


session.add_all([kashif, majid, ehsan])
session.commit()