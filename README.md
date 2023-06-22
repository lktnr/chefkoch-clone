# CHEFKOCH-ClONE

## Installation

**prerequesites:**

- pip(lorenz.kuchtner@MACCJJXMX2K19 chefkoch-clone % pip --version
  pip 23.1.2 from /opt/homebrew/lib/python3.10/site-packages/pip (python 3.10))
- docker(Docker version 20.10.21, build baeda1f)

1. install requirements (`pip install -r requirements.txt`)
2. install and start docker images(`docker compose up --detach`)
3. start application(`flask --app chefkoch-clone run --debug`)

## Startup

- to run:
  `flask --app chefkoch-clone run`
- to run with debugger (recommended):
  `flask --app chefkoch-clone run --debug`

## Requirements

- To freeze:
  `pip freeze > requirements.txt`
- To install:
  `pip install -r requirements.txt`
