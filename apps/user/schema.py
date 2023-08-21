# user/schema.py
import graphene
from graphene_django.types import DjangoObjectType
from .models import AppUser

class UserType(DjangoObjectType):
    class Meta:
        model = AppUser

class Query(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.Int())

    def resolve_user(self, info, id):
        return AppUser.objects.get(pk=id)

schema = graphene.Schema(query=Query)
