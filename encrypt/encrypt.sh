#!/bin/bash

/usr/bin/expect << EOF
	spawn gpg --output text.txt.asc --encrypt -r 02B1A9097AB4A50614D1BCD158E2A908E8FA51B1 $1
	expect -exact "Все равно использовать данный ключ? (y/N)"
	send -- "y\r"
	expect eof
EOF

/usr/bin/expect << EOF

	spawn gpg --output text.txt.sig --local-user 203D32DFCFF14A413F6C29AE09BFEE9C4FF2337B --detach-sign $1
	expect {
		"Фраза-пароль" {
			send -- "q"
			expect -exact "*^[(B^[\[m"
			send -- "w"
			expect -exact "*^[(B^[\[m"
			send -- "e"
			expect -exact "*^[(B^[\[m"
			send -- "r"
			expect -exact "*^[(B^[\[m"
			send -- "t"
			expect -exact "*^[(B^[\[m"
			send -- "y"
			expect -exact "*^[(B^[\[m"
			send -- "1"
			expect -exact "*^[(B^[\[m"
			send -- "2"
			expect -exact "*^[(B^[\[m"
			send -- "3"
			expect -exact "*^[(B^[\[m"
			send -- "\r"
		}
	}

EOF

sudo python send_mail.py
sudo rm -R text.txt.sig text.txt.asc
