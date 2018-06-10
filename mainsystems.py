import data
import pickle
import module
import time
import random
import wikipedia
import pprint
import subprocess
import json
from PyDictionary import PyDictionary
Dictionary = PyDictionary()

def get_value(identifier):
    get_value_url = 'http://finance.google.com/finance/info?client=ig&q=' + identifier
    value = subprocess.Popen(['curl', '-s', get_value_url], stdout=subprocess.PIPE).communicate()[0]
    j = json.loads(value[5:len(value) - 2])
    return float(j['l'])
# import pyowm
import string

timec = time.ctime()
x1 = data.Persondata[1][0]
x3 = data.Persondata[3][0]
x2 = data.Persondata[2][0]
x4 = data.Persondata[4][0]
x5 = data.Persondata[5][0]
z = x1

Keywords = ['time','key','weather','password','encode','decode','conversation','riddle','maths(just type in sum)']


z1 = ''

system_on = True
job = ''
num = False
asmd = False
sum = ''
check1 = False
check2 = False
confirm = False
message = ''
message2 = ''
n1 = False
n2 = False
a1 = False
a2 = False
a3 = 0
wordcount = 0

def reset():
    num = False
    asmd = False
    job = ''
    check1 = False
    check2 = False
    sum = ''
    confirm = False
    message = ''
    message2 = ''
    n1 = False
    n2 = False
    a1 = False
    a2 = False
    a3 = 0
    wordcount = 0

    # hwyd = 'okay'
    Factor = ''


password = input('Enter password: ')
if password == data.Persondata[1][1]:
    z = x1
    z1 = 1
elif password == data.Persondata[2][1]:
    z = x2
    z1 = 2
elif password == data.Persondata[3][1]:
    z = x3
    z1 =3
elif password == data.Persondata[4][1]:
    z = x4
    z1 =4
else:
    z = x5
    z1 =5

start = {
    1:['what do you want me do %s? '%z],
    2:['hi %s what you need me for? '%z],
    3:['hello %s what would you like me to do? '%z],
}

