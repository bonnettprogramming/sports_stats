import requests
import configparser

default_config_file = 'config/test.ini'


def test_api_call(key, service):
    params = {
        'service': service,
        'key': key
    }
    # url = "https://api.natstat.com/v2/players/{service}/?key={key}&format=json&id=21".format(service=service, key=key)
    url = "https://api.natstat.com/v2/teams/{service}/?key={key}&format=json&".format(**params)
    result = requests.get(url)
    result_json = result.json()
    print('result_json', result_json)
    print_json(result_json)


def print_item(item, level=0):
    """
    print an item
    :param item:
    :param level:
    :return:
    """
    output = ""
    for index in range(level):
        output += '\t'
    output += item
    print(output)


def print_json(json_object, level=0):
    """
    print a human-readable version of json object
    :param json_object: this should be a decoded json object or dictionary
    :param level: leave this alone
    :return: nothing
    """
    for key in json_object:
        print_item(key, level)
        if type(json_object[key]) is dict:
            print_json(json_object[key], level + 1)
        else:
            print_item(json_object[key], level + 1)


def create_config(filename=default_config_file):
    """
    Create a default config file
    :param filename:
    :return:
    """
    test = configparser.ConfigParser()
    test['api_info'] = {
        'key': 'XXXX-XXXXXX',
        'service': 'NBA'
    }
    with open(filename, 'w') as file:
        test.write(file)
        file.flush()
        file.close()


def load_config(filename=default_config_file):
    """
    load the config file
    :param filename: only provide if you want to override default
    :return:
    """
    parser = configparser.ConfigParser()
    with open(filename, 'r') as file:
        parser.read_file(file)
    return parser


if __name__ == '__main__':
    # create_config()
    config = load_config()
    params = {
        'key': config['api_info']['key'],
        'service': config['api_info']['service']
    }
    test_api_call(**params)
