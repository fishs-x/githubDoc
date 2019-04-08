from models import BaseModel, db


class Docs(BaseModel):
    __tablename__ = 'docs'
    title = db.Column('title', db.String(120))
    desc = db.Column('desc', db.String(255))
    url = db.Column('url', db.String(255))
    author = db.Column('author', db.String(255))

    @property
    def to_json(self):
        return {'title': self.title, 'desc': self.desc, 'url': self.url, 'id': self.id, 'author': self.author}
