## test_upload.py
###这个代码叫upload_seperate.py，现在创建test_upload.py，通过[pytest test_upload.py]和def test，assert  == 1/2/3/4的方式构建 怎么弄
## if[python3 upload_seperate.py]we can return 1
## if[python3 upload_seperate.py none.txt] we can return 2
## if[python3 upload_seperate.py sample.png]we can return 3
## if[python3 upload_seperate.py grade.pdf]we can return 4
#seperate upload from auth.py app.py nowclient.py
import pytest
from upload_separate import main

def test_no_input(monkeypatch):
    # 测试没有输入文件的情况
    monkeypatch.setattr('sys.argv', ['upload_separate.py'])
    assert main(None) == 1

def test_nonexistent_file(monkeypatch):
    # 测试输入不存在的文件
    monkeypatch.setattr('sys.argv', ['upload_separate.py', 'none.txt'])
    assert main('none.txt') == 2

def test_unsupported_file_type(monkeypatch):
    # 测试输入不支持的文件类型
    monkeypatch.setattr('sys.argv', ['upload_separate.py', 'sample.png'])
    assert main('sample.png') == 3

def test_supported_pdf_file(monkeypatch):
    # 测试输入支持的文件类型（假设grade.pdf存在）
    monkeypatch.setattr('sys.argv', ['upload_separate.py', 'grade.pdf'])
    assert main('grade.pdf') == 4

# 运行 pytest
# 这将在命令行中自动寻找以 test_ 开头的函数并执行它们

