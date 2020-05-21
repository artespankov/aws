import boto3

QUEUE_NAME = "artem-training-queue"

# Get the service resource
sqs = boto3.resource('sqs')

queue = sqs.create_queue(QueueName=QUEUE_NAME, Attributes={'DelaySeconds': "5"})
print(f"Queue URL: {queue.url}")
print(f"Delay time {queue.attributes.get('DelaySeconds')}")

queue_reference = sqs.get_queue_by_name(QueueName=QUEUE_NAME)
print(f"Queue URL: {queue.url}")
print(f"Delay time {queue.attributes.get('DelaySeconds')}")

for queue in sqs.queues.all():
    print(f"Queue URL: {queue.url}")

response = queue.send_message(MessageBody='Something not very useful here')
print(f"Message ID: {response.get('MessageId')}")
print(f"Message Body: {response.get('MD5OfMessageBody')}")

response2 = queue.send_message(MessageBody='Something not very useful here',
                               MessageAttributes={
                                   'Author': {
                                       'StringValue': 'Art',
                                       'DataType': 'String'
                                   }
                               })

response = queue.send_messages(Entries=[
    {
        'Id': '1',
        'MessageBody': 'Something not very useful here'
    },
    {
        'Id': '2',
        'MessageBody': 'Something not very useful here',
        'MessageAttributes': {
            'Author': {
                'StringValue': 'Art',
                'DataType': 'String'
            }
        }
    }
])

print(f"Failed messages: {response.get('Failed')}")
