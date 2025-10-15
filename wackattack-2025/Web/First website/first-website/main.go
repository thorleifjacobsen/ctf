package main

import (
	"log"
	"net/http"
	"os"
	"path/filepath"
)

var FLAG = "wack{}"

func main() {
	dir, _ := os.Getwd()
	fs := http.FileServer(http.Dir(dir))
	mux := http.NewServeMux()

	mux.HandleFunc("GET /", func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path == "/" {
			http.ServeFile(w, r, filepath.Join(dir, "index.html"))
			return
		}
		http.StripPrefix("/", fs).ServeHTTP(w, r)
	})

	log.Fatal(http.ListenAndServe(":8080", mux))
}
