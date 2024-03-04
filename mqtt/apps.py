from django.apps import AppConfig
from . import mqtt

class MQTTConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mqtt'

    def ready(self):
        # Start the MQTT subscriber when Django application starts
        mqtt.mqtt_subscriber()
