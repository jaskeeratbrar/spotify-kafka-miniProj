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
   ```bash
   git clone <repository-url>  
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt

### Configuring the Scripts
- Set your Spotify API credentials in `producer.py`. Replace `your_client_id` and `your_client_secret` with your actual credentials.

### Running the Producer
1. Ensure Kafka is running.
2. Run the `producer.py` script to fetch and send data to Kafka:
   ```bash
   python3 producer.py


### Running the Consumer
1. Run the `consumer.py` script to consume messages from Kafka:
   ```bash
   python3 consumer.py

2. Check the `received_messages` directory for text files containing the fetched data.

## Project Structure
- `producer.py`: Script to fetch data from Spotify's API and send it to Kafka.
- `consumer.py`: Script to consume data from Kafka and write to files.
- `received_messages/`: Directory where the consumer script saves output files.

## Usage Example
Running both the producer and the consumer will provide you with real-time data from Spotify:
   
   ```bash
   ### Terminal window 1:
   python3 producer.py

   ### Terminal window 1:
   python3 consumer.py

## Contributing
Contributions to this project are welcome! Please fork the repository, make your changes, and submit a pull request.






