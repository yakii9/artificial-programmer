from modules.base.file_helper import FileHelper
from modules.base.url_helper import UrlHelper


class UrlSaver:
    def __init__(self, url, directory):
        self.url = url
        self.directory = directory

    def save(self):
        url_tool = UrlHelper(self.url)
        html = url_tool.get_html()
        file_tool = FileHelper()
        file_tool.write_text_to_file(html, self.directory, prefix=self.url)
