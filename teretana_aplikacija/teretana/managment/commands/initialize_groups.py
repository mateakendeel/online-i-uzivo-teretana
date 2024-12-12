from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Create default groups and permissions'

    def handle(self, *args, **kwargs):
        admin_group, created = Group.objects.get_or_create(name='Administrator')
        user_group, created = Group.objects.get_or_create(name='User')

        if created:
            self.stdout.write('Groups created successfully!')
        else:
            self.stdout.write('Groups already exist.')
