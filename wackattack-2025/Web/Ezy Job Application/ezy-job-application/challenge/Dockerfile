FROM golang:tip-trixie


# Setup puppeteer start
RUN apt-get update

RUN apt-get install -y wget gnupg 
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/googlechrome-linux-keyring.gpg 
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/googlechrome-linux-keyring.gpg] https://dl-ssl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list 
RUN apt-get update 
RUN apt-get install -y google-chrome-stable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-khmeros fonts-freefont-ttf libxss1 dbus dbus-x11 --no-install-recommends 
RUN rm -rf /var/lib/apt/lists/* 

RUN which google-chrome-stable || true

ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true 
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/google-chrome-stable

RUN apt-get update
RUN apt-get install -y unzip
RUN curl -fsSL https://bun.sh/install | bash

ENV BUN_INSTALL="/root/.bun"
ENV PATH=$BUN_INSTALL/bin:$PATH

RUN bun add puppeteer --global
# Setup puppeteer end


# Set the working directory inside the container
WORKDIR /app

# Copy the source code
COPY . .

# Build the Go application
RUN go build -o server main.go

# Expose port 8080
EXPOSE 8080

# Run the server
CMD ["./server"]