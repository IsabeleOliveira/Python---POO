""" Como usar um MIXIN """


class LogMixin:
    @staticmethod
    def write(msg):
        with open('HM_log.py', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_infor(self, msg):
        self.write(f'INFOR: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')
