from django.core.management.base import BaseCommand, CommandError
from curations.models import Collection, Asset

import yaml

class Command(BaseCommand):
  help = 'Populates Collection, Asset db from yaml file'
  
  def add_arguments(self, parser):
    parser.add_argument('yaml_file', type=str)

  def handle(self, *args, **options):
    yaml_file = options['yaml_file']
    msg = 'Parsing yaml file %s' % yaml_file
    print(msg)

    yaml_text = open(yaml_file).read()
    yaml_data = yaml.load(yaml_text, yaml.SafeLoader)
    if 'content' in yaml_data:
      contents = yaml_data['content']
      for c in contents:
        print(c['title'])
    else:
      print("Yaml missing 'content' tag.")
