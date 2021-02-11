import sqlalchemy
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


class Departament(SqlAlchemyBase):
    __tablename__ = 'departaments'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, name='Название')
    chief = sqlalchemy.Column(sqlalchemy.Integer,
                              sqlalchemy.ForeignKey('users.id'))
    members = sqlalchemy.Column(sqlalchemy.String, name='список id',
                                nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, name='Почта', index=True,
                              unique=True, nullable=True)
    user = orm.relation('User')

    def __repr__(self):
        return f'<Departament> {self.id} {self.title} {self.email}'
