#!/bin/bash

FETCH_DIR="$HOME/informator/fetchmail/attachments"
SCRIPT_DIR="$HOME/informator/decrypt"
ARCHIVE_DIR="$SCRIPT_DIR/archive"
ERROR_DIR="$SCRIPT_DIR/error_msg"

var_asc=$(ls $FETCH_DIR | grep ".asc")
var_sig=$(ls $FETCH_DIR | grep ".sig")

### Логирование случаев, с хорошими ключами

function saveInArchive {
	dir=$(echo $(($(date +%s%N)/1000000)))
	if [[ ! -d ${ARCHIVE_DIR}/${dir} ]]; then
		mkdir ${ARCHIVE_DIR}/${dir}
	fi

	mv ${FETCH_DIR}/${a} ${ARCHIVE_DIR}/${dir}
	mv ${FETCH_DIR}/${b} ${ARCHIVE_DIR}/${dir}
	mv ${SCRIPT_DIR}/${plane_text_path}.txt ${ARCHIVE_DIR}/${dir}
}

### Логирование случаев, с плохими ключами

function checkKeyFailed {
	dir=$(echo $(($(date +%s%N)/1000000)))
        if [[ ! -d ${ERROR_DIR}/${dir} ]]; then
		mkdir ${ERROR_DIR}/${dir}
	fi

        mv ${FETCH_DIR}/${a} ${ERROR_DIR}/${dir}
        mv ${FETCH_DIR}/${b} ${ERROR_DIR}/${dir}

	if [[ -e ${SCRIPT_DIR}/${plane_text_path}.txt ]]; then
        	rm -R ${SCRIPT_DIR}/${plane_text_path}.txt
	fi

	echo "ERROR: Checking key-pair failed"
}

### Взять данные ключей из файла decrypt.conf

function getCreditals {
	while read line; do
        	arg=$(echo $line | awk '{print $1}')
        	if [[ "$arg" == "PASSWORD" ]]; then
               		 creditals[PASSWORD]=$(echo $line | awk '{print $3}')
			 passphrase=$(echo ${creditals[PASSWORD]} | openssl enc -base64 -d)
        	fi
	done < /home/alexeysenu/informator/decrypt/decrypt.conf
}

for a in $var_asc; do
	### Проверка файлов на одинаковый источник
	res_a=$(echo "$a" | awk -F "." '{print $1}')
	for b in $var_sig; do
		res_b=$(echo "$b" | awk -F "." '{print $1}')
		if [[ "$res_a" == "$res_b" ]]; then
			plane_text_path=$(echo $(($(date +%s%N)/1000000)))
			getCreditals
		
			### Проверка шифрования
			decrypt_message=$(gpg --output ${SCRIPT_DIR}/${plane_text_path}.txt --batch --yes --passphrase "qwerty123" --decrypt ${FETCH_DIR}/${a} 2>&1)
			echo "$decrypt_message"
			if echo "$decrypt_message" | grep "encrypted with 2048-bit\|зашифровано 2048-битным ключом" > /dev/null; then
			
				### Проверка цифровой подписи
				decrypt_message=$(gpg --verify ${FETCH_DIR}/${b} ${SCRIPT_DIR}/${plane_text_path}.txt 2>&1)
				if echo "$decrypt_message" | grep "Действительная подпись\|Good signature" > /dev/null; then
					echo "GOOD ALL"
					text=$(cat ${SCRIPT_DIR}/${plane_text_path}.txt)
					saveInArchive
					#echo $text >> ${SCRIPT_DIR}/out.txt
					python ${SCRIPT_DIR}/con.py "$text"
				else
					checkKeyFailed
				fi
			else
				checkKeyFailed
			fi
			break
		fi
	done
done
