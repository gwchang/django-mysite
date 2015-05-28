from django.core.management.base import BaseCommand, CommandError
from curations.models import Collection, Asset

class Command(BaseCommand):
  help = 'Populates Collection, Asset db from yaml file'
  
  def add_arguments(self, parser):
    parser.add_argument('yaml_file', type=str)

  def handle(self, *args, **options):
    yaml_file = options['yaml_file']
    msg = 'Parsing yaml file %s' % yaml_file
    print(msg)

