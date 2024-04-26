import time
from functions import get_df

def lambda_handler(event, context):    

    time1 = time.time()
    time.sleep(1)
    time2 = time.time()

    return {
        'statusCode' : 200,
        'body' : f'Hello World ! {time1, time2}',
    }

