FROM ubuntu
MAINTAINER bradley.soper@dell.com

ENV ANSIBLE_HOST_KEY_CHECKING=false

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN apt-add-repository -y --update ppa:ansible/ansible
RUN apt-get install -y ansible
RUN mkdir /code

WORKDIR /code

COPY ./ansible_playbook.py /code
COPY ./roles/all/tasks/main.yml /code/roles/all/tasks/main.yml
COPY ./hosts /code
COPY ./playbook.yml /code


ENTRYPOINT ["ansible-playbook", "playbook.yml", "-u", "root", "-i","hosts"]

