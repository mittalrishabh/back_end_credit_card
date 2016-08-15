----------------------------------
Yodlee PFM/Aggregation Sample Apps
----------------------------------
 - Yodlee Sample Apps/Libraries can be used :
	i)  To Consume Yodlee PFM/Aggregation API's 
	ii) Provides seamless interaction to Yodlee API's

Note : 
	i)  Yodlee Apps/Apis are categorized into three different categories i.e. :  Authentication/PFM/Aggregation
	ii) Response From all APIs is JSON and utilities parses and provides key/value pair arrays for the same.
	iii) Account addition sample code is just having an example for Non-MFA and MFA providers.
		* MFA provider ID - 16442 (Dag Site Multilevel)
		* Non MFA provider ID - 16441 (Dag Site)
		There can be multiple providers, and the MFA/Non-MFA calls will vary based on the nature of providers. 
		Please follow the API documentation for more details on the same.
		For Non MFA , after Account Addition, getRefresh API should be called till the time we get refresh status as REFRESH_COMPLETE/LOGIN_FAILURE
		For MFA, refresh API should be called till we get REFRESH_COMPLETE/LOGIN_FAILURE, if we get MFA/LoginForm in intermediate steps, we should
		be posting MFA Challenge. For more details please refer API Documentation.
		Refresh call can be a polling call which can be made by end user after a delay of every 10-20 ms, till the time refresh is complete or login failure.
	iv) In this sample app, the credentails and other data are encrypted using the public key. 
		Public keys will be different for each customers. 

-------------------------------------
Python Installation and its setup: 
-------------------------------------
1] Download python 2.7.9 (https://www.python.org/) 
2] Install pip along with python and put python folder path in your system path variable (Ex: D:\Python) . [In Linux, terminal, sudo apt-get install pip]
3] Download https://codeload.github.com/kennethreitz/requests/legacy.zip/master , Requests package. Extract under python directory.
4] In windows command prompt, navigate to the Python folder (Ex: D:\Python)
5] Run "Python setup.py install".
6] Then Reboot the windows machine. 
7] Open Python shell and check by executing "import requests", and we should not get any errors. 
8] Install yaml package for converting unicode byte to normal. then execute the code. [In Linux,terminal, sudo apt-get install yaml]
To install yaml, go to http://pyyaml.org/wiki/PyYAML. and download and install for the required python version used. Next check in the python shell , that it installed yaml.


----------------------------------------------
Steps to execute the code:
----------------------------------------------
1] Go to the python source code folder.
2] Configure the Yodlee URL in the file "Config.cfg.txt".
	Eg: localURLVer1 = "https://stage.api.yodlee.com/ysl/private-yodlee/"
3] Provide your  cobrand's and user's  credential in Config.cfg.txt
3] For using the PKI enabled account addition options, replace the content of the file "publickey.txt" with the public key content shared.
4) Run the main file as -> "python MainApp.py".
----------------------------------------------