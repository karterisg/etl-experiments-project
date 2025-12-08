# My Data Project - υπό κατασκευή

Αυτό είναι το πρώτο μου μεγάλο **data science project** και είναι ακόμα υπό εξέλιξη.  
Εδώ δείχνω πώς δουλεύω με **Python, Pandas και PySpark** για ETL, ανάλυση δεδομένων και προετοιμασία για ML.

---

## Τι έκανα μέχρι τώρα

1. Δημιουργήθηκε ο φάκελος του project (`python_project/my-data-project`) και η βασική δομή με φακέλους για **data**, **scripts**, **notebooks** και **tests**.  
2. Έφτιαξα **virtual environment (`venv`)** για να κρατάω ξεχωριστά τις βιβλιοθήκες.  
3. Εγκατέστησα τις βασικές βιβλιοθήκες:

   - `numpy`, `pandas`, `matplotlib`, `scikit-learn`, `jupyter`, `pyspark`, `reportlab`  

4. Έφτιαξα το πρώτο μου **ETL script** (`src/etl/load_clean_data.py`) που:

   - φορτώνει τα raw δεδομένα από CSV  
   - καθαρίζει κενά και περιττούς χαρακτήρες  
   - υπολογίζει μέσους όρους για τα κενά αριθμητικά πεδία  
   - σώζει τα καθαρά δεδομένα σε νέο CSV (`clean_data.csv`)  

---

## Τα πρώτα δεδομένα

Το αρχικό CSV `data/raw_data.csv` για δοκιμή:

name,age,salary
Γιάννης,30,50000
Άννα,,
Μιχάλης,40,60000
Σοφία,25,



Με το ETL script, δημιουργείται το `clean_data.csv`, έτοιμο για ανάλυση.

---

## Τι έκανα μετά

1. Δημιούργησα ένα **script ανάλυσης με Spark** (`src/analysis/spark_analysis.py`) που:

   - φορτώνει τα καθαρά δεδομένα σε Spark DataFrame  
   - εμφανίζει τις πρώτες γραμμές  
   - υπολογίζει μέσο μισθό ανά όνομα και συνολικό μέσο μισθό  

2. Δημιούργησα ένα πιο **πλήρες script** (`src/analysis/spark_analysis_report.py`) που:

   - τρέχει την ανάλυση με Spark  
   - συλλέγει τα Spark jobs (Job ID, Status, αριθμός Stages)  
   - σώζει τα jobs σε CSV (`data/spark_jobs.csv`)  
   - δημιουργεί PDF report (`data/spark_jobs_report.pdf`) με τις ίδιες πληροφορίες  

---

## Πώς τρέχω το project

1. Ενεργοποιώ το virtual environment (`venv`):

```bash
source venv/bin/activate  # Linux / WSL

1.Τρέχω το ETL script για να καθαρίσω τα δεδομένα:

python src/etl/load_clean_data.py




2.Τρέχω το Spark analysis report script για CSV + PDF:

python src/analysis/spark_analysis_report.py


Σημείωση: Για να δουλέψει το Spark χρειάζεται εγκατεστημένο JDK και σωστά ορισμένο JAVA_HOME!!!!!!!!!!!!!!

Όλα τα παραγόμενα αρχεία (clean_data.csv, spark_jobs.csv, spark_jobs_report.pdf) αποθηκεύονται μέσα στο φάκελο data/.

---------------------------------------
Tests για τον κώδικα του cleaning


Πώς τρέχω τα tests:

Με Python built-in unittest:

python tests/test_etl.py


Έτσι βεβαιώνεσαι ότι το ETL module λειτουργεί σωστά και καθαρίζει τα δεδομένα όπως πρέπει.



## Notebooks

Στον φάκελο `notebooks/` κρατάω όλα τα Jupyter notebooks για ανάλυση δεδομένων και πειράματα.  
Κάθε notebook περιέχει **code cells** για Python κώδικα και **Markdown cells** για τίτλους, περιγραφές και σημειώσεις.  
Αυτό επιτρέπει να βλέπω άμεσα αποτελέσματα, plots και outputs χωρίς να τρέχω ξεχωριστά scripts.

### Εξαρτήσεις για τα notebooks

Για να τρέξουν σωστά, χρειάζεται να εγκατασταθούν οι παρακάτω βιβλιοθήκες στο virtual environment (`venv`):

```bash
pip install pandas matplotlib seaborn::::::

REQUIRMENTS:::::
pandas για φόρτωση και επεξεργασία δεδομένων

matplotlib και seaborn για plots και visualization