"""import threading
import time

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import TestModel

@receiver(post_save, sender=TestModel)
def signal_receiver(sender, instance, **kwargs):
    print("Signal Started")
    print(f"Signal Thread ID: {threading.get_ident()}")

    time.sleep(5)

    print("Signal Completed")"""

import threading
import time

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import TestModel


@receiver(post_save, sender=TestModel)
def signal_receiver(sender, instance, **kwargs):

    print("Signal Started")
    print(f"Signal Thread ID: {threading.get_ident()}")

    count = TestModel.objects.count()
    print(f"Signal sees record count = {count}")

    time.sleep(1)

    print("Signal Completed")
