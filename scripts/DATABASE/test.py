import yaml

config_path = 'images.yml'
config_file = open(config_path)
config_dict = yaml.load(config_file, Loader=yaml.FullLoader)

print(config_dict['family']['2020'])
