# coding=utf-8

import os
import json
from mvg_api import *

"""res = get_stations("")
with open('testfile.json','w') as file:
	file = json.dump(res, file)
"""

ids =  "1110 , 6 , 1 , 300 , 5 , 150 , 140 , 580 , 500 , 340 , 190 , 400 , 50 , 1170 , 260 , 200 , 320 , 1130 , 1150 , 2 , 1010 , 920 , 1230 , 590 , 170 , 1190 , 1460 , 760 , 670 , 1430 , 560 , 1180 , 510 , 780 , 1480 , 750 , 1500 , 490 , 460 , 480 , 312 , 80 , 40 , 1530 , 1520 , 770 , 790 , 1510 , 1140 , 1220 , 130 , 1070 , 430 , 1540 , 160 , 110 , 280 , 1470 , 1210 , 1260 , 1250 , 1050 , 740 , 1030 , 520 , 1450 , 380 , 60 , 360 , 350 , 1330 , 30 , 570 , 1040 , 680 , 250 , 1200 , 540 , 1440 , 70 , 1340 , 530 , 1490 , 410 , 420 , 270 , 470 , 990 , 1060 , 180 , 370 , 1240 , 1020 , 120 , 240 , 1160"
ids = ids.replace(" ", "").split(',')


res = get_departures(1)
refinedRes = []
for x in res:
	#print x
	if x['product'] == 'u':
		refinedRes.append(x)

refJson = json.dumps(refinedRes)

with open('departures.json','w') as file:
	file = json.dump(refinedRes, file)
