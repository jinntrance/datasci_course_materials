import json
import re
import sys


def lines(fp):
    print str(len(fp.readlines()))


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}
    public_terms = {}
    for line in sent_file:
        term, score = line.split('\t')
        scores[term] = int(score)
    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in tweet:
            s = 0.0
            terms = re.findall(r"[\w']+", tweet['text'])
            size = len(terms)
            for t in terms:
                if t in scores:
                    s += scores[t]
            for t in terms:
                if t not in scores:
                    if t in public_terms:
                        public_terms[t] += s/size
                    else:
                        public_terms[t] = s/size
    max_ratio = 5.0/max(abs(max(public_terms.values())), abs(min(public_terms.values())))
    for t in public_terms.keys():
        v = public_terms[t]*max_ratio
        print t, v


if __name__ == '__main__':
    main()
