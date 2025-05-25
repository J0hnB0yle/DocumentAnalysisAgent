# tests/test_document_analysis.py
import sys
import os
import unittest

# Add project root to sys.path to allow direct import of app.core
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.core import load_document, summarize_document, extract_information, analyze_document

class TestDocumentAnalysis(unittest.TestCase):

    def test_load_document(self):
        # Test with a dummy file path, actual file interaction is mocked by placeholder
        result = load_document("dummy.pdf")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_summarize_document(self):
        result = summarize_document("Some sample text for summarization.")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_extract_information(self):
        result = extract_information("Some sample text.", "names")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_analyze_document(self):
        result = analyze_document("Some sample text.", "What is this about?")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()
