import graphene
from core.schema import Query as core_query
from core.schema import Mutation as core_mutation


class Query(core_query, graphene.ObjectType):
    pass


class Mutation(core_mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
