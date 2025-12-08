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
        # Δημιουργία μικρού test DataFrame
        df = pd.DataFrame({
            "name": ["Γιάννης", "Άννα"],
            "age": [30, None],
            "salary": [50000, None]
        })

        # Τρέξε τη συνάρτηση clean_data
        cleaned_df = clean_data(df)

        # Έλεγχος ότι δεν υπάρχουν κενά
        self.assertEqual(cleaned_df["age"].isnull().sum(), 0)
        self.assertEqual(cleaned_df["salary"].isnull().sum(), 0)

if __name__ == "__main__":
    unittest.main()
