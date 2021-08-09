from math import e
import numpy as np
import random as r
import csv

x=0

##############################################################################
def regr21(small, medium_low, medium_high, num_emp, num_emp_square, south, ict, ht_noict, industrial, turnover, turnover_sq, no_dis, no_extra, no_dataloss):
    r = -2.055*small -0.512*medium_low -0.854*medium_high +(1.47*10**(-4))*num_emp +(-1.11*10**(-9))*num_emp_square +0.220*south +0.996*ict -0.103*ht_noict +0.534*industrial +(1.81*10**(-3))*turnover +(-2.59*10**(-7))*turnover_sq -0.353*no_dis -1.437*no_extra -0.398*no_dataloss
    r1 = -1.414 + r
    odds = e**r1
    prob = (odds)/(1+odds)
    return prob

#danni tra 50k e 199k
def regr22(small, medium_low, medium_high, num_emp, num_emp_square, south, ict, ht_noict, industrial, turnover, turnover_sq, no_dis, no_extra, no_dataloss):
    r = -2.055*small -0.512*medium_low -0.854*medium_high +(1.47*10**(-4))*num_emp +(-1.11*10**(-9))*num_emp_square +0.220*south +0.996*ict -0.103*ht_noict +0.534*industrial +(1.81*10**(-3))*turnover +(-2.59*10**(-7))*turnover_sq -0.353*no_dis -1.437*no_extra -0.398*no_dataloss
    r1 = -3.747 + r
    odds = e**r1
    prob = (odds)/(1+odds)
    return prob

#danni da 200k in su
def regr23(small, medium_low, medium_high, num_emp, num_emp_square, south, ict, ht_noict, industrial, turnover, turnover_sq, no_dis, no_extra, no_dataloss): 
    r = -2.055*small -0.512*medium_low -0.854*medium_high +(1.47*10**(-4))*num_emp +(-1.11*10**(-9))*num_emp_square +0.220*south +0.996*ict -0.103*ht_noict +0.534*industrial +(1.81*10**(-3))*turnover +(-2.59*10**(-7))*turnover_sq -0.353*no_dis -1.437*no_extra -0.398*no_dataloss
    r1 = -6.341 + r
    odds = e**r1
    prob = (odds)/(1+odds)
    return prob
##############################################################################
def regr11(small, south, hightech, industrial, b_exp, m_exp, difficult):
    r = -0.156 -0.109*small -0.206*south +0.080*hightech -0.113*industrial +0.016*b_exp +0.172*m_exp +0.212*difficult
    prob = (e**r)/(1+e**r)
    return prob
    
def regr12(small, south, hightech, industrial, b_exp, m_exp, difficult, skill):
    r = -0.401 -0.097*small -0.225*south +0.040*hightech -0.052*industrial +0.005*b_exp +0.200*m_exp +0.255*difficult +0.465*skill
    prob = (e**r)/(1+e**r)
    return prob
    
def regr13(small, south, hightech, industrial, b_exp, m_exp, difficult, skill, nocloud, nobgai, noiot):
    r = -0.419 -0.118*small -0.217*south +0.034*hightech -0.045*industrial +0.027*b_exp +0.155*m_exp +0.231*difficult +0.450*skill -0.037*nocloud +0.020*nobgai -0.115*noiot
    prob = (e**r)/(1+e**r)
    return prob
##########################################################################

