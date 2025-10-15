# Codeworks

Our developers has made this new project, could you check if everything is safe?

[⬇️ codeproject.zip](./codeproject.zip)

# Writeup

Saw quickly this was a git repository, so I extracted the zip file and checked the git log:

```bash
$ git log
commit 59aefc3b732644ee0ae7ca965100656eaea9173e (HEAD -> main, origin/main, origin/HEAD)
Author: Daniel Christensen <danchrist@hotmail.no>
Date:   Thu Oct 13 10:31:08 2022 +0200

    Removed secret

commit eb5cd22a8f392b56312b459d3cb2bfaafa53bf94
Author: Daniel Christensen <danchrist@hotmail.no>
Date:   Thu Oct 13 10:29:10 2022 +0200

    First commit
```

Checked out the first commit and there was a `.env` file containing the flag.