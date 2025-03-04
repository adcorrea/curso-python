from typing import Dict, Union, List, Any

# Dicionários e conjuntos
pessoa: Dict[str, str] = {'nome': 'Antonio', 'sobrenome': 'Junior'}
pessoa_U: Dict[str, Union[str, int]] = {'nome': 'Antonio', 'sobrenome': 'Junior', 'idade' : 38}
pessoa_A: Dict[str, Any] = {'nome': 'Antonio', 'sobrenome': 'Junior', 'idade' : 38}
pessoa_L: Dict[str, Union[str, int, List[int]]] = {'nome': 'Antonio', 'sobrenome': 'Junior', 'idade' : 38, 'l': [1, 2]}