#!/bin/bash


#recordar BASH en lugar de SH
    echo "Cleaning"
    cd ~/MongoDB-GKE/Xshards\(noreplica\)-1router-config\(noreplica\)/scripts/
    ./teardown.sh;
    cd ~
    echo "Finished"
