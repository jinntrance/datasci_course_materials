import json
import sys
import re


def lines(fp):
    print str(len(fp.readlines()))


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}
    states = {}
    tweets = {}
    for line in sent_file:
        term, score = line.split('\t')
        scores[term] = int(score)
    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in tweet:
            tweets[tweet['id']] = tweet
            if 'user' in tweet:
                if 'en' == tweet['user']['lang']:
                    s = sum([scores[t] for t in re.findall(r"[\w']+", tweet['text']) if t in scores])
                    if s !=0:
                        if tweet['text'] in states:
                            states[tweet['id']] += s
                        else:
                            states[tweet['id']] = s
    i = sorted(states, key=states.get, reverse=True)[0]
    print tweets[i]['text'][:2]


if __name__ == '__main__':
    main()
