from django.core.management.base import BaseCommand

from mail.tasks import item_production_mailer


class Command(BaseCommand):
    help = 'Reports production created on a perticular day'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)
    #     return parser

    def handle(self, *args, **options):
        result = item_production_mailer()
        if result:
            self.stdout.write(
                'Successfully')
        else:
            self.stdout.write(
                'Failed to run')
