# tests/test_etl.py
import sys
import os
import unittest
import pandas as pd

# Προσθήκη του root folder στο path για να βρει το src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.etl.load_clean_data import clean_data  # τώρα θα δουλέψει

class TestETL(unittest.TestCase):
    def test_clean_data(self):
        # Δημιουργία μικρού test DataFrame με τα νέα ονόματα στηλών
        df = pd.DataFrame({
            "First Name": ["Jose", "Diane"],
            "Last Name": ["Lopez", "Carter"],
            "Age": [25, None],
            "Salary": [8500, None]
        })

        # Τρέξε τη συνάρτηση clean_data
        cleaned_df = clean_data(df)

        # Έλεγχος ότι δεν υπάρχουν κενά στις στήλες Age και Salary
        self.assertEqual(cleaned_df["Age"].isnull().sum(), 0)
        self.assertEqual(cleaned_df["Salary"].isnull().sum(), 0)

if __name__ == "__main__":
    unittest.main()
