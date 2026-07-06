# Simple Flask App

Aplikacja Dydaktyczna wyświetlająca imię i wiadomość w różnych formatach dla zajęć
o Continuous Integration, Continuous Delivery i Continuous Deployment.

- W projekcie wykorzystujemy virtual environment, aby stworzyć hermetyczne środowisko dla aplikacji:

tworzymy hermetyczne środowisko dla bibliotek aplikacji:

$ python -m venv .venv

aktywowanie hermetycznego środowiska

$ source .venv/Scripts/activate # Windows (Git Bash)

lub:

$ source .venv/bin/activate # Linux/Mac

$ pip install -r requirements.txt
$ pip install -r test_requirements.txt

sprawdzenie zainstalowanych pakietów

$ pip list


Sprawdź: https://docs.python.org/3/tutorial/venv/ oraz https://flask.palletsprojects.com/

---

## Uruchamianie aplikacji

jako zwykły program

$ python main.py

albo przez Flask:

$ PYTHONPATH=. FLASK_APP=hello_world flask run


---

## Uruchamianie testów


$ PYTHONPATH=. pytest -v
$ PYTHONPATH=. pytest -v -s


---

## Makefile (single point of entry)

Projekt wykorzystuje Makefile jako centralne miejsce uruchamiania komend:


$ make deps # instalacja zależności
$ make lint # sprawdzenie jakości kodu (flake8)
$ make test # uruchomienie testów
$ make run # uruchomienie aplikacji
$ make docker_build # budowa obrazu Docker
$ make docker_push # wysłanie obrazu do Docker Hub


---

## Docker

Budowanie obrazu:


$ make docker_build


Uruchomienie kontenera:


$ docker run -p 5000:5000 hello-world-printer


---

## CI/CD – CircleCI

Projekt wykorzystuje CircleCI do automatyzacji procesu:

- instalacja zależności (`make deps`)
- linting kodu (`make lint`)
- testy (`make test`)
- budowa obrazu Docker (`make docker_build`)
- publikacja obrazu do Docker Hub (`make docker_push`)

Pipeline uruchamia się automatycznie po każdym pushu do repozytorium.

---

## Kontynuacja pracy


$ deactivate


---

## Pomocnicze

### Ubuntu / Docker

- Instalacja Docker:
https://docs.docker.com/engine/install/

---

## CentOS / Docker


$ yum remove docker
docker-common
container-selinux
docker-selinux
docker-engine

$ yum install -y yum-utils

$ yum-config-manager
--add-repo
https://download.docker.com/linux/centos/docker-ce.repo

$ yum makecache fast
$ yum install -y docker-ce
$ systemctl start docker

---

## Integracja z CI/CD

Projekt nie używa już TravisCI — zastąpiony został przez CircleCI, który automatyzuje cały pipeline budowania, testowania i wdrażania aplikacji.