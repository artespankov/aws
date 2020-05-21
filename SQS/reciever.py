import boto3

QUEUE_NAME = "artem-training-queue"

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName=QUEUE_NAME)

for message in queue.receive_messages(MessageAttributeNames=['Author']):
    author_name = ''
    if message.message_attributes is not None:
        author_name = message.message_attributes.get('Author').get('StringValue')

    print(f'Hi there! Message: {message.body}. Author: {author_name}')

    message.delete()