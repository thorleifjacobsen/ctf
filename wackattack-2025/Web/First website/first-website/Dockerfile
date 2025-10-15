FROM golang:tip-trixie

WORKDIR /

COPY . .

ARG FLAG="wack{}"
RUN go build -ldflags "-X main.FLAG=${FLAG}" -o server main.go

EXPOSE 8080

CMD ["./server"]