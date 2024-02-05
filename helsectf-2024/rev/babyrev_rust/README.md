# babyrev_rust

En babyrev er litt Rust(en) i programmering. Hen har programmet inn et flagg i kildekoden, kompilert det til en binærfil (se vedlagt fil) men har så greid å mistet kildekoden. Om hen bare hadde skrevet ned argumentet. Kan du finne flagget og levere det inn?

Reven har noen vage minner om at det kan være et par hint i filen som kan hjelpe en ivrig REverser i å finne flagget.

[⬇ babyrev_rust](./babyrev_rust)

# Writeup

Started by looking into the decompiler (ghidra), then while doing that I ran ltrace to see where it stops and it seems like the flag is leaked in memcpy calls.

```bash
$ ltrace ./babyrev_rust x
memcpy(0x55a70cb17ba0, "f", )= 0x55a70cb17ba0
memcpy(0x55a70cb17ba1, "", 0)= 0x55a70cb17ba1
memcpy(0x55a70cb17ba1, "a", 1)= 0x55a70cb17ba1
memcpy(0x55a70cb17ba2, "", 0)= 0x55a70cb17ba2
memcpy(0x55a70cb17ba2, "l", 1)= 0x55a70cb17ba2
memcpy(0x55a70cb17ba3, "", 0)= 0x55a70cb17ba3
memcpy(0x55a70cb17ba3, "s", 1)= 0x55a70cb17ba3
memcpy(0x55a70cb17ba4, "", 0)= 0x55a70cb17ba4
memcpy(0x55a70cb17ba4, "e", 1)= 0x55a70cb17ba4
memcpy(0x55a70cb17ba5, "", 0)= 0x55a70cb17ba5
memcpy(0x55a70cb17ba5, "_", 1)= 0x55a70cb17ba5
memcpy(0x55a70cb17ba6, "", 0)= 0x55a70cb17ba6
memcpy(0x55a70cb17ba6, "f", 1)= 0x55a70cb17ba6
memcpy(0x55a70cb17ba7, "", 0)= 0x55a70cb17ba7
memcpy(0x55a70cb17ba7, "l", 1)= 0x55a70cb17ba7
memcpy(0x55a70cb17ba8, "", 0)= 0x55a70cb17ba8
memcpy(0x55a70cb17ba8, "a", 1)= 0x55a70cb17ba8
memcpy(0x55a70cb17ba9, "", 0)= 0x55a70cb17ba9
memcpy(0x55a70cb17ba9, "g", 1)= 0x55a70cb17ba9
memcpy(0x55a70cb17baa, "", 0)= 0x55a70cb17baa
memcpy(0x55a70cb17baa, "s", 1)= 0x55a70cb17baa
memcpy(0x55a70cb17bab, "", 0)= 0x55a70cb17bab
memcpy(0x55a70cb17bab, "_", 1)= 0x55a70cb17bab
memcpy(0x55a70cb17bac, "", 0)= 0x55a70cb17bac
memcpy(0x55a70cb17bac, "a", 1)= 0x55a70cb17bac
memcpy(0x55a70cb17bad, "", 0)= 0x55a70cb17bad
memcpy(0x55a70cb17bad, "r", 1)= 0x55a70cb17bad
memcpy(0x55a70cb17bae, "", 0)= 0x55a70cb17bae
memcpy(0x55a70cb17bae, "e", 1)= 0x55a70cb17bae
memcpy(0x55a70cb17baf, "", 0)= 0x55a70cb17baf
memcpy(0x55a70cb17baf, "_", 1)= 0x55a70cb17baf
memcpy(0x55a70cb17bb0, "", 0)= 0x55a70cb17bb0
memcpy(0x55a70cb17bb0, "n", 1)= 0x55a70cb17bb0
memcpy(0x55a70cb17bb1, "", 0)= 0x55a70cb17bb1
memcpy(0x55a70cb17bb1, "o", 1)= 0x55a70cb17bb1
memcpy(0x55a70cb17bb2, "", 0)= 0x55a70cb17bb2
memcpy(0x55a70cb17bb2, "t", 1)= 0x55a70cb17bb2
memcpy(0x55a70cb17bb3, "", 0)= 0x55a70cb17bb3
memcpy(0x55a70cb17bb3, "_", 1)= 0x55a70cb17bb3
memcpy(0x55a70cb17bb4, "", 0)= 0x55a70cb17bb4
memcpy(0x55a70cb17bb4, "c", 1)= 0x55a70cb17bb4
memcpy(0x55a70cb17bb5, "", 0)= 0x55a70cb17bb5
memcpy(0x55a70cb17bb5, "o", 1)= 0x55a70cb17bb5
memcpy(0x55a70cb17bb6, "", 0)= 0x55a70cb17bb6
memcpy(0x55a70cb17bb6, "o", 1)= 0x55a70cb17bb6
memcpy(0x55a70cb17bb7, "", 0)= 0x55a70cb17bb7
memcpy(0x55a70cb17bb7, "l", 1)= 0x55a70cb17bb7
memcpy(0x55a70cb17bb8, "", 0)= 0x55a70cb17bb8
memcpy(0x55a70cb17bb8, "_", 1)= 0x55a70cb17bb8
memcpy(0x55a70cb17bb9, "", 0)= 0x55a70cb17bb9
memcpy(0x55a70cb17bb9, "t", 1)= 0x55a70cb17bb9
memcpy(0x55a70cb17bba, "", 0)= 0x55a70cb17bba
memcpy(0x55a70cb17bba, "o", 1)= 0x55a70cb17bba
memcpy(0x55a70cb17bbb, "", 0)= 0x55a70cb17bbb
memcpy(0x55a70cb17bbb, "_", 1)= 0x55a70cb17bbb
memcpy(0x55a70cb17bbc, "", 0)= 0x55a70cb17bbc
memcpy(0x55a70cb17bbc, "h", 1)= 0x55a70cb17bbc
memcpy(0x55a70cb17bbd, "", 0)= 0x55a70cb17bbd
memcpy(0x55a70cb17bbd, "u", 1)= 0x55a70cb17bbd
memcpy(0x55a70cb17bbe, "", 0)= 0x55a70cb17bbe
memcpy(0x55a70cb17bbe, "n", 1)= 0x55a70cb17bbe
memcpy(0x55a70cb17bbf, "", 0)= 0x55a70cb17bbf
memcpy(0x55a70cb17bbf, "t", 1)= 0x55a70cb17bbf
memcpy(0x55a70cb17bc0, "", 0)= 0x55a70cb17bc0
memcpy(0x55a70cb17bc0, "_", 1)= 0x55a70cb17bc0
memcpy(0x55a70cb17bc1, "", 0)= 0x55a70cb17bc1
memcpy(0x55a70cb17bc1, "c", 1)= 0x55a70cb17bc1
memcpy(0x55a70cb17bc2, "", 0)= 0x55a70cb17bc2
memcpy(0x55a70cb17bc2, "o", 1)= 0x55a70cb17bc2
memcpy(0x55a70cb17bc3, "", 0)= 0x55a70cb17bc3
memcpy(0x55a70cb17bc3, "r", 1)= 0x55a70cb17bc3
memcpy(0x55a70cb17bc4, "", 0)= 0x55a70cb17bc4
memcpy(0x55a70cb17bc4, "r", 1)= 0x55a70cb17bc4
memcpy(0x55a70cb17bc5, "", 0)= 0x55a70cb17bc5
memcpy(0x55a70cb17bc5, "e", 1)= 0x55a70cb17bc5
memcpy(0x55a70cb17bc6, "", 0)= 0x55a70cb17bc6
memcpy(0x55a70cb17bc6, "c", 1)= 0x55a70cb17bc6
memcpy(0x55a70cb17bc7, "", 0)= 0x55a70cb17bc7
memcpy(0x55a70cb17bc7, "t", 1)= 0x55a70cb17bc7
memcpy(0x55a70cb17bc8, "", 0)= 0x55a70cb17bc8
memcpy(0x55a70cb17bc8, "l", 1)= 0x55a70cb17bc8
memcpy(0x55a70cb17bc9, "", 0)= 0x55a70cb17bc9
memcpy(0x55a70cb17bc9, "y", 1)= 0x55a70cb17bc9
memcpy(0x55a70cb17bca, "", 0)= 0x55a70cb17bca
memcpy(0x55a70cb17bca, " ", 1)= 0x55a70cb17bca
memcpy(0x55a70cb17bcb, "", 0)= 0x55a70cb17bcb
memcpy(0x55a70cb17bcb, " ", 1)= 0x55a70cb17bcb
memcpy(0x55a70cb17cb0, " ", 1)= 0x55a70cb17cb0
memcpy(0x55a70cb17cb1, "", 0)= 0x55a70cb17cb1
memcpy(0x55a70cb17cb1, " ", 1)= 0x55a70cb17cb1
memcpy(0x55a70cb17cb2, "", 0)= 0x55a70cb17cb2
memcpy(0x55a70cb17cb2, "}", 1)= 0x55a70cb17cb2
memcpy(0x55a70cb17cb3, "", 0)= 0x55a70cb17cb3
memcpy(0x55a70cb17cb3, "!", 1)= 0x55a70cb17cb3
memcpy(0x55a70cb17cb4, "", 0)= 0x55a70cb17cb4
memcpy(0x55a70cb17cb4, "g", 1)= 0x55a70cb17cb4
memcpy(0x55a70cb17cb5, "", 0)= 0x55a70cb17cb5
memcpy(0x55a70cb17cb5, "i", 1)= 0x55a70cb17cb5
memcpy(0x55a70cb17cb6, "", 0)= 0x55a70cb17cb6
memcpy(0x55a70cb17cb6, "t", 1)= 0x55a70cb17cb6
memcpy(0x55a70cb17cb7, "", 0)= 0x55a70cb17cb7
memcpy(0x55a70cb17cb7, "k", 1)= 0x55a70cb17cb7
memcpy(0x55a70cb17cb8, "", 0)= 0x55a70cb17cb8
memcpy(0x55a70cb17cb8, "i", 1)= 0x55a70cb17cb8
memcpy(0x55a70cb17cb9, "", 0)= 0x55a70cb17cb9
memcpy(0x55a70cb17cb9, "r", 1)= 0x55a70cb17cb9
memcpy(0x55a70cb17cba, "", 0)= 0x55a70cb17cba
memcpy(0x55a70cb17cba, "_", 1)= 0x55a70cb17cba
memcpy(0x55a70cb17cbb, "", 0)= 0x55a70cb17cbb
memcpy(0x55a70cb17cbb, "t", 1)= 0x55a70cb17cbb
memcpy(0x55a70cb17cbc, "", 0)= 0x55a70cb17cbc
memcpy(0x55a70cb17cbc, "v", 1)= 0x55a70cb17cbc
memcpy(0x55a70cb17cbd, "", 0)= 0x55a70cb17cbd
memcpy(0x55a70cb17cbd, "i", 1)= 0x55a70cb17cbd
memcpy(0x55a70cb17cbe, "", 0)= 0x55a70cb17cbe
memcpy(0x55a70cb17cbe, "t", 1)= 0x55a70cb17cbe
memcpy(0x55a70cb17cbf, "", 0)= 0x55a70cb17cbf
memcpy(0x55a70cb17cbf, "a", 1)= 0x55a70cb17cbf
memcpy(0x55a70cb17cc0, "", 0)= 0x55a70cb17cc0
memcpy(0x55a70cb17cc0, "l", 1)= 0x55a70cb17cc0
memcpy(0x55a70cb17cc1, "", 0)= 0x55a70cb17cc1
memcpy(0x55a70cb17cc1, "e", 1)= 0x55a70cb17cc1
memcpy(0x55a70cb17cc2, "", 0)= 0x55a70cb17cc2
memcpy(0x55a70cb17cc2, "r", 1)= 0x55a70cb17cc2
memcpy(0x55a70cb17cc3, "", 0)= 0x55a70cb17cc3
memcpy(0x55a70cb17cc3, "_", 1)= 0x55a70cb17cc3
memcpy(0x55a70cb17cc4, "", 0)= 0x55a70cb17cc4
memcpy(0x55a70cb17cc4, "r", 1)= 0x55a70cb17cc4
memcpy(0x55a70cb17cc5, "", 0)= 0x55a70cb17cc5
memcpy(0x55a70cb17cc5, "e", 1)= 0x55a70cb17cc5
memcpy(0x55a70cb17cc6, "", 0)= 0x55a70cb17cc6
memcpy(0x55a70cb17cc6, "m", 1)= 0x55a70cb17cc6
memcpy(0x55a70cb17cc7, "", 0)= 0x55a70cb17cc7
memcpy(0x55a70cb17cc7, "i", 1)= 0x55a70cb17cc7
memcpy(0x55a70cb17cc8, "", 0)= 0x55a70cb17cc8
memcpy(0x55a70cb17cc8, "r", 1)= 0x55a70cb17cc8
memcpy(0x55a70cb17cc9, "", 0)= 0x55a70cb17cc9
memcpy(0x55a70cb17cc9, "_", 1)= 0x55a70cb17cc9
memcpy(0x55a70cb17cca, "", 0)= 0x55a70cb17cca
memcpy(0x55a70cb17cca, "t", 1)= 0x55a70cb17cca
memcpy(0x55a70cb17ccb, "", 0)= 0x55a70cb17ccb
memcpy(0x55a70cb17ccb, "s", 1)= 0x55a70cb17ccb
memcpy(0x55a70cb17ccc, "", 0)= 0x55a70cb17ccc
memcpy(0x55a70cb17ccc, "u", 1)= 0x55a70cb17ccc
memcpy(0x55a70cb17ccd, "", 0)= 0x55a70cb17ccd
memcpy(0x55a70cb17ccd, "r", 1)= 0x55a70cb17ccd
memcpy(0x55a70cb17cce, "", 0)= 0x55a70cb17cce
memcpy(0x55a70cb17cce, "_", 1)= 0x55a70cb17cce
memcpy(0x55a70cb17ccf, "", 0)= 0x55a70cb17ccf
memcpy(0x55a70cb17ccf, "k", 1)= 0x55a70cb17ccf
memcpy(0x55a70cb17cd0, "", 0)= 0x55a70cb17cd0
memcpy(0x55a70cb17cd0, "s", 1)= 0x55a70cb17cd0
memcpy(0x55a70cb17cd1, "", 0)= 0x55a70cb17cd1
memcpy(0x55a70cb17cd1, "a", 1)= 0x55a70cb17cd1
memcpy(0x55a70cb17cd2, "", 0)= 0x55a70cb17cd2
memcpy(0x55a70cb17cd2, "r", 1)= 0x55a70cb17cd2
memcpy(0x55a70cb17cd3, "", 0)= 0x55a70cb17cd3
memcpy(0x55a70cb17cd3, "{", 1)= 0x55a70cb17cd3
memcpy(0x55a70cb17cd4, "", 0)= 0x55a70cb17cd4
memcpy(0x55a70cb17cd4, "f", 1)= 0x55a70cb17cd4
memcpy(0x55a70cb17cd5, "", 0)= 0x55a70cb17cd5
memcpy(0x55a70cb17cd5, "t", 1)= 0x55a70cb17cd5
memcpy(0x55a70cb17cd6, "", 0)= 0x55a70cb17cd6
memcpy(0x55a70cb17cd6, "c", 1)= 0x55a70cb17cd6
memcpy(0x55a70cb17cd7, "", 0)= 0x55a70cb17cd7
memcpy(0x55a70cb17cd7, "e", 1)= 0x55a70cb17cd7
memcpy(0x55a70cb17cd8, "", 0)= 0x55a70cb17cd8
memcpy(0x55a70cb17cd8, "s", 1)= 0x55a70cb17cd8
memcpy(0x55a70cb17cd9, "", 0)= 0x55a70cb17cd9
memcpy(0x55a70cb17cd9, "l", 1)= 0x55a70cb17cd9
memcpy(0x55a70cb17cda, "", 0)= 0x55a70cb17cda
memcpy(0x55a70cb17cda, "e", 1)= 0x55a70cb17cda
memcpy(0x55a70cb17cdb, "", 0)= 0x55a70cb17cdb
memcpy(0x55a70cb17cdb, "h", 1)= 0x55a70cb17cdb
De må prøve hardere.
__cxa_finalize(0x55a70bacae90, 2, 0, 1)= 1
+++ exited (status 0) +++
```

Extracting that data with a quick regexp search in vscode gave me this.

```
false_flags_are_not_cool_to_hunt_correctly    }!gitkir_tvitaler_remir_tsur_ksar{ftcesleh
```

Which is the flag reversed. So the flag is: `helsectf{rask_rust_rimer_relativt_riktig!}`

# Flag

```
helsectf{rask_rust_rimer_relativt_riktig!}
```