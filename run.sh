FILE=/home/ubuntu/Project/projectGitPython_VIVET_SARROT/.myenv
if [ ! -e "$FILE" ]; then
	python3 -m venv .myenv
	echo "environnement crée"
else
	echo "environnement pré-existant"
fi
source .myenv/bin/activate
pip install -r requirements.txt
python main.py
