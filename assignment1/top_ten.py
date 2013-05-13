import json
import sys
import re


def lines(fp):
    print str(len(fp.readlines()))


def main():
    tweet_file = open(sys.argv[1])
    tags = {}
    for line in tweet_file:
        tweet = json.loads(line)
        if 'entities' in tweet:
            for t in tweet['entities']['hashtags']:
                print t['text']
                if t['text'] not in tags:
                    tags[t['text']] = 1.0
                else:
                    tags[t['text']] += 1.0
    top = sorted(tags,key=tags.get,reverse=True)
    for i in range(0, 9):
        print top[i], tags[top[i]]


if __name__ == '__main__':
    main()

