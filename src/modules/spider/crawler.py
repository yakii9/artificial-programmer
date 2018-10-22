from modules.base.url_helper import ElementsFinder, UrlHelper


class WebCrawler:

    def __init__(self, entry_url, progression=10):
        self.base_url = entry_url
        self.progression = progression
        self.links_web = []

    def get_links_web(self):
        return self.links_web

    def generate_crawl_web(self):
        self.get_links([self.base_url], 0, self.progression)

    def get_links(self, unprocessed_pages, current_level, max_level):
        url_tool = UrlHelper()
        base_url = url_tool.get_domain_name(self.base_url)

        self.links_web.append([])

        finder = ElementsFinder(base_url, '')
        for page_url in unprocessed_pages:
            print('processing: '+page_url)
            try:
                html = url_tool.get_html(page_url).decode("utf-8")
                finder.feed(html)
                links = finder.page_links()
                self.links_web[current_level].append(links)
            except Exception as e:
                pass

        if current_level >= max_level:
            return

        for unprocessed_links in self.links_web[current_level]:
            self.get_links(unprocessed_links, current_level+1, max_level)