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


for i in xrange(58):
    doc = randDoc(i)
    print(json.dumps(doc))
    if i % 1000 == 0:
        print(".", end="", file=sys.stderr)


#Para pasar a json y poblar la bd

#python mb100.py > mb100.json
"siteRootAdmin", "password"
#mongoimport --db admin --collection gb10 --username siteRootAdmin --password password -v --drop  --file
#mongoimport --db nodo0 --collection mb100 -v   --file mb100.json --port 27018
#db.mycoll.stats()