# -*- coding: utf-8 -*-
# ロガーに複数のハンドラーを登録する

from __future__ import print_function
import logging

# ロガー取得
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# ハンドラー生成
h1 = logging.StreamHandler()
h1.setLevel(logging.DEBUG)
h2 = logging.FileHandler("handler2.log")
h2.setLevel(logging.ERROR)

# フォーマッタ生成
fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# フォーマッタ登録
h1.setFormatter(fmt)
h2.setFormatter(fmt)

# ハンドラー登録
logger.addHandler(h1)
logger.addHandler(h2)

# ログ出力
logger.debug("Debugログ") # h1
logger.info("Infoログ")   # h1
logger.warn("Warnログ")   # h1
logger.error("Errorログ") # h1, h2
