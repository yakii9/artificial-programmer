from modules.save import save
import json

if __name__ == '__main__':
    print('digger says hello to you!')
    with open('config\\base.json', 'rt', encoding='latin-1') as f:
        json_str = f.read()
        base_config = json.loads(json_str)
    save(base_config['entry_url'], base_config['save_to'])
