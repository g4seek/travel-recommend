# coding=UTF8

# 解析html源代码
# 1.通过urllib2请求url并获取网页源代码
# 2.将html源代码保存在本地目录下

# urllib2官方文档
# https://docs.python.org/2.7/library/urllib2.html

import urllib2
import datetime

import threadpool


class PageFetcher:
    def __init__(self):
        # self.uri_template = 'http://ticket.lvmama.com/scenic-{0}'
        self.uri_template = 'http://www.ly.com/scenery/BookSceneryTicket_{0}.html'
        self.file_dir = '/Users/lvzimin/Desktop/files/ly/'
        self.thread_num = 50

    # 获取指定uri的html源代码
    @staticmethod
    def get_html_source(uri):
        request = urllib2.Request(uri)
        request.add_header('User-Agent', 'Mozilla/5.0')
        try:
            response = urllib2.urlopen(request)
        except Exception:
            return ''

        if response.getcode() == 200:
            return response.read()

    # 把文本存入文件
    def save_html_file(self, file_name, content):
        abs_path = self.file_dir + file_name
        new_file = open(abs_path, 'w')
        new_file.write(content)
        new_file.close()

    # 抓取单个网页
    def fetch_page(self, index):
        source = self.get_html_source(self.uri_template.format(str(index)))
        date_str = datetime.datetime.now().strftime("%H:%M:%S")
        if source != '':
            print(date_str + ',saving file...id:' + str(index))
            self.save_html_file(str(index) + '.html', source)
        else:
            print(date_str + ',skip file...id:' + str(index))

    # 尝试循环抓取网页
    def try_loop_fetch(self, start, end):
        fetch_range = []
        for i in range(start, end + 1):
            fetch_range.append(i)

        pool = threadpool.ThreadPool(self.thread_num)
        requests = threadpool.makeRequests(self.fetch_page, fetch_range)
        [pool.putRequest(req) for req in requests]
        pool.wait()


if __name__ == '__main__':
    pageFetcher = PageFetcher()
    pageFetcher.try_loop_fetch(100000, 100000)
