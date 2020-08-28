# -*- coding: utf-8 -*-
import ambient
import bme280_sample
import weathernewsdata
import webpressdata

chID = 25204
wkey = '7b84d86c582bef4d'

am = ambient.Ambient(chID, wkey)

# センサー計測データ読み込み
sensdata = bme280_sample.readData() 
bme_t = sensdata[0]
bme_p = sensdata[1]
bme_h = sensdata[2]

#気象ウェブページからスクレイピング
webdata = weathernewsdata.readData() 
web_t = webdata[0]
web_h = webdata[1]

# 気象ウェブページからスクレイピング
web_p = webpressdata.readData()

r = am.send({
           'd1': bme_t,
           'd2': bme_p,
           'd3': bme_h,
           'd4': web_t,
           'd5': web_p,
           'd6': web_h
           })
print(r.status_code)
r.close()
