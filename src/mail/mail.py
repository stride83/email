#coding=utf-8
'''
Created on 2017��2��27��

@author: stride83
'''
from urllib import _hexdig
"""
此类主要用于进行autotest的报告自动发布，
1：需要有很强的接口性；
2：并且需要支持较多的图像化的功能;
3：数据分析功能


"""

import smtplib
from email.mime.text import  MIMEText
from email.header import Header

import re


class Email(object):
    '''
    classdocs
    '''

    
    def __init__(self, **params):
        '''
        Constructor
        params:sender;receiver;subject;smtpserver;username;password
        '''
        expect=('password','receiver','sender',
                'smtpserver','subject','username')
        if len(set(params.keys())^set(expect)) != 0:
            self._help()
        self.password=params['password']
        self.receiver=params['receiver']
        self.sender=params['sender']
        self.smtpserver=params['smtpserver']
        self.subject=params['subject']
        self.username=params['username']
        
        
    
    def _help(self):
        print '''
        please input the follow parameters:
        1:sender: 
        2:receiver:
        3:subject:
        4:username:
        5:password:
        6:smtpserver:
        
        '''
    
    def EmailBody(self,params):
        pass
    
    
    
if __name__=="__main__":
    email=Email(**{'sender':1,'receiver':2,'subject':3,
                 'username':4,'password':5,'smtpserver':6})
    
        