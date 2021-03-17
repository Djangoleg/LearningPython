import yaml
import os

yaml_config_path = "config.yaml"

try:

    def make_path(val, pref=""):
        for dir, path in dict(val).items():
            dir_path = os.path.join(pref, dir)
            os.makedirs(dir_path, exist_ok=True)
            if isinstance(path, dict):
                make_path(path, dir_path)
            else:
                for x in path:
                    if isinstance(x, dict):
                        make_path(x, dir_path)
                    elif isinstance(x, str):
                        with open(os.path.join(dir_path, x), "w") as f:
                            f.write("")


    with open(yaml_config_path, 'r', encoding="utf-8") as yaml_file:
        struct_dic = yaml.safe_load(yaml_file)

    make_path(struct_dic)

except yaml.YAMLError as yaml_exc:
    if hasattr(yaml_exc, 'problem_mark'):
        mark = yaml_exc.problem_mark
    print("Error position: (%s:%s)" % (mark.line + 1, mark.column + 1))

except Exception as e:
    print(f"Global error : {e}")





