import json
import re
import sys
from decimal import Decimal


def lines(fp):
    print str(len(fp.readlines()))


def main():
    tweet_file = open(sys.argv[1])
    public_terms = {}
    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in tweet:
            terms = re.findall(r"[\w']+", tweet['text'])
            for t in terms:
                if t in public_terms:
                    public_terms[t] += 1
                else:
                    public_terms[t] = 1
    s = sum(public_terms.values())
    for t in public_terms.keys():
        v = public_terms[t]*1.0/s
        print t, v

if __name__ == '__main__':
    main()
