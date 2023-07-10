from main import session
from models import User, Comment

comment = session.query(Comment).filter_by(id=3).first()

session.delete(comment)
session.commit()