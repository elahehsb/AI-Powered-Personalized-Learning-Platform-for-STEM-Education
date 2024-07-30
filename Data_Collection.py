import time
import json
import random
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def generate_interaction():
    while True:
        interaction = {
            'student_id': random.randint(1, 1000),
            'timestamp': int(time.time()),
            'question': random.choice(['Explain Pythagorean theorem', 'What is the law of gravity?', 'Describe a chemical reaction']),
            'response': random.choice(['Correct', 'Incorrect', 'Partially Correct']),
            'feedback': random.choice(['Great job!', 'Needs Improvement', 'Try again'])
        }
        producer.send('student_interactions', value=interaction)
        time.sleep(1)

generate_interaction()
