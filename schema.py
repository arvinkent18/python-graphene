import graphene
import json

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    created_at = graphene.DateTime()

class Query(graphene.ObjectType):
    hello = graphene.String()
    is_admin = graphene.Boolean()
    
    
    def resolve_hello(self, info):
        return "world"
    
    def resolve_is_admin(self, info):
        return True
    
schema = graphene.Schema(query=Query)

result = schema.execute(
    '''
    {
        hello
        isAdmin
    }
    '''
)

dictResult = dict(result.data.items())

print(json.dumps(dictResult,indent=2))