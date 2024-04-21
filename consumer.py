from kafka import KafkaConsumer
import json
from datetime import datetime
import os

def create_consumer(topic_name):
    """Create and return a Kafka consumer configured to consume messages from a specified topic."""
    consumer = KafkaConsumer(
        topic_name,
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',  # Start from the earliest message available
        group_id='my-group',  # Consumer group ID
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserialize JSON messages
    )
    return consumer

def extract_artist_name(message):
    """Extract the artist's name from the message."""
    artists = message.get('artists', [])
    if artists:
        return artists[0].get('name', 'UnknownArtist')
    return 'UnknownArtist'

def write_message_to_file(message, artist_name):
    """Write the received message to a text file named after the artist and a timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{artist_name}_{timestamp}.txt"
    # Ensure the directory exists
    if not os.path.exists('received_messages'):
        os.makedirs('received_messages')
    filepath = os.path.join('received_messages', filename)
    with open(filepath, 'w') as file:
        json.dump(message, file, indent=4)
    print(f"Message written to {filename}")

def process_messages(consumer):
    """Process incoming messages from the Kafka topic."""
    print("Listening for messages...")
    try:
        for message in consumer:
            artist_name = extract_artist_name(message.value)
            print("Received message from artist:", artist_name)
            print(json.dumps(message.value, indent=4))  # Pretty print the JSON data
            write_message_to_file(message.value, artist_name)  # Write message to file
    except KeyboardInterrupt:
        print("Consumer stopped.")
    finally:
        consumer.close()
        print("Consumer connection closed.")

if __name__ == "__main__":
    topic_name = 'testingFuture'
    consumer = create_consumer(topic_name)
    process_messages(consumer)
