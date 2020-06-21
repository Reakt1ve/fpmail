#!/bin/bash

FETCH_DIR="/home/andrey/fetchmail/attachments"
SCRIPT_DIR="/home/andrey/decrypt"
ARCHIVE_DIR="$SCRIPT_DIR/archive"
ERROR_DIR="$SCRIPT_DIR/error_msg"

var_asc=$(ls $FETCH_DIR | grep ".asc")
var_sig=$(ls $FETCH_DIR | grep ".sig")

function saveInArchive {
	dir=$(echo $(($(date +%s%N)/1000000)))
	sudo mkdir ${ARCHIVE_DIR}/${dir}

	sudo mv ${FETCH_DIR}/${a} ${ARCHIVE_DIR}/${dir}
	sudo mv ${FETCH_DIR}/${b} ${ARCHIVE_DIR}/${dir}
	sudo mv ${SCRIPT_DIR}/${plane_text_path}.txt ${ARCHIVE_DIR}/${dir}
}

function checkKeyFailed {
	dir=$(echo $(($(date +%s%N)/1000000)))
        sudo mkdir ${ERROR_DIR}/${dir}

        sudo mv ${FETCH_DIR}/${a} ${ERROR_DIR}/${dir}
        sudo mv ${FETCH_DIR}/${b} ${ERROR_DIR}/${dir}
        sudo rm -R ${SCRIPT_DIR}/${plane_text_path}.txt

	echo "ERROR: Checking key-pair failed"
}

function main {
	for a in $var_asc; do
		res_a=$(echo "$a" | awk -F "." '{print $1}')
		for b in $var_sig; do
			res_b=$(echo "$b" | awk -F "." '{print $1}')
			if [[ "$res_a" == "$res_b" ]]; then
				plane_text_path=$(echo $(($(date +%s%N)/1000000)))
				decrypt_message=$(sudo gpg --output ${SCRIPT_DIR}/${plane_text_path}.txt --decrypt ${FETCH_DIR}/${a} 2>&1)
				if echo "$decrypt_message" | grep "зашифровано 2048-битным ключом" > /dev/null; then
					decrypt_message=$(sudo gpg --verify ${FETCH_DIR}/${b} ${SCRIPT_DIR}/${plane_text_path}.txt 2>&1)
						if echo "$decrypt_message" | grep "Действительная подпись пользователя" > /dev/null; then
							echo "GOOD ALL"
							text=$(sudo cat ${SCRIPT_DIR}/${plane_text_path}.txt)
							saveInArchive
							echo $text >> ${SCRIPT_DIR}/out.txt
							sudo python con.py "$text"
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
}

main
