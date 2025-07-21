Car value API

## Build

### With uv

Install [uv](https://github.com/astral-sh/uv)

```{bash}
uv sync --locked
uv run fastapi run main.py --port 8005 --host 0.0.0.0
```

### With docker

Install [docker](https://www.docker.com/)

```{bash}
docker build -t car_value .
docker run -it car_value
```

## Describe

POST at `/car-value/` with parameters:

```{json}
{
    "brand": string | null,
    "company": string | null,
    "km": integer | null,
    "model": string | null,
    "seats": integer | null,
    "transmission": string | null,
    "year": integer | null
}
```

See more at [http://0.0.0.0:8005/docs](http://0.0.0.0:8005/docs)
