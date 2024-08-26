from datetime import datetime, timedelta
from event.repository import EventRepository
from event.task_scheduler.tasks import send_email_notification


def schedule_event_reminder_email(user_instance, event_instance):
    event_time = datetime.strptime(
        event_instance["start_time"], "%Y-%m-%dT%H:%M:%S.%fZ"
    )
    notification_time = event_time - timedelta(minutes=2)
    delay_in_seconds = (notification_time - datetime.utcnow()).total_seconds()
    print("Delay: ", delay_in_seconds)
    user_name = user_instance.name
    user_email = user_instance.email
    event_title = event_instance["title"]
    event_start_time = event_instance["start_time"]
    # send_email_notification.apply_async((user_name, user_email, event_title, event_start_time), countdown=delay_in_seconds)
