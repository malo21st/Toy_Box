#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 19:25:40 2019

@author: malo21st
"""

import requests

from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import *
from janome.charfilter import *

import re

p = re.compile(r"<[^>]*?>")

MESSAGE_INIT = "ニックネームを入力して、[Enter]キーを押して下さい。"
MESSAGE_ERROR= "ニックネームが間違っています。もう一度、入力して下さい。"
#import pandas as pd
#import pickle

URL = "https://connpass.com/api/v1/event/?"
OPTION = "&count=100&order=2"

def event_search(query):
    query = 'nickname=' + query
    url = URL + query + OPTION
    data = requests.get(url).json()
    if data['results_available'] == 10000:
        return None

    events = data["events"]
    result = ""

    for event in events:
        for k, v in event.items():
            if k == "title":
                temp = v.replace('#',' ')
                temp = temp.replace('@',' ')
                e_title = temp
            try:
                if k == "series":
                    s_title = v['title']
            except:
                s_title = ""
        result = result + e_title + "、" + s_title + "、" 
    return result

def get_dict(user):
    if user == "":
        return {'word':[MESSAGE_INIT], 'freq':[5]}
    events = event_search(user)
    if not events:
        return {'word':[MESSAGE_ERROR], 'freq':[5]}

    # Janomeの準備 --- (*2)
    char_filters = [UnicodeNormalizeCharFilter()] #, RegexReplaceCharFilter(r"[IiⅠｉ?.*/~=()〝 <>:：《°!！!？（）-]+", "")]
    tokenizer = Tokenizer()
    token_filters = [POSKeepFilter(["名詞", "動詞", "副詞,一般"]), POSStopFilter(["名詞,非自立", "名詞,数", "名詞,代名詞", "名詞,接尾", "名詞,サ変接続"])] #,LowerCaseFilter()]
    analyzer = Analyzer(char_filters, tokenizer, token_filters)
    tokens = analyzer.analyze(events)

    # 形態素をカウント --- (*3)
    counter = {}
    for t in tokens:
        bf = t.base_form
        if not bf in counter: counter[bf] = 0
        counter[bf] += 1

    # カウントの多い順に並び替える --- (*4)
    sc = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    # # 並び替えたものを表示 --- (*5)
    # for i, t in enumerate(sc):
    #     if i >= 100: break
    #     key, cnt = t
    #     print((i + 1), ".", key, "=", cnt)
    word = []
    freq = []

    for w, f in sc:
        word.append(w)
        freq.append(f)
        
    return {'word':word, 'freq':freq}        

if __name__ == '__main__':
    main()
