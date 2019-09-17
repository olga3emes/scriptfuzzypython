#!/bin/bash
#  First.sh
#
#
#  Created by Olga M. Moreno Martín on 08/07/2019.
SEED=30

for ((i=1; i<=$SEED; i++ ))
do
#recordar BASH en lugar de SH
    echo "1-Kubernetes environment"
    cd ~/MongoDB-GKE/Xshards\(noreplica\)-1router-config\(noreplica\)/scripts/
    ./generate.sh
    cd ~
kubectl exec -it mongos-router-0 -c mongos-container -- mongo mydatabase --eval 'db.getSiblingDB("admin").auth("main_admin", "abc123"); db.system.js.save({_id: "feq",  value: function feq (arrayA, arrayB) {   alfaA = arrayA  [0];betaA = arrayA  [1];gammaA = arrayA  [2];deltaA = arrayA  [3];    alfaB = arrayB  [0];betaB = arrayB  [1];gammaB = arrayB  [2];deltaB = arrayB  [3];if (gammaA >= betaB && betaA <= gammaB) {return 1;}if (deltaA <= alfaB || alfaA >= deltaB) {return 0;}if (deltaA > alfaB && gammaA < betaB) {  return ((deltaA - alfaB) / ((betaB - alfaB) - (gammaA - deltaA)));} else { return ((deltaB - alfaA) / ((betaA - alfaA) - (gammaB - deltaB)));}}});db.loadServerScripts();'
    #todos los operadores flexibles deben ir definidos de esta forma.
    nohup kubectl port-forward mongos-router-0  --namespace default 27017:27017 &
    echo "2 - Python Script"
    cd ~/scriptfuzzypython
    python outdatabase.py ${i} ${i+10};
    cd ~
    #recoger atributos necesarios
    echo "3 - Cleaning"
    cd ~/MongoDB-GKE/Xshards\(noreplica\)-1router-config\(noreplica\)/scripts/
    ./teardown.sh;
    cd ~
    echo "Finished" ${i}
done

