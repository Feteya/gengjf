#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
# Created on 2018/07/26 by lzx

import os

def initialize():
	global line_num
	line_num=0
	global file_num
	file_num=0
	global atoms_num
	atoms_num=0
	global head_file
	head_file="# hf/3-21g\n\nTitle Card Required\n\n0 1\n"
	global temp_file_name
	temp_file_name=''

def rmgjffile():
	path=os.getcwd()
	suffix=".gjf"
	for file in os.listdir(path):
		if file.endswith(suffix):
			os.remove(file)

def process(temp_line):
	global atoms_num
	global line_num
	global file_num
	global head_file
	global temp_file_name
	
	line_num+=1
	
	if line_num==1:
		atoms_num=int(temp_line)

	if (line_num%(atoms_num+2))==1:
		if atoms_num!=int(temp_line):
			raise ValueError("Wrong total number of atoms")
		file_num+=1
		temp_file_name=''.join(['geo',str(file_num),'.gjf'])
		os.mknod(temp_file_name)
		temp_gjf=open(temp_file_name,'w')
		temp_gjf.write(head_file)
		temp_gjf.close()
	elif (line_num%(atoms_num+2))==2:
		pass
	else:
		temp_line_list=temp_line[:].split()
		new_line_list=temp_line_list[0:4]
		new_line='    '.join(new_line_list)
		temp_gjf=open(temp_file_name,'a')
		temp_gjf.write(new_line)
		temp_gjf.write('\n')
		temp_gjf.close()		
		
initialize()
rmgjffile()
	
geo_end_xyz_file=open(r'geo_end.xyz')

while True:
	line=geo_end_xyz_file.readline()
	if not line:break
	process(line)
geo_end_xyz_file.close()

