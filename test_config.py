import configparser
import Contants

config = configparser.ConfigParser()
config.read('resources/config.ini')
print(config.sections())


def get_config_value(config, section, name, default):
    if config.has_option(section, name):
        return config.get(section, name)
    else:
        return default


print('Step 1: ')
for table in get_config_value(config, 'SNF_COPY', Contants.SNOWFLAKE_COPY_TABLES,{}).split(','):
    print(table)
    if get_config_value(config, 'SNF_COPY', Contants.SNOWFLAKE_TABLE_COPY_CLONE_ENABLED.format(table),'N') == 'Y':
        print(f"{table} clone enabled")

for table in get_config_value(config, 'SNF_PARSE', Contants.SNOWFLAKE_PARSE_TABLES,{}).split(','):
    print(table)
