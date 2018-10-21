import urllib.request
import datetime
import re


def get_html(url):
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
        return html
    except Exception as e:
        print(e)


def write_html_to_file(html, directory, url=''):
    time_stamp = datetime.datetime.now().strftime('%Y_%m_%d%H_%M_%S')
    pattern = re.compile('http://|https://')
    url = pattern.sub('', url)
    file_name = directory + url + 'T' + time_stamp + '.diggerdata'
    with open(file_name, 'wt', encoding='utf-8') as f:
        f.write(html.decode("utf-8"))


def save(url, directory):
    html = get_html(url)
    write_html_to_file(html, directory, url)

