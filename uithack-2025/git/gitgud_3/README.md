# gitgud_3

Our AI has been acting up lately. Apparently, it has been inserting wierd symbols and leaking secrets all over the codebase. And of course, our unpaid interns are unable to find them, kids these days *sigh*. Can you help us find all the secrets? You might have to clean them up a bit before you can extract them. PS: pls dont tell the boss, he loves that AI and will blame us for everything.

*Note: All flags can be found in the same repo. You can download the repo from gitgud_1.* *There is a dedicated flag for each gitgud challenge, the last number in the flag is the challenge number.*


# Writeup

I started by checking the file `flag3b.txt`, which contained a fragment of the flag:

```bash
cat flag3b.txt
```

It revealed:

```bash
_t0g3th3r_3}
```

I suspected that the first part of the flag might be somewhere else in the repository, I found the word "Awe5ome" in the file, which seemed like a good candidate for the first half of the flag.

I combined it with the second part:

```
UiTHack25{Awe5ome_t0g3th3r_3}
```

But that didn’t work. I realized that the first part might be stored in a previous commit or branch.

I found a clue in the commit message **"Only halfway there, continue at home"**, which made me investigate the repository deeper. Using the SSH key found in `README.md`, I authenticated to the remote GitHub repository.

After cloning the repository, I checked other branches using `git branch -a` and saw `other-branch`. Once switched the file `flag3.txt` appeared and I had the full flag.

# Flag

```
UiTHack25{L0v3_wh3n_4_pl4n_c0m3s_t0g3th3r_3}
```