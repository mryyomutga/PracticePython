# -*- coding: utf-8 -*-
# logconf.yamlを用いたロガーの設定
# pipでPyYAMLをインストール
# pip install PyYAML
# Windowsの場合
# UnicodeDecodeErrorが発生する場合
# chcpで現在の文字コードがShiftJIS(932)である場合
# chcp 65001でUTF-8に変更してから再度インストールする

from __future__ import print_function
import yaml
from logging import config, getLogger

config.dictConfig(yaml.load(open("logconf.yml", encoding="UTF-8").read()))
logger = getLogger(__name__)
logger.error("エラーが発生しました")
