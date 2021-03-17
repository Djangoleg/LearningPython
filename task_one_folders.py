import os

"""
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
"""
direct_dict = {"my_project": ["settings", "mainapp", "adminapp", "authapp"]}

for k, v in direct_dict.items():
    for d in v:
        dir_path = os.path.join(k, d)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

