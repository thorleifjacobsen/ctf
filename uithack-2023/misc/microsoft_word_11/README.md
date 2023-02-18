# Microsoft Word 1.1!

You can now get the new Microsoft Word 1.1! It has all the features you need, and more for only 498$!
In the dark ages of computer word processing, what you wrote (and saw on the screen, if you had one) was cryptic formatting commands embedded within the text, like this:
.nf
.ll 4.0i
.in 2.0i
101 Main Street
Morristown, NJ 07960
15 March, 1997
.sp 1i
.in 0
Dear Sir,
.fi
.ti 0.25i
I just wanted to drop you a note to thank you…

After "compiling" and printing, you finally saw the result – which often wasn’t what you wanted. Make changes. Try again.
But not anymore, and for only 498$ you can get the new Microsoft Word 1.1!
Try the free 23-day trial of our free-version!

Download

# Writeup

Looking around this is a git repository.

```
$ ls -lah
total 24K
drwxrwxr-x  4 toffe toffe 4.0K Dec 15 21:47 .
drwxr-xr-x  3 toffe toffe 4.0K Feb 18 02:12 ..
drwxrwxr-x  8 toffe toffe 4.0K Dec 15 21:37 .git
drwxrwxr-x 16 toffe toffe  12K Dec 15 21:37 word1.1
```

Running `git log` show that Bill Gates loves his commits. Using `git log -s` I can search for commits with a given text. So:

```
$ git log -S UiTHack
commit b7be4e200923494ac092dec1492c74e6b1ad6936
Author: Bill Gates <Bill@MS.com>
Date:   Thu Jan 25 21:23:07 1990 +0100

    Common flags
```

This seems to simple. 

```
└─$ git --no-pager show b7be4e200923494ac092dec1492c74e6b1ad6936 | head -n 20
commit b7be4e200923494ac092dec1492c74e6b1ad6936
Author: Bill Gates <Bill@MS.com>
Date:   Thu Jan 25 21:23:07 1990 +0100

    Common flags

diff --git a/src/RAREFLAG.H b/src/RAREFLAG.H
index 71a3847..d147021 100644
--- a/src/RAREFLAG.H
+++ b/src/RAREFLAG.H
@@ -34,6 +34,8 @@ struct RF {   /* Rare flag */
        int fInDyadic: 1;
        int fExtendedMemory: 1;
        int fInDisplayFli : 1;  /* Flag to avoid recursion */
+       int UiTHack23: 1;       /* Did you really think you could grep the flag */
+       int rot : 13;   /* I'll at least give you a hint till you find it ;) */

.... LOTS MORE DATA ...
```

So the two lines I care about here is: 

```
int UiTHack23: 1;       /* Did you really think you could grep the flag */
int rot : 13;   /* I'll at least give you a hint till you find it ;) */
```

So I need to search for the rotated one? `HvGUnpx`


```
└─$ git log -S HvGUnpx
commit 27b60f0f1dcd3d4fd63a206a5b8f8b51a210d53b
Author: Bill Gates <Bill@MS.com>
Date:   Wed Jun 15 22:18:21 1988 +0200

    Removing credentials from enterprice version

commit d6cc5a03e6e88c16fd0ba2167d7e9918a660ff11
Author: Bill Gates <Bill@MS.com>
Date:   Mon May 16 22:18:08 1988 +0200

    add help feature for enduser
```

Guessing this was removed in the second commit and the first one is where it is I'll show that commit, even though both would have shown it when I think about it. Oh well:

```bash
$ git show d6cc5a03e6e88c16fd0ba2167d7e9918a660ff11 
commit d6cc5a03e6e88c16fd0ba2167d7e9918a660ff11
Author: Bill Gates <Bill@MS.com>
Date:   Mon May 16 22:18:08 1988 +0200

    add help feature for enduser

diff --git a/src/CREDENTIALS b/src/CREDENTIALS
new file mode 100644
index 0000000..1547c05
--- /dev/null
+++ b/src/CREDENTIALS
@@ -0,0 +1 @@
+HvGUnpx23{jbeq1.1_npghnyyl_pbfg_498$_va_1990!}


.... LOTS MORE DATA ...
```

Flag rotated 13 times back became:

 ```
 UiTHack23{word1.1_actually_cost_498$_in_1990!}
 ```