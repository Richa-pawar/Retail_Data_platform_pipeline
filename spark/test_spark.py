import os

# Windows Spark fixes
os.environ["SPARK_LOCAL_HOSTNAME"] = "localhost"
os.environ["PYSPARK_PYTHON"] = r"D:\cloud_nexus\retail-data-pipeline\.venv\Scripts\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"D:\cloud_nexus\retail-data-pipeline\.venv\Scripts\python.exe"


from pyspark.sql import SparkSession


spark = (
    SparkSession.builder
    .appName("RetailPipelineTest")
    .master("local[2]")
    .config("spark.driver.host", "127.0.0.1")
    .config("spark.driver.bindAddress", "127.0.0.1")
    .config("spark.python.worker.reuse", "false")
    .getOrCreate()
)


data = [
    (1, "Laptop", 50000),
    (2, "Mobile", 30000)
]


df = spark.createDataFrame(
    data,
    ["id", "product", "price"]
)


df.show()


spark.stop()