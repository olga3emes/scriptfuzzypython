from __future__ import print_function
import sys
import random
import json


def randDoc(id):
    x=[]
    y=[]
    post = {"_id":id, "x": x, "y":y}

    x.append(random.uniform(0.0,2.0))
    x.append(random.uniform(2.0,6.0))
    x.append(random.uniform(6.0,8.0))
    x.append(random.uniform(8.0,10.0))

    y.append(random.uniform(0.0,1.5))
    y.append(random.uniform(1.5,3.0))
    y.append(random.uniform(3.0,7.0))
    y.append(random.uniform(7.0,15.0))

    post["x"]
    post["y"]
    return post


for i in xrange(500000000):
    doc = randDoc(i)
    print(json.dumps(doc))
    if i % 1000 == 0:
        print(".", end="", file=sys.stderr)


#Para pasar a json y poblar la bd

#python m50.py > m50.json
"siteRootAdmin", "password"
#mongoimport --db admin --collection datas100 --username siteRootAdmin --password password -v --drop  --file m100.json
#mongoimport --db system --collection js -v   --file fuzzy.json
#db.mycoll.stats()