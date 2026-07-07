import json
import os


def load_alert(alert_name):

    file_path = os.path.join(
        "knowledge",
        "alerts",
        f"{alert_name}.json"
    )

    if not os.path.exists(file_path):
        return None

    with open(file_path, "r") as file:

        return json.load(file)