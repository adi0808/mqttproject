import mqttclient


# Running the publisher task
mqttclient.publish_message("test.mosquitto.org", 1883, "vegam_aditya", "world")
