# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from collections import defaultdict

from core.common import CommonView
from data_app.models import Article, ArticleCategory, ArticleCategoryMapping
from data_app.schemas import ArticleCategorySchema, LineItemSchema


class ArticleCategoryView(CommonView):

    def get(self, request):

        article_categories = ArticleCategory.objects.all()

        return self.schema_response(ArticleCategorySchema, article_categories)


class ArticleView(CommonView):

    def get(self, request):
        body = self.load_body_data()
        title = body.get('title')
        type= body.get('type')
        if not all([type, title]):
            return self.error_response(err_msg="缺少参数: title/type")
        paginator = self.paginator()
        # django底层会优化sql
        category = ArticleCategory.objects.filter(title=title, type=type).first()
        if not category:
            return self.error_response(err_msg="错误的请求!!!")
        article_ids = ArticleCategoryMapping.objects.filter(category_id=category.id).values_list('article_id')
        # 找到该文章id对应的所有分类和tag
        start = (paginator.page_num - 1) * paginator.page_size
        articles = Article.objects.filter(id__in=article_ids).order_by('-created')
        # 找出这些articles的所有分类和标签
        maps = ArticleCategoryMapping.objects.filter(article_id__in=articles.values_list('id'))
        article_id_2_category_ids = defaultdict(list)
        for map in maps:
            article_id_2_category_ids[map.article_id].append(map.category_id)
        categories = ArticleCategory.objects.filter(id__in=maps.values_list('category_id'))

        for article in articles:
            article.categories = []
            article.tags = []
            category_ids = article_id_2_category_ids.get(article.id, [])
            if category_ids:
                for category in categories:
                    if category.id in category_ids:
                        if category.type == 'category':
                            article.categories.append(category)
                        elif category.type == 'tag':
                            article.tags.append(category)

        return self.pagination_response(rows=articles[start: start + paginator.page_size], count=len(articles), page_num=paginator.page_num, page_size=paginator.page_size, schema=LineItemSchema)


