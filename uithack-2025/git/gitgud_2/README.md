# gitgud_2

Our AI has been acting up lately. Apparently, it has been inserting wierd symbols and leaking secrets all over the codebase. And of course, our unpaid interns are unable to find them, kids these days *sigh*. Can you help us find all the secrets? You might have to clean them up a bit before you can extract them. PS: pls dont tell the boss, he loves that AI and will blame us for everything.

*Note: All flags can be found in the same repo. You can download the repo from gitgud_1.* *There is a dedicated flag for each gitgud challenge, the last number in the flag is the challenge number.*


# Writeup

I started by listing the Git tags to search for hidden clues:

```bash
$ git tag -l
secret-flag
```

I noticed a tag named "secret-flag". I then inspected its contents using `git show secret-flag`

```bash
tag secret-flag
Tagger: gitgod <UiTHack25-ai@example.com>
Date:   Wed Feb 19 17:23:13 2025 +0000

\U|i/T\H|a/c\k|2/5{aR3_7h3r3_07H3r_74G5_Th4n_l47357?_2}

commit 48316406818b5192361a974cde163a1e9c58468f
Author: gitgod <UiTHack25-ai@example.com>
Date:   Wed Feb 19 17:23:13 2025 +0000

    Init AI

diff --git a/requirements.txt b/requirements.txt
new file mode 100755
index 0000000..cce4075
--- /dev/null
+++ b/requirements.txt
@@ -0,0 +1,2 @@
+langchain==0.1.20
+langchain-openai==0.1.6
diff --git a/src/__init__.py b/src/__init__.py
new file mode 100755
index 0000000..e69de29
diff --git a/src/chat.py b/src/chat.py
new file mode 100755
index 0000000..4aca4a0
--- /dev/null
+++ b/src/chat.py
@@ -0,0 +1,56 @@
+from abc import abstractmethod
+from pathlib import Path
+from langchain_core.messages.base import BaseMessage
+from langchain_openai.chat_models import AzureChatOpenAI
+
+KEY_PATH = "C:\\Windows\\users\\me\\Documents\\myproject\\"
+
+API_KEY = None
+API_VERSION = "2024-02-01"  # https://learn.microsoft.com/en-us/azure/ai-services/openai/reference
+ENDPOINT = "https://gpt-course.openai.azure.com/"
+DEPLOYMENT_NAME = "gpt-35"
+
+
+def init_agent() -> AzureChatOpenAI:
+    global API_KEY
+
+    with open(KEY_PATH + "gpt_key.txt") as file:
+        API_KEY = file.read().strip()
+
+    agent = AzureChatOpenAI(
+        api_key=API_KEY,
+        api_version=API_VERSION,
+        azure_endpoint=ENDPOINT,
+        deployment_name=DEPLOYMENT_NAME,
+    )
+
+    return agent
+
+
+class AbstractLLM:
+    @abstractmethod
+    def invoke(self, query: str, **kwargs) -> str | list[str | dict]:
+        pass
+
+
+class LLM(AbstractLLM):
+    def __init__(self) -> None:
+        self.agent = init_agent()
+
+    def invoke(self, query: str, **kwargs) -> str | list[str | dict]:
+        """query the llm and get a response"""
+        query = (
+            """Imagine you are a superpowerfull AI that
+            are much better than all other LLM's"
+            answear this query perfectly: """
+            + query
+        )
+
+        response = self.agent.invoke(query, **kwargs).content
+
+        return response
+
+
+if __name__ == "__main__":
+    agent = LLM()
+    print(agent.invoke("Hello, how are you?"))
```

The output revealed an obfuscated flag:

```
\U|i/T\H|a/c\k|2/5{aR3_7h3r3_07H3r_74G5_Th4n_l47357?_2}
```

After cleaning up the text, I obtained the second flag.

# Flag

```
UiTHack25{aR3_7h3r3_07H3r_74G5_Th4n_l47357?_2}
```