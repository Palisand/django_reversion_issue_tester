from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from app.models import Foo, Bar


class Command(BaseCommand):

    def handle(self, *args, **options):
        Foo.objects.bulk_create(
            (
                Foo(
                    thing="123",
                    stuff="123",
                ),
                Foo(
                    thing="123",
                    stuff="123",
                ),
            )
        )
        Bar.objects.bulk_create(
            (
                Bar(
                    thing="123",
                    stuff="123",
                ),
                Bar(
                    thing="123",
                    stuff="123",
                )
            )
        )
        User.objects.create_superuser(
            username="test",
            email="test@mail.com",
            password="pass"
        )
