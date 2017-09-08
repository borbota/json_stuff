#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

with open("data.json", "r") as jsonfile:
	data = json.load(jsonfile)

	nodes = data["nodes"]
	for i in range(len(nodes)):
		attributes = nodes[i]["attributes"] # attributes are not always there, want to update when it is
		color = nodes[i]["color"]
		if len(attributes) != 0:
			print attributes
			nodes[i]["color"] = "rgb(0,0,0)"
			print color
		else:
			pass
with open("data.json", "w") as jsonfile:
	json.dump(data, jsonfile)
  
 """
 #example 
 u'nodes': [{u'attributes': {u'blabla': u'blablabla'},
   u'color': u'rgb(1,2,3)',
   u'id': u'4845',
   u'label': u'name1',
   u'size': 4.365002155303955,
   u'x': 914.4984741210938,
   u'y': 15.235029220581055},
   {u'attributes': {},
   u'color': u'rgb(161,108,18)',
   u'id': u'4540',
   u'label': u'name2',
   u'size': 4.365002155303955,
   u'x': -985.0382080078125,
   u'y': -310.0407409667969},
"""
