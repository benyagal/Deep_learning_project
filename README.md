# Deep Learning Project - Docker

## Építés
docker build -t deep-learning-project .

## Futtatás (GPU)
docker run --gpus all -it --rm -v $(pwd)/data:/data deep-learning-project

## Notebook
docker run --gpus all -it --rm -p 8888:8888 -v $(pwd)/data:/data -v $(pwd)/notebook:/app/notebook deep-learning-project jupyter notebook --ip=0.0.0.0 --allow-root --notebook-dir=/app/notebook
