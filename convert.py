import polars as pl

df = pl.read_parquet("./data/cars.parquet")
df.write_excel("cars.xlsx")
