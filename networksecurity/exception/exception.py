import sys
#sys is used to extract detailed Exception information

from networksecurity.logging import logger


class NetworkSecurityException(Exception):
#The class inherits from Exception so it behaves like a normal Python exception.
#you are explicitly inheriting from Python’s built-in Exception class.

#Exception, ValueError, TypeError, etc classes come from the "builtins" module, which is always available automatically.


    def __init__(self,error_message,error_details:sys):
        #error_message: the original error (e.g., ZeroDivisionError message).
        #error_details:sys:  passed the sys module itself so that sys.exc_info() can be called. that is error_details.exec_info()

        self.error_message = error_message
        #error_message: the original error (e.g., ZeroDivisionError message).
        
        _,_,exc_tb = error_details.exc_info() #_ and _ are ignored placeholders for type & value.

        
        #error_details.exc_info() / (sys.exc_info()) → returns a tuple ((exc_type, exc_value, exc_tb)) of the most recent exception.
        #which is:
        
        #      1) exc_type → the exception class (e.g., <class 'ZeroDivisionError'>)
        #      2) exc_value → the actual exception instance (e.g., ZeroDivisionError('division by zero'))
        #      3) exc_tb → the traceback object, it extracts:
        #                a) tb_lineno                       → the exact line number in code where the error happened.
        #                b) tb_frame.f_code.co_filename     → the file name where the error occurred.
        #                c) exc_tb.tb_frame.f_code.co_name  → the function name where the error occurred.

        
        
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename 
        
        

    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))
        #When you print the exception, you get a nice readable error message with:file name,line number,error message

if __name__=='__main__':
    try:
        logger.logging.info("Entering the try block")
        a=1/0
        print("This will not be printed",a)
    except Exception as e:
           raise NetworkSecurityException(e,sys)
    