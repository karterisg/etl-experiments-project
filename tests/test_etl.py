import unittest
import pandas as pd
from src.etl.load_clean_data import clean_data  # χρειαζόμαστε σωστά unit tests για να διασφαλίσουμε την ποιότητα του ETL

class TestETL(unittest.TestCase):
    def test_clean_data(self):
        df = pd.DataFrame({"age": [30, None], "salary": [50000, None]})
        cleaned_df = clean_data(df)
        self.assertEqual(cleaned_df["age"].isnull().sum(), 0)
        self.assertEqual(cleaned_df["salary"].isnull().sum(), 0)

if __name__ == "__main__":
    unittest.main()
