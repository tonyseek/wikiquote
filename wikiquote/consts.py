#!/usr/bin/env python
#-*- coding:utf-8 -*-

LANG_URL = "https://meta.wikimedia.org/wiki/Wikiquote#List_of_Wikiquotes"
LANG_XPATH = "//*[@id='mw-content-text']/div[2]/table[1]/tr/td[4]/a"
LANG_LABEL_XPATH = "//*[@id='mw-content-text']/div[2]/table[1]/tr/td[3]/a"

DAILY_CN_XPATH = "//*[@id='mf-qotd']/table/tr/descendant::*/text()"
DAILY_EN_XPATH = "//*[@id='mf-qotd']/div/div[2]/table/tr[1]/td/descendant::*/text()"
