# Abstração

from pathlib import Path
from datetime import datetime


LOG_FILE = Path(__file__).parent / 'log.log'

class Log:

    def _log(self, msg):
        raise NotImplementedError('Implemente o método Log')
    
    def log_error(self, msg):
        return self._log(f'Erro: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Sucesso: {msg}')
    
    
class LogFileMixin(Log):

    def _log(self, msg):
        f_msg = f'<<LOG>> {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}: {msg}'

        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(f_msg)
            #quebra de linha
            arquivo.write('\n')


class LogPrintMixin(Log):

    def _log(self, msg):
        print(f'<<LOG>> {msg} {self.__class__.__name__}')
    

if __name__ == '__main__':
    l = LogFileMixin()
    l.log_error('Ola')
    l.log_success('Ola')

    l_2 = LogPrintMixin()
    l_2.log_error('Ola')