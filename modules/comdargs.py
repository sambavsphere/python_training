import sys
arguments = sys.argv
req_args = arguments[1:]
req_args = map(int,req_args)
#req_args = [int(i) for i in req_args]
print sum(req_args)

