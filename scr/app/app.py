import time
from functions import get_df

def lambda_handler(event, context):    

    return {
        'statusCode' : 200,
        'body' : f'Hello World ! {time.time(), get_df(), time.time()}',
    }
