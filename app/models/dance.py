from app import db


class Dance(db.Model):
    __tablename__ = 'dance'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    turns = db.relationship('Turn', backref='dance')


class Turn(db.Model):
    __tablename__ = 'turn'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    dance_id = db.Column(db.Integer, db.ForeignKey('dance.id'), nullable=False)

    pass
