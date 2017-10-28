# -*- coding: utf-8 -*-
# logconf.iniを用いたロガーの設定
from __future__ import print_function
import logging.config

logging.config.fileConfig("logconf.ini")
logger = logging.getLogger("sample")
logger.error("エラーが発生しました")
