# coding=utf-8
import re

from django.template.defaultfilters import striptags

from marshmallow import fields, post_dump

from core.common import BaseSchema


class ArticleCategorySchema(BaseSchema):
    pid = fields.Integer()
    user_id = fields.Integer()
    slug = fields.String()
    title = fields.String()
    content = fields.String()
    summary = fields.String()
    style = fields.String()
    type = fields.String()
    icon = fields.String()
    count = fields.Integer()
    order_number = fields.Integer()
    flag = fields.String()
    meta_keywords = fields.String()
    meta_description = fields.String()
    created = fields.DateTime()
    modified = fields.DateTime()


class LineItemSchema(BaseSchema):

    title = fields.String()         # 文章标题
    thumbnail = fields.String()     # 封面图
    content = fields.String()       # 内容
    modified = fields.DateTime()    # 更新时间
    summary = fields.String()       # 文字摘要
    tags = fields.Nested(ArticleCategorySchema, many=True)   # 文章标签
    categories = fields.Nested(ArticleCategorySchema, many=True)          # 文章分类

    @post_dump
    def make_obj(self, data):
        data['content'] = re.sub(r'&(.*?);', '', striptags(data['content']).replace('\n', '')[:200])
        data['thumbnail'] = "https://news-img.bolome.com" + data['thumbnail']
        return data


