# Abstração

from abc import ABC, ABCMeta, abstractmethod

# class Log(metaclass=ABCMeta):

class Log(ABC):

    @abstractmethod
    def _log(self, msg): ...
    
    def log_error(self, msg):
        return self._log(f'Erro: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Sucesso: {msg}')
 

class LogPrintMixin(Log):

    def _log(self, msg):
        print(f'<<LOG>> {msg} {self.__class__.__name__}')


if __name__ == '__main__':
    l = LogPrintMixin()

    l.log_error('oi')