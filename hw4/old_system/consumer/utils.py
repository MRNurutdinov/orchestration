import datetime
import json
import logging
from dataclasses import dataclass
from typing import Coroutine, Callable

from aiokafka import AIOKafkaConsumer
from confluent_kafka import Producer

logging.basicConfig(filename='logs/output.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def create_producer(KAFKA_HOST):
    conf = {
        'bootstrap.servers': KAFKA_HOST,
    }

    return Producer(conf)


@dataclass
class TopicWithFunction:
    topic_name: str
    func: Callable[..., Coroutine]


async def send_data_topic(producer: Producer, topic_name: str, data: dict):
    message = json.dumps(data).encode('utf-8')
    try:
        future = producer.produce(topic_name, value=message)
        producer.flush()
    except Exception as e:
        logging.WARNING(f"Failed to produce message: {e}")


async def consume_messages(topic_name: str, GROUP_ID: str, KAFKA_HOST: str):
    consumer = AIOKafkaConsumer(
        *[topic_name],
        bootstrap_servers=KAFKA_HOST,
        group_id=GROUP_ID,
        auto_offset_reset='earliest',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')))

    await consumer.start()
    try:
        async for message in consumer:
            text = f"get: {message.value}, {datetime.datetime.now().time()}"
            logging.warning(text)
    except KeyboardInterrupt:
        logging.WARNING("Interrupted")
        pass
    finally:
        logging.WARNING("Stopping consumer")
        await consumer.stop()
