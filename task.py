#!/usr/bin/env python3

import json
import os

TASK_DATA_PATH = "tasks.json"


def get_tasks() -> list[str]:
    # check the file exists and is not empty
    if not os.path.exists(TASK_DATA_PATH) or os.path.getsize(TASK_DATA_PATH) == 0:
        return ["You currently have no tasks!"]

    ret_arr = []
    with open(TASK_DATA_PATH, "r") as f:
        stream = json.loads(f.read())

        for task in stream:
            _id, name = task["id"], task["name"]
            ret_arr.append(f"{_id}. {name}")

    # remove the extra new line
    return ret_arr


if __name__ == "__main__":
    for t in get_tasks():
        print(t)
