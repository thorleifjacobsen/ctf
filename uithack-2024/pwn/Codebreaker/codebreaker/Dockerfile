FROM ubuntu:22.04
LABEL Description="UiTHack24 codebreaker"

RUN useradd -d /home/ctf -m -p ctf -s /bin/bash ctf
WORKDIR /home/ctf

COPY ynetd .
COPY codebreaker .
COPY flag.txt .

RUN chown -R root:root /home/ctf
RUN chmod -R a+rx /home/ctf

USER ctf
CMD ./ynetd -p 9001 ./codebreaker

# docker build -t codebreaker .
# docker run -dp 9001:9001 -it codebreaker
