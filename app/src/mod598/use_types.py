from typing import Dict, Union, NewType, List

# Alias
MeuDict = Dict[str, Union[str, int, List[int]]]
pessoa_M: MeuDict = {'nome': 'Antonio', 'sobrenome': 'Junior', 'idade' : 38, 'l': [1, 2]}

# Tipo personalizado
UserId = NewType('UserId', int)
user_id = UserId(12345)