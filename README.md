# My Data Project - υπό κατασκευή

Αυτό είναι το πρώτο μου μεγάλο data science project και είναι ακόμα υπό εξέλιξη.   
Εδώ δείχνω δουλεύω με Python, Pandas και PySpark για ETL, ανάλυση δεδομένων και προετοιμασία για ML.

---

## Τι έκανα μέχρι τώρα

1. Φτιάχτηκε ο φάκελος του project (`python_project/my-data-project`) και όλη η βασική δομή με φακέλους για data, scripts, notebooks και tests.  
2. Έκανα virtual environment (`venv`) για να κρατάω όλες τις βιβλιοθήκες ξεχωριστά.  
3. Κατέβασα και εγκατέστησα τις βασικές βιβλιοθήκες που χρειάζομαι:  
   - `numpy`, `pandas`, `matplotlib`, `scikit-learn`, `jupyter`, `pyspark`, `reportlab`  
4. Έφτιαξα το πρώτο μου ETL script (`src/etl/load_clean_data.py`) που:  
   - φορτώνει τα raw δεδομένα από CSV  
   - καθαρίζει κενά και περιττούς χαρακτήρες  
   - υπολογίζει μέσους όρους για τα κενά αριθμητικά πεδία  
   - σώζει τα καθαρά δεδομένα σε νέο CSV (`clean_data.csv`)  

---

## Τα πρώτα δεδομένα που χρησιμοποίησα

Έφτιαξα ένα μικρό CSV `data/raw_data.csv` με μερικές γραμμές για δοκιμή:

name,age,salary
Γιάννης,30,50000
Άννα,,
Μιχάλης,40,60000
Σοφία,25,



Με το ETL script, αυτό έγινε `clean_data.csv`, έτοιμο για ανάλυση.

---

## Τι έκανα μετά

1. Δημιούργησα ένα script ανάλυσης με Spark (`src/analysis/spark_analysis.py`).  
2. Το script φορτώνει τα καθαρά δεδομένα σε Spark DataFrame και κάνει μερικές βασικές αναλύσεις:  
   - εμφάνιση των πρώτων γραμμών  
   - μέσος μισθός ανά όνομα  
   - συνολικός μέσος μισθός  
3. Δημιούργησα ένα πιο ολοκληρωμένο script (`src/analysis/spark_analysis_report.py`) που:  
   - τρέχει την ανάλυση με Spark  
   - συλλέγει τα Spark jobs (Job ID, Status, αριθμό Stages)  
   - σώζει τα jobs σε CSV (`data/spark_jobs.csv`)  
   - δημιουργεί PDF report (`data/spark_jobs_report.pdf`) με τις ίδιες πληροφορίες  

---

## Πώς τρέχω το project

1. Ενεργοποιώ το virtual environment (`venv`):

```bash
source venv/bin/activate  # Linux / WSL



Τρέχω πρώτα το ETL script για να καθαρίσω τα δεδομένα:

python src/etl/load_clean_data.py


Μετά τρέχω το Spark analysis script για βασική ανάλυση:

python src/analysis/spark_analysis.py


Τέλος τρέχω το Spark analysis report script για CSV + PDF:

python src/analysis/spark_analysis_report.py


Σημείωση: Για να δουλέψει το Spark χρειάζεται εγκατεστημένο JDK και σωστά ορισμένο JAVA_HOME!!!!!!!!!!



Όλα τα παραγόμενα αρχεία (clean_data.csv, spark_jobs.csv, spark_jobs_report.pdf) σώζονται μέσα στο φάκελο data/.