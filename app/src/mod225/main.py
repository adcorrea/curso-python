from utils.log import LogFileMixin, LogPrintMixin


if __name__ == '__main__':
    l = LogFileMixin()
    l.log_error('Ola')
    l.log_success('Ola')

    l_2 = LogPrintMixin()
    l_2.log_error('Ola')