def scrittura(nome, lista):
	with open(nome, mode='a+', newline='') as tabella:
		tabella_w = csv.writer(tabella, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		tabella_w.writerow(lista)

##############################################################################


scrittura('tabella3.csv',['ID','small','m-low','m-high','num emp','nesq','south','ICT','HTnoICT','ind','turn','turnsq','big export','medium export','skill share','no cloud','no big data/AI','no IOT','nodis','noextra','nodata','difficult','PROB ATTACCO','PROB1','PROB2','PROB3','PROB4'])

while x != 100:
	x+=1
	r.seed(int(x)+18)
	small = r.randint(0, 1)
	if small == 1:
		medium_low = 0
		medium_high = 0
		num_emp = r.randint(20,49)
		num_emp_square = num_emp**2
	else:
		r.seed(int(x)+1)
		medium_low = r.randint(0, 1)
		if medium_low == 1:
			medium_high = 0
			num_emp = r.randint(50, 199)
			num_emp_square = num_emp**2
		else:
			r.seed(int(x)+7)
			medium_high = r.randint(0, 1)
			if medium_high == 1:
				num_emp = r.randint(200, 499)
				num_emp_square = num_emp**2
			else:
				num_emp = r.randint(500, 2000)
				num_emp_square = num_emp**2
	r.seed(int(x)+9)
	south = r.randint(0, 1)
	r.seed(int(x)+88)
	ict = r.randint(0, 1)
	
	if ict == 1:
		ht_noict = 0
		industrial = 0
	else:
		r.seed(int(x)+8)
		ht_noict = r.randint(0,1)
		hightech = ht_noict
		if ht_noict == 1:
			industrial = 0
		else:
			r.seed(int(x)+2)
			industrial = r.randint(0, 1)
	
	r.seed(int(x)+78)
	turnover = r.randint(800,5000)
	turnover_sq = turnover**2
	r.seed(int(x)+10)
	no_dis = r.randint(0, 1)
	r.seed(int(x)+99)
	no_extra = r.randint(0, 1)
	r.seed(int(x)+51)
	no_dataloss = r.randint(0, 1)
	
	r.seed(int(x)+88)
	b_exp = r.randint(0, 1)
	if b_exp == 1:
		m_exp = 0
	else:
		r.seed(int(x)+7)
		m_exp = r.randint(0, 1)

	r.seed(int(x)+10)
	difficult = r.randint(0, 1)
	r.seed(int(x)+3)
	skill = r.uniform(0,1)
	r.seed(int(x)+4)
	no_choices = r.randint(0, 1)
	
	if skill == 0:
		p = regr11(small, south, hightech,industrial, b_exp, m_exp, difficult)
		
		#scrittura('tabella1.csv', [str(id),str(small),str(south),str(hightech),str(industrial),str(b_exp),str(m_exp),str(difficult),'-','-','-','-',str(round(p*100))+'%'])
		#print(str(id)+'	'+str(small)+'	'+str(south)+'	'+str(hightech)+'	'+str(industrial)+'	'+str(b_exp)+'	'+str(m_exp)+'	'+str(difficult)+'	-	-	-	-	'+str(p)+'\n')
		
	elif skill != 0 and no_choices == 0:
		p = regr12(small, south, hightech,industrial, b_exp, m_exp, difficult, skill)
		#print(str(id)+'	'+str(small)+'	'+str(south)+'	'+str(hightech)+'	'+str(industrial)+'	'+str(b_exp)+'	'+str(m_exp)+'	'+str(difficult)+'	'+str(skill)+'	-	-	-	'+str(p)+'\n')
		#scrittura('tabella1.csv', [str(id),str(small),str(south),str(hightech),str(industrial),str(b_exp),str(m_exp),str(difficult),str(round(skill*100))+'%','-','-','-',str(round(p*100))+'%'])	
			
		

	elif skill != 0 and no_choices != 0:
		r.seed(int(x)+55)
		nocloud = r.randint(0, 1)
		r.seed(int(x)+44)
		nobgai = r.randint(0, 1)
		r.seed(int(x)+33)
		noiot = r.randint(0, 1)
		
		p = regr13(small, south, hightech, industrial, b_exp, m_exp, difficult, skill, nocloud, nobgai, noiot)
		#scrittura('tabella1.csv', [str(id),str(small),str(south),str(hightech),str(industrial),str(b_exp),str(m_exp),str(difficult),str(round(skill*100))+'%',str(nocloud),str(nobgai),str(noiot),str(round(p*100))+'%'])
		#print(str(id)+'	'+str(small)+'	'+str(south)+'	'+str(hightech)+'	'+str(industrial)+'	'+str(b_exp)+'	'+str(m_exp)+'	'+str(difficult)+'	'+str(skill)+'	'+str(nocloud)+'	'+str(nobgai)+'	'+str(noiot)+'	'+str(p)+'\n')


	a = regr21(small, medium_low, medium_high, num_emp, num_emp_square, south, ict, ht_noict, industrial, turnover, turnover_sq, no_dis, no_extra, no_dataloss)
	b = regr22(small, medium_low, medium_high, num_emp, num_emp_square, south, ict, ht_noict, industrial, turnover, turnover_sq, no_dis, no_extra, no_dataloss)
	c = regr23(small, medium_low, medium_high, num_emp, num_emp_square, south, ict, ht_noict, industrial, turnover, turnover_sq, no_dis, no_extra, no_dataloss)
	

	p4 = c
	p3 = b-c
	p2 = a-b
	p1 = 1-a
	
	scrittura('tabella3.csv',[str(x),str(small),str(medium_low),str(medium_high),str(num_emp),str(num_emp_square),str(south),str(ict),str(ht_noict),str(industrial),str(turnover),str(turnover_sq),str(b_exp),str(m_exp),str(round(skill*100))+'%',str(nocloud),str(nobgai),str(noiot),str(no_dis),str(no_extra),str(no_dataloss),str(difficult),str(round(p*100))+'%',str(round(p1*100))+'%',str(round(p2*100))+'%',str(round(p3*100))+'%',str(round(p4*100))+'%'])
	#print(str(x)+'	'+str(small)+'	'+str(medium_low)+'	'+str(medium_high)+'	'+str(num_emp)+'	'+str(num_emp_square)+'		'+str(south)+'	'+str(ict)+'	'+str(ht_noict)+'	'+str(industrial)+'	'+str(turnover)+'	'+str(turnover_sq)+'		'+str(no_dis)+'	'+str(no_extra)+'	'+str(no_dataloss)+'	'+str(round(p1*100))+'%	'+str(round(p2*100))+'%	'+str(round(p3*100))+'%	'+str(round(p4*100))+'%\n')