from clinet import PubSubClient
import time

def on_message(topic, message):
    print(f"Received message on topic '{topic}': {message}")

# Create and connect the client
client = PubSubClient()
client.connect()

# Set up the message callback
client.on_message(on_message)

# Subscribe to a topic
client.subscribe("test_topic")

# Publish a message
client.publish("test_topic", "Hello, PubSub!")

# Keep the script running
try:
    while True:
        client.publish("test_topic", "Hello, PubSub!")
        time.sleep(1)
except KeyboardInterrupt:
    print("Disconnecting...")
    client.disconnect()