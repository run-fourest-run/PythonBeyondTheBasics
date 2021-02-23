

class LoggingContextManager:
    def __enter__(self):
        print('LoggingContextManager.__enter__()')
        return 'your are in a with block!'
    def __exit__(self,exc_type,exc_val, exc_tb):
        if exc_type = None:
            print("LoggingContextManager.__exit__: normal exit detected")

        else:
            print('LoggingContextManager.__exit__: Exception Detected! Type={},Value/Instance={}, traceback = {}'.format(exc_type,exc_val,exc_tb))



if __name__ == "__main__":
    with LoggingContextManager() as x:
        print(x)
