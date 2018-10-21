import datetime
import re


class FileHelper:
    def __init__(self):
        self.request_head_pattern = re.compile('http://|https://')

    def write_text_to_file(self, text, directory, suffix='.diggerdata', prefix=''):
        time_stamp = datetime.datetime.now().strftime('%Y_%m_%d%H_%M_%S')
        prefix = self.request_head_pattern.sub('', prefix)
        file_name = directory + prefix + 'T' + time_stamp + suffix
        with open(file_name, 'wt', encoding='utf-8') as f:
            f.write(text.decode("utf-8"))
            f.close()
