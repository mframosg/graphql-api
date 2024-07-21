import graphene
from graphene_django.types import DjangoObjectType
from django.db.models import Q
from .models import User
from .views import create_random_users

class InvalidGenderError(ValueError):
    pass

class InvalidAgeError(ValueError):
    pass

class InvalidCriteriaError(ValueError):
    pass

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'name', 'age', 'gender')

def resolve_users(self, _info, gender=None, age=None, criteria=None):
    valid_genders = ['M', 'F']
    criteria_map = {'greater': 'gt', 'less': 'lt', 'equal': ''}
    
    if gender and gender.upper() not in valid_genders:
        raise InvalidGenderError(f"Invalid gender, must be one of {valid_genders}")

    query = Q()
    if gender:
        query &= Q(gender=gender.upper())

    if age is not None:
        if not 18 <= age <= 70:
            raise InvalidAgeError("Age must be between 18 and 70.")
        if criteria in criteria_map:
            filter_lookup = f'age__{criteria_map[criteria]}' if criteria_map[criteria] else 'age'
            query &= Q(**{filter_lookup: age})
        else:
            raise InvalidCriteriaError("Invalid criteria provided. Must be one of ['greater', 'less', 'equal'].")

    return User.objects.filter(query)

class FillTable(graphene.Mutation):
    class Arguments:
        num_entries = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, num_entries):
        create_random_users(num_entries)
        return FillTable(success=True)

class Query(graphene.ObjectType):
    users = graphene.List(UserType, gender=graphene.String(), age=graphene.Int(), criteria=graphene.String())

    def resolve_users(self, info, gender=None, age=None, criteria=None):
        return resolve_users(self, info, gender, age, criteria)

class Mutation(graphene.ObjectType):
    fill_table = FillTable.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)