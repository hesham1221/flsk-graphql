import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField,SQLAlchemyObjectType
from db import (
    User as UserRepo,
    Posts as PostRepo,
    session
)

class UserSchema(SQLAlchemyObjectType):
    class Meta:
        model=UserRepo


class PostSchema(SQLAlchemyObjectType):
    class Meta:
        model=PostRepo      


class Query(graphene.ObjectType):
    users = graphene.List(UserSchema)
    def resolve_users(self, info):
        query = UserSchema.get_query(info)  # SQLAlchemy query
        return query.all()


schema=graphene.Schema(query=Query)