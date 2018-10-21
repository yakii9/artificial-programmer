from modules.save import save
import json

if __name__ == '__main__':
    print('digger says hello to you!')
    with open('config\\base.json', 'rt', encoding='utf-8') as f:
        json_str = f.read()
        base_config = json.loads(json_str)
    print('digger is working now.')
    save(base_config['entry_url'], base_config['save_to'])
    print('working complete!')
