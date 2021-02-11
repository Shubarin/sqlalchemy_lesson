import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey('users.id'))
    job = sqlalchemy.Column(sqlalchemy.String, name='description')
    work_size = sqlalchemy.Column(sqlalchemy.Integer, name='hours')
    collaborators = sqlalchemy.Column(sqlalchemy.String,
                                      name='list of id of participants')
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, name='дата начала')
    end_date = sqlalchemy.Column(sqlalchemy.DateTime, name='дата окончания')
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean,
                                    name='признак завершения')
    user = orm.relation('User')