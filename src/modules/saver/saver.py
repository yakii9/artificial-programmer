import urllib2


def get_html(url):
    try:
        s = urllib2.urlopen(url).read()
        return s
    except urllib2.HTTPError as e:
        print(e.code)
    except urllib2.URLErrror as e:
        print(str(e))
    finally:
        return ''
