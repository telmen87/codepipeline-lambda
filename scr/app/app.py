import time
from functions import get_df

def lambda_handler(event, context):
    
    print(get_df())

    return {
        'statusCode' : 200,
        'body' : f'Hello World ! {time.time()}',
    }