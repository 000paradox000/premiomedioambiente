from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create or reset admin user"
    data = dict(username="admin",
                email="admin@premiomedioambiente.caracoltv.com",
                first_name="Admin",
                last_name="User")
    password = "admin"

    def handle(self, *args, **options):
        user_model = get_user_model()
        objects = user_model.objects
        admin_user = objects.filter(username=self.data.get("username"))
        exists = admin_user.exists()

        if exists:
            admin_user.update(**self.data)
            admin_user = admin_user.first()
            admin_user.set_password(self.password)
        else:
            admin_user = objects.create_superuser(**self.data, password=self.password)

        admin_user.save()
