# -*- coding: UTF-8 -*-

# from distutils.core import setup
# import py2exe
# setup(console=["dytt.py"])

#info:myvpn.swjtu.edu.cn
#username:2016044855
#passwd:swjtu2022

from distutils.core import setup

import py2exe

import sys

	
# this allows to run itwith a simple double click.
	
sys.argv.append ('py2exe')
	
py2exe_options = {
	
       "includes":["sip"], # �����QtӦ��Ҫ������һ�У������������Ҫ
       "dll_excludes":["MSVCP90.dll"],
       "compressed":1, # 1--ѹ���ļ�
       "optimize":2,
       "ascii":0,
       "bundle_files":0,}		
setup (
     name = 'PyQtDemo',
     version = '1.0',	
     console = ["dytt.py", # �˴���ΪҪ����Ľű�],		
     options = {'py2exe':py2exe_options } 	
     )