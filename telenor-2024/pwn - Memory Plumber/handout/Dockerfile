FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y build-essential socat && \
    adduser --disabled-password --gecos '' netcatuser && \
    chown -R root:netcatuser /home/netcatuser && \
    chmod 750 /home/netcatuser

WORKDIR /home/netcatuser

COPY ./leak /home/netcatuser
copy ./flag.txt /home/netcatuser

EXPOSE 1235
CMD su -l netcatuser -c "socat -dd TCP4-LISTEN:1235,fork,reuseaddr EXEC:/home/netcatuser/leak"
