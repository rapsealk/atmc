import graphene
from graphene_django import DjangoObjectType

from airlines.models import Airline


class AirlineType(DjangoObjectType):
    class Meta:
        model = Airline
        fields = ("id", "name")


class Query(graphene.ObjectType):
    airlines = graphene.List(AirlineType)

    def resolve_airlines(root, info: graphene.ResolveInfo):
        return Airline.objects.all()
