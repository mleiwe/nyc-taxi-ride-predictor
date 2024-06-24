# nyc-taxi-ride-predictor
MLOps course repository for all the NYC taxi code

## How to run
Install docker
```bash
docker pull mageai/mageai:latest
```

```bash
nyc-taxi-ride-predictor % docker run -it -p 6789:6789 -v $(pwd):/home/src mageai/mageai /app/run_app.sh mage start nyc-taxi-ride-predictor
```
