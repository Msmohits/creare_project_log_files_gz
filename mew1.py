import gzip
import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler
from dotenv import load_dotenv

load_dotenv()
file = os.getenv('file')

class GZiprotator:
    def __call__(self,source,dest):
        os.rename(source,dest)
        f_in = open(dest,'rb')
        f_out = gzip.open('%s.gz' % dest, 'wb')
        f_out.writelines(f_in)
        f_out.close()
        f_in.close()
        os.remove(dest)

logging.basicConfig(level=logging.NOTSET)
logger_info = logging.getLogger('info')
logger_debug = logging.getLogger('debug')
logger_warning = logging.getLogger('warning')
logger_error = logging.getLogger('error')
logger_critical =logging.getLogger('critical')
logger_set = logging.getLogger('env')


if file == 'INFO':
    lvl = logging.INFO
    file_name = 'env.log'
    uselvl = logger_set.info
elif file == 'DEBUG':
    lvl = logging.DEBUG
    file_name = 'env.log'
    uselvl = logger_set.debug
elif file =='WARNING':
    lvl = logging.WARNING
    file_name = 'env.log'
    uselvl = logger_set.warning
elif file =='ERROR':
    lvl = logging.ERROR
    file_name = 'env.log'
    uselvl = logger_set.error
elif file =='CRITICAL':
    lvl = logging.CRITICAL
    file_name = 'env.log'
    uselvl = logger_set.critical




file_handler_info = logging.FileHandler('info.log')
file_handler_debug = logging.FileHandler('debug.log')
file_handler_warning = logging.FileHandler('warning.log')
file_handler_error = logging.FileHandler('error.log')
file_handler_critical = logging.StreamHandler(sys.stdout)
file_handler_set = logging.FileHandler(file_name)



file_handler_info.setLevel(logging.INFO)
file_handler_debug.setLevel(logging.DEBUG)
file_handler_warning.setLevel(logging.WARNING)
file_handler_error.setLevel(logging.ERROR)
file_handler_critical.setLevel(logging.CRITICAL)
file_handler_set.setLevel(lvl)

formatter = logging.Formatter( '[%(asctime)s] -  [Log_Level = %(levelname)s]  -  [File_Name = %(filename)s] -  [Func_Name = %(funcName)s] - [Line_No = %(lineno)d] - [Message = %(message)s]')



file_handler_info =TimedRotatingFileHandler(
    'info.log',
    when = 's',
    interval =4,
    backupCount=3,
    )

file_handler_debug =TimedRotatingFileHandler(
    'debug.log',
    when = 's',
    interval =4,
    backupCount=3,
    )

file_handler_warning =TimedRotatingFileHandler(
    'warning.log',
    when = 's',
    interval =4,
    backupCount=3,
    )

file_handler_error =TimedRotatingFileHandler(
    'error.log',
    when = 's',
    interval =4,
    backupCount=3,
    )

file_handler_critical =TimedRotatingFileHandler(
    'critical.log',
    when = 's',
    interval =4,
    backupCount=3,
    )

file_handler_set =TimedRotatingFileHandler(
    'env.log',
    when = 's',
    interval =4,
    backupCount=3,
    )


file_handler_info.setFormatter(formatter)
file_handler_debug.setFormatter(formatter)
file_handler_warning.setFormatter(formatter)
file_handler_error.setFormatter(formatter)
file_handler_critical.setFormatter(formatter)
file_handler_set.setFormatter(formatter)

file_handler_info.rotator = GZiprotator()
file_handler_debug.rotator = GZiprotator()
file_handler_warning.rotator = GZiprotator()
file_handler_error.rotator = GZiprotator()
file_handler_critical.rotator = GZiprotator()
file_handler_set.rotator = GZiprotator()

logger_info.addHandler(file_handler_info)
logger_debug.addHandler(file_handler_debug)
logger_warning.addHandler(file_handler_warning)
logger_error.addHandler(file_handler_error)
logger_critical.addHandler(file_handler_critical)
logger_set.addHandler(file_handler_set)


def func():

    for i in range (1,10000):
        try :
            a = 7
            b = 0
            s = a/i
            # d = a/b
            print(s)

            logger_info.info("file info")
            logger_debug.debug('file debug')
            logger_warning.warning('file warning')
            logger_error.error('file error')
            logger_critical.critical('console error')
            uselvl('evn logs here')


        except:

            return 'error'
        finally:
            pass

func()


