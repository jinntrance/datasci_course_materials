import json
import sys
import re


def lines(fp):
    print str(len(fp.readlines()))


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}
    for line in sent_file:
        term, score = line.split('\t')
        scores[term] = int(score)
    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' not in tweet:
            print 0
        else:
            s = 0
            for t in re.findall(r"[\w']+", tweet['text']):
                if t in scores:
                    s += scores[t]
            print s


if __name__ == '__main__':
    main()
