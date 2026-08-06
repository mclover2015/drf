import os

from django.contrib.auth import apps, get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from configs.celery import app

from core.dataclasses.user_dataclass import UserDataClass
from core.services.jwt_service import ActivateToken, JWTService

UserModel = get_user_model()

class EmailService:

    @staticmethod
    @app.task
    def __send_mail(to: str, template_name: str, context: dict, subject=''):
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject, from_email=os.environ.get("EMAIL_HOST_USER"), to=[to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    @classmethod
    def register(cls, user: UserDataClass):
        token = JWTService.create_token(user, ActivateToken)
        url = f'http://localhost:3000/activate/{token}'
        cls.__send_mail.delay(
            user.email,
            'register.html',
            {'name': user.profile.name,
             'url': url},
            'register'
        )
    @staticmethod
    @app.task
    def spam():
        for user in UserModel.objects.all():
            user: UserDataClass = user
            EmailService.__send_mail(user.email, 'spam.html', {'user': user.profile.name}, subject='Spam')