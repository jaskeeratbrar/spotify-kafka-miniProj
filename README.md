# Spotify Kafka Integration

This project consists of two main scripts, `producer.py` and `consumer.py`, which integrate with the Spotify API and Apache Kafka to fetch real-time data about music tracks and process this information for further analysis.

## producer.py
The `producer.py` script is responsible for authenticating with Spotify's API and retrieving data for a specific album. The script then serializes this data as JSON and sends it to a Kafka topic.

### Key Features:
- OAuth authentication with Spotify
- Fetches album data using Spotify's Web API
- Sends data to a Kafka topic for consumption

## consumer.py
The `consumer.py` script listens to the Kafka topic for new messages, extracts the artist's name from each message, and writes the message to a text file named with the artist's name and the current timestamp.

### Key Features:
- Consumes messages from a Kafka topic
- Extracts artist name from the message data
- Writes each message to a uniquely named file based on the artist's name and timestamp

## Setup and Configuration

### Prerequisites
- Python 3.7+
- Kafka (with a running Kafka server)
- Spotify Developer account and API credentials

### Installation
1. Clone the repository to your local machine.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt

