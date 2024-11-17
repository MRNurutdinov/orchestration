import datetime
import json
import logging
from dataclasses import dataclass
from typing import Coroutine, Callable

from aiokafka import AIOKafkaConsumer
from confluent_kafka import Producer


def create_producer(KAFKA_HOST):
    conf = {
        'bootstrap.servers': KAFKA_HOST,
    }

    return Producer(conf)


@dataclass
class TopicWithFunction:
    topic_name: str
    func: Callable[..., Coroutine]


async def send_data_topic(producer: Producer, topic_name: str, message: str):
    try:
        producer.produce(topic_name, value=json.dumps(message).encode('utf-8'))
        producer.flush()
    except Exception as e:
        logging.WARNING(f"Failed to produce message: {e}")

