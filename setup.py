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
	
       "includes":["sip"], # 如果是Qt应用要加上这一行，如果不是则不需要
       "dll_excludes":["MSVCP90.dll"],
       "compressed":1, # 1--压缩文件
       "optimize":2,
       "ascii":0,
       "bundle_files":0,}		
setup (
     name = 'PyQtDemo',
     version = '1.0',	
     console = ["dytt.py", # 此处改为要打包的脚本],		
     options = {'py2exe':py2exe_options } 	
     )