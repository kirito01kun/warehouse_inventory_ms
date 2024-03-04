import paho.mqtt.client as mqtt
from mongoengine import connect
from .models import RackInventory


def on_message(client, userdata, message):
    payload = message.payload.decode('utf-8')
    # Check if the received message is the same as the last message
    level_data = payload.split('-')
    rack_inventory = RackInventory.objects(rack_number=level_data[0]).first()
    if rack_inventory:
        rack_inventory.level_0 = int(level_data[1])
        rack_inventory.level_1 = int(level_data[2])
        rack_inventory.level_2 = int(level_data[3])
        rack_inventory.level_3 = int(level_data[4])
        rack_inventory.save()


def mqtt_subscriber():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)    
    client.on_message = on_message
    client.connect("localhost", 1883)  # Use localhost if the broker is running on the same machine
    client.subscribe("InvLevel")  # Update with your MQTT topic
    client.loop_start()
