all: build-network build

check-vars:
ifndef DNS_SUFFIX
	$(error env var DNS_SUFFIX is not set)
endif

build-network:
docker network create --driver=overlay traefik-net

build:
faas-cli build -f ./ansible-playbook3.yml

refresh: destroy build

destroy:
docker image rm bsoper/ansible-playbook3
sleep 2

destroy-all: destroy
docker network rm traefik-net

