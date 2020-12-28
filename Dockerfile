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

#set work directory
WORKDIR /data

#set UID fetchmail user
RUN usermod -u 10001 fetchmail 

RUN useradd procmail -u 10002 -m -d /home/procmail

COPY ./procmail_trigger.py /data

#set permissions for data directory
RUN chown -R fetchmail:nogroup /data \
    && chmod -R 0744 /data

#set default user for docker container
USER fetchmail

CMD ["fetchmail", "-vvv", "--nosyslog", "--nodetach", "--pidfile", "/tmp/fetchmail.pid", "-f", "/data/fetchmailrc/.fetchmailrc"]
