from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col

# Δημιουργία Spark session
spark = SparkSession.builder \
    .appName("MyDataProject") \
    .getOrCreate()

# Φόρτωση καθαρισμένων δεδομένων
df = spark.read.csv("data/clean_data.csv", header=True, inferSchema=True)

print("Πρώτες γραμμές του DataFrame:")
df.show()

# Κάποιες aggregations
print("Μέσος μισθός ανά όνομα:")
df.groupBy("name").agg(avg("salary").alias("avg_salary")).show()

print("Μέσος μισθός για όλο το dataset:")
df.select(avg(col("salary")).alias("overall_avg_salary")).show()

# Κλείσιμο Spark session
spark.stop()
