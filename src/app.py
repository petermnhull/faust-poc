import faust
import datetime as dt

import settings


class MyFaustApp(faust.App):
    """
    Simple Faust app for generating and processing messages.
    """

    def __init__(self, name: str, broker: str, web_port: int):
        super().__init__(
            name,
            broker=f"kafka://{broker}",
            topic_allow_declare=True,
            topic_disable_leader=True,
            web_port=web_port,
        )

        # Kafka topics
        input_topic = self.topic(settings.INPUT_TOPIC)
        output_topic = self.topic(settings.OUTPUT_TOPIC)

        @self.timer(interval=1)
        async def every_second():
            """
            Produces one message a second to input topic.
            :return:
            """
            message = {"message": "Hello!", "created_at": str(dt.datetime.now())}
            await input_topic.send(value=message)

        @self.agent(input_topic)
        async def process_message(stream):
            """
            Receives message from input stream and processes it.
            :param stream:
            :return:
            """
            async for message in stream:
                message["processed_at"] = str(dt.datetime.now())
                await output_topic.send(value=message)

        @self.agent(output_topic)
        async def print_message(stream):
            """
            Receives message from output stream and prints it.
            :param stream:
            :return:
            """
            async for message in stream:
                message["received_at"] = str(dt.datetime.now())
                print(message)
