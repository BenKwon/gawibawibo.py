"""
Traditional gawi-bawi-bo game

@author SeungJoo Kwon
@created 12-10-2016

"""

import random
	
	

def determine_winner(a,b):
	"""
	Determint WINNER of thegame.
	:param a: my hand parameter
	:param b: cpu hand parameter
	:return None : None is returned. (void)
	
	"""
	if((a-b==1)or(a-b==-2)):
		print("당신이 승리하였습니다")
		
	elif(b==a):
		print("비겼습니다")
	
	else:
		print("당신이 패배 하였습니다")
		
	"""gawi : 1 bawi: 2 bo: 3"""

while(True):
	cpu_output_index =[1,2,3]
	cpu_output =["가위","바위","보"]	b = random.randint(1,3)
	x = input("가위:1,바위:2,보:3 중에 하나를 골라주세요 :")
	a = int(x)
	print("컴퓨터가 "+cpu_output[b-1]+"를 냈습니다")
