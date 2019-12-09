import compileall
import os
from shutil import move
from shutil import copytree
import sys


def compile_pyc(target, out):
    # assert not os.path.exists(out),"文件夹已存在"
    copytree(target, out)
    compileall.compile_dir(out)
    range_file(out)


def range_file(path):
    file_list = os.listdir(path)
    for file_name in file_list:
        if file_name == "__pycache__":
            pycache_path = os.path.join(path, file_name)
            for pyc_file_name in os.listdir(pycache_path):
                new_name = pyc_file_name.replace("cpython-37.pyc", "pyc")
                move(os.path.join(pycache_path, pyc_file_name), os.path.join(path, new_name))
            os.rmdir(pycache_path)
        elif file_name.endswith(".py"):
            os.remove(os.path.join(path, file_name))

        elif os.path.isdir(os.path.join(path, file_name)):
            range_file(os.path.join(path, file_name))


if __name__ == '__main__':
    assert len(sys.argv) == 3, "使用方式：python py_2_pyc.py 目标文件夹 输出文件夹"
    compile_pyc(sys.argv[1], sys.argv[2])
