import requests
from kafka import KafkaProducer
import json


def get_spotify_access_token(client_id, client_secret):
    """Authenticate to the Spotify API and return the access token."""
    url = 'https://accounts.spotify.com/api/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    response = requests.post(url, headers=headers, data=payload)
    response_data = response.json()
    return response_data['access_token']


def fetch_album_data(access_token, album_id):
    """Fetch album data from Spotify."""
    url = f'https://api.spotify.com/v1/albums/{album_id}/?market=US'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    return response.json()


def create_producer():
    """Create and return a Kafka producer."""
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    return producer


def send_data(producer, topic, data):
    """Send data to a specified Kafka topic."""
    # Convert data to a JSON string for a pretty print
    data_string = json.dumps(data, indent=4)
    print("First few lines of the Spotify response:")
    # Print only the first few lines of the response to avoid overwhelming the console
    print('\n'.join(data_string.split('\n')[:20]))
    producer.send(topic, value=data)
    producer.flush()


if __name__ == "__main__":
    client_id = ''  # removed for privacy concern
    client_secret = '' # it is tied to my personal account
    album_id = '3bSNhnaQQXpC639OQ4pMyP'  # Example album ID

    access_token = get_spotify_access_token(client_id, client_secret)
    album_data = fetch_album_data(access_token, album_id)

    kafka_topic = 'testingFuture'  # Replace with your Kafka topic
    producer = create_producer()
    send_data(producer, kafka_topic, album_data)

    print("Data sent to Kafka topic successfully.")

