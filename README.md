# Deep Learning Project - Docker

## Építés
docker build -t my-dl-project-work-app:1.0 .

## Futtatás (CPU)
docker run -d --name my-ml-container --gpus all -v D:\Egyetem\Melytanulas\data:/data -v D:\Egyetem\Melytanulas\output:/app/output my-dl-project-work-app:1.0

## Kód futtatás
docker exec my-ml-container bash run.sh

## Leállítás és törlés
docker stop my-ml-container

docker rm my-ml-container
