"""import threading
import time

from django.http import HttpResponse

from .models import TestModel


def test_signal(request):

    start = time.time()

    print(
        f"Caller Thread ID : {threading.get_ident()}"
    )

    TestModel.objects.create(
        name="Accuknox"
    )

    end = time.time()

    return HttpResponse(
        f"Request Completed in {end-start:.2f} seconds"
    )
    """

from django.http import HttpResponse
from django.db import transaction
from .models import TestModel

def test_signal(request):
    TestModel.objects.create(name="Accuknox")
    return HttpResponse("Signal Test Completed")


def transaction_test(request):
    try:
        with transaction.atomic():

            TestModel.objects.create(
                name="Transaction Test"
            )

            print("Object Created")

            raise Exception("Rollback Transaction")

    except Exception:
        print("Transaction Rolled Back")

    count = TestModel.objects.count()

    return HttpResponse(
        f"Final Database Count = {count}"
    )