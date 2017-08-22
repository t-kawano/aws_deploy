# -*- coding: utf-8 -*-
import datetime
import json


"""
デプロイ用Lambda
"""

def get(event, context):
    try:
        event = extract_request_body(event)
        now = datetime.datetime.now()
        now_str = now.strftime('%Y/%m/%d')
        Log = BzspLogger()
        Log.info(event)
        # TODO validation check
        return {'nani': now_str, 'seda': json.dumps(event, ensure_ascii=True)}
    except Exception as e:
        print("error da bokeeeeeeeeeeeeeeeeeeee!")
