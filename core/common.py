# coding=utf-8
import logging as log
import json
import math
import urllib
from collections import namedtuple

import simplejson
from django.http import JsonResponse
from django.views import View
from marshmallow.schema import Schema


class CommonView(View):

    def __load_body_data(self):
        ret = {}
        try:
            if self.request.method == 'GET':
                uri = self.request.build_absolute_uri()
                ret = {}
                stage_1 = uri.split("?", 1)
                if len(stage_1) > 1:
                    stage_2 = stage_1[-1].split("&")
                    for x in stage_2:
                        key, value = x.split('=')
                        ret[key] = urllib.unquote(value)
            return json.loads(self.request.body) or ret
        except Exception, e:
            if self.request.method != 'GET':
                log.error('load json data error: %s  data: %s' % (e, self.request.body))
            return {} or ret

    def load_body_data(self, body_data=None):
        if not body_data:
            return self.__load_body_data()

        try:
            return json.loads(body_data) or {}
        except Exception, e:
            log.error('load json data error: %s  data: %s' % (e, body_data))
            return {}

    def paginator(self, rows=10):
        page_num = int(self.load_body_data().get("page", 1))
        page_size = int(self.load_body_data().get("rows", rows))
        def get_pagination_data(total):
            total_pages = int(math.ceil(float(total) / page_size))
            return {
                'page_num': page_num,
                'page_size': page_size,
                'total_pages': total_pages,
                'total_items': total
            }

        Paginator = namedtuple('Paginator', 'start offset page_num page_size get_pagination_data')
        return Paginator(
            start=(page_num - 1) * page_size,
            offset=page_num * page_size,
            page_num=page_num,
            page_size=page_size,
            get_pagination_data=get_pagination_data,
        )

    def pagination_response(self, rows = None, count = None, page_num = 1, page_size = 10, schema=None, **kwargs):
        if count % page_size == 0: total_page = count/page_size
        if count % page_size != 0: total_page = count/page_size + 1
        kwargs.update({"rows": rows if not schema else schema().dump(rows, many=True).data, "page": page_num, "total_page": total_page, "records": count})
        return self.response(kwargs)

    def response(self, *args, **kwargs):

        data = {"success": True}
        data.update({"result": args})
        return JsonResponse(data, status=200)

    def error_response(self, err_msg=None):
        data= {"success": False}
        data.update({"err_msg": err_msg})
        return JsonResponse(data, status=400)

    def schema_response(self, schema, query_sets):
        data = schema().dump(query_sets, many=True).data
        return self.response(data)


class SingletonSchema(Schema):
    _instance = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(SingletonSchema, cls).__new__(cls, *args, **kwargs)
        return cls._instance[cls]


class BaseSchema(SingletonSchema):

    class Meta:
        strict = True
        json_module = simplejson
        dateformat = "%Y-%m-%d %H:%M:%S"
        ordered = True
