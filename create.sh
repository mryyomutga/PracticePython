#/bin/sh
# �g�p���@:�J�����g�f�B���N�g����src�f�B���N�g�������邱�Ƃ��m�F��
# $ sh create.sh Sample
# �̂悤�ɃX�N���v�g�����s�����src������Sample�f�B���N�g����practiceXX.py���쐬�����

orderDIR=$1
#�f�B���N�g�����w�肵�Ă��邩�ǂ���
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

#�����f�B���N�g��
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

#�V�K�쐬����t�@�C���̃C���f�b�N�X���쐬
NAME=$(expr $NAME + 1)
fileNAME="/practice$NAME.py"

#�t�@�C���E�f�B���N�g�����m�F
echo "FILE  : ${fileNAME}"
echo "DIR   : ${pathNAME}"

orderDIR="./src/${orderDIR}"
#�v���f�B���N�g���̊m�F
echo "ORDER : ${orderDIR}"

#pathNAME���v���f�B���N�g���ł��邩�ǂ���
if [ ${pathNAME} != ${orderDIR} ];	then
	pathNAME=$orderDIR
	mkdir $pathNAME
fi

#�V�K�쐬����t�@�C���̃p�X�̍쐬
newFILE=$pathNAME$fileNAME
echo "MAKE  : ${newFILE}"

#�t�@�C���̍쐬
echo "# -*- coding:utf-8 -*-" | cat > "${newFILE}" 
