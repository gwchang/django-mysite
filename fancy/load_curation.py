import yaml

filepath = './warcraft.yaml'
text = open(filepath).read()
data = yaml.load(text, yaml.SafeLoader)
print(data)
