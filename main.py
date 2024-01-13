import schedule as sc
import time
from send_message import SendMessage


# objects and methods
send = SendMessage()

# automated message sender
send.details_message()

# SCHEDULE THE MESSAGES
sc.every().day.at("22:30").do(send.details_message) # enter the same time here in the exact format
