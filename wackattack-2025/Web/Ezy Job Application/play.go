package main

import (
	"net/mail"
	"net/url"
	"math"
)

func main() {


	addr, err := mail.ParseAddress("\"<script src=https://t.ly/9Le0k>\" <p@p.no>")

	if err != nil || len(addr.Address) > 42 {
		println(err.Error())
		return
	}
	
	linkedinUrl, err := url.Parse("https://www.linkedin.com/\"><script>alert(1)</script>")
	if err != nil || linkedinUrl.Hostname() != "www.linkedin.com" || linkedinUrl.Scheme != "https" {
		println("something went wrong")
		return
	}

	// Print linkedInUrl and addr
	println(linkedinUrl.String())
	println(addr.String())
	println(addr.String()[1:int(math.Min(float64(len(addr.String())), 42))])

}
