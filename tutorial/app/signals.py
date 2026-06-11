from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Employee


@receiver(post_save,sender=Employee)
def user_created(sender,instance,created,**kwargs):
    print(f"{sender=},{instance=},{created=}")

    