#if [python3 textanalyzer_seperate.py] , we can get return 1
#if [python3 textanalyzer_seperate.py none.txt], we can get return 2
#if [python3 textanalyzer_seperate.py grade.pdf], we can get return 3
#if [python3 textanalyzer_seperate.py test.txt], we can get return 4
#这个代码是在单独运行textanalyzer并汇报错误或者正确情况
#报错都和return都在[analyze_doucment]进行，而不是在mianpart进行，并且每个情况保存为return 数字
#如果，根本没有输入文件，print("error:do not enter a document for text analyze“）输出并让[analyze_doucment]return1
#如果，输入根本不存在的文件，print("error:document does not exist“）输出并让[analyze_doucment]return2
#如果，输入存在的文件但是不是txt，print("error:document exists but this module only accept txt. we use upload.py to transfer document into txt and then put it into textanalyzer.py “）输出并让[analyze_doucment]return3
#如果，输入存在的txt，print("successfully“）输出并让return4
#这个代码叫textanalyzer_seperate.py，现在创建test_textanalyzer.py，通过[pytest test_textanalyzer.py]和def test，assert  == 1/2/3/4的方式构建 怎么弄
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
