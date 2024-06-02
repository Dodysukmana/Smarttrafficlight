import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

broker_address = "mqtt.eclipseprojects.io"  # Ganti dengan alamat broker MQTT Anda

client = mqtt.Client('Temperature_Inside')
client.connect(broker_address, 1883)

# Kirim angka "1" ke topik "control/led"
client.publish("control/led", "1")

client.loop_forever()