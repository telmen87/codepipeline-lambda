import time

def lambda_handler(event, context):

    return {
        'statusCode' : 200,
        'body' : f'Hello World ! {time.time()}'
    }