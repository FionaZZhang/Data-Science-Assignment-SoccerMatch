# This file contains code for verifying your solutions
# You must not edit code in this file, or your submission will not work when we attempt to mark it

from assignment1 import *
import os
import sys
import pandas as pd

taskID = sys.argv[1]

def csvVerifier(tasknum, path, answer):
    try:
        taskout = pd.read_csv(path).values.tolist()
        if taskout == answer:
            print('Task ' + tasknum + ' Correct')
        else:
            print('Error in Task ' + tasknum + '.  Program produced:')
            print(taskout)
            print('Expected:')
            print(answer)
    except:
        print('Unable to open ' + path + '.  File may not exist')

def task9verifier(tasknum, path, answer):
    try:
        taskout = pd.read_csv(path).values.tolist()
        taskout = [sorted([sublst[0], sublst[1]]) + [round(sublst[2], 4)] for sublst in taskout]   
        answer = [sorted([sublst[0], sublst[1]]) + [round(sublst[2], 4)] for sublst in answer]
        
        taskout = [sublst for sublst in taskout if sublst[2] < 0.97]
        answer = [sublst for sublst in answer if sublst[2] < 0.97]

        if taskout == answer:
            print('Task ' + tasknum + ' Correct')
        else:
            print('Error in Task ' + tasknum + '.  Program produced:')
            print(taskout)
            print('Expected:')
            print(answer)
    except:
        print('Unable to open ' + path + '.  File may not exist')

def verifytask1():
    task1out = task1()
    answer = ['ARS', 'BHA', 'BOU', 'BUR', 'CAR', 'CHE', 'CRY', 'EVE', 'FUL', 'HUD', 'LEI', 'LIV', 'MCI', 'MUN', 'NEW', 'SOU', 'TOT', 'WAT', 'WHU', 'WOL']
    if task1out == answer:
        print('Task 1 Correct')
    else:
        print('Error in Task 1.  Program produced:')
        print(task1out)
        print('Expected:')
        print(answer)

def verifytask2():
    filename = 'task2.csv'
    if os.path.exists(filename):
        os.remove(filename)
    task2()
    answer = [['ARS', 8, 8], ['BHA', 5, 7], ['BOU', 6, 5], ['BUR', 3, 9], ['CAR', 2, 5], ['CHE', 10, 3], ['CRY', 3, 6], ['EVE', 7, 6], ['FUL', 7, 9], ['HUD', 2, 10], ['LEI', 6, 5], ['LIV', 9, 1], ['MCI', 11, 3], ['MUN', 6, 7], ['NEW', 3, 6], ['SOU', 4, 4], ['TOT', 9, 4], ['WAT', 9, 3], ['WHU', 2, 10], ['WOL', 4, 5]]
    csvVerifier('2', filename, answer)
    
