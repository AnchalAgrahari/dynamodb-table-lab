

import boto3
import json

def readJSON(filePath, table_name):
    try:
        client = boto3.client('dynamodb')
        table = client.Table(table_name)

        with open (filePath,"r") as f :
            data = json.load(f)

        with table.batch_writer() as batch:
            for item in data :
                batch.put_item(Item=item)

            print(f"successfully loaded {len(data)} item from '{filePath}' into '{table_name}'.")

    except Exception as e:
        print("An excption has occured while reading file",e)      
if __name__ == '__main__' :
    try:
        filePath = '/home/anchal/Documents/ddb_tables/tag_resource.json'
        table_name = 'First-table'
        readJSON(filePath, table_name)
    except Exception as e :
        print("An error occured while finding file or dynamoDB Table",e)




import boto3
import json

def add_data_in_DynamoTable(table_name):
    try:
        client = boto3.client('dynamobd', region_name='us-west-1')
        response = client.put_item(
            TableName = 'First-table',
            Item = {
                'UserId': {
            'S': 'vintageSongs',
        },
            'Branch': {
                'N': 'Bollywood'
            }

            }
        )
    except Exception as e :
        print(f"The iteme were added in the {table_name} in dynamoDB Table.")

if __name__ == '__main__':
    try:
        table_name = 'First-table'
        add_data_in_DynamoTable(table_name)
    except Exception as e:
        print("An erroe occured while reading the tavle nanme")





