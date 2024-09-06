from pathlib import Path

content = "I love programming.\n"
content += "I love creating new games.\n"
content += "I also love working with data.\n"

path = Path('programming.txt')
# path.write_text('I love programming!')
path.write_text(content)