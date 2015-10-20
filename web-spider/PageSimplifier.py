# coding=UTF8

# 1.分析html代码,删除无用的文件
# 2.删除重复或多余的html代码

from bs4 import BeautifulSoup
import threadpool
import os


class PageSimplifier:
    def __init__(self):
        pass

    # 删除无用的文件
    def delete_invalid_file(self):
        pass

    # 删除多余的代码
    def delete_redundant_source(self):
        pass

    def read_file(self, file_path):
        page_file = open(file_path, 'r+')
        return page_file.read()

    def delete_file(self, file_path):
        print ("file deleted:" + file_path)
        os.remove(file_path)
        pass


# 同程
class LySimplifier(PageSimplifier):
    def delete_invalid_file(self, index):
        path_template = "/Users/lvzimin/Desktop/files/ly/{0}.html"
        file_path = path_template.format(str(index))
        html = lySimplifier.read_file(file_path)
        soup = BeautifulSoup(html, "html.parser")
        title = soup.title.string
        if u'门票_门票多少钱' in title:
            self.delete_file(file_path)

    def delete_redundant_source(self):
        pass


if __name__ == '__main__':
    lySimplifier = LySimplifier()

    fetch_range = []
    for i in range(12600, 100000 + 1):
        fetch_range.append(i)

    pool = threadpool.ThreadPool(50)
    requests = threadpool.makeRequests(lySimplifier.delete_invalid_file, fetch_range)
    [pool.putRequest(req) for req in requests]
    pool.wait()
