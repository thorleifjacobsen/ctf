# Generate directories, readmes, and other assets for CTF challenges

import os
import requests
import sys
import re
from dotenv import load_dotenv
load_dotenv()


def get_env_var(key, prompt, force_new=False):
    if force_new or not os.getenv(key):
        value = input(prompt)
        os.environ[key] = value
        return value
    return os.getenv(key)

force_new = "-n" in sys.argv

API_KEY = get_env_var("API_KEY", "Enter your API key: ", force_new)
BASE_URL = get_env_var("BASE_URL", "Enter the base URL (e.g., https://ctf.example.com): ", force_new)

with open(".env", "w") as f:
    f.write(f"API_KEY={API_KEY}\nBASE_URL={BASE_URL}\n")

HEADERS = {"Authorization": f"Token {API_KEY}", "Content-Type": "application/json"}

def_flag_content = "# Flag\n\n```\nflag{goes_here}\n```"
def_writeup_content = "# Writeup\n\n<Enter writeup here>\n\n"

def get_challenges():
    response = requests.get(f"{BASE_URL}/api/v1/challenges", headers=HEADERS)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print("Failed to retrieve challenges.")
        sys.exit(1)

def get_challenge_details(challenge_id):
    response = requests.get(f"{BASE_URL}/api/v1/challenges/{challenge_id}", headers=HEADERS)
    if response.status_code == 200:
        return response.json().get("data", {})
    else:
        print(f"Failed to retrieve details for challenge {challenge_id}.")
        return None

def download_file(file_url, save_path):
    if os.path.exists(save_path):
        print(f"File already exists, skipping: {save_path}")
        return
    
    response = requests.get(f"{BASE_URL}{file_url}", headers=HEADERS, stream=True)
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
    else:
        print(f"Failed to download file: {file_url}")

def extract_connection_info(connection_info):
    if not connection_info:
        return ""
    
    urls = re.findall(r'https?://\S+', connection_info)
    if urls:
        return "\n".join(f"[🔗 {url}]({url})" for url in urls)
    else:
        return "```\n" + connection_info.strip() + "\n```"

def update_readme(ctf_name, challenges):
    root_readme_path = os.path.join(os.getcwd(), ctf_name, "README.md")
    completed = sum(1 for ch in challenges if ch.get("solved_by_me", False))
    total = len(challenges)
    
    # Preserve existing top section if already modified
    if os.path.exists(root_readme_path):
        with open(root_readme_path, "r") as f:
            old_content = f.read()
        top_section_end = old_content.find("# Challenges")
        if top_section_end != -1:
            top_section = old_content[:top_section_end].strip()
        else:
            top_section = f"# {ctf_name.replace('-', ' ').title()}\n\n<your description here>\n"
    else:
        top_section = f"# {ctf_name.replace('-', ' ').title()}\n\n<your description here>\n"
    
    content = f"{top_section}\n\n# Challenges\n\nProgress: {completed}/{total} completed ({total - completed} left)\n\n"
    
    categories = {}
    for challenge in challenges:
        category = challenge.get("category", "Uncategorized")
        name = challenge.get("name", "Unknown")
        points = challenge.get("value", 0)
        solved = "✅" if challenge.get("solved_by_me", False) else "❌"
        challenge_path = f"{category}/{name}/README.md".replace(" ", "%20")
        
        if category not in categories:
            categories[category] = []
        categories[category].append(f"- {solved} [{name} ({points}p)]({challenge_path})")
    
    for category, tasks in categories.items():
        content += f"## {category}\n\n" + "\n".join(tasks) + "\n\n"
    
    # Add bragshots if images exist
    bragshots = []
    image_files = ["scoreboard.png", "profile.png"]
    for img in image_files:
        img_path = os.path.join(os.getcwd(), ctf_name, img)
        if os.path.exists(img_path):
            bragshots.append(f"![{img}](./{img})")
    
    if bragshots:
        content += "# Bragshots\n\n" + "\n\n".join(bragshots) + "\n\n"
    
    with open(root_readme_path, "w") as f:
        f.write(content)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 crawl.py <ctfname>")
        sys.exit(1)
    
    ctf_name = sys.argv[1]
    base_path = os.path.join(os.getcwd(), ctf_name)
    os.makedirs(base_path, exist_ok=True)
    
    challenges = get_challenges()

    # Find challnege "hackproof banking" and pritn its details only
    # for challenge in challenges:
    #     if challenge.get("name") == "remote":
    #         details = get_challenge_details(challenge.get("id"))
    #         print(details)
    #         break
    # sys.exit(1)
    
    for challenge in challenges:
        category = challenge.get("category", "uncategorized").replace("/", "_")
        name = challenge.get("name", "unknown").replace("/", "_")
        challenge_id = challenge.get("id")
        
        print(f"Processing challenge: {name} ({category})")
        
        challenge_path = os.path.join(base_path, category, name)
        os.makedirs(challenge_path, exist_ok=True)
        
        details = get_challenge_details(challenge_id)
        if not details:
            continue
        
        files = details.get("files", [])
        description = details.get("description", "No description available.").strip()
        connection_info = extract_connection_info(details.get("connection_info", ""))
        readme_path = os.path.join(challenge_path, "README.md")



        # Preserve writeup and flag if already modified
        if os.path.exists(readme_path):
            with open(readme_path, "r") as f:
                old_content = f.read()
            
            writeup_start = old_content.find("# Writeup")
            flag_start = old_content.find("# Flag")
            
            writeup_content = old_content[writeup_start:flag_start] if writeup_start != -1 and flag_start != -1 else def_writeup_content
            flag_content = old_content[flag_start:] if flag_start != -1 else def_flag_content
        else:
            writeup_content = def_writeup_content
            flag_content = def_flag_content
        
        file_info = ""
        for file_url in files:
            filename = file_url.split("/")[-1].split("?")[0]
            file_path = os.path.join(challenge_path, filename)
            if not os.path.exists(file_path):
                download_file(file_url, file_path)
            file_info += f"[⬇️ {filename}](./{filename})\n"

        if connection_info.strip():
            description += "\n\n" + connection_info.strip()
        if file_info.strip():
            description += "\n\n" + file_info.strip()
            
        readme_content = f"# {name}\n\n{description.strip()}\n\n" + writeup_content + flag_content
        
        with open(readme_path, "w") as readme_file:
            readme_file.write(readme_content)
    
    update_readme(ctf_name, challenges)
    
    print(f"CTF challenges saved in: {base_path}")

if __name__ == "__main__":
    main()
