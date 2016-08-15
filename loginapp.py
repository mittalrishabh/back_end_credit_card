#Copyright (c) 2015 Yodlee, Inc. All Rights Reserved.

 # This software is the confidential and proprietary information of Yodlee, Inc.
 # Use is subject to license terms.

import http1              #importing http1, its the key for all the apps, and to post and get the json response
import httplib, urllib    #imports all the libraries in http and url
import json               #library package for the json response access
import yaml               #converts unicode to byte code
import requests           #requests, for requesting the response from json
from requests import *    #imports all the libraries in the requests
import ConfigParser


class LoginApp:
  global cobSession
  global userSession
  global cobrandLogin
  global cobrandPassword
  global locale
  global userName
  global userPassword
  global userLocale
  
  fqcn = "LoginApp"
  config=ConfigParser.RawConfigParser()
  _SECTION = 'BaseURLSection'
  config.readfp(open('Config.cfg.txt'))
  #self._app_name = config.get(_SECTION, 'baseURL')
  localURLVer1 = config.get(_SECTION, "baseURL")
  print localURLVer1
  cobrandLogin = config.get(_SECTION, "cobrandLogin")
  cobrandPassword = config.get(_SECTION, "cobrandPassword")
  locale = config.get(_SECTION, "locale")
  userName = config.get(_SECTION, "loginName")
  userPassword = config.get(_SECTION, "password")
  userLocale = config.get(_SECTION, "userLocale")
    
  @staticmethod
  def doCoBrandLogin(coBrandUserName, coBrandPassword, locale):#doCoBrandLogin gives the CoBrandLogin session response#
	global cobSession
	mn = "doCoBrandLogin(coBrandUserName=" + coBrandUserName + ",coBrandPassword=" +coBrandPassword+ ",locale=" + locale + " )"
	print(LoginApp.fqcn + " :: " + mn)
	coBrandLoginURL = LoginApp.localURLVer1 + "v1/cobrand/login"
	requestBody = json.dumps("{"+'"'+"cobrand"+'":{'+'"'+"cobrandLogin"+'"'+":"+'"'+coBrandUserName+'",'+'"'+"cobrandPassword"+'"'+":"+'"'+coBrandPassword+'",'+'"'+"locale"+'":"'+locale+'"'+"}}")
	requestBody = json.loads(requestBody)
	jsonResponse = http1.HTTP.doPost(coBrandLoginURL, requestBody)
	loginTokens = json.loads(jsonResponse)
	result = loginTokens.get("session",{})
	cobSession = result.get("cobSession", "abc")
	print "Cobrand Session Token:- " + cobSession
	
  @staticmethod
  def doMemberLogin(userName, userPassword, userLocale):
	global userSession
	mn = "doMemberLogin(loginName="+userName+",password="+userPassword+",coBrandSessionCredential='"+cobSession+"'locale=" + userLocale + ")"
	print(LoginApp.fqcn + " :: " + mn)
    #requestBody="coBrandSessionCredential="+cobSession+",&loginName="+userName+"&password="+userPassword+""
	requestBody = json.dumps("{"+'"'+"user"+'":{'+'"'+"loginName"+'"'+":"+'"'+userName+'",'+'"'+"password"+'"'+":"+'"'+userPassword+'",'+'"'+"locale"+'":"'+userLocale+'"'+"}}")
	requestBody = json.loads(requestBody)
	userLoginURL = LoginApp.localURLVer1 + "v1/user/login"
	headerVal = {'Authorization':'{cobSession='+cobSession+'}'}
	jsonResponse = http1.HTTP.doPostUser(userLoginURL,headerVal, requestBody)
	print jsonResponse
	userloginResponse = json.loads(jsonResponse)
	addAccResponse = userloginResponse.get("user",{})
	userresult = addAccResponse.get("session",{})
	userSession = userresult.get("userSession", "abc")
	print "User Session Token:- " + userSession
    
#coBrandUserName = raw_input('Enter your coBrandUserName: ')
#coBrandPassword = raw_input('Enter your coBrand password: ')
#LoginApp.doCoBrandLogin(coBrandUserName,coBrandPassword)
LoginApp.doCoBrandLogin(cobrandLogin,cobrandPassword,locale)
#userName = raw_input("Enter your userName: ")
#userPassword = raw_input("Enter " + userName + "'s password:  ")
LoginApp.doMemberLogin(userName, userPassword, userLocale)
#LoginApp.doMemberLogin(config.get("login", "loginName"), config.get("login", "password"))
