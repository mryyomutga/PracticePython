# -*- coding: utf-8 -*-
import pkg1.mod1
pkg1.mod1.func1()

# 実行結果
# $ python -m pkg1
#   __init__.py : pkg1
#   pkg1/mod1.py : pkg1.mod1

# .pyではなくpkg1に対して実行することが可能
# 実行可能な組込みモジュール
# json.toolを用いるとjson文字列を読みやすくダンプする
# $ python -m json.tool sample.json