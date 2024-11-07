from django.apps import AppConfig


class PollsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "polls"


# def ready(self):
#         import polls.signals  # Імпортуємо signals для автоматичного створення токенів




# # myapp/signals.py
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User

# @receiver(post_save, sender=User)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
