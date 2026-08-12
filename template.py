import os

# Root project name
PROJECT_NAME = "VendorRegistrationAndOnboarding"

# Directory structure
structure = {
    ".": [
        ".env",
        ".env.example",
        ".gitignore",
        "main.py",
        "requirements.txt",
        "dockerfile",
        ".dockerignore",
        "pyproject.toml",
        "README.md",
    ],

    "Config": [
        "Config.yaml",
    ],

    f"src/{PROJECT_NAME}": [
        "__init__.py",
    ],

    f"src/{PROJECT_NAME}/configurations": [
        "__init__.py",
        "configure.py",
        "configuration_manager.py",
    ],

    f"src/{PROJECT_NAME}/Agents": [
        "__init__.py",
    ],

    f"src/{PROJECT_NAME}/Agents/Prompts": [
        "__init__.py",
    ],

    f"src/{PROJECT_NAME}/Agents/agents_dir": [
        "__init__.py",
    ],

    f"src/{PROJECT_NAME}/Agents/tools": [
        "__init__.py",
    ],

    f"src/{PROJECT_NAME}/Agents/formatters": [
        "__init__.py",
    ],

    f"src/{PROJECT_NAME}/Agents/Pipelines": [
        "__init__.py",
    ],

    f"src/{PROJECT_NAME}/utils": [
        "__init__.py",
        "utilities.py",
    ],

    f"src/{PROJECT_NAME}/MongoHandler": [
        "__init__.py",
        "Handler.py",
    ],

    f"src/{PROJECT_NAME}/DTOs": [
        "__init__.py",
    ],

    f"src/{PROJECT_NAME}/Repositories": [
        "__init__.py",
    ],

    f"src/{PROJECT_NAME}/Services": [
        "__init__.py",
    ],

    f"src/{PROJECT_NAME}/Controllers": [
        "__init__.py",
    ],
}


def create_structure():
    for folder, files in structure.items():
        os.makedirs(folder, exist_ok=True)

        for file in files:
            file_path = os.path.join(folder, file)

            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    if file == "__init__.py":
                        f.write("# Package initializer\n")
                    else:
                        f.write("")

    print("✅ Project structure created successfully!")


if __name__ == "__main__":
    create_structure()