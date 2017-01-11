#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from datetime import datetime
import os
import sys
import json
import facebook
import requests

FACEBOOK_PAGE_TOKEN = os.environ.get('FACEBOOK_PAGE_TOKEN')
API_TOKEN = os.environ.get('API_TOKEN')               #lambdaの環境変数からkintoneアプリのAPIトークンをとってくる（
KINTONE_ENDPOINT = os.environ.get('KINTONE_ENDPOINT') #lambdaの環境変数からkintoneのエンドポイントをとってくる
LINE = u'''{やりたいこと}  [{ポイント}ポイント]
'''

class Timeline:
    def __init__(self):
        self.page_endpoint = facebook.GraphAPI(FACEBOOK_PAGE_TOKEN)

    def post_page(self, message):
        self.page_endpoint.put_wall_post(message=message)

def lambda_handler(event, context):
    resp = requests.get(KINTONE_ENDPOINT, headers={'X-Cybozu-API-Token': API_TOKEN});
    records = json.loads(resp.text)['records']

    lines = []
    for record in records:
        data = dict( (k, v['value']) for k, v in record.items())
        lines.append(LINE.format(**data))

    try:
        timeline = Timeline()
        timeline.post_page('\n'.join(lines))
    except (IOError, facebook.GraphAPIError) as e:
        print e
        exit(9)
