FROM debian:stable-slim
MAINTAINER Andrey Senushchenkov "r3akt1vee@gmail.com" 

#getting actual and neccesery components from apt installer 
RUN apt-get update \
    && apt-get install -y fetchmail \
       procmail \
       openssl \
       ca-certificates \
       uudeview \
    && apt-get clean

#set environment for rcs files
RUN usermod -u 10001 -md /home/fetchmail fetchmail \
    && touch /home/fetchmail/.procmailrc \
    && chown fetchmail:nogroup /home/fetchmail/.procmailrc \
    && chmod 700 /home/fetchmail/.procmailrc 

COPY ./procmail_trigger.py /home/fetchmail

#set procmail_trigger script permissions
RUN chown fetchmail:nogroup /home/fetchmail/procmail_trigger.py \
    && chmod 700 /home/fetchmail/procmail_trigger.py 

#set default user for docker container
USER fetchmail

CMD ["fetchmail", "-vvv", "--nosyslog", "--nodetach", "--pidfile", "/tmp/fetchmail.pid", \
     "-f", "/home/fetchmail/fetchmailrc/.fetchmailrc"]
