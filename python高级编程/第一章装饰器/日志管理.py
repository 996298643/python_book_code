import functools
import time
import logging

def logger(method):

    def inner(*args , **kwargs):


        start = time.time()    #开始时间

        return_value = method(*args, **kwargs)

        end = time.time()      #结束时间

        delta = end - start

        logger = logging.getLogger('decorator.logged')

        logger.warning("call method"+method.__name__+",start time="+str(start)+",end time = "+str(end)+",return_value="+return_value)

        return return_value

    return inner

@logger
def return_value_method(value):
    return str(value)

print(return_value_method(5))