# git Author (488)

pAAskeharen synes git er veldig stas. Han kan se historikk på endringer han har gjort. Han lurer på om noen kan ha kludret til forfatteren på en av endringen

# Writeup

`git log` in the repo shows this author on one of the commits:

```
commit 857c64a3d78b23f2cc0433644ae18372715af450
Author: pAAskeharen <68656c73656374667b6731742e656d41496c7d@pAAskeharen.kyllingland.egg>
Date:   Mon Mar 20 08:06:27 2023 +0100

    håper alle får en god påske
```

`gid diff` on it shows only a letter change. So the Author need to mean something.

`68656c73656374667b6731742e656d41496c7d` is what catches my eye, it seems to be some kind of hex, knowing that `a` is 61, the `h` is at 68. So trying to paste it into [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Hex('None')&input=Njg2NTZjNzM2NTYzNzQ2NjdiNjczMTc0MmU2NTZkNDE0OTZjN2Q) and convert from hex. Voilà

# Flag

```
helsectf{g1t.emAIl}
```