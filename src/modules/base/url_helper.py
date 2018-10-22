import urllib.request
from html.parser import HTMLParser
from urllib import parse


class ElementsFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass


class UrlHelper:

    def __init__(self):
        pass

    @staticmethod
    def get_html(url):
        try:
            with urllib.request.urlopen(url) as response:
                html = response.read()
            return html
        except Exception as e:
            print(e)

    def get_domain_name(self, url):
        try:
            results = self.get_sub_domain_name(url).split('.')
            return results[-2] + '.' + results[-1]
        except:
            return ''

    # Get sub domain name (name.example.com)
    @staticmethod
    def get_sub_domain_name(url):
        try:
            return parse.urlparse(url).netloc
        except:
            return ''
