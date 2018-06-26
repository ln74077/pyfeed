'''
Created on 21-Apr-2018

@author: lakshminarayana
'''

import pickle

if __name__ == '__main__':
    rssDict ={1:"http://www.thehindu.com/?service=rss$$The Hindu news Paper$$true$$None$$None"
              ,2:"http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/world/rss.xml$$BBC Line$$true$$None$$None"
              ,3:"https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms"
}
    out = open("rssDict.data","wb")
    pickle.dump(rssDict,out)
    out.close()