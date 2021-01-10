<h1><b>Fpmail</b></h1>

<p>This docker image will run as a single process.</p>

<h2>Volume</h2>
<p>Run as a single container:</p>
<pre>docker run --rm -d \
            -v /etc/fpmail/.procmailrc:/home/fetchmail/.procmailrc \ 
            -v /etc/fpmail/fetchmail:/home/fetchmail/fetchmailrc \
            -v /etc/fpmail/procmail:/home/fetchmail/procmailrc \
            -v /etc/fpmail/Mail:/home/fetchmail/Mail \
            -e FPMAIL_OUT_DMS="1.1.1.1" fpmail
</pre>
<p>Note: FPMAIL_OUT_DMS is optional env variable. It is required in case if you have a decision-making system.</p>

<h2>Permissions</h2>
<p>UID fetchmail = 10001; GUID nogroup = 65534</p>
<pre>chown fetchmail:nogroup fetchmail && chmod 700 fetchmail
     chown fetchmail:nogroup procmail && chmod 700 procmail
     chown fetchmail:nogroup Mail && chmod 700 Mail
     chown fetchmail:nogroup .procmailrc && chmod 700 .procmailrc
</pre>

<h2>Docker-compose</h2>
<pre>fpmail:
         image: fpmail:latest
         restart: always
         environment:
           FPMAIL_OUT_DMS="1.1.1.1"
         volumes:
           - /etc/fpmail/.procmailrc:/home/fetchmail/.procmailrc
           - /etc/fpmail/fetchmailrc:/home/fetchmail/fetchmailrc
           - /etc/fpmail/procmailrc:/home/fetchmail/procmailrc
           - /etc/fpmail/Mail:/home/fetchmail/Mail
         ports:
           - 993:993
           - 10128:10128
</pre>
