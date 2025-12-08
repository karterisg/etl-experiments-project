from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col
import pandas as pd
from reportlab.pdfgen import canvas
import os

# Δημιουργία Spark session
spark = SparkSession.builder.appName("MyDataProject").getOrCreate()
sc = spark.sparkContext

# Φόρτωση καθαρισμένων δεδομένων
data_csv = "data/clean_data.csv"
df = spark.read.csv(data_csv, header=True, inferSchema=True)

# Τρέχον analysis
print("Πρώτες γραμμές του DataFrame:")
df.show()

print("Μέσος μισθός ανά όνομα:")
df.groupBy("name").agg(avg("salary").alias("avg_salary")).show()

print("Μέσος μισθός για όλο το dataset:")
df.select(avg(col("salary")).alias("overall_avg_salary")).show()

# Λήψη πληροφοριών για Spark jobs
tracker = sc.statusTracker()
jobs = tracker.getJobIdsForGroup(None)

jobs_data = []
for jobId in jobs:
    job_info = tracker.getJobInfo(jobId)
    if job_info:
        jobs_data.append({
            "jobId": jobId,
            "status": job_info.status,             # τρέχον status
            "numStages": len(job_info.stageIds)    # πόσα stages έχει το job
        })

# Δημιουργία φακέλου data αν δεν υπάρχει
os.makedirs("data", exist_ok=True)

# Αποθήκευση jobs σε CSV
jobs_csv_path = "data/spark_jobs.csv"
pd.DataFrame(jobs_data).to_csv(jobs_csv_path, index=False)
print(f"Spark jobs αποθηκεύτηκαν σε CSV: {jobs_csv_path}")

# Δημιουργία PDF report
pdf_path = "data/spark_jobs_report.pdf"
c = canvas.Canvas(pdf_path)
c.drawString(100, 750, "Spark Jobs Report")

for i, row in enumerate(jobs_data):
    c.drawString(100, 720 - i*20, f"Job {row['jobId']} - Status: {row['status']} - Stages: {row['numStages']}")

c.save()
print(f"PDF report δημιουργήθηκε: {pdf_path}")

# Κλείσιμο Spark session
spark.stop()
