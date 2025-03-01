# gitgud_1

Our AI has been acting up lately. Apparently, it has been inserting wierd symbols and leaking secrets all over the codebase. And of course, our unpaid interns are unable to find them, kids these days *sigh*. Can you help us find all the secrets? You might have to clean them up a bit before you can extract them. PS: pls dont tell the boss, he loves that AI and will blame us for everything.

*Note: All flags can be found in the repo downloaded from gitgud_1.* *There is a dedicated flag for each gitgud challenge, the last number in the flag is the corresponding challenge number.*

[⬇️ ai.zip](./ai.zip)


# Writeup

Unzipped the file and went into the folder. Started by checking t
I started by exploring deleted files with the command:

```bash
git log --diff-filter=D --name-only --all
```

This revealed the file `secr3t.txt`, which had been deleted in one of the commits.

I checked the contents of `secr3t.txt` in earlier commits:

```bash
$ git log -p -- secr3t.txt
commit 2ba911eb4114bc2f94c8b28dcecad4dfcf63c06b
Author: gitgod <UiTHack25-ai@example.com>
Date:   Wed Feb 19 17:23:13 2025 +0000

    Remove API key

diff --git a/secr3t.txt b/secr3t.txt
deleted file mode 100644
index 8567525..0000000
--- a/secr3t.txt
+++ /dev/null
@@ -1 +0,0 @@
-'U'i'T|H'a'c'k'2'5'{H0w_t0_r3m0V3_S3cr37_fr0m_g1t?_1}

commit e6fd0293b688c071042b5a85b6bcdc9d0a8b3afc
Author: gitgod <UiTHack25-ai@example.com>
Date:   Wed Feb 19 17:23:13 2025 +0000

    Add some very important information

diff --git a/secr3t.txt b/secr3t.txt
new file mode 100644
index 0000000..8567525
--- /dev/null
+++ b/secr3t.txt
@@ -0,0 +1 @@
+'U'i'T|H'a'c'k'2'5'{H0w_t0_r3m0V3_S3cr37_fr0m_g1t?_1}
```

And that shows the flag. 

# Flag

```
UiTHack25{H0w_t0_r3m0V3_S3cr37_fr0m_g1t?_1}
```