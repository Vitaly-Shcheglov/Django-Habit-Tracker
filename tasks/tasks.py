import os
from celery import shared_task
import requests
from django.utils import timezone
from .models import Habit

TELEGRAM_API_URL = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}/sendMessage"


@shared_task
def send_reminder(habit_id, chat_id):
    """
    Отправляет напоминание о привычке пользователю в Telegram.

    Параметры:
        habit_id (int): ID привычки, о которой нужно напомнить.
        chat_id (int): ID чата Telegram, куда будет отправлено сообщение.
    """
    try:
        habit = Habit.objects.get(id=habit_id)

        message = f"Напоминание: Время выполнять привычку '{habit.action}' в '{habit.location}'."

        response = requests.post(TELEGRAM_API_URL, data={"chat_id": chat_id, "text": message})

        if response.status_code != 200:
            raise Exception(f"Ошибка при отправке сообщения: {response.text}")

        print(f"Напоминание отправлено для привычки: {habit.action}")

    except Habit.DoesNotExist:
        print(f"Привычка с ID {habit_id} не найдена.")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


@shared_task
def send_scheduled_reminders():
    """
    Находит привычки, которые нужно напомнить, и отправляет уведомления.
    """
    now = timezone.now()

    habits = Habit.objects.filter(time__hour=now.hour, time__minute=now.minute)

    for habit in habits:
        send_reminder.delay(habit.id, habit.user.telegram_chat_id)
