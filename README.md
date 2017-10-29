# PracticePython
Pythonの練習

## 目的
専門ゼミ・研究でPythonを使用する機会が多いため、自習したソースを管理する

Pythonの文法確認のために自分専用のWikiを作成する

### 参考資料

- [Python学習講座](http://www.python.ambitious-engineer.com/)

## 後回し
lambda式・関数デコレータ・関数アノテーションは必要に応じて学習

### create.shについて
#### 要望

- 新しくファイルを作ったり、ディレクトリを作って管理するのが面倒なので、ファイルやディレクトリの新規作成を自動化したい

- いちいちファイルの先頭に
    ```python
    # -*- coding: utf-8 -*-
    ```
    を書くのが面倒なので、これも作成時に自動的に記述したい

#### 仕様
- カレントディレクトリにsrcディレクトリを作成する
- src配下には引数で指定した名前でディレクトリを自動で作成する
- 指定したディレクトリにpracticeXX.pyというファイル名が作成される(XXは連番)

#### 実行方法
以下のコマンドを入力する(testディレクトリにファイルを作成したい場合)

```
$ sh create.sh test
  ORDER : ./src/test
  FILE  : practice1.py
  DIR   : ./src/test
  MAKE  : ./src/test/practice1.py
```

実行後、以下のようなディレクトリが新規作成される(src、testディレクトリがない場合)
testディレクトリ配下にpractice1.pyが作成される

```
$ tree
C:.
└─src
    └─test
```

practice1.pyには以下のコメントが自動的に記述される

```
$ cat src/test/practice1.py
  # -*- coding: utf-8 -*-
```

### 追記(2017/10/28)
- シェルスクリプトを変更しました。

    BASE_PROG.pyには以下の2文が記述されており、これを新規作成されたファイルに書き込みます

    書き込む内容を変更する場合はBASE_PROG.pyを変更してください
    ```python
    # -*- coding: utf-8 -*-
    from __future__ import print_function
    ```

- 実行方法を変更しました

    Foundationディレクトリのtestディレクトリに作成する場合、以下のコマンドを実行してください
    ```sh
    sh create.sh Foundation/test
    ```
    `sh create.sh src直下のディレクトリ/ファイルを新規作成するディレクトリ`のように実行してください

    `src/directory/`には作成されないので注意してください

## 更新情報
<table width=800>
    <tr>
        <th width=100 align="center">Date</th>
        <th width=700 align="left">Activity</th>
    </tr>
    <tr>
        <td width=100 align=center>2017/10/17(Tue)</td>
        <td width=700>変数・文字列・リスト・タプル・辞書<br>if-elif-else文</td>
    </tr>
    <tr>
        <td width=100 align=center>2017/10/19(Thu)</td>
        <td width=700>for-else文・set型・オブジェクトのID<br>while-else文・pass<br>関数の定義・global宣言・関数オブジェクト<br>内部関数・nonlocal宣言<br>ジェネレータ</td>
    </tr>
    <tr>
        <td width=100 align=center>2017/10/21(Sat)</td>
        <td width=700>クラスの定義・クラスオブジェクト・クラス変数<br>クラスメソッド・スタティックメソッド<br>新規作成のためのシェルスクリプトの作成</td>
    </tr>
    <tr>
        <td width=100 align=center>2017/10/22(Sun)</td>
        <td width=700>クラスの継承<br>プライベートメンバ<br>例外処理<br>シェルスクリプトの修正</td>
    </tr>
    <tr>
        <td width=100 align=center>2017/10/24(Tue)</td>
        <td width=700>ファイルの入出力<br>ファイル・ディレクトリの存在確認・作成・削除</td>
    </tr>
    <tr>
        <td width=100 align=center>2017/10/25(Wed)</td>
        <td width=700>文字列の基本的な操作・変換・フォーマット<br>モジュールのimport・自作モジュールの作成</td>
    </tr>
    <tr>
        <td width=100 align=center>2017/10/26(Thu)</td>
        <td width=700>標準ライブラリ(OrderedDict)<br>標準ライブラリ(datetime, date, time)<br>標準ライブラリ(json)</td>
    </tr>
    <tr>
        <td width=100 align=center>2017/10/27(Fri)</td>
        <td width=700>標準ライブラリ(csv)<br>標準ライブラリ(copy)</td>
    </tr>
    <tr>
        <td width=100 align=center>2017/10/28(Sat)</td>
        <td width=700>ログ出力(logging, logger)<br>組み込み関数(map,filter,zip,reduce)<br>シェルスクリプトの修正<br>[Python学習講座] 入門編 終了</td>
    </tr>
</table>
