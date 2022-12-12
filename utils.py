# Модуль функций
import os
import re
from typing import Iterable, Iterator, Any, List, Pattern, Optional, Callable

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DATA_DIR = os.path.join(BASE_DIR, "data\\")
DATA_DIR = './data/'


def filter_query(param: str, data: Iterable[str]) -> List[str]:
    return list(filter(lambda row: param in row, data))


def map_query(param: str, data: Iterable[str]) -> List[str]:
    col_number: int = int(param)
    return list(map(lambda row: row.split(' ')[col_number], data))


def unique_query(data: Iterable[str], *args: Any, **kwargs: Any) -> List[str]:
    return list(set(data))
    # result = []
    # for row in data:
    #     if row not in result:
    #         result.append(row)
    # return result


def sort_query(param: str, data: Iterable[str]) -> List[str]:
    reverse: bool = False if param == 'asc' else True
    return sorted(data, reverse=reverse)


def limit_query(param: str, data: List[str]) -> List[str]:
    limit: int = int(param)
    return list(data[:limit])


def regex_query(param: str, data: Iterable[str]) -> Iterator[str]:
    regex: Pattern[str] = re.compile(param)
    return filter(lambda x: re.search(regex, x), data)


def check_param(param: dict) -> bool:
    """Функция проверки параметров и наличия файла"""
    valid_keys: list = ['file_name', 'cmd1', 'value1', 'cmd2', 'value2']
    for key in param.keys():
        if key not in valid_keys:
            return False

    valid_cmd_commands: list = ['filter', 'map', 'sort', 'unique', 'limit', 'regex']
    if param.get('cmd1', 'none') not in valid_cmd_commands or param.get('cmd2', 'none') not in valid_cmd_commands:
        return False

    file_name: Optional[Any] = param.get('file_name')
    if file_name is None:
        return False
    full_name: str = DATA_DIR + file_name
    # full_name: str = './data/' + file_name
    if not os.path.exists(full_name):
        return False

    return True


CMD_TO_FUNCTION: dict[str, Callable] = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query,
    'regex': regex_query
}


def build_query(cmd: str, param: str, file_name: str, data: Optional[Iterable[str]]) -> Optional[Any]:
    if not data:
        file_name = DATA_DIR + file_name
        with open(file_name) as file:
            data = list(map(lambda row: row.strip(' '), file))
    return CMD_TO_FUNCTION[cmd](param=param, data=data)
