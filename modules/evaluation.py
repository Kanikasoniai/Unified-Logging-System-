import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "app")
    )
)

from logger import log_event

def generate_score():

    log_event(
        module="evaluation",
        event="score_generated",
        data={
            "score": 95
        }
    )

generate_score()