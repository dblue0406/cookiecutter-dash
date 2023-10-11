.PHONY: help, ci-black, ci-flake8, ci-test, isort, black, docs, dev-start, dev-stop

## Ensure this is the same name as in docker-compose.yml file
CONTAINER_NAME="{{cookiecutter.repo_name}}_${USER}"

PROJECT={{cookiecutter.repo_name}}

PROJ_DIR="/mnt/{{cookiecutter.repo_name}}"
VERSION_FILE:=VERSION
COMPOSE_FILE=docker/docker-compose.yml
TAG:=$(shell cat ${VERSION_FILE})
ENV=dev

start-env: .env ## Primary make command for devs, spins up containers
	docker-compose -f $(COMPOSE_FILE) --project-name $(PROJECT) up $(ENV) -d --no-recreate

stop-env: ## Spin down active containers
	docker-compose -f $(COMPOSE_FILE) --project-name $(PROJECT) down $(ENV)

# Useful when Dockerfile/requirements are updated)
rebuild-env: .env ## Rebuild images for dev containers
	docker-compose -f $(COMPOSE_FILE) --project-name $(PROJECT) up $(ENV) -d --build

log-env:
	docker logs $(CONTAINER_NAME)_$(ENV)

###
stop-all: ## Spin down active containers
	docker-compose -f $(COMPOSE_FILE) --project-name $(PROJECT) down

rebuild-all: .env ## Rebuild images for dev containers
	docker-compose -f $(COMPOSE_FILE) --project-name $(PROJECT) up -d --build