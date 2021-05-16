import datetime as dt
import logging

from src.app import app
from src import settings

# Kafka topics
input_topic = app.topic(settings.INPUT_TOPIC)
output_topic = app.topic(settings.OUTPUT_TOPIC)

@app.agent(input_topic)
async def process_message(stream):
    """
    Receives message from input stream and processes it.
    :param stream:
    :return:
    """
    async for message in stream:
        message["processed_at"] = str(dt.datetime.now())
        await output_topic.send(value=message)

@app.agent(output_topic)
async def print_message(stream):
    """
    Receives message from output stream and prints it.
    :param stream:
    :return:
    """
    async for message in stream:
        message["received_at"] = str(dt.datetime.now())
        logging.info(message)
