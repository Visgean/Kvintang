#! /usr/bin/python
# -*- coding: UTF-8 -*-

# @author: 	Visgean Skeloru 
# email: 	<visgean@gmail.com>
# jabber: 	<visgean@jabber.org>
# github: 	http://github.com/Visgean


import os, sys
from kvintang.dict.models import Subject, Tag, Term

data_files = os.listdir("data")

subject = Subject(name="Math")
subject.save()

for filename in data_files:
	with open("data/"+filename, "r") as ffile:
		data = ffile.read()
	
	tag = Tag(name=filename)
	tag.save()
	
	for line in data.splitlines():
		trm = line.split("\t")
		term = Term(englishVersion=trm[0], czechVersion=trm[1], subject=subject)
		term.save()
		term.tags.add(tag)
		term.save()
		
		