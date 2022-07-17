### Fastapi with minimum of DDD

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
- presentations
Presentation layer, everything connected with requests, responses are here
- service
Service layer, business-logic locates here
- tests
Unit, e2e, functional tests
- .env
Localfile for settings, do not commit it to git
- entrypoints.py
Entrypoints for executing service. Uvicorn and mangum are located here.
