FROM node:10.19.0
LABEL Description="UiTHack24 3D Cipher"
EXPOSE 7000

RUN useradd -d /home/ctf -m -p ctf -s /bin/bash ctf
WORKDIR /home/ctf

COPY ["app.js", "/home/ctf/"]
COPY ["static/", "/home/ctf/static/"]

USER ctf
WORKDIR /home/ctf

RUN npm install express
CMD ["node", "app.js"]

# docker build -t rubiks_cube .
# docker run -dp 7000:7000 -it --rm rubiks_cube
