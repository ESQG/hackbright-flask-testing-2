from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""

    games=[]
    games.append(Game(name="Hanabi", description="A cooperative card game: put on a fireworks show!"))

    games.append(Game(name="Dominion", description="A deck-building game: get more land than your opponents"))

    games.append(Game(name="Settlers of Catan", description="An elegant board game: trade sheep for wood"))

    db.session.add_all(games)
    db.session.commit()

if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print "Connected to DB."
 