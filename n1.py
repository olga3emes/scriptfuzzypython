from __future__ import print_function
import sys
import random
import json


def randDoc(id):
    x = []
    y = []
    texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eleifend lacus ut" \
            " ipsum euismod tincidunt. Pellentesque aliquam ultrices nunc in euismod. Ut tristique nibh" \
            " mauris. In a feugiat purus. In ut nunc at lorem iaculis posuere vitae vitae augue. Curabitur" \
            " vel augue mollis, egestas velit at, mollis purus. Mauris non laoreet justo, vitae ornare libero." \
            " Nulla at mi diam.Vivamus a lectus vel est convallis dapibus a vitae lorem. Nulla facilisi." \
            " Nulla leo nulla, porttitor nec elementum et, dapibus condimentum magna. Maecenas molestie sem " \
            "vel feugiat volutpat. Proin eget risus eu arcu viverra placerat eget et urna. Nunc commodo diam " \
            "at arcu pulvinar, vel elementum nunc efficitur. Integer dui mauris, dignissim et bibendum sit amet, " \
            "tristique sodales ipsum. Nulla porta ultrices diam eu venenatis. Suspendisse gravida ex et malesuada " \
            "ullamcorper. Nunc aliquam ipsum sit amet lacus tempus fringilla. Ut convallis facilisis diam. Nulla " \
            "tortor turpis, consectetur a dolor vel, suscipit pharetra est. Nunc cras amet."
    post = {"_id": id, "x": x, "y": y, "texto": texto}

    x.append(random.uniform(0.0, 2.0))
    x.append(random.uniform(2.0, 6.0))
    x.append(random.uniform(6.0, 8.0))
    x.append(random.uniform(8.0, 10.0))

    y.append(random.uniform(0.0, 1.5))
    y.append(random.uniform(1.5, 3.0))
    y.append(random.uniform(3.0, 7.0))
    y.append(random.uniform(7.0, 15.0))

    post["x"]
    post["y"]
    post["texto"]
    return post


for i in xrange(500000000):
    doc = randDoc(i)
    print(json.dumps(doc))
    if i % 1000 == 0:
        print(".", end="", file=sys.stderr)

# Para pasar a json y poblar la bd

# python m50.py > m50.json
"siteRootAdmin", "password"
# mongoimport --db admin --collection datas100 --username siteRootAdmin --password password -v --drop  --file m100.json
# mongoimport --db system --collection js -v   --file fuzzy.json
# db.mycoll.stats()
