#coding=UTF8

##解析html源代码
# 1.通过urllib2请求url并获取网页源代码
# 2.将html源代码保存在本地目录下
# 3.

#urllib2官方文档
#https://docs.python.org/2.7/library/urllib2.html

import urllib2


class HtmlParser:

    def __init__(self):
        self.name = 'HtmlParser'
        self.file_dir = 'E:\\project\\python\\files\\lvmama\\'

    # 获取指定uri的html源代码
    @staticmethod
    def get_html_source(uri):
        request = urllib2.Request(uri)
        request.add_header('User-Agent', 'fake-client')
        response = urllib2.urlopen(request)

        html_source = ''
        if response.getcode() == 200:
            html_source = response.read()

        return html_source

    # 把文本存入文件
    def save_txt_file(self, file_name, content):
        abs_path = self.file_dir + file_name
        new_file = open(abs_path, 'w')
        new_file.write(content)
        new_file.close()


if __name__ == '__main__':
    htmlParser = HtmlParser()
    product_id = 157434
    source = HtmlParser.get_html_source('http://ticket.lvmama.com/scenic-157434')
    print(source)
    htmlParser.save_txt_file(str(product_id) + '.html', source)