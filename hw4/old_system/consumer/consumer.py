import asyncio
import os

from utils import consume_messages

KAFKA_HOST = os.environ.get('KAFKA_HOST')
GROUP_ID = os.environ.get('GROUP_ID')
TOPIC_NAME = os.environ.get('TOPIC_NAME')

asyncio.run(consume_messages(TOPIC_NAME, GROUP_ID, KAFKA_HOST))
