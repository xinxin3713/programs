from urllib import request
import urllib
from html.parser import HTMLParser


class MovieParser(HTMLParser):
    """

    """
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []
        # 重载HTMLParser自带的函数,
    def handle_starttag(self, tag, attrs):
        def _attr(attrlist, attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None
        # 可以在这class后面找到每个li标签的特征属性比如catrgory在下面判断
        if tag == 'li' and _attr(attrs, 'data-title'):
            movie= {}
            movie['title'] = _attr(attrs, 'data-title')
            movie['rate'] = _attr(attrs, 'data-rate')
            movie['director'] = _attr(attrs, 'data-director')
            movie['actors'] = _attr(attrs, 'data-actors')
            movie['date']=_attr(attrs,'data-date')
            movie['release']=_attr(attrs,'data-release')
            movie['star']=_attr(attrs,'data-star')
            movie['data-duration']=_attr(attrs,'data-duration')
            self.movies.append(movie)
            print('%(title)s|%(rate)s|%(director)s|%(actors)s|%(date)s|%(release)s|%(star)s|%(data-duration)s' % movie)

def print_movies(url):

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    # Python3的urllib
    req = urllib.request.Request(url, headers=header)
    s = urllib.request.urlopen(req)
    parser = MovieParser()
    parser.feed((s.read()).decode('utf-8'))
    s.close()


if __name__ == '__main__':
    url = 'https://movie.douban.com/'
    # 返回一个电影列表
    print_movies(url)
