import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "app")
    )
)

from logger import log_event

def send_email():

    log_event(
        module="notification",
        event="email_sent",
        data={
            "recipient": "student@gmail.com"
        }
    )

send_email()