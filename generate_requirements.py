def parse_pyproject_toml(pyproject_path='pyproject.toml'):
    dependencies = []
    with open(pyproject_path, 'r') as file:
        in_dependencies = False
        for line in file:
            line = line.strip()
            if line == "dependencies = [":
                in_dependencies = True
            elif in_dependencies and line == "]":
                break
            elif in_dependencies:
                # Remove quotes and comma, then strip whitespace
                dependency = line.replace('"', '').replace(',', '').strip()
                dependencies.append(dependency)
    return dependencies

def write_requirements_txt(dependencies, requirements_path='requirements.txt'):
    with open(requirements_path, 'w') as file:
        for dependency in dependencies:
            file.write(f"{dependency}\n")
    print(f"Requirements written to {requirements_path}")

if __name__ == '__main__':
    dependencies = parse_pyproject_toml()
    write_requirements_txt(dependencies)
