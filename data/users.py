import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, name='фамилия')
    name = sqlalchemy.Column(sqlalchemy.String, name='имя')
    age = sqlalchemy.Column(sqlalchemy.Integer, name='возраст')
    position = sqlalchemy.Column(sqlalchemy.String, name='должность')
    speciality = sqlalchemy.Column(sqlalchemy.String, name='профессия')
    address = sqlalchemy.Column(sqlalchemy.String, name='адрес')
    email = sqlalchemy.Column(sqlalchemy.String, unique=True,
                              name='электронная почта')
    hashed_password = sqlalchemy.Column(sqlalchemy.String,
                                        name='хэшированный пароль')
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                      name='дата изменения')
    city_from = sqlalchemy.Column(sqlalchemy.String, name="родной город", nullable=True)

    jobs = orm.relation("Jobs", back_populates='user')
    departaments = orm.relation("Departament", back_populates='user')

    def __repr__(self):
        return f'<Colonist> {self.id} {self.surname} {self.name}'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
