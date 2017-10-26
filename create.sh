#/bin/sh
# 使用方法:カレントディレクトリにsrcディレクトリがあることを確認し
# $ sh create.sh Sample
# のようにスクリプトを実行するとsrc直下にSampleディレクトリとpracticeXX.pyが作成される

orderDIR=$1
# ディレクトリを指定しているかどうか
if [ -z "$orderDIR" ];	then
	echo "ERROR : Argument(Directory) is NONE"
	exit 1
fi

var=0
srcDIR=`ls | grep "src"`
if [ -z ${srcDIR} ];	then
	mkdir "src"
	var=1
fi

# 要求ディレクトリの有無
search=`ls ./src | grep -w $orderDIR`
if [ -z ${search} ];	then
	orderDIR="./src/${orderDIR}"
	mkdir "${orderDIR}"
else
	orderDIR="./src/${orderDIR}"
fi	

# 要求ディレクトリの確認
echo "ORDER : ${orderDIR}"

# 検索ディレクトリ
DIRPATH=./src/*/
OLD_NAME=0
if [ $var -eq 1 ];	then
	pathNAME=$orderDIR
	NAME=1
else
	for FILE in ${DIRPATH}*
	do
		NAME=`echo ${FILE#*/practice} | grep -o '[0-9]*' `
		if [ -z $NAME ];	then
			NAME=$OLD_NAME
		elif [ $NAME -gt $OLD_NAME ]; then
			OLD_NAME=$NAME
			pathNAME=$(dirname $FILE)
		else
			NAME=$OLD_NAME
		fi
	done
	# 新規作成するファイルのインデックスを作成
	NAME=$(expr $NAME + 1)
fi

# ファイル名の作成
fileNAME="practice$NAME.py"

# ファイル・ディレクトリ名確認
echo "FILE  : ${fileNAME}"
echo "DIR   : ${pathNAME}"

# pathNAMEが要求ディレクトリであるかどうか
if [ ${pathNAME} != ${orderDIR} ];	then
	pathNAME=$orderDIR
fi

# 新規作成するファイルのパスの作成
fileNAME="/practice$NAME.py"
newFILE=$pathNAME$fileNAME
echo "MAKE  : ${newFILE}"

# ファイルの作成
echo "# -*- coding: utf-8 -*-" | cat > "${newFILE}" 
