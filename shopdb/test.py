import os
import base64
import time
from flask import Flask, request
from datetime import datetime
from google.cloud import storage

app = Flask(__name__)

def upload_to_gcs(bucket_name, message,current_timestamp, file_name_prefix='status'):
    """Uploads a message to a GCS bucket with a unique filename based on timestamp."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    
    # Generate a unique filename using a timestamp
    timestamp = current_timestamp

    file_name = f'{file_name_prefix}_{timestamp}.txt'
    
    blob = bucket.blob(file_name)

    current_time = datetime.utcnow().isoformat()
    blob.upload_from_string(f'{current_time}: {message}\n', content_type='text/plain')
    print(f'Message "{message}" uploaded to {bucket_name}/{file_name}.')

@app.route('/', methods=['POST'])
def hello_world():
    print('starting function')
    # Pobranie bieżącego czasu
    current_time = datetime.now()
    current_timestamp = datetime.utcnow().strftime('%Y%m%d-%H%M%S')

    # Wyświetlenie bieżącego czasu
    print("START:", current_time)
    bucket_name = 'webhooks_run_test'
    upload_to_gcs(bucket_name, 'Application is still running.',current_timestamp, "start")
    # Krok 1: Pobranie JSONa z requesta
    envelope = request.get_json()
    if not envelope:
        print('Bad Request: invalid JSON')
        return 'Bad Request: invalid JSON', 400
    print('Step 1: JSON retrieved successfully')

    # Krok 2: Pobranie wiadomości Pub/Sub
    pubsub_message = envelope['message']
    print('Step 2: Pub/Sub message retrieved successfully')

    # Krok 3: Dekodowanie wiadomości
    try:
        if isinstance(pubsub_message, dict) and 'data' in pubsub_message:
            print('Step 3a: Retrieving data field from Pub/Sub message...')
            encoded_data = pubsub_message['data']
            print(f'Step 3a: Encoded data retrieved: {encoded_data}')

            # print('Step 3b: Decoding base64 encoded data...')
            # decoded_bytes = base64.b64decode(encoded_data)
            # print(f'Step 3b: Decoded bytes: {decoded_bytes}')
        else:
            data = pubsub_message.get('data', 'No data')
            print(f'Raw message data: {data}')
        print('Step 3: Message data decoded successfully')
    except Exception as e:
        print(f'Error during decoding message data: {str(e)}')
        return 'Error during decoding message data', 500

    # Krok 4: Delay for 10 seconds
    print('Starting 10 seconds delay...')
    time.sleep(10)
    print('10 seconds delay finished.')
    upload_to_gcs(bucket_name, 'Application is no more running.',current_timestamp, "end")
    print(f'END OF WORK {current_time}')
    return 'Hello, World!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)