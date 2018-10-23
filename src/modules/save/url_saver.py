from modules.base.file_helper import FileHelper
from modules.base.url_helper import UrlHelper


class UrlSaver:

    @staticmethod
    def save(url, directory):
        url_tool = UrlHelper()
        try:
            html = UrlHelper.get_html(url)
            file_tool = FileHelper()
            file_tool.write_text_to_file(html, directory, prefix=url_tool.get_domain_name(url))
        except Exception as e:
            print(e)
            pass
