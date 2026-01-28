from pyspark.sql import SparkSession
from pyspark.sql.functions import concat_ws, avg, col
import pandas as pd
from reportlab.pdfgen import canvas
import os

spark = SparkSession.builder.appName("MyDataProject").getOrCreate()
sc = spark.sparkContext

data_csv = "data/web_data.csv" 
df = spark.read.csv(data_csv, header=True, inferSchema=True)


df = df.withColumn("Full Name", concat_ws(" ", col("First Name"), col("Last Name")))


print("Πρώτες γραμμές του DataFrame:")
df.show(5)


print("Μέσος μισθός ανά άτομο:")
df.groupBy("Full Name").agg(avg("Salary").alias("avg_salary")).show()


print("Μέσος μισθός για όλο το dataset:")
df.select(avg(col("Salary")).alias("overall_avg_salary")).show()


tracker = sc.statusTracker()
jobs = tracker.getJobIdsForGroup(None)

jobs_data = []
for jobId in jobs:
    job_info = tracker.getJobInfo(jobId)
    if job_info:
        jobs_data.append({
            "jobId": jobId,
            "status": job_info.status,             
            "numStages": len(job_info.stageIds)
        })


os.makedirs("data", exist_ok=True)


jobs_csv_path = "data/spark_jobs.csv"
pd.DataFrame(jobs_data).to_csv(jobs_csv_path, index=False)
print(f"Spark jobs αποθηκεύτηκαν σε CSV: {jobs_csv_path}")


pdf_path = "data/spark_jobs_report.pdf"
c = canvas.Canvas(pdf_path)
c.drawString(100, 750, "Spark Jobs Report")

for i, row in enumerate(jobs_data):
    c.drawString(100, 720 - i*20, f"Job {row['jobId']} - Status: {row['status']} - Stages: {row['numStages']}")

c.save()
print(f"PDF report δημιουργήθηκε: {pdf_path}")


spark.stop()
