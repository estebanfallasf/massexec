;ò
E)ÈMc           @   s?   d  Z  d k Z d k Z d k Z d k Td f  d     YZ d S(   sO  
Description:	This module is used to explain the usage of the flags to the user.
Author:		Anibal G. Vindas <anibal@hp.com>
Date:		2011.04.14
Comment:	This new version does not have the flag '-v | --version', because that legend is included in the core script.
		Also the flag '-d' was created in order to pass a dictionary path file.

N(   s   *s   useClassc           B   sS   t  Z d  Z d Z d Z d Z d Z d Z e Z	 d d d g Z
 d   Z d   Z RS(   sQ  
	Description:	This module is used to explain the usage of the flags to the user.
	Author:		Anibal G. Vindas <anibal@hp.com>
	Date:		2011.04.15
	Comment:	This new version does not have the flag '-v | --version', because that legend is included in the core script. Also the flag '-d' was created in order to pass a dictionary path file.
	s    s   -ss   -os   -cc         C   s0   d } | d | d | d | d } | Sd  S(   Ns5   	####################################################s]   
		Welcome to Mass Executer.
		This program can help you to execute command lines massively.
su   
		This program is an initiative of the Unix computer ITO Automation.
		Any concern or help is going to be welcomed.
s.   
		See the instructions using the option '-h'
s   

(   s   seps   msg(   s   selfs   msgs   sep(    (    s1   /automation/massexec/source/8.4/usage_20110425.pys   welcome   s    "	c   	      C   s  d d d g } d } x? | D]7 } | t i j o  | GHd | d GHt i   q q Wy) t i t i d d d	 g  \ } } Wn2 t i	 j
 o# } t |  GH| GHt i   n XxÄ| D]¼\ } } | d
 d f j o | GHt i   q¼ | d j o | i   } t |  _ q¼ | d j oE | i   } | |  _ t i i |  o | GHd GHt i   qxq¼ | d j oD | i   } | |  _ t |  d j  o | GHd GHt i   qxq¼ | d j oK | i   } | |  _ t |  d j  p
 | d j o | GHd GHt Sqxq¼ | d j oX | i   } t |  d j  p t i i |  o | GHd GHt i   qx| |  _ q¼ t Sq¼ Wt Sd  S(   Ns   -ss   -os   -csY  
	Usage:
		core.py 
		[-h] [--help] To print this message. 
		[-d <dictionary file>] This flag is optional, but a dictionary file must be included when use it. 
		-s <server list path> This file is mandatory. It must be a list of servers.
		-c <commands string | Text file containing  commands> It is mandatory. A string conteining the commands separeted by ';' must be included.
			Or a path of the file with the commands.
		-o <output file> Mandatory flag with the output report. If the file already exists it will be appended.
		-r Introduces password every time system is waiting for user entry.
	s   Warning: 
Argument 's   ' not found.
i   s
   hrc:s:o:d:s   helps   -hs   --helps   -rs   -ds,   Warning:
	-d option needs a valid file path.i   s@   Warning:
	-c option cannot be empty or less than two characters.i   s    sQ   -o option needs a valid file path. Also argument must has more than 3 characters.s"   -s option needs a valid file path.(   s   arguments_ars   howtos   ars   syss   argvs   exits   getopts   optss   argss   GetoptErrors   errs   strs   os   as   strips   Trues   selfs   sudos   vorts   oss   paths   existss   com_s   lens   out_files   Falses   servers_(	   s   selfs   as   errs   argss   howtos   os   ars   arguments_ars   opts(    (    s1   /automation/massexec/source/8.4/usage_20110425.pys   use,   sj     ) 			 ' (   s   __name__s
   __module__s   __doc__s   msgs   com_s   servers_s   out_files   vorts   Falses   sudos   arguments_ars   welcomes   use(    (    (    s1   /automation/massexec/source/8.4/usage_20110425.pys   useClass   s    	(   s   __doc__s   oss   syss   getopts   stats   useClass(   s   syss   getopts   oss   useClass(    (    s1   /automation/massexec/source/8.4/usage_20110425.pys   ?	   s   