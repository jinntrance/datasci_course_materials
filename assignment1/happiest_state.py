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
            if 'place' in tweet:
                if tweet['place']:
                    if tweet["place"]["country_code"] == "US":
                        if 'user' in tweet:
                            tweets[tweet['id']] = tweet
                            s = sum([scores[t] for t in re.findall(r"[\w']+", tweet['text']) if t in scores])
                            sid = tweet['place']['full_name'][-2:]
                            if tweet['text'] in states:
                                states[sid] += s
                            else:
                                states[sid] = s
    i = sorted(states, key=states.get, reverse=True)[0]
    print i


if __name__ == '__main__':
    main()
