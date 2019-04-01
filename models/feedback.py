from models import BaseModel, db


class Feedback(BaseModel):
    __tablename__ = 'feedback'
    msg = db.Column('msg', db.Text())

    @property
    def to_json(self):
        return {'msg': self.msg}
