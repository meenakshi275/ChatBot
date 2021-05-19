from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')
#Download the punkt package
nltk.download('punkt',quiet=True)
#get the Articlehh
article=Article('https://www.air.org/resource/mental-health-awareness')
article.download()
article.parse()
article.nlp()
corpus=article.text

article=Article('https://health.usnews.com/conditions/mental-health')
article.download()
article.parse()
article.nlp()
corpus=article.text

article=Article('https://psychcentral.com/disorders/disorders')
article.download()
article.parse()
article.nlp()
corpus=article.text

article=Article('https://www.nami.org/About-Mental-Illness/Treatments/Treatment-Settings')
article.download()
article.parse()
article.nlp()
corpus=article.text

#print article
#print(corpus)
test=corpus
sentence_list=nltk.sent_tokenize(test)
#print(sentence_list)
#A function to return a random greeting message to a user
def greet_response(text):
    text=text.lower()

    bot_greet=['hello','HELLO','HI','HEY','hi','hey','wassup','hii','hiii','whasup','Hello']
    user_greet=['HI','HII','hiii','heLLO','Hello','hi','hello','helo','hii','wassup']


    for word in text.split():
        if word in user_greet:
            return random.choice(bot_greet)
#index sort function
def index_sort(list_var):
    length=len(list_var)
    list_index=list(range(0,length))
    x=list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]]>x[list_index[j]]:
                #swap
                temp=list_index[i]
                list_index[i]=list_index[j]
                list_index[j]=temp
 
    return list_index

#bot response to actual queries
def bot_response(user_input):
    user_input=user_input.lower()
    sentence_list.append(user_input)
    bot_response=''
    cm=CountVectorizer().fit_transform(sentence_list)
    similarity_score=cosine_similarity(cm[-1],cm)
    similarity_score_list=similarity_score.flatten()
    index=index_sort(similarity_score_list)
    index=index[1:]
    response_flag=0



    j=0
    for i in range(len(index)):
        if similarity_score_list[index[i]]>0.0:
            bot_response=bot_response+' '+sentence_list[index[i]]
            response_flag=1
            j=j+1
        
        if j>5:
            break
    

    if response_flag==0:
        bot_response=bot_response+'I apologize, that i have not understood your meaning. '

    sentence_list.remove(user_input)

    return bot_response

#start chat
print("Welcome to Mental Health Care Helpline Center.I am here to help you with the information regarding mental health .If you want to end the chat then press 'Bye' or 'exit")



exit_list=['bye','exit','Bye','BYE','BYe','ByE','EXIT','eXiT','EXit','ExiT','bYe','eXIt']
while(True):
    user_input=input()
    if user_input.lower() in exit_list:
        print('Bot: Thank you for contacting.See you later')
        break
    else:
        if greet_response(user_input)!=None:
            print('Bot:'+greet_response(user_input))
        else:
            print('Bot:'+bot_response(user_input)) 