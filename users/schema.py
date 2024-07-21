import graphene
from graphene_django.types import DjangoObjectType
from .models import User
from .views import create_random_users

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'name', 'age', 'gender')

class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return User.objects.all()



class FillTable(graphene.Mutation):
    class Arguments:
        num_entries = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, num_entries):
        create_random_users(num_entries)
        return FillTable(success=True)

class Mutation(graphene.ObjectType):
    fill_table = FillTable.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)