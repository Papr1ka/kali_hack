# in file task.py
from celery.app import Celery
from datetime import datetime
import os


app = Celery('app_name', backend="rpc://", broker='amqp://myuser:mypassword@localhost:5672/myvhost')


@app.task
def dummy_task():
    folder = "/tmp/celery"
    os.makedirs(folder, exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%s")
    with open(f"{folder}/task-{now}.txt", "w") as f:
        f.write("hello!")
