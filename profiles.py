from pathlib import Path
import json
PROFILES_DIR = Path("profiles")
PROFILES_DIR.mkdir(exist_ok=True)


def get_profiles():
    profiles_list = []

    for profile in PROFILES_DIR.iterdir():
        if profile.suffix == ".json":
            profiles_list.append(profile.stem)

    return profiles_list

def save_profile(profile_name, data):
    path = PROFILES_DIR / f"{profile_name}.json" 
    
    with open (path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        
        
def load_profile(profile_name):
    path = PROFILES_DIR / f"{profile_name}.json"
    with open (path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data