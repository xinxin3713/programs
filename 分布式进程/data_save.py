#!/usr/bin/env python
# _*_coding:utf-8 _*_
__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/4/3"

import codecs
import time

class DataOutput(object):

    def __init__(self):
        self.filepath ='baike_%s.html'%(time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime()))
        self.output_head(self.filepath)
        self.datas =[]

    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)
        if len((self.datas)>10):
            self.output_html(self.filepath)

    def output_head(self,path):

        fout = codecs.open(path,'w',encoding='urt-8')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        fout.close()

    def output_html(self,path):
        fout = codecs.open(path,'a',encoding='urt-8')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s<td>'%data['url'])
            fout.write('<td>%s<td>' % data['title'])
            fout.write('<td>%s<td>'%data['summary'])
            fout.write('<tr>')
            self.datas.remove(data)
        fout.close()


    def output_end(self,path):
        fout = codecs.open(path,'a',encoding='utf-8')
        fout.write(('</table>'))
        fout.write("</body>")
        fout.write("</html>")
        fout.close()