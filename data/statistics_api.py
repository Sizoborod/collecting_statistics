import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase




class Statistic(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'statistic'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    # team_leader = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    game1 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)
    game2 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)
    game3 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)
    game4 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)
    game5 = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)



    user = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relationship('User')


    def __repr__(self):
        return f'<statistic> {self.user} {" ".join([str(i) for i in [self.game1, self.game2, self.game3, self.game4]])}'
