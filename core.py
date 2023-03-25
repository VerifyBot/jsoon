import _io
import typing

from jsoon.decoder import JsonDecoder
from jsoon.encoder import JsonEncoder


import json

def loads(raw: str) -> typing.Union[dict, list]:
  return JsonDecoder(raw).data

def load(fp: typing.Union[_io.TextIOWrapper, str]):
  """Take a json file and parse it into a python object"""
  if isinstance(fp, str):
    with open(fp, encoding='utf-8') as f:
      raw = f.read()
  else:
    raw = fp.read()

  return loads(raw)


def dumps(obj: typing.Union[dict, list, tuple], indent: int = 2) -> str:
  """Take a python object and return its json raw format"""
  return JsonEncoder(obj, indent).raw


def dump(obj: typing.Union[dict, list, tuple], fp: typing.Union[_io.TextIOWrapper, str], indent: int = 2):
  """Take a python object and dump it into a json file"""
  js = dumps(obj, indent)

  if isinstance(fp, str):
    with open(fp, 'w', encoding='utf-8') as f:
      f.write(js)
  else:
    fp.write(js)


if __name__ == '__main__':
  dump(
    {"name": "היי"},
    "heb.json"
  )
  print(load('heb.json'))