# CHEFKOCH-CLONE

## Installation

**prerequesites:**

- git(git version 2.34.1)
- pip(pip 23.1.2, python 3.10)
- docker(Docker version 24.0.2, build cb74dfc)
- docker-compose

**steps to install:**

1. clone repo (`git clone https://github.com/lktnr/chefkoch-clone.git`)
2. install requirements (`pip install -r requirements.txt`)
3. install and start docker images(`docker compose up --detach`)
4. start application(`flask --app chefkoch-clone run --debug`)

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
