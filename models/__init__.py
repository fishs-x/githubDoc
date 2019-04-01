from datetime import datetime
from extensions import db


class CRUDMixin:
    """Mixin that adds convenience methods for CRUD (create, read, update, delete)
    operations.
    """

    @classmethod
    def create(cls, *args, **kwargs):
        """Create a new record and save it the database."""
        instance = cls()
        for field in args:
            for k, v in field.items():
                setattr(instance, k, v)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        # Prevent changing ID of object
        kwargs.pop('id', None)
        for attr, value in kwargs.items():
            if value is not None:
                setattr(self, attr, value)
        setattr(self, 'update_at', datetime.now())
        return commit and self.save() or self

    def save(self, commit=True):
        """Save the record."""
        if not getattr(self, 'create_at'):
            setattr(self, 'create_at', datetime.now())
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """Remove the record from the database."""
        db.session.delete(self)
        return commit and db.session.commit()


class BaseModel(CRUDMixin, db.Model):
    """Base model class that includes CRUD convenience methods."""
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    create_at = db.Column('create_at', db.TIMESTAMP, )
    update_at = db.Column('update_at', db.TIMESTAMP, default=datetime.now())
    __abstract__ = True
