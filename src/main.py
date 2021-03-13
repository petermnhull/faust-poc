from app import MyFaustApp
import settings

if __name__ == "__main__":
    """
    Create app and run it.
    """
    app = MyFaustApp(
        name="Peter's Faust App",
        broker=settings.KAFKA_BROKER,
        web_port=settings.WEB_PORT,
    )
    app.main()
