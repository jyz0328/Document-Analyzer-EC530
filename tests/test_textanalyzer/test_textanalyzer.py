#run [pytest test_textanalyzer.py]to see results
import pytest
from unittest import mock
import os
import textanalyzer_separate

# Mock sys.argv for no input scenario
def test_no_input():
    with mock.patch('sys.argv', ['textanalyzer_separate.py']):
        with pytest.raises(SystemExit) as e:
            textanalyzer_separate.main()
        assert e.value.code == 1

# Mock for nonexistent file
def test_nonexistent_file():
    with mock.patch('sys.argv', ['textanalyzer_separate.py', 'none.txt']):
        with mock.patch('os.path.exists', return_value=False):
            with pytest.raises(SystemExit) as e:
                textanalyzer_separate.main()
            assert e.value.code == 2

# Mock for non-txt file input
def test_non_txt_file():
    with mock.patch('sys.argv', ['textanalyzer_separate.py', 'grade.pdf']):
        with mock.patch('os.path.exists', return_value=True):
            with mock.patch('textanalyzer_separate.analyze_document', return_value=3):
                with pytest.raises(SystemExit) as e:
                    textanalyzer_separate.main()
                assert e.value.code == 3

# Mock for valid txt file
def test_valid_txt_file():
    with mock.patch('sys.argv', ['textanalyzer_separate.py', 'test.txt']):
        with mock.patch('os.path.exists', return_value=True):
            with mock.patch('textanalyzer_separate.analyze_document', return_value=4):
                with pytest.raises(SystemExit) as e:
                    textanalyzer_separate.main()
                assert e.value.code == 4
