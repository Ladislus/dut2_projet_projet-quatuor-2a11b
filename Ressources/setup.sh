if [ ! -d ../Developpement/venv ]; then
  virtualenv -p python3 ../Developpement/venv
fi

source ../Developpement/venv/bin/activate
pip install -r requirement.txt

echo 'FLASK_APP =' > ../Developpement/.flaskenv
echo 'FLASK_ENV = development' >> ../Developpement/.flaskenv
