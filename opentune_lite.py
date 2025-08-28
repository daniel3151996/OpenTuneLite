import json
import os

def load_definition(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def main():
    print("=== OpenTune Lite ===")
    defs_dir = os.path.join(os.path.dirname(__file__), "defs")
    for f in os.listdir(defs_dir):
        if f.endswith(".json"):
            print(f"Loaded DEF: {f}")
    print("Program ready. Future versions will support editing, logging, and flashing.")

if __name__ == "__main__":
    main()
