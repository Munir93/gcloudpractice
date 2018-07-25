import config
from google.cloud import pubsub
import os
import time

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/709231/PycharmProjects/DataMigrationProjectGCP/pubsub-with-storage.json"
publisher = pubsub.PublisherClient()
topic_path = publisher.topic_path(config.PROJECT_ID, 'twitter-stream')

'''Create sub client'''
subscriber = pubsub.SubscriberClient()

'''Creating subscription '''
subscription_path = subscriber.subscription_path(config.PROJECT_ID, 'twitter_sub')
#subscriber.create_subscription(subscription_path,topic_path)



'''Subscribe to subscription'''
def callback(message):
    print('Received message: {}'.format(message.data))
    message.ack()


subscriber.subscribe(subscription_path, callback=callback)

# The subscriber is non-blocking, so we must keep the main thread from
# exiting to allow it to process messages in the background.
print('Listening for messages on {}'.format(subscription_path))
while True:
    time.sleep(60)