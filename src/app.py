import faust

from src import settings

app = faust.App(
    settings.APP_NAME,
    broker=f"kafka://{settings.KAFKA_BROKER}",
    topic_allow_declare=True,
    topic_disable_leader=True,
    web_port=settings.WEB_PORT,
    autodiscover=True,
    origin="src",
)
