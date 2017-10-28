# -*- coding: utf-8 -*-
# ログ出力(logger)
# loggingよりloggerを使用する
from __future__ import print_function
import logging

# ロガーの取得
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# ハンドラーの生成
handle = logging.StreamHandler()
handle.setLevel(logging.DEBUG)

# フォーマッタの生成
fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# ハンドラーにフォーマッタを設定する
handle.setFormatter(fmt)

# ロガーにハンドラーを設定する
logger.addHandler(handle)

# ログ出力
logger.info("output")
