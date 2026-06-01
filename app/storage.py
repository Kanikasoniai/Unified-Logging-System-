import os
import json

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "logs.json")


MAX_SIZE = 5 * 1024


def save_log(log_data):

    print("Saving:", log_data)

    # Check if log file exists and exceeds size limit
    if os.path.exists(LOG_FILE):
        if os.path.getsize(LOG_FILE) >= MAX_SIZE:

            backup_file = os.path.join(LOG_DIR, "logs_backup.json")

            if os.path.exists(backup_file):
                os.remove(backup_file)

            os.rename(LOG_FILE, backup_file)

    with open(LOG_FILE, "a") as file:
        json.dump(log_data, file, default=str)
        file.write("\n")