def verifytask3():
    filename = 'task3.csv'
    if os.path.exists(filename):
        os.remove(filename)
    task3()
    answer = [['001.txt', 0], ['002.txt', 3], ['003.txt', 1], ['004.txt', 0], ['005.txt', 0], ['006.txt', 4], ['007.txt', 2], ['008.txt', 0], ['009.txt', 0], ['010.txt', 2], ['011.txt', 3], ['012.txt', 4], ['013.txt', 5], ['014.txt', 5], ['015.txt', 3], ['016.txt', 0], ['017.txt', 1], ['018.txt', 0], ['019.txt', 0], ['020.txt', 0], ['021.txt', 0], ['022.txt', 0], ['023.txt', 0], ['024.txt', 0], ['025.txt', 100], ['026.txt', 4], ['027.txt', 0], ['028.txt', 25], ['029.txt', 0], ['030.txt', 0], ['031.txt', 0], ['032.txt', 3], ['033.txt', 0], ['034.txt', 0], ['035.txt', 1], ['036.txt', 0], ['037.txt', 6], ['038.txt', 1], ['039.txt', 0], ['040.txt', 2], ['041.txt', 7], ['042.txt', 0], ['043.txt', 6], ['044.txt', 0], ['045.txt', 0], ['046.txt', 3], ['047.txt', 0], ['048.txt', 0], ['049.txt', 0], ['050.txt', 6], ['051.txt', 3], ['052.txt', 0], ['053.txt', 3], ['054.txt', 0], ['055.txt', 3], ['056.txt', 3], ['057.txt', 4], ['058.txt', 0], ['059.txt', 5], ['060.txt', 0], ['061.txt', 4], ['062.txt', 0], ['063.txt', 4], ['064.txt', 0], ['065.txt', 3], ['066.txt', 0], ['067.txt', 0], ['068.txt', 0], ['069.txt', 6], ['070.txt', 0], ['071.txt', 5], ['072.txt', 2], ['073.txt', 3], ['074.txt', 0], ['075.txt', 5], ['076.txt', 0], ['077.txt', 3], ['078.txt', 0], ['079.txt', 0], ['080.txt', 0], ['081.txt', 4], ['082.txt', 5], ['083.txt', 5], ['084.txt', 0], ['085.txt', 5], ['086.txt', 3], ['087.txt', 6], ['088.txt', 6], ['089.txt', 0], ['090.txt', 0], ['091.txt', 1], ['092.txt', 0], ['093.txt', 0], ['094.txt', 2], ['095.txt', 0], ['096.txt', 2], ['097.txt', 0], ['098.txt', 1], ['099.txt', 0], ['100.txt', 0], ['101.txt', 0], ['102.txt', 0], ['103.txt', 1], ['104.txt', 0], ['105.txt', 0], ['106.txt', 0], ['107.txt', 0], ['108.txt', 0], ['109.txt', 0], ['110.txt', 0], ['111.txt', 0], ['112.txt', 0], ['113.txt', 0], ['114.txt', 0], ['115.txt', 0], ['116.txt', 0], ['117.txt', 0], ['118.txt', 0], ['119.txt', 0], ['120.txt', 1], ['121.txt', 0], ['122.txt', 2], ['123.txt', 2], ['124.txt', 9], ['125.txt', 55], ['126.txt', 4], ['127.txt', 0], ['128.txt', 2], ['129.txt', 1], ['130.txt', 3], ['131.txt', 4], ['132.txt', 0], ['133.txt', 0], ['134.txt', 0], ['135.txt', 5], ['136.txt', 0], ['137.txt', 0], ['138.txt', 0], ['139.txt', 0], ['140.txt', 3], ['141.txt', 2], ['142.txt', 4], ['143.txt', 6], ['144.txt', 3], ['145.txt', 3], ['146.txt', 0], ['147.txt', 5], ['148.txt', 6], ['149.txt', 4], ['150.txt', 0], ['151.txt', 3], ['152.txt', 0], ['153.txt', 2], ['154.txt', 4], ['155.txt', 0], ['156.txt', 0], ['157.txt', 0], ['158.txt', 4], ['159.txt', 0], ['160.txt', 0], ['161.txt', 4], ['162.txt', 0], ['163.txt', 1], ['164.txt', 1], ['165.txt', 1], ['166.txt', 0], ['167.txt', 0], ['168.txt', 0], ['169.txt', 2], ['170.txt', 3], ['171.txt', 0], ['172.txt', 0], ['173.txt', 0], ['174.txt', 0], ['175.txt', 0], ['176.txt', 1], ['177.txt', 0], ['178.txt', 0], ['179.txt', 0], ['180.txt', 0], ['181.txt', 1], ['182.txt', 0], ['183.txt', 0], ['184.txt', 0], ['185.txt', 0], ['186.txt', 0], ['187.txt', 2], ['188.txt', 1], ['189.txt', 0], ['190.txt', 0], ['191.txt', 0], ['192.txt', 2], ['193.txt', 0], ['194.txt', 0], ['195.txt', 0], ['196.txt', 0], ['197.txt', 0], ['198.txt', 5], ['199.txt', 0], ['200.txt', 0], ['201.txt', 0], ['202.txt', 0], ['203.txt', 0], ['204.txt', 0], ['205.txt', 0], ['206.txt', 21], ['207.txt', 6], ['208.txt', 0], ['209.txt', 0], ['210.txt', 1], ['211.txt', 5], ['212.txt', 18], ['213.txt', 0], ['214.txt', 0], ['215.txt', 0], ['216.txt', 3], ['217.txt', 0], ['218.txt', 0], ['219.txt', 9], ['220.txt', 0], ['221.txt', 0], ['222.txt', 6], ['223.txt', 0], ['224.txt', 4], ['225.txt', 0], ['226.txt', 3], ['227.txt', 0], ['228.txt', 0], ['229.txt', 0], ['230.txt', 0], ['231.txt', 8], ['232.txt', 0], ['233.txt', 0], ['234.txt', 0], ['235.txt', 0], ['236.txt', 0], ['237.txt', 3], ['238.txt', 2], ['239.txt', 0], ['240.txt', 0], ['241.txt', 0], ['242.txt', 0], ['243.txt', 0], ['244.txt', 0], ['245.txt', 4], ['246.txt', 1], ['247.txt', 2], ['248.txt', 0], ['249.txt', 3], ['250.txt', 0], ['251.txt', 0], ['252.txt', 2], ['253.txt', 4], ['254.txt', 0], ['255.txt', 3], ['256.txt', 0], ['257.txt', 0], ['258.txt', 0], ['259.txt', 4], ['260.txt', 2], ['261.txt', 5], ['262.txt', 3], ['263.txt', 6], ['264.txt', 0], ['265.txt', 6]]
    csvVerifier('3', filename, answer)

