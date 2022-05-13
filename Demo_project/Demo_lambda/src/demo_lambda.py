import boto3

def lambda_handler(event,context):
    try:
        if event is not None:
            message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])
            return {
                    'message': message
                }
        else:
            print("event is null ")

    except Exception as e:
        print("pls check not found values",e)



def create_table(dynamodb=None):
    dynamodb = boto3.resource(
        'dynamodb', endpoint_url="http://localhost:8000")
    # Table defination
    table = dynamodb.create_table(
        TableName='table_name',
        KeySchema=[
            {
                'AttributeName': 'primary_key_id',
                'KeyType': 'HASH'  # Partition key or sort key(RANGE)
            },
            {
                'AttributeName': 'datacount',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'device_id',
                # AttributeType defines the data type. 'S' is string type and 'N' is number type
                'AttributeType': 'S' #string type
            },
            {
                'AttributeName': 'datacount',
                'AttributeType': 'N'
            },
        ],
        ProvisionedThroughput={
            # ReadCapacityUnits set to 10 strongly consistent reads per second
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10  # WriteCapacityUnits set to 10 writes per second
        }
    )
    return table



if __name__ == '__main__':
    table = create_table()
    # Print table status
    print("Status:", table.table_status)