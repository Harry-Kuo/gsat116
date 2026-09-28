"""題庫 YAML 讀寫：多行字串用 | 區塊格式，保留中文與欄位順序。"""
from pathlib import Path

import yaml


class _Dumper(yaml.SafeDumper):
    pass


def _str(dumper, data):
    style = "|" if "\n" in data else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


_Dumper.add_representer(str, _str)


def dump(obj, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    text = yaml.dump(obj, Dumper=_Dumper, allow_unicode=True, sort_keys=False, width=1000)
    Path(path).write_text(text, encoding="utf-8")


def load(path):
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))
