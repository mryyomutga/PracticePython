# -*- coding: utf-8 -*-
# ログ出力(logging)
from __future__ import print_function

import logging

# logging.warning("Warning!") # WARNING:root:Warning!
# logging.error("Error!!")    # ERROR:root:Error!!

# logging.basicConfig(level=logging.DEBUG)

# logging.debug("Debug")
# logging.info("Info")
# logging.warning("Warning")
# logging.error("Error")
# logging.critical("Critical")

# ログのフォーマット
# 実行時は7~16行目をコメントアウト
log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# logging.basicConfig(format = log_fmt, level = logging.DEBUG)
# 2017-10-28 03:07:55,002 - root - ERROR - エラーの発生
# logging.error("エラーの発生")

# ログメッセージに変数を埋め込む
# logging.error("error %s %s", "abc", "efg")
# logging.error("error {0} {1}".format("abc", "efg"))

# ログファイルに書き出す
# 実行時は7~27行目をコメントアウト
logging.basicConfig(filename = "sample.log", format = log_fmt)
logging.error("error %s %s", "abc", "efg")
logging.error("error {0} {1}".format("abc", "efg"))
