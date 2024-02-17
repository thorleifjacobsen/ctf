FROM node:10.19.0
LABEL Description="UiTHack24 Space traversal"
EXPOSE 8001

RUN useradd -d /home/ctf -m -p ctf -s /bin/bash ctf
WORKDIR /home/ctf

COPY ["app.js", "flag.txt", "/home/ctf/"]
COPY ["static/", "/home/ctf/static/"]

USER ctf
WORKDIR /home/ctf

RUN npm install express
CMD ["node", "app.js"]

# docker build -t space_traversal .
# docker run -dp 8001:8001 -it --rm space_traversal
