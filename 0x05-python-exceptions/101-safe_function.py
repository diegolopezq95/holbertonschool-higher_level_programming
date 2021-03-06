#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as err:
        sys.stderr.write("Exception: " + str(err) + "\n")
        return None
