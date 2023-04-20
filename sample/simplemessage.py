from boto3 import resource
from dotenv import load_dotenv

load_dotenv()

# Get the service resource
sqs = resource('sqs')

queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds':'5'})

# You can now access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))

# Get the queue
queue2 = sqs.get_queue_by_name(QueueName='test')

# Create a new message
response = queue2.send_message(MessageBody='world')

# The response is NOT a resource, but gives you a message ID and MD5
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))