def verifytask4():
    filename='task4.png'
    if os.path.exists(filename):
        os.remove(filename)
    task4()
    if os.path.exists(filename):
        print('task4.png produced successfully')
    else:
        print('task4.png not produced')

def verifytask5():
    filename='task5.png'
    filename2='task5.csv'
    if os.path.exists(filename):
        os.remove(filename)
    if os.path.exists(filename2):
        os.remove(filename2)
    task5()
    if os.path.exists(filename):
        print('task5.png produced successfully')
    else:
        print('task5.png not produced')
    answer = [['Arsenal', 82], ['Bournemouth', 4], ['Brighton', 1], ['Burnley', 11], ['Cardiff', 11], ['Chelsea', 91], ['Crystal Palace', 7], ['Everton', 31], ['Fulham', 14], ['Huddersfield', 1], ['Leicester City', 2], ['Liverpool', 51], ['Manchester City', 22], ['Manchester United', 69], ['Newcastle United', 4], ['Southampton', 21], ['Tottenham', 22], ['Watford', 2], ['West Ham United', 0], ['Wolverhampton', 1]]
    csvVerifier('5', filename2, answer)

def verifytask6():
    filename='task6.png'
    if os.path.exists(filename):
        os.remove(filename)
    task6()
    if os.path.exists(filename):
        print('task6.png produced successfully')
    else:
        print('task6.png not produced')

def verifytask7():
    filename='task7.png'
    if os.path.exists(filename):
        os.remove(filename)
    task7()
    if os.path.exists(filename):
        print('task7.png produced successfully')
    else:
        print('task7.png not produced')

