import pytest
from django.core.management import call_command

from sample.models import SampleModel


@pytest.mark.django_db
def test_sample_command():
    call_command("sample_command", 3)
    assert SampleModel.objects.count() == 3
