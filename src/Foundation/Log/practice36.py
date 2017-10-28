# -*- coding: utf-8 -*-
from __future__ import print_function
import logging

logger1 = logging.getLogger("Parent")
logger1.setLevel(logging.DEBUG)

h1 = logging.StreamHandler()
h1.setLevel(logging.DEBUG)

h1.setFormatter(logging.Formatter("Format 1 %(message)s"))
logger1.addHandler(h1)

logger2 = logging.getLogger("Parent.childe")
logger2.error("エラーメッセージ")   # Format 1 エラーメッセージ
