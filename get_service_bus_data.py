# import os
from azure.servicebus import ServiceBusClient, ServiceBusMessage


CONNECTION_STR = "Endpoint=sb://wessel-service-bus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=+Hfqcib8PaLZvP52NW5ilbPrhm1XCUwVRY8R2IastYY="
QUEUE_NAME = "wessel-queue"

#CLient aamaken NODIG
servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)

print('--> Get Service Bus data')        
with servicebus_client:
    receiver = servicebus_client.get_queue_receiver(queue_name=QUEUE_NAME, max_wait_time=5)
    with receiver:
        for msg in receiver:
            print("Received: " + str(msg))
            receiver.complete_message(msg)
