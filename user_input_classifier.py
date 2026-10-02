    #introduction
ques0=input("Hey, my name is Thalion ,what's your's? ")
print("Nice to meet you", ques0)


#gender
ques1=input('What is your gender? male or female?')
if ques1=='male' :
    print("Ah so its Mr.", ques0) 
if ques1=='female' :
    print("Ah so its Ms.", ques0)


#age differentiation 
ques2= input('What is your age ?')    

#--->male

if ques1=='male':
    if int(ques2) < 12 :
        print("What a lovely little boy you must be, hope you have a wonderfull childhood.")
    if 18> int(ques2) >=12 :
        print("A little man I see, eat well and grow up to become a respected handsome man.")
    if 30> int(ques2) >=18 :
        print("Young man , i hope the flame of your youth shine enternally and illimunate this world.")
    if 60> int(ques2) >=30 :
        print("Come let's talk about life.")
    if int(ques2) >=60 :
        print("I request some wisdom from you SIR.")
    
#--->female   

if ques1=='female' :
    if int(ques2) < 12 :
        print("What a lovely little girl you must be, hope you have a wonderfull childhood.")
    if 18> int(ques2) >=12 :
        print("A little lady I see, eat well and grow up to become a well respected beautifull lady.")
    if 30> int(ques2) >=18 :
        print("Young lady , i hope you don't ever lose he pure heart of youth and may your life be blissfull.")
    if 60> int(ques2) >=30 :
        print("How's life.")
    if int(ques2) >=60 :
        print("I request some wisdom from you MADAM.")

#--->male

if ques1=='male' :
    if int(ques2)<12 :
        print('What a cute little boy you must be, hope you have a wonderfull childhood.')
    if 12<=int(ques2)<18 :
        print('A little man I see, eat well and grow up to become respected young man.')
    if 18<=int(ques2)<30 :
        print('Young man, I hope the flame of your heart shines eternally and forever illuminates the world')
    if 30<=int(ques2)<60 :
        print("How's life.")
    if 60<=int(ques2) :
        print('Please give me guidance , senior.')

#--->female

if ques1=='female' :
    if int(ques2)<12 :
        print('What a cute little girl you must be , hope you have a wonderfull childhood.') 
    if 12<=int(ques2)<18 :
        print('A little lady I see, eat well andd grow up to become a respected young woman.')
    if 18<=int(ques2)<30 :
        print("Young lady, I hope you don't ever lose the pure heart of youth and may your life be blissfull")
    if 30<=int(ques2)<60 :
        print("yound ldy , I hope you dont ever loe")
