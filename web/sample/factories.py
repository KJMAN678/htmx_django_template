from factory import Faker, django


class SampleModelFactory(django.DjangoModelFactory):
    class Meta:
        model = "sample.SampleModel"

    name = Faker("name")
    description = Faker("text")
