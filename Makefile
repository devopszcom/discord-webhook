# CONTAINER_REGISTRY_URL=ro.lan:5000
CONTAINER_REGISTRY_URL=devopszcom

DOCKER_IMAGE=discord-webhook
VERSION=0.1

all: build

build:
	docker build --tag=${CONTAINER_REGISTRY_URL}/${DOCKER_IMAGE}:${VERSION} .

push:
	docker push ${CONTAINER_REGISTRY_URL}/${DOCKER_IMAGE}:${VERSION}
