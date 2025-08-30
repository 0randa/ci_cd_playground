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


def add_task(name) -> None:
    task_list = []

    if not os.path.exists(TASK_DATA_PATH) or os.path.getsize(TASK_DATA_PATH) == 0:
        task_list.append({"id": 1, "name": name})
    else:
        with open(TASK_DATA_PATH, "r") as f:
            task_list = json.loads(f.read())
            task_list.append({"id": len(task_list) + 1, "name": name})

    with open(TASK_DATA_PATH, "w") as f:
        f.write(json.dumps(task_list))


if __name__ == "__main__":
    add_task("yoo")
