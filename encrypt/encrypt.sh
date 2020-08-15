#!/bin/bash

declare -A creditals
BUFFER=$HOME/informator/encrypt/buffer.txt

while read line; do
	arg=$(echo $line | awk '{print $1}')
	if [[ "$arg" == "PASSWORD" ]]; then
		creditals[PASSWORD]=$(echo $line | awk '{print $3}')
	fi

	if [[ "$arg" == "ENCRYPTION_KEY" ]]; then
		creditals[ENCRYPTION_KEY]=$(echo $line | awk '{print $3}')
	fi

	if [[ "$arg" == "SIGN_KEY" ]]; then
		creditals[SIGN_KEY]=$(echo $line | awk '{print $3}')
	fi
done < $HOME/informator/encrypt/encrypt.conf

echo "$1" > $BUFFER

gpg --output ./text.txt.asc --encrypt -r ${creditals[ENCRYPTION_KEY]} $BUFFER
gpg --output ./text.txt.sig --local-user ${creditals[SIGN_KEY]} --batch --yes --passphrase "$(echo ${creditals[PASSWORD]} | openssl enc -base64 -d)" --detach-sign $BUFFER
python $HOME/informator/encrypt/send_mail.py
rm -R ./text.txt.sig ./text.txt.asc $BUFFER
