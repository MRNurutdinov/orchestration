import asyncio
import time

import env
import utils


async def send():
    print(env.KAFKA_HOST, ";", env.TOPIC_NAME)
    producer = utils.create_producer(env.KAFKA_HOST)
    n = 0
    while True:
        await utils.send_data_topic(producer, env.TOPIC_NAME, f"Это цифра {n}")
        print("Сообщение отправлено,а теперь спать...")
        n += 1
        time.sleep(2)


asyncio.run(send())
