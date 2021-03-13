# faust-poc
Some Faust ideas.

## How to Run

### Requirements
- Python 3
- Docker

### Run Local Kafka
1. Run a local Kafka server with

``docker-compose -f dev/kafka.yaml up``

2. With `docker ps`, find the Docker container ID of the `wurstmeister/kafka` container and save to environment with `export KAFKA_CONTAINER_ID=<container ID>`.

Now we can do the following:

- Listen on a topic:

``
docker container exec ${KAFKA_CONTAINER_ID} kafka-console-consumer.sh --bootstrap-server :9092 --topic <Topic name>
``

### Run App
1. Open a clean Python3 environment and install requirements with

``
pip install -r requirements.txt
``

2. Run the main app with

``
python src/main.py worker
``