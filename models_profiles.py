from app import db

class profiles(db.Model):
	id = db.Column('profiles_id', db.Integer, primary_key=True)
	name = db.Column(db.String(500), unique=True)

	def __init__(self, name):
		self.name = name
