# coding=utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    pid = models.IntegerField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=128, blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    edit_mode = models.CharField(max_length=32, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    link_to = models.CharField(max_length=512, blank=True, null=True)
    thumbnail = models.CharField(max_length=512, blank=True, null=True)
    style = models.CharField(max_length=32, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    order_number = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=32, blank=True, null=True)
    comment_status = models.IntegerField(blank=True, null=True)
    comment_count = models.IntegerField(blank=True, null=True)
    comment_time = models.DateTimeField(blank=True, null=True)
    view_count = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    flag = models.CharField(max_length=256, blank=True, null=True)
    meta_keywords = models.CharField(max_length=512, blank=True, null=True)
    meta_description = models.CharField(max_length=512, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'


class ArticleCategory(models.Model):
    pid = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    slug = models.CharField(max_length=128, blank=True, null=True)
    title = models.CharField(max_length=512, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    style = models.CharField(max_length=32, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    icon = models.CharField(max_length=128, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    order_number = models.IntegerField(blank=True, null=True)
    flag = models.CharField(max_length=256, blank=True, null=True)
    meta_keywords = models.CharField(max_length=256, blank=True, null=True)
    meta_description = models.CharField(max_length=256, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_category'


class ArticleCategoryMapping(models.Model):
    article_id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'article_category_mapping'
        unique_together = (('article_id', 'category_id'),)


class ArticleComment(models.Model):
    pid = models.IntegerField(blank=True, null=True)
    article_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=128, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    wechat = models.CharField(max_length=64, blank=True, null=True)
    qq = models.CharField(max_length=32, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    reply_count = models.IntegerField(blank=True, null=True)
    order_number = models.IntegerField(blank=True, null=True)
    vote_up = models.IntegerField(blank=True, null=True)
    vote_down = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=32, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_comment'


class Attachment(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    path = models.CharField(max_length=512, blank=True, null=True)
    mime_type = models.CharField(max_length=128, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    flag = models.CharField(max_length=256, blank=True, null=True)
    order_number = models.IntegerField(blank=True, null=True)
    accessible = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attachment'


class Menu(models.Model):
    pid = models.IntegerField(blank=True, null=True)
    text = models.CharField(max_length=128, blank=True, null=True)
    url = models.CharField(max_length=512, blank=True, null=True)
    target = models.CharField(max_length=32, blank=True, null=True)
    icon = models.CharField(max_length=64, blank=True, null=True)
    flag = models.CharField(max_length=32, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    order_number = models.IntegerField(blank=True, null=True)
    relative_table = models.CharField(max_length=32, blank=True, null=True)
    relative_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class Option(models.Model):
    key = models.CharField(unique=True, max_length=128, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'option'


class PaymentRecord(models.Model):
    id = models.IntegerField(primary_key=True)
    product_id = models.IntegerField(blank=True, null=True)
    product_name = models.TextField(blank=True, null=True)
    trx_no = models.CharField(unique=True, max_length=50)
    trx_type = models.CharField(max_length=30, blank=True, null=True)
    trx_nonce_str = models.CharField(max_length=64, blank=True, null=True)
    payer_user_id = models.CharField(max_length=50, blank=True, null=True)
    payer_name = models.CharField(max_length=256, blank=True, null=True)
    payer_fee = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    order_ip = models.CharField(max_length=30, blank=True, null=True)
    order_referer_url = models.CharField(max_length=1024, blank=True, null=True)
    order_from = models.CharField(max_length=30, blank=True, null=True)
    pay_status = models.IntegerField(blank=True, null=True)
    pay_type = models.CharField(max_length=50, blank=True, null=True)
    pay_bank_type = models.CharField(max_length=128, blank=True, null=True)
    pay_amount = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    pay_success_amount = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    pay_success_time = models.DateTimeField(blank=True, null=True)
    pay_complete_time = models.DateTimeField(blank=True, null=True)
    refund_no = models.CharField(max_length=64, blank=True, null=True)
    refund_desc = models.CharField(max_length=256, blank=True, null=True)
    refund_time = models.DateTimeField(blank=True, null=True)
    thirdparty_appid = models.CharField(max_length=32, blank=True, null=True)
    thirdparty_mch_id = models.CharField(max_length=32, blank=True, null=True)
    thirdparty_trade_type = models.CharField(max_length=16, blank=True, null=True)
    thirdparty_transaction_id = models.CharField(max_length=32, blank=True, null=True)
    thirdparty_user_openid = models.CharField(max_length=64, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=32, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    field1 = models.CharField(max_length=1024, blank=True, null=True)
    field2 = models.CharField(max_length=1024, blank=True, null=True)
    field3 = models.CharField(max_length=1024, blank=True, null=True)
    field4 = models.CharField(max_length=1024, blank=True, null=True)
    field5 = models.CharField(max_length=1024, blank=True, null=True)
    field6 = models.CharField(max_length=1024, blank=True, null=True)
    field7 = models.CharField(max_length=1024, blank=True, null=True)
    field8 = models.CharField(max_length=1024, blank=True, null=True)
    field9 = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_record'


class Permission(models.Model):
    action_key = models.CharField(max_length=512)
    node = models.CharField(max_length=512)
    type = models.CharField(max_length=32)
    text = models.CharField(max_length=1024, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permission'


class Role(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    flag = models.CharField(max_length=64, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role'


class RolePermissionMapping(models.Model):
    role_id = models.IntegerField(primary_key=True)
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'role_permission_mapping'
        unique_together = (('role_id', 'permission_id'),)


class SinglePage(models.Model):
    slug = models.CharField(unique=True, max_length=128, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    edit_mode = models.CharField(max_length=32, blank=True, null=True)
    link_to = models.CharField(max_length=512, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    thumbnail = models.CharField(max_length=128, blank=True, null=True)
    style = models.CharField(max_length=32, blank=True, null=True)
    flag = models.CharField(max_length=32, blank=True, null=True)
    status = models.CharField(max_length=32)
    view_count = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=256, blank=True, null=True)
    meta_description = models.CharField(max_length=256, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'single_page'


class User(models.Model):
    username = models.CharField(unique=True, max_length=128, blank=True, null=True)
    nickname = models.CharField(max_length=128, blank=True, null=True)
    realname = models.CharField(max_length=128, blank=True, null=True)
    identity = models.CharField(max_length=128, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    salt = models.CharField(max_length=32, blank=True, null=True)
    anonym = models.CharField(max_length=32, blank=True, null=True)
    wx_openid = models.CharField(unique=True, max_length=64, blank=True, null=True)
    wx_unionid = models.CharField(unique=True, max_length=64, blank=True, null=True)
    qq_openid = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(unique=True, max_length=64, blank=True, null=True)
    email_status = models.CharField(max_length=32, blank=True, null=True)
    mobile = models.CharField(unique=True, max_length=32, blank=True, null=True)
    mobile_status = models.CharField(max_length=32, blank=True, null=True)
    gender = models.CharField(max_length=16, blank=True, null=True)
    signature = models.CharField(max_length=2048, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    company = models.CharField(max_length=256, blank=True, null=True)
    occupation = models.CharField(max_length=256, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    zipcode = models.CharField(max_length=128, blank=True, null=True)
    site = models.CharField(max_length=256, blank=True, null=True)
    graduateschool = models.CharField(max_length=256, blank=True, null=True)
    education = models.CharField(max_length=256, blank=True, null=True)
    avatar = models.CharField(max_length=256, blank=True, null=True)
    idcardtype = models.CharField(max_length=128, blank=True, null=True)
    idcard = models.CharField(max_length=128, blank=True, null=True)
    remark = models.CharField(max_length=512, blank=True, null=True)
    status = models.CharField(max_length=32, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    create_source = models.CharField(max_length=128, blank=True, null=True)
    logged = models.DateTimeField(blank=True, null=True)
    activated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserRoleMapping(models.Model):
    user_id = models.IntegerField(primary_key=True)
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_role_mapping'
        unique_together = (('user_id', 'role_id'),)


class Utm(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    user_id = models.IntegerField(blank=True, null=True)
    anonym = models.CharField(max_length=32, blank=True, null=True)
    action_key = models.CharField(max_length=512, blank=True, null=True)
    action_query = models.CharField(max_length=512, blank=True, null=True)
    action_name = models.CharField(max_length=128, blank=True, null=True)
    source = models.CharField(max_length=32, blank=True, null=True)
    medium = models.CharField(max_length=32, blank=True, null=True)
    campaign = models.CharField(max_length=128, blank=True, null=True)
    content = models.CharField(max_length=128, blank=True, null=True)
    term = models.CharField(max_length=256, blank=True, null=True)
    ip = models.CharField(max_length=64, blank=True, null=True)
    agent = models.CharField(max_length=1024, blank=True, null=True)
    referer = models.CharField(max_length=1024, blank=True, null=True)
    se = models.CharField(max_length=32, blank=True, null=True)
    sek = models.CharField(max_length=512, blank=True, null=True)
    device_id = models.CharField(max_length=128, blank=True, null=True)
    platform = models.CharField(max_length=128, blank=True, null=True)
    system = models.CharField(max_length=128, blank=True, null=True)
    brand = models.CharField(max_length=128, blank=True, null=True)
    model = models.CharField(max_length=128, blank=True, null=True)
    network = models.CharField(max_length=128, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm'


class WechatMenu(models.Model):
    pid = models.IntegerField(blank=True, null=True)
    text = models.CharField(max_length=512, blank=True, null=True)
    keyword = models.CharField(max_length=128, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    order_number = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wechat_menu'


class WechatReply(models.Model):
    keyword = models.CharField(max_length=128, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wechat_reply'
