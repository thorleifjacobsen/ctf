package main

import (
	"fmt"
	"log"
	"math"
	"net"
	"net/http"
	"net/mail"
	"net/url"
	"os"
	"strconv"
	"text/template"
)

var FLAG = os.Getenv("FLAG")

var registrations = make(map[int]Registration)
var regTmpl = template.Must(template.ParseFiles("templates/registration.html"))

type Registration struct {
	Address  string
	LinkedIn string
}

func registrationHandler(w http.ResponseWriter, r *http.Request) {
	addr, err := mail.ParseAddress(r.FormValue("address"))

	if err != nil || len(addr.Address) > 42 {
		fmt.Fprintf(w, "something went wrong")
		return
	}
	linkedinUrl, err := url.Parse(r.FormValue("linkedin"))
	if err != nil || linkedinUrl.Hostname() != "www.linkedin.com" || linkedinUrl.Scheme != "https" {
		fmt.Fprintf(w, "something went wrong")
		return
	}

	id := len(registrations)
	registrations[id] = Registration{
		Address:  addr.String(),
		LinkedIn: linkedinUrl.String(),
	}

	// simulate that admin looks at your registration
	// cmd := exec.Command("bun", "bot.ts", "--registrationId", fmt.Sprintf("%d", id))
	// err = cmd.Run()
	// if err != nil {
	// 	http.Error(w, err.Error(), http.StatusInternalServerError)
	// 	return
	// }

	w.WriteHeader(http.StatusCreated)
	fmt.Fprintf(w, "Signed up, you are %d in waitlist to get a job!", id)
}

func viewRegistrationHandler(w http.ResponseWriter, r *http.Request) {
	ip, _, err := net.SplitHostPort(r.RemoteAddr)
	if err != nil || ip != "127.0.0.1" {
		http.Error(w, "only admin can look at registration", http.StatusUnauthorized)
		return
	}

	id, _ := strconv.Atoi(r.PathValue("id"))
	registration, exists := registrations[id]
	if !exists {
		http.Error(w, "not found", http.StatusNotFound)
		return
	}

	data := struct {
		Id       int
		Address  string
		LinkedIn string
	}{
		Id:       id,
		Address:  registration.Address[1:int(math.Min(float64(len(registration.Address)), 42))],
		LinkedIn: registration.LinkedIn,
	}

	if err := regTmpl.Execute(w, data); err != nil {
		http.Error(w, "template error", http.StatusInternalServerError)
		return
	}
}

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("POST /register", registrationHandler)
	mux.HandleFunc("GET /admin/registration/{id}", viewRegistrationHandler)
	mux.HandleFunc("GET /admin/flag", getFlagHandler)
	mux.HandleFunc("GET /{$}", func(w http.ResponseWriter, r *http.Request) {
		regTmpl.Execute(w, nil)
	})
	log.Println("Server starting on :8080")
	log.Fatal(http.ListenAndServe(":8080", mux))
}

func getFlagHandler(w http.ResponseWriter, r *http.Request) {
	ip, _, err := net.SplitHostPort(r.RemoteAddr)
	if err != nil || ip != "127.0.0.1" {
		http.Error(w, "only admin can get the flag", http.StatusUnauthorized)
		return
	}

	// HAHAH secure the flag with all means!
	w.Header().Set("Content-Security-Policy", "default-src 'none'; frame-ancestors http://localhost 'self';")
	w.Header().Set("X-Frame-Options", "SAMEORIGIN")
	w.Header().Set("X-Content-Type-Options", "nosniff")
	w.Header().Set("Referrer-Policy", "no-referrer")
	w.Header().Set("Access-Control-Allow-Origin", "http://localhost")
	w.Header().Set("Access-Control-Allow-Credentials", "true")

	w.Write([]byte(FLAG))
}
