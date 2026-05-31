import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "app")
    )
)

from logger import log_event


def login_user():

    log_event(
        module="auth",
        event="user_login",
        data={
            "user_id": 101
        }
    )


login_user()
