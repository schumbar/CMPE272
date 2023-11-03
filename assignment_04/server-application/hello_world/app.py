import datetime
import json

def lambda_handler(event, context):
    today = datetime.date.today()
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    message = f"Today's date is: {today} and the current time is: {current_time}"

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
        }),
    }
