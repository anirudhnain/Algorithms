from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
import random
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError


# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):

    dynamodb = boto3.resource("dynamodb", region_name='eu-west-1')
    
    table = dynamodb.Table('GraphTable')
    
    try:
        response = table.get_item(
            Key={
                'GraphName': 'TestGraph'
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response["Item"]
        return createGraph(item["GraphStructure"])

def createGraph(s):
    
    graph = {}
    edges = s.split(',')
    
    nodes = {}
    adjacencyGraph = {}
    for edge in edges:
    	n1,n2 = edge.split('->')
    	if n1 not in adjacencyGraph:
    		adjacencyGraph[n1] = set()
    
    	adjacencyGraph[n1].add(n2)
    
    
    #create subgraph from graph
    subGraph = {}
    for key in adjacencyGraph.keys():
    	booleanArray = [True, False]
    	if random.choice(booleanArray):
    		start = random.randint(0, len(adjacencyGraph[key]))
    		end = random.randint(0, len(adjacencyGraph[key]))
    		if start>end:
    			start,end = end,start
    		elif start == end:
    			start -= 1
    
    		subGraph[key] = list(adjacencyGraph[key])[start:end]
    
    return subGraph
https://medium.com/coinmonks/how-does-hyperledger-fabric-works-cdb68e6066f5