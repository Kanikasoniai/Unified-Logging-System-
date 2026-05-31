import os
import json

LOG_FILE = os.path.join("logs", "logs.json")

def save_log(log_data):
    print("Saving:", log_data)

    with open(LOG_FILE, "a") as file:
        json.dump(log_data, file, default=str)
        file.write("\n")