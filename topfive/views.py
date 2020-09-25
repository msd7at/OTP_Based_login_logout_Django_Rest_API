from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests
# import smtplib as sm
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
# Create your views here.
import os
import tweepy as tw
import pandas as pd
API_KEYS="Confidential Data"
API_SECRET_KEYS='Confidential Data'
ACCESS_TOKEN='Confidential Data'
ACCESS_TOKEN_SECRET='Confidential Data'
# from .ssh.keys import ACCESS_TOKEN,ACCESS_TOKEN_SECRET,API_KEYS,API_SECRET_KEYS

def get_the(unn):
    auth= tw.OAuthHandler(API_KEYS,API_SECRET_KEYS)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
        # auth = tw.OAuthHandler(consumer_key, consumer_secret)
        # auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=0.5)
            #x=api.statuses_lookup(id_=["elonmusk"],map=True)
    top_5=[]
    x=api.user_timeline(unn,count=5)
    for status in x: 
        top_5.append(status.text)
    return top_5 
em=get_the("elonmusk")
nav=get_the("naval")
ems='\n -->'.join(map(str, em))
ems="     Latest Tweets from Elon Musk\n-->"+"\n"+ems
nacm='\n -->'.join(map(str,nav)) 
nacm="\n"+"    Latest Tweets from Naval \n-->"+"\n"+nacm
op=ems+nacm

@login_required(login_url="/this")
def PrintTopFive(request):
    ree={"elon":em,"nav":nav}
    print(em,"00000000000000",nav)
    res=render(request,'topfive/topfive.html',context=ree)
    return res

def send_mail():
    sender_email = "jhamunda7at@gmail.com"
    receiver_email = "ultimategamer10082211@gmail.com"


    password = "';lkjhgf"
    message = MIMEMultipart("alternative")
    message["Subject"] = "Tweet Updates"
    message["From"] = sender_email
    message["To"] = receiver_email
    text=op
    # text = """\
    # Hi,
    # How are you?
    # Real Python has many great tutorials:
    # www.realpython.com"""
    part1 = MIMEText(text, "plain")
    message.attach(part1)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
# while True:
#     send_mail()
#     time.sleep(30)
