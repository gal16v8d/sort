# sort

Base desktop UI applying sort algorithms.

# Get started

Install poetry:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Init repo:

```bash
poetry new sort
```

Create the virtual env folder:

```bash
mkdir .venv
```

Install all the dependencies in the project (clean-state):

```bash
poetry install
```

Install any dependency you need:

```bash
poetry add lib_here
```

Remove a dependency you don't need:

```bash
poetry remove lib_here
```

# Set up

# env

Activate using the command:

```bash
source .venv/bin/activate
```

Exit virtual env:

```bash
exit
```

or

```bash
deactivate
```

# Advanced use cases

If multiple python versions are found in the operative system, then

- use pyenv to handle the versions
- if needed set the local python for this project, like

```bash
pyenv local 3.12.1
```

- you can confirm all good by checking

```bash
pyenv which python
```

- set the specific python version like

```bash
poetry env use $USER_HOME/.pyenv/versions/3.12.1/bin/python
```

- then install using commands like the ones in the previous section

# launch

```bash
python3 sort/app.py
```
