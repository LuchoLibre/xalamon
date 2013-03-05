#!/usr/bin/env python
import os

# Change this to 'grep' by show, username, jobtype, status, etc. Comment out for ALL
RushFilter = "| grep ghouraba"
# HowMany Procesors would you like to add
extraProcs = "\'+mantra8GB=1@1\'"

def execCommands (command) :
  #Comment the following line to test
	#f = os.popen(command)
	print "did: " + command

def getJobs (RushFilter):
	global JobsFound 
	try:
		JobsFound = os.popen("rush -laj | grep 'Run\|Wait'" + RushFilter) 
	except NameError:
		JobsFound = os.popen("rush -laj | grep 'Run\|Wait'") 

def buildCommands (JobsFound):
	for job in JobsFound.readlines():
		jobColumns = job.split()
		command = "rush -fu -ac " + extraProcs + " " + str(jobColumns[1])
		execCommands (command)

getJobs (RushFilter)
buildCommands (JobsFound)		
