#!/bin/bash
# deploy_chaddi.sh

# Stop if there is an error
set -e

# Go to chaddi home
cd /opt/software/chaddi-api

git reset --hard origin

git pull

./kill_prod.sh

./run_prod.sh