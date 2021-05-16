import datetime as dt

from src.app import app
from src import settings

# Kafka topics
input_topic = app.topic(settings.INPUT_TOPIC)
output_topic = app.topic(settings.OUTPUT_TOPIC)

@app.timer(interval=1)
async def every_second():
    """
    Produces one message a second to input topic.
    :return:
    """
    message = {"message": "Hello!", "created_at": str(dt.datetime.now())}
    await input_topic.send(value=message)
