import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("Django_Habit_Tracker")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.timezone = "UTC"
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "send-reminders-every-minute": {
        "task": "notifications.tasks.send_scheduled_reminders",
        "schedule": crontab(),
    },
}


@app.task(bind=True)
def debug_task(self):
    """Пример задачи для отладки."""
    print(f"Request: {self.request!r}")
