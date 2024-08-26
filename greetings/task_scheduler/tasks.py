from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from core.models import User
from greetings.repository import GreetingsRepository  

@shared_task
def send_birthday_greetings():
    today = timezone.now().date()
    users_with_birthday = User.objects.filter(date_of_birth=today)

    for user in users_with_birthday:
        GreetingsRepository().send_birthday_greetings_email(user.username, user.email)
        


