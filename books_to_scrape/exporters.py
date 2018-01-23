# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/22 0022 下午 4:40'

from scrapy.exporters import BaseItemExporter

import xlwt


# excel导出
class ExcelItemExporter(BaseItemExporter):
    def __init__(self, file, **kwargs):
        self._configure(kwargs)

        self.file = file
        self.wbook = xlwt.Workbook()
        self.wsheet = self.wbook.add_sheet('scrapy')

        self.row = 0

    def export_item(self, item):
        fields = self._get_serialized_fields(item)
        for col, v in enumerate(x for _, x in fields):
            self.wsheet.write(self.row, col, v)

        self.row += 1

    def finish_exporting(self):
        self.wbook.save(self.file)