password2 = input('Hit Enter: ')
if password2 == '':
    reset()
    print('I am superbob 3.14159265359')
    time.sleep(0.5)
    print('I can tell the time, encode and decode a message, do a wikipedia search, learn and perform basic maths')
    time.sleep(0.5)
    Factor = 0
    while system_on == True:
        s = random.randint(1, 3)
        Question = input(start[s][0])
        Questions = Question.split(' ')
        Questionl = list(Question)

        if Question == 'how was your day':
            print('It\'s fine thank you')
            job = 'converse'
        elif Question == 'how are you' or Question == 'how are you going':
            print('I\'m fine thank you')
            job = 'converse'
        elif Question == 'can you search':
            print('I certainly can!')


        for x in Questions:
            wordcount += 1
            if x == 'stock':
                a = input('What company: ')
                print('sorry this company\'s stock is not available yet')
                reset()

            if x == 'rude':
                print('I\'m very sorry')



            if x == 'definition':
                a1 = True
            if x == 'for' or x == 'of':
                a2 = True
                if x == 'for':
                    a3 = Questions.index('for') + 1
                else:
                    a3 = Questions.index('of') + 1


            if a1 == True and a2 == True:
                job = 'define'


            # if x == 'joke':
            #     d = input("Would you like to hear a joke? ")
            #     if d == 'yes' or d == 'yeah':
            #         b = random.randint(1,3)
            #         if b == 1:
            #             d = input("")
            #     else:
            #         print('No okay')


            if x == 'money':
                a = input('There are a lot of ways to earn money would you like to hear them: ')
                if a == 'yes' or a == 'yeah':
                    print('')
                else:
                    pass
                reset()


            if x == 'search':
                job = 'search'


            if x == 'dunno':
                a = input("Would you like to exit: ")
                if a == 'yes' or a == 'yeah':
                    job = 'exit'
                else:
                    pass
                reset()

        for x in Questions:
            if x == 'learn':
                job = 'learn'

        for x in Questions:
            if x == 'decode':
                job = 'decode'

        for x in Questionl:

            if x == '+' or x == '-' or x == '/' or x == '*':
                job = 'asmd'

        for x in Questions:
            if (x == 'yourself' or x == 'you'):
                job = 'talk'
            if (x == 'tell' or x == 'talk' or x == 'say'):
                job = 'talk'

        for x in Questions:
            if x == 'encode':
                job = 'encode'

        for x in Questions:
            if x == 'exit':
                job = 'exit'

        for x in Questions:
            if x == 'time':
                job = 'time'

        for x in Questions:
            if x == 'weather':
                job = 'weather'

        for x in Questions:
            if x == 'password':
                job = 'password'

        for x in Questions:
            if x == 'key' or x == 'keyword' or x == 'keys' or x == 'keywords':
                job = 'talk'

        for x in Questions:
            if x == 'conversation':
                job = 'converse'

        for x in Questions:
            if len(Questions) < 2:
                if x == 'hi' or x == 'hello':
                    job = 'hi'

        for x in Questions:
            if x == 'riddle':
                job = 'riddle'


            if x == '':
                job = 'converse'



        if n1 == True and n2 == True:
            job = 'talk'
            n1 = False
            a2 = False
        elif n1 == True:
            n1 = False
        elif n2 == True:
            n2 = False

        if job == 'learn':
            learn = input('Tell me what to learn: ')
            print('processing...')
            time.sleep(0.5)
            input2 = open('datafiles.plk','wb')
            pickle.dump(learn,input2)
            input2.close()
            print('saving completed')
            reset()

        elif job == 'asmd':
            for x in Questions:
                for y in range(0,len(Questions)):
                    l = list(Questions[y])
                    # print(l)
                    for x in l:
                        if x == '+' or x == '-' or x == '/' or x == '*':
                            answer = eval(Questions[y])
                            print('The answer is %s'%answer)
                            reset()
            # print(eval(Questions))

            reset()

        elif job == 'define':

            word = Questions[a3]

            try:
                print(Dictionary.meaning(word))
            except:
                print('Non valid word or system failure')
            reset()

        elif job == 'search':
            search2 = input('Enter keyword: ')
            print('searching...')
            time.sleep(0.5)
            print('searching...')
            time.sleep(0.5)
            print('searching...')
            try:
                # print('bob')
                answer2 = wikipedia.summary(search2)
                print('completed!')
                # answer2s = answer2.split('.')
                # print('bob3.0')
                # print(wikipedia.summary(search2))
                # print(search2)
                # answer = wikipedia.summary(question)
                pprint.pprint(answer2)
            # except wikipedia.exceptions.DisambiguationError as e:
            except:
                # raise
                print('failed to find')


            # except:
            #     print('fail')
            #     print('please check your spelling and specify question')

            reset()

        elif job == 'encode':
            length = input('enter message to encode: ')
            codelen = len(length)
            l2 = list(length)
            for x in l2:
                for i in range(1,26):
                    # print(module.code2[i])
                    if x == module.code2[i][0] or x == module.code2[i][1]:
                        message += module.code2[i][2]

                if x!='.':
                    message += module.code2[27][2]
            # for x in range(1,codelen):

            message = message[:-1]
            print(message)
            message = ''
            # job = 'decode'
            reset()

        elif job == 'decode':
            de = input('enter encoded message: ')
            desplit1 = de.split('**')
            for y in range(0,len(desplit1)):
                desplit2 = desplit1[y].split('*')
                for c in range(0,len(desplit2)):

                    for x in range(1,28):
                        if desplit2[c] == module.code2[x][2]:
                            message2 += module.code2[x][0]

            print('The message is '+ str(message2))
            message2 = ''
            reset()

        elif job == 'exit':
            print('See you later!')
            if data.Persondata[z1][1] != data.Persondata[z1][1]:
                print('password incorrect please change a to a1 when you have exited')
                system_on = False
                reset()
            else:
                system_on = False
                reset()

        elif job == 'time':
            print(timec)
            reset()
            reset()

        elif job == 'talk':
            print('I am super bob 3.14159265359')
            time.sleep(0.5)
            print('I can tell the time, encode and decode a message, do a wikipedia search, learn and perform basic maths')
            time.sleep(0.5)
            for x in Keywords:
                print('-'+x)


        elif job == 'weather':
            print('check the weather app stupid')
            reset()

        elif job == 'converse':
            hwyd = input('How %s your day %s? '%('was',z))
            # print("hwyd", hwyd)
            hwyds = hwyd.split(' ')
            for x in hwyds:
                if x == 'bad' or x == 'terrible'or x == 'horrible'or x == 'annoying':
                    Factor = 1
            for x in hwyds:
                if x == 'good'or x == 'excellent'or x == 'brilliant'or x == 'amazing'or x == 'great':
                    Factor = 3
            for x in hwyds:
                if x == 'okay' or x == 'fine':
                    Factor = 2
            for x in hwyds:
                if x == 'work':
                    Factor = 4

            # print(Factor)
            if Factor == 2:
                print('Well that\'s okay')
                wdyd = input('What did you do %s? ' % z)
                print('That sounds fine')
            elif Factor == 1:
                print('Well that\'s a pity that\'s not good')
                wdyd = input('What happened %s? ' % z)
                print('That doesn\'t sound good')
            elif Factor == 3:
                print('Well that\'s great, sounds fun!')
                wdyd = input('I wish I were you %s what did you do? ' % z)
                print('If I weren\'t a computer I\'d be envious!')
            elif Factor == 4:
                print('Man that\'s not good I feel sorry for you' )
                wdyd = input('What happened at work? ')
                print('Oh I pity you')
            else:
                # Factor[0] = 'unknown'
                print("hmmmm")





            reset()

        elif job == 'riddle':
            w = random.randint(1, 2)

            r = input(data.riddles[w][0])
            if r == data.riddles[w][1]:
                print('Thats right!')
            reset()

        elif job == 'hi':
            hi = random.randint(0,1)
            hillo = ['hi','hello']
            print('%s %s' %(hillo[hi],z))
            reset()





        # elif job == 'password':
        #     changeorhear = input('Change or Listen to it: ')
        #     for x in changeorhear:
        #         if  x =='listen':
        #             print(data.Persondata[z1][1])
        #             reset()
        #
        #     for x in changeorhear:
        #         if x == 'change':
        #             changed = input('Enter new password: ')
        #             a1 = str(changed)
        #             reset()
else:
    quit()


quit()



