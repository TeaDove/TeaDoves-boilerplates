#!/usr/bin/env bash

CR_ID=crp16aikrt0oubeh8m1h

docker login \
  --username iam \
  --password "$(yc iam create-token)" \
  cr.yandex

docker build . -t "cr.yandex/${CR_ID}/main-database-image"
docker push "cr.yandex/${CR_ID}/main-database-image"
yc container image list
