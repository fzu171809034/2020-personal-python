import json
import argparse
import os


def readjson(addr):
    filelist = os.listdir(addr)
    fp = open('data.json', 'w', encoding='utf-8')
    for file in filelist:
        pathname = addr + '\\' + file
        f = open(pathname,'r',encoding='utf-8')
        for line in f:
            data = json.loads(line)
            fp.write(line)
    fp.close()
    f.close()
    return


def calculate_result(datalist, username, reponame, eventname):
    count = 0
    for da in datalist:
        if len(username) != 0 and len(reponame) == 0:
            if username == da['actor']['login'] and da['type'] == eventname:
                count += 1
            else:
                pass
        elif len(username)==0 and len(reponame) != 0:
            if reponame == da['repo']['name'] and da['type'] == eventname:
                count +=1
            else:
                pass
        elif len(username)!=0 and len(reponame)!=0:
            if username==da['actor']['login'] and reponame==da['repo']['name'] and eventname==da['type']:
                count+=1
        else:
            pass
    print(count)
    return


def main():
    data = []
    username = ''
    reponame = ''
    eventname = ''
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--init', default='')
    parser.add_argument('-u', '--user', default='')
    parser.add_argument('-r', '--repo', default='')
    parser.add_argument('-e', '--event', default='')
    args = parser.parse_args()
    datapath = args.init
    if len(datapath) != 0:
        readjson(datapath)
    username = args.user
    reponame = args.repo
    eventname = args.event
    l = []
    data = open('data.json','r',encoding='utf-8')
    for da in data:
        l.append(json.loads(da))
    calculate_result(l,username,reponame,eventname)


if __name__ == "__main__":
    main()
