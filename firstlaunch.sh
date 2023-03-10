python3 -m venv venv || source ./venv/bin/activate
git clone https://github.com/Antonomaz/Corpus.git 2> /dev/null || cd Corpus && git pull && cd ..

./venv/bin/python -m pip install -U pip
./venv/bin/python -m pip install -r requirements.txt

# ./spacy_install.sh ./venv/bin/python