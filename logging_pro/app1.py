import logging
logging.basicConfig(filename="log2.txt",level=logging.DEBUG,
	format="%(asctime)s->%(levelname)s->%(message)s")
logging.info("progra started")
a=raw_input("Ente a value:")
b=raw_input("Enter b value:")
logging.debug("a={0}".format(a))
logging.debug("b={0}".format(b))
if not a.isdigit() or not b.isdigit():
	logging.warn(" Given non digits info")
try:
	a=float(a)
	b=float(b)
	res= a/b
	logging.debug("result={0}".format(res))
except Exception as err:
	logging.exception(err)
logging.info("Program ended")