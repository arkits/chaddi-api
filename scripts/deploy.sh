#!/bin/bash
# deploy_chaddi.sh

# Stop if there is an error
set -e

pwd

ls -l

# Go to chaddi home
cd /opt/software/chaddi-api/scripts/

git reset --hard origin

git pull

./kill_prod.sh

./run_prod.sh