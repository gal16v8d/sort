# sort

# Get started

Install python3-venv:
sudo apt install python3-venv
Install python3 tkinter for UI:
sudo apt install python3-tk
Install pipenv:
pip3 install pipenv
Then create the folder for allocate the virtual environment:
mkdir .venv
Launch pipenv:
pipenv install --skip-lock
Then activate the virtual env:
pipenv shell
Run command inside virtualenv:
pipenv run
Exit virtual env:
exit o deactivate

# set up

Configure all your dependencies in Pipfile.
See: https://pypi.org/

# launch

python3 sort/app.py
