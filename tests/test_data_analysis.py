# tests/test_data_analysis.py
import sys
import os
import unittest
import pandas as pd

# Add project root to sys.path to allow direct import of data_analysis_agent.core
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_analysis_agent.core import load_data, analyze_data, create_visualization, recommend_visualizations, explain_analysis

class TestDataAnalysis(unittest.TestCase):

    def test_load_data(self):
        # Test with dummy file paths, actual file interaction is mocked by placeholder
        df_csv = load_data("dummy.csv")
        self.assertIsNotNone(df_csv)
        self.assertIsInstance(df_csv, pd.DataFrame)

        df_excel = load_data("dummy.xlsx")
        self.assertIsNotNone(df_excel)
        self.assertIsInstance(df_excel, pd.DataFrame)
        
        df_none = load_data("dummy.txt") # Assuming this returns None
        self.assertIsNone(df_none)


    def test_analyze_data(self):
        dummy_df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        result = analyze_data(dummy_df)
        self.assertIsInstance(result, dict)
        self.assertIn('insights', result)
        self.assertIn('statistics', result)

    def test_create_visualization(self):
        dummy_df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        img_str, error = create_visualization(dummy_df, "histogram", ["A"], "Test Histo")
        self.assertIsInstance(img_str, str) # Placeholder returns a base64 string
        self.assertIsNone(error)
        self.assertTrue(len(img_str) > 0)

    def test_recommend_visualizations(self):
        dummy_df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        result = recommend_visualizations(dummy_df)
        self.assertIsInstance(result, dict)
        self.assertIn('enhanced_suggestions', result)

    def test_explain_analysis(self):
        dummy_df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        result = explain_analysis(dummy_df, "Correlation", {'columns': ['A', 'B']})
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()
