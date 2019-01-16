if [ ! -d ../Developpement/ ]; then
  mkdir ../Developpement
fi

if [ ! -d ../venv/ ]; then
  virtualenv -p python3 ../venv
fi

source ../venv/bin/activate
pip install -r requirement.txt

echo 'FLASK_APP = Developpement' > ../.flaskenv
echo 'FLASK_ENV = development' >> ../.flaskenv
