#building a currency convertor
import argparse 

parser = argparse.ArgumentParser(description="calculate curecny exchange ")
parser.add_argument('amount', type=int, help="enter the amount to be converted")
parser.add_argument('rate', type=int, help="enter the exchange rate")
parser.add_argument('--v', "--verbosity", help="Provide exchanged amount in sentence", action="store_true")


args = parser.parse_args()
a = (args.amount)
b = (args.rate)
answer = (args.amount * args.rate)
if args.v:
	print(a, "exchanged at rate", b,  "is", answer, "in the local currency")
else:
	print(answer)