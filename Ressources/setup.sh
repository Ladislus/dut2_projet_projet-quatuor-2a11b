virtualenv -p python3 ../Developpement/venv
pip install -r requirement.txt

echo 'FLASK_APP =' > ../Developpement/.flaskenv
echo 'FLASK_ENV = development' >> ../Developpement/.flaskenv
