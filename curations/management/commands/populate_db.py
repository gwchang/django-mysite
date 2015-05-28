from django.core.management.base import BaseCommand, CommandError
from curations.models import Collection, Asset

import yaml

class Command(BaseCommand):
  help = 'Populates Collection, Asset db from yaml file'
  
  def add_arguments(self, parser):
    parser.add_argument('yaml_file', type=str)

  def handle(self, *args, **options):
    # Delete all records
    if True:
      Collection.objects.all().delete()
      print('Delete all records in Collection.')
      
      Asset.objects.all().delete()
      print('Delete all records in Asset.')

    # Parse yaml file
    yaml_file = options['yaml_file']
    msg = 'Parsing yaml file %s' % yaml_file
    print(msg)

    yaml_text = open(yaml_file).read()
    yaml_data = yaml.load(yaml_text, yaml.SafeLoader)
    if 'content' in yaml_data:
      contents = yaml_data['content']
      for c in contents:
        self.handle_collection(c)
    else:
      print("Yaml missing 'content' tag.")

  def handle_collection(self, node):
    title = node['title']
    print(title)

    if Collection.objects.filter(title_text=title).exists():
      print("%s already exists in db." % title)
    else:
      c = Collection(
          title_text        = node['title'],
          author_text       = node['by'], 
          description_text  = node['description'],
          homepage_url      = node['link'])
      c.save()

      for asset_node in node['images']:
        a = Asset( 
          file_text = asset_node['asset'],
          title_text = asset_node['title'],
          link_url = asset_node['link'],
          price_text = asset_node.get('price',''),
          collection = c)
        a.save()

      print(c.id)
