import requests
import csv
import json

def isCrawl(inf):
  try:
    return 'message' in inf and len(inf['likes']['data']) > 24
  except:
    return False

def extract(inf):
  return [inf['message'],
          requests.get('https://graph.facebook.com/v2.10/%s/likes?access_token=%s&summary=true' % (inf['id'], token)).json()['summary']['total_count'],
          inf['created_time'][:19],
          inf['permalink_url']
          ]

if __name__ == '__main__':
  with open('./config.json') as file:
    config = json.load(file)

    fanpageID = config['fanPageID']
    token = config['token']
    outputFile = config['filename']

  info = []
  res = requests.get('https://graph.facebook.com/v2.10/%s/posts?access_token=%s&pretty=1&fields=message,likes,created_time,permalink_url&limit=100' % (fanpageID, token)).json()
  n = 0

  while 'data' in res:
    info.extend([extract(inf) for inf in res['data'] if isCrawl(inf)])
    try:
      res = requests.get(res['paging']['next']).json()
      n += 1
      print('Finish page %d\r' % n, end = '\r')
    except:
      print('\n')
      break

  info.sort(key = lambda x: -x[1])

  with open(outputFile, 'w') as file:
    w = csv.writer(file)
    for i in info[:config['showNum']]:
      w.writerow(i)
