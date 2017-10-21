#/bin/sh
# 使用方法:カレントディレクトリにsrcディレクトリがあることを確認し
# $ sh create.sh Sample
# のようにスクリプトを実行するとsrc直下にSampleディレクトリとpracticeXX.pyが作成される

orderDIR=$1
#ディレクトリを指定しているかどうか
if [ -z "$orderDIR" ];	then
	echo "ERROR : Argument(Directory) is NONE"
	exit 1
fi

srcDIR=`ls | grep "src"`
if [ -z ${srcDIR} ];	then
	echo "\"src\" directory is not found."
	echo "make \"src\" directory ? (yes/no)"
	read ans

	if [ $ans = "yes" ];	then
		mkdir "src"
	elif [ $ans = "y" ];	then
		mkdir "src"
	else
		echo "ERROR : do\'nt exist \"src\" directory"
		echo "        Please make \"src\" directory"
		exit 1
	fi
fi

#検索ディレクトリ
DIRPATH=./src/*/
OLD_NAME=00
for FILE in ${DIRPATH}*
do
	NAME=`echo ${FILE##*/practice} | grep -o '[0-9]*' `
	if [ -z $NAME ];	then
		NAME=$OLD_NAME
		break
	elif [ $NAME -gt $OLD_NAME ]; then
		OLD_NAME=$NAME
		pathNAME=$(dirname $FILE)
	else
		NAME=$OLD_NAME
	fi
done

#新規作成するファイルのインデックスを作成
NAME=$(expr $NAME + 1)
fileNAME="/practice$NAME.py"

#ファイル・ディレクトリ名確認
echo "FILE  : ${fileNAME}"
echo "DIR   : ${pathNAME}"

orderDIR="./src/${orderDIR}"
#要求ディレクトリの確認
echo "ORDER : ${orderDIR}"

#pathNAMEが要求ディレクトリであるかどうか
if [ ${pathNAME} != ${orderDIR} ];	then
	pathNAME=$orderDIR
	mkdir $pathNAME
fi

#新規作成するファイルのパスの作成
newFILE=$pathNAME$fileNAME
echo "MAKE  : ${newFILE}"

#ファイルの作成
echo "# -*- coding:utf-8 -*-" | cat > "${newFILE}" 
