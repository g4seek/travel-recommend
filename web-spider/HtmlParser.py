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
        self.uri_template = 'http://ticket.lvmama.com/scenic-{0}'
        self.file_dir = 'E:\\project\\python\\files\\lvmama\\'

    # 获取指定uri的html源代码
    def get_html_source(self, uri):
        request = urllib2.Request(uri)
        request.add_header('User-Agent', '	Mozilla/5.0')
        try:
            response = urllib2.urlopen(request)
        except:
            return ''

        if response.getcode() == 200:
            return response.read()

    # 把文本存入文件
    def save_txt_file(self, file_name, content):
        abs_path = self.file_dir + file_name
        new_file = open(abs_path, 'w')
        new_file.write(content)
        new_file.close()


    #尝试循环抓取网页
    def try_loop_fetch(self, start, end):
        for i in range(start, end):
            source = self.get_html_source(self.uri_template.format(str(i)))
            if source != '':
                print('saving file...id:' + str(i))
                self.save_txt_file(str(i) + '.html', source)
            else:
                print('skip file...id:' + str(i))


if __name__ == '__main__':
    htmlParser = HtmlParser()
    htmlParser.try_loop_fetch(664, 100000)