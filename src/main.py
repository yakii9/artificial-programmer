from modules.spider.crawler import WebCrawler
import json


if __name__ == '__main__':
    print('digger says hello to you!')

    with open('config\\base.json', 'rt', encoding='utf-8') as f:
        json_str = f.read()
        base_config = json.loads(json_str)

    print('digger is working now.')

    entry_url = base_config['entry_url']
    directory = base_config['save_to']

    crawler = WebCrawler(entry_url, directory, 10)
    crawler.generate_crawl_web()

    print('working complete!')
