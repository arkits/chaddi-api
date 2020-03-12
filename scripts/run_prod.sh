cd ..

source .env/bin/activate

pip install -r requirements.txt

cd src

echo "Running Chaddi-API"
gunicorn -b 0.0.0.0:8789 chaddi_api:app > ../chaddi_api.log 2>&1 & 