import requests
from bs4 import BeautifulSoup
from colorama import Fore
import os
os.system("clear")

def telegram_bot (bot_message) :
    bot_token = 'Bot_Token'
    bot_chatID = 'UID_account'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
    '&parse mode=MarkdownV2&text=' + bot_message
    
    response = requests.get (send_text)
    return response.json()

def ysamm():
    ysamm = requests.get('https://ysamm.com/',headers={"user-agent": "curl/7.79.1"})
    ysamm_soup = BeautifulSoup(ysamm.content, 'html.parser')
    try:
        for i in range(0,10):
            db =[]
            ysamm_link = ysamm_soup.find_all('a',{"class": "more-link"})[i]['href']
            ysamm_title = ysamm_soup.find_all('h2',{"class": "entry-title"})[i].text.split("<h1>")[0].split("</h1>")[0].split("<a>")[0].split("</a>")[0]
            db.append(f"[ysamm.com] : {ysamm_link} : {ysamm_title}")
                    
            with open('/Users/ali/Downloads/My Project/project/python/get write up/db.txt','r+') as f:
                readfile = f.read()
                for line in db:
                    if line in readfile:
                        print(f"{Fore.RED}[ysamm.com]",f"{Fore.YELLOW}[{ysamm_title}]",f"{Fore.GREEN}[{ysamm_link}]",f"{Fore.RED}EXIST")
                        continue
                    else:
                        telegram_bot(f"{ysamm_link}\n{ysamm_title}")
                        print(f"{Fore.BLUE}[ysamm.com]",f"{Fore.YELLOW}[{ysamm_title}]",f"{Fore.GREEN}[{ysamm_link}]",f"{Fore.RED}SUCSSES")
                        f.write(line)
                        f.write('\n')
    except:
        pass

def medium():

    medium_list = [
        "https://medium.com/feed/tag/application-security",
        "https://medium.com/feed/tag/hacking",
        "https://medium.com/feed/tag/infosec",
        "https://medium.com/feed/tag/cybersecurity",
        "https://medium.com/feed/tag/ctf",
        "https://medium.com/feed/tag/penetration-testing",
        "https://medium.com/feed/tag/writeup",
        "https://medium.com/feed/tag/vulnhub",
        "https://medium.com/feed/tag/security",
        "https://medium.com/feed/tag/bug-hunter",
        "https://medium.com/feed/tag/info-sec-writeups",
        "https://medium.com/feed/tag/ethical-hacking",
        "https://medium.com/feed/tag/api-security",
        "https://medium.com/feed/tag/ssrf",
        "https://medium.com/feed/tag/sqli",
        "https://medium.com/feed/tag/sql-injection",
        "https://medium.com/feed/tag/xxe",
        "https://medium.com/feed/tag/cross-site-scripting",
        ]

    db_serch = [
        "application-security",
        "hacking",
        "infosec",
        "cybersecurity",
        "ctf",
        "penetration-testing",
        "writeup",
        "vulnhub",
        "security",
        "bug-hunter",
        "info-sec-writeups",
        "ethical-hacking",
        "api-security",
        "ssrf",
        "sqli",
        "sql-injection",
        "xxe",
        "cross-site-scripting"
        ]

    for url in medium_list:
        try:
            while True:
                db_s = db_serch.pop(0)
                print(db_s)
                break
        except:
            break
        if db_s in url:
            num = 2
            while True:
                db = []
                try:
                    Url = requests.get(url)
                    soup = BeautifulSoup(Url.content, 'html.parser')
                    item = soup.find_all('link')[num]
                    title = soup.find_all('title')[num].text.strip('<title>').strip('</title>')
                    link = item.next_element.strip()
                    num += 1


                    db.append(f"[medioum] : {link} : {title} ")              
                    with open('/Users/alikharrat/Downloads/My Project/project/python/get write up/db.txt','r+') as f:
                        readfile = f.read()
                        for line in db:
                            if line in readfile:
                                continue
                            else:
                                telegram_bot(f"{title}\n{link}")
                                print(f"{Fore.BLUE}[{db_s}]",f"{Fore.YELLOW}[{title}]",f"{Fore.GREEN}[{link}]",f"{Fore.RED}SUCSSES")
                                f.write(line)
                                f.write('\n')
                except:
                    break

def xdavidhume(): 
    xdavidhume = requests.get('https://bugs.xdavidhu.me/', headers={"user-agent": "curl/7.79.1"})
    xdavidhume_soup = BeautifulSoup(xdavidhume.content, 'html.parser')
    for i in range(0,6):
        db =[]
        xdavidhume_link = xdavidhume_soup.find_all('a',{"itemprop": "url"})[i]['href']
        xdavidhume_title = xdavidhume_soup.find_all('p',{"itemprop": "name headline"})[i].text.split("<p>")[0].split("</p>")[0]
        db.append(f"[bug.xdavidhu.me] : https://bugs.xdavidhu.me/{xdavidhume_link} : {xdavidhume_title}")
                
        with open('/Users/alikharrat/Desktop/My Project/python/get write up/db.txt','r+') as f:
            readfile = f.read()
            for line in db:
                if line in readfile:
                    print(f"{Fore.RED}[bug.xdavidhu.me]",f"{Fore.YELLOW}[{xdavidhume_title}]",f"{Fore.GREEN}[{xdavidhume_link}]",f"{Fore.RED}EXIST")
                    continue
                else:
                    telegram_bot(f"{xdavidhume_link}\n{xdavidhume_title}")
                    print(f"{Fore.BLUE}[bug.xdavidhu.me]",f"{Fore.YELLOW}[{xdavidhume_title}]",f"{Fore.GREEN}[{xdavidhume_link}]",f"{Fore.RED}SUCSSES")
                    f.write(line)
                    f.write('\n')

def snowscan(): 
    snowscan = requests.get('https://snowscan.io/feed',headers={"user-agent": "curl/7.79.1"})
    snowscan_soup = BeautifulSoup(snowscan.content, 'html.parser')
    for i in range(2,12):
        db =[]
        snowscan_link = snowscan_soup.find_all('link')[i]["href"]
        snowscan_title = snowscan_soup.find_all('title',{"type":"html"})[i-1].text

        db.append(f"[snowscan.io] : {snowscan_link} : {snowscan_title}")
                    
        with open('/Users/alikharrat/Desktop/My Project/python/get write up/db.txt','r+') as f:
            readfile = f.read()
            for line in db:
                if line in readfile:
                    print(f"{Fore.RED}[snowscan.io]",f"{Fore.YELLOW}[{snowscan_title}]",f"{Fore.GREEN}[{snowscan_link}]",f"{Fore.RED}EXIST")
                    continue
                else:
                    telegram_bot(f"{snowscan_link}\n{snowscan_title}")
                    print(f"{Fore.BLUE}[snowscan.io]",f"{Fore.YELLOW}[{snowscan_title}]",f"{Fore.GREEN}[{snowscan_link}]",f"{Fore.RED}SUCSSES")
                    f.write(line)
                    f.write('\n')

def assetnote():
    assetnote = requests.get('https://blog.assetnote.io/feed.xml',headers={"user-agent": "curl/7.79.1"})
    assetnote_soup = BeautifulSoup(assetnote.content, 'html.parser')
    for i in range(0,10):
        db =[]
        assetnote_link = assetnote_soup.find_all('guid')[i].text
        assetnote_title = assetnote_soup.find_all('title')[i+1].text

        db.append(f"[assetnote.] : {assetnote_link} : {assetnote_title}")
                    
        with open('/Users/alikharrat/Desktop/My Project/python/get write up/db.txt','r+') as f:
            readfile = f.read()
            for line in db:
                if line in readfile:
                    print(f"{Fore.RED}[assetnote]",f"{Fore.YELLOW}[{assetnote_title}]",f"{Fore.GREEN}[{assetnote_link}]",f"{Fore.RED}EXIST")
                    continue
                else:
                    telegram_bot(f"{assetnote_link}\n{assetnote_title}")
                    print(f"{Fore.BLUE}[assetnote]",f"{Fore.YELLOW}[{assetnote_title}]",f"{Fore.GREEN}[{assetnote_link}]",f"{Fore.RED}SUCSSES")
                    f.write(line)
                    f.write('\n')

def omespino():
    omespino = requests.get('https://omespino.com/feed/',headers={"user-agent": "curl/7.79.1"})
    omespino_soup = BeautifulSoup(omespino.content, 'html.parser')
    for i in range(0,10):
        db =[]
        omespino_link = omespino_soup.find_all('comments')[i].text.split("#respond")[0]
        omespino_title = omespino_soup.find_all('title')[i].text

        db.append(f"[omespino] : https://omespino.com{omespino_link} : {omespino_title}")
                    
        with open('/Users/alikharrat/Desktop/My Project/python/get write up/db.txt','r+') as f:
            readfile = f.read()
            for line in db:
                if line in readfile:
                    print(f"{Fore.RED}[omespino]",f"{Fore.YELLOW}[{omespino_title}]",f"{Fore.GREEN}[https://omespino.com{omespino_link}]",f"{Fore.RED}EXIST")
                    continue
                else:
                    telegram_bot(f"{omespino_link}\n{omespino_title}")
                    print(f"{Fore.BLUE}[omespino]",f"{Fore.YELLOW}[{omespino_title}]",f"{Fore.GREEN}[https://omespino.com{omespino_link}]",f"{Fore.RED}SUCSSES")
                    f.write(line)
                    f.write('\n')

def traget():
    url = "https://chaos-data.projectdiscovery.io/index.json"
    json_data = requests.get(url).json()
    i=0
    while True:
        db =[]
        try:
            program_url = json_data[i]['program_url']
            URL = json_data[i]['URL']
            bounty = json_data[i]['bounty']
            last_updated = json_data[i]['last_updated']
            i += 1
            if bounty == True:
                db.append(f"{program_url} : {last_updated} : {URL}")
                with open('/Users/alikharrat/Desktop/My Project/python/get write up/traget.txt','r+') as f:
                    readfile = f.read()
                    for line in db:
                        if line in readfile:
                            print(f"{Fore.RED}[{program_url}]",f"{Fore.YELLOW}[{last_updated}]",f"{Fore.GREEN}[{URL}]",f"{Fore.RED}EXIST")
                            continue
                        else:
                            # telegram_bot(f"{ysamm_link}\n{ysamm_title}")
                            print(f"{Fore.RED}[{program_url}]",f"{Fore.YELLOW}[{last_updated}]",f"{Fore.GREEN}[{URL}]",f"{Fore.RED}SUCSSES")
                            f.write(line)
                            f.write('\n')
            else: 
                continue
        except:
            break

def main():
    print(f'''
{Fore.LIGHTCYAN_EX}1- [ Find new write's up] 
''')

    command = int(input("\t\t\t\t\t\t\t        what do you want to do? "))
    if command == 1 :
        print(f"""
{Fore.LIGHTCYAN_EX}1- [ ysamm ]
{Fore.LIGHTCYAN_EX}2- [ medium ]
{Fore.LIGHTCYAN_EX}3- [ xdavidhume ]
{Fore.LIGHTCYAN_EX}4- [ snowscan ]
{Fore.LIGHTCYAN_EX}5- [ assetnote ]
{Fore.LIGHTCYAN_EX}6- [ omespino ]
        """)
        choose = int(input("choose website:"))
        if choose == 1:
            ysamm()
        elif choose == 2:
            medium()
        elif choose == 3:
            xdavidhume()
        elif choose == 4:
            snowscan()
        elif choose == 5:
            assetnote()
        elif choose == 6:
            omespino
main()