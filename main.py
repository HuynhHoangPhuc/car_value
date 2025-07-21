import math
from fastapi import FastAPI
from pydantic import BaseModel
import polars as pl


class CarValueRequest(BaseModel):
    brand: str | None = None
    company: str | None = None
    km: int | None = None
    model: str | None = None
    seats: int | None = None
    transmission: str | None = None
    year: int | None = None


app = FastAPI()

# Load the preprocessed car data
cars = pl.read_parquet("./data/cars.parquet")


@app.post("/car-value/")
def get_car_value(request: CarValueRequest):
    # Filter the DataFrame based on the request parameters
    # Use True for optional parameters that are None to include all values
    filtered_cars = cars.filter(
        (
            pl.col("brand") == request.brand.lower()
            if request.brand is not None
            else True
        )
        & (
            pl.col("company") == request.company.lower()
            if request.company is not None
            else True
        )
        & (pl.col("km") == request.km if request.km is not None else True)
        & (
            pl.col("model") == request.model.lower()
            if request.model is not None
            else True
        )
        & (pl.col("seats") == request.seats if request.seats is not None else True)
        & (
            pl.col("transmission") == request.transmission.lower()
            if request.transmission is not None
            else True
        )
        & (pl.col("year") == request.year if request.year is not None else True)
    )

    # Get the car value from the filtered DataFrame
    car_value = filtered_cars.select("price").to_series().mean()

    return int(math.ceil(car_value))