def verifytask8():
    filename = 'data/football/001.txt'
    taskout = task8(filename)
    answer=['man', 'utd', 'stroll', 'cup', 'win', 'wayne', 'rooney', 'made', 'winning', 'return', 'everton', 'manchester', 'united', 'cruised', 'fa', 'cup', 'quarter', 'finals', 'rooney', 'received', 'hostile', 'reception', 'goals', 'half', 'quinton', 'fortune', 'cristiano', 'ronaldo', 'silenced', 'jeers', 'goodison', 'park', 'fortune', 'headed', 'home', 'minutes', 'ronaldo', 'scored', 'nigel', 'martyn', 'parried', 'paul', 'scholes', 'free', 'kick', 'marcus', 'bent', 'missed', 'everton', 'best', 'chance', 'roy', 'carroll', 'later', 'struck', 'missile', 'saved', 'feet', 'rooney', 'return', 'always', 'going', 'potential', 'flashpoint', 'involved', 'angry', 'exchange', 'spectator', 'even', 'kick', 'rooney', 'every', 'touch', 'met', 'deafening', 'chorus', 'jeers', 'crowd', 'idolised', 'year', 'old', 'everton', 'started', 'brightly', 'fortune', 'needed', 'alert', 'scramble', 'away', 'header', 'bent', 'near', 'goal', 'line', 'cue', 'united', 'take', 'complete', 'control', 'supreme', 'passing', 'display', 'goodison', 'park', 'pitch', 'cutting', 'fortune', 'gave', 'united', 'lead', 'minutes', 'rising', 'meet', 'ronaldo', 'cross', 'eight', 'yards', 'portuguese', 'youngster', 'allowed', 'much', 'time', 'space', 'hapless', 'gary', 'naysmith', 'united', 'dominated', 'without', 'creating', 'many', 'clear', 'cut', 'chances', 'almost', 'paid', 'price', 'making', 'domination', 'two', 'minutes', 'half', 'time', 'mikel', 'arteta', 'played', 'superb', 'ball', 'area', 'bent', 'played', 'onside', 'gabriel', 'heintze', 'hesitated', 'carroll', 'plunged', 'fee', 'save', 'united', 'almost', 'doubled', 'lead', 'minutes', 'ronaldo', 'low', 'drive', 'yards', 'took', 'deflection', 'tony', 'hibbert', 'martyn', 'dived', 'save', 'brilliantly', 'martyn', 'came', 'everton', 'rescue', 'three', 'minutes', 'later', 'rooney', 'big', 'moment', 'almost', 'arrived', 'raced', 'clean', 'veteran', 'keeper', 'outstanding', 'form', 'nothing', 'martyn', 'could', 'united', 'doubled', 'lead', 'minutes', 'doubled', 'advantage', 'scholes', 'free', 'kick', 'took', 'deflection', 'martyn', 'could', 'parry', 'ball', 'ronaldo', 'reacted', 'first', 'score', 'easily', 'everton', 'problems', 'worsened', 'james', 'mcfadden', 'limped', 'injury', 'may', 'trouble', 'ahead', 'everton', 'goalkeeper', 'carroll', 'required', 'treatment', 'struck', 'head', 'missile', 'thrown', 'behind', 'goal', 'rooney', 'desperate', 'search', 'goal', 'return', 'everton', 'halted', 'martyn', 'injury', 'time', 'outpaced', 'stubbs', 'martyn', 'denied', 'england', 'striker', 'manchester', 'united', 'coach', 'sir', 'alex', 'ferguson', 'fantastic', 'performance', 'us', 'fairness', 'think', 'everton', 'missed', 'couple', 'players', 'got', 'young', 'players', 'boy', 'ronaldo', 'fantastic', 'player', 'persistent', 'never', 'gives', 'know', 'many', 'fouls', 'gets', 'wants', 'ball', 'truly', 'fabulous', 'player', 'everton', 'martyn', 'hibbert', 'yobo', 'stubbs', 'naysmith', 'osman', 'carsley', 'arteta', 'kilbane', 'mcfadden', 'bent', 'subs', 'wright', 'pistone', 'weir', 'plessis', 'vaughan', 'manchester', 'united', 'carroll', 'gary', 'neville', 'brown', 'ferdinand', 'heinze', 'ronaldo', 'phil', 'neville', 'keane', 'scholes', 'fortune', 'rooney', 'subs', 'howard', 'giggs', 'smith', 'miller', 'spector', 'referee', 'styles', 'hampshire']
    if taskout == answer:
        print('Task 8 Correct')
    else:
        print('Error in Task 8.  Program produced:')
        print(taskout)
        print('Expected:')
        print(answer)

def verifytask9():
    filename = 'task9.csv'
    if os.path.exists(filename):
        os.remove(filename)
    task9()
    answer = [['003.txt', '210.txt', 1.0000000000000002], ['163.txt', '164.txt', 1.0000000000000002], ['158.txt', '161.txt', 1.0], ['087.txt', '088.txt', 1.0], ['018.txt', '027.txt', 0.99898981295962], ['189.txt', '205.txt', 0.9066406430977976], ['002.txt', '262.txt', 0.7977968482141655], ['132.txt', '138.txt', 0.7796526739153473], ['018.txt', '024.txt', 0.6665301812555335], ['024.txt', '027.txt', 0.6654451540811809]]
    task9verifier('9', filename, answer)
    
if taskID == 'task1':
    verifytask1()
elif taskID == 'task2':
    verifytask2()       
elif taskID == 'task3':    
    verifytask3()  
elif taskID == 'task4':
    verifytask4()     
elif taskID == 'task5':
    verifytask5()
elif taskID == 'task6':
    verifytask6()   
elif taskID == 'task7':
    verifytask7()   
elif taskID == 'task8':
    verifytask8()   
elif taskID == 'task9':    
    verifytask9()
else:
    verifytask1()
    verifytask2()       
    verifytask3()  
    verifytask4()     
    verifytask5()
    verifytask6()   
    verifytask7()   
    verifytask8()     
    verifytask9()