from modules.save.url_saver import UrlSaver
import json


if __name__ == '__main__':
    print('digger says hello to you!')

    with open('config\\base.json', 'rt', encoding='utf-8') as f:
        json_str = f.read()
        base_config = json.loads(json_str)

    print('digger is working now.')

    entry_url = base_config['entry_url']
    directory = base_config['save_to']

    UrlSaver.save(entry_url, directory)

    print('working complete!')
