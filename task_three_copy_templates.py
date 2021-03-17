import os
from shutil import copytree

project_dir = "my_project"
templates_dir = "templates"

try:
    """
    В задаче 2 создан каталог с подкаталогами и файлами my_project.
    В подкаталогах есть папки и файлы шаблонов *.html.
    В результате работы этой программы, в каталоге my_project будет создан каталог templates,
    куда будут скопированы файлы шаблонов.
    """
    for root, dirs, files in os.walk(project_dir):
        if root.find(templates_dir) > 0 and len(files) == 0:
            copytree(os.path.join(root), os.path.join(project_dir, templates_dir), dirs_exist_ok=True)

except Exception as e:
    print(f"Global error : {e}")