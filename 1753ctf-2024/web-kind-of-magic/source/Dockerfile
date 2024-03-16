FROM archlinux:latest

ARG FLAG

RUN mkdir /app
WORKDIR /app

EXPOSE 1337

RUN pacman --noconfirm -Syu && \
	pacman --noconfirm -S libpng libraqm liblqr libxext fontconfig lcms2 libltdl pkg-config clang rust && \
	curl https://archive.archlinux.org/packages/i/imagemagick/imagemagick-7.1.0.49-1-x86_64.pkg.tar.zst > imagemagick-7.1.0.49.tar.zst && \
	pacman --noconfirm -U imagemagick-7.1.0.49.tar.zst && \
	rm imagemagick-7.1.0.49.tar.zst

RUN echo $FLAG > /flag
ADD src src

RUN cd src && cargo build -r && cp target/release/image_resizer .. && cargo clean

RUN	cp src/Rocket.toml . && ln -s src/static .

CMD ["/app/image_resizer"]
