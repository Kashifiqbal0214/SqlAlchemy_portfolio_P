from main import session
from models import User, Comment
from sqlalchemy import select

statement = select(Comment).join(Comment.user).where(
    User.username == 'kashif'
).where(
    Comment.text == 'Hello World'
)

result = session.scalars(statement)

print(result)