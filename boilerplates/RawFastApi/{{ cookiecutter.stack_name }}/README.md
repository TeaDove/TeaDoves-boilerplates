### Minimum Fastapi

#### Install
```shell
cd deployment
./install.sh
./start.sh
```

#### Structure
- services
Source code of services
- deployment
Scripts for deployment and running
- extras
Request examples and other satellites

#### Service structure
- core
Settings, DDD containers, loggers etc
- api
main api folder
- tests
Unit, e2e, functional tests
- .env
Localfile for settings, do not commit it to git
- entrypoints.py
Entrypoints for executing service. Uvicor is located here.
