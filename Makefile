KAFKA_BROKER=9092
ZOOKEEPER_HOST=2181

make kafka:
	docker-compose -f dev/kafka.yaml up

make list-topics:
	docker container exec ${KAFKA_CONTAINER_ID} kafka-topics.sh --bootstrap-server :${KAFKA_BROKER} --list --zookeeper :${ZOOKEEPER_HOST}

make listen-topic:
	docker container exec ${KAFKA_CONTAINER_ID} kafka-console-consumer.sh --bootstrap-server :${KAFKA_BROKER} --topic ${TOPIC}