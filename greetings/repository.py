# from app.utils.config import settings

from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
from core.models import User
from utils.email.sender import SendEmail
from django.contrib.auth import get_user_model
from django.db import models


class GreetingsRepository:

    def send_birthday_greetings_email(self, user_name, user_email):
        html_template_path = "birthday_greetings.html"
        template_data = {
            "sender": None,
            "subject": f"Happy Birthday, {user_name}!",
            "name": user_name,
            "all_recipients": [user_email],
            "path_to_html_template": html_template_path,
            "path_to_attachment_file": None,  # optional

        }
        SendEmail().send_email(template_data=template_data)


