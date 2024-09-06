from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()

# splitlines() постросно сохраняет весь контент в список
# lines = content.replace('Python', 'Java').splitlines()

def recreate_content():
    for line in content.replace('Python', 'Java').splitlines():
        print(line)

recreate_content()
print(content)
