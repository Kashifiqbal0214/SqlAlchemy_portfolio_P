from flask import Flask , render_template, request
from main import session
from models import User

kashif = session.query(User).filter_by(username = 'kashif').first()
