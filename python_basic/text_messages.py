texts = ['where you at', "i'm outside rn", 'can you go to the store']
sent_messages = []

def show_messages(texts):
    """Print text messages in list"""
    for text in texts:
        print(text)

def send_messages(texts):
    """Move text messages in list to "sent" list"""
    while texts:
        sending_message = texts.pop()
        print(sending_message)
        sent_messages.append(sending_message)


print(texts)
print(sent_messages)

send_messages(texts[:])

print(texts)
print(sent_messages)