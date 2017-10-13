try:
	from urllib2 import urlopen as uReq
except:
	from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import urllib
my_url='https://www.scholarships.com/financial-aid/college-scholarships/scholarship-directory/academic-major'

uClient = uReq(my_url)
page_html=uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")

containers=page_soup.findAll("ul",{"id":"ullist"})
listpoints = containers[0].findAll("li")
for points in listpoints:
	links=points.a["href"]
	bas="https://www.scholarships.com"
	finlink=bas+links
	u1Client=uReq(finlink)
	page1_html=u1Client.read()
	u1Client.close()
	page1_soup = soup(page1_html,"html.parser")
	cont=page1_soup.findAll("td")
	for pts in cont:
		lks=pts.a["href"]
		finlks=bas+lks
		'''u2Client=uReq(finlks)
		page2_html=u2Client.read()
		u2Client.close()
		page2_soup = soup(page2_html,"html.parser")'''
		u2client=urllib.urlopen(finlks.encode('utf-8')).read()
		page2_soup=soup(u2client,"html.parser")
		details=page2_soup.find("div",{"id":"divscholdetails"})
		det=details.ul
		info=det.findAll("li")
		flag=0
		for inform in info:
			if inform.text=='Website Address':
				flag=1
				wadd=inform.text
			if flag==1:
				wadd+=inform.text
			if inform.text=='Contact':
				flag=2
				contact=inform.text
			if flag==2:
				contact+=inform.text
			if inform.text=='Address':
				flag=3
				add=inform.text
			if flag==3:
				add+=inform.text
			if inform.text=='Application Deadline':
				flag=4
				dline=inform.text
			if flag==4:
				dline+=inform.text
			if inform.text=='Number Of Awards':
				flag=5
				awards=inform.text
			if flag==5:
				awards+=inform.text
			if inform.text=='Maximum Amount':
				flag=6
				amount=inform.text
			if flag==6:
				amount+=inform.text
			if inform.text=='Scholarship Description':
				flag=7
				des=inform.text
			if flag==7:
				des+=inform.text
		'''		
		print("Website Address: "+wadd)
		print("Contact: "+contact)
		print("Address: "+add)
		print("Application Deadline: "+dline)
		print("Number of Awards: "+awards)
		print("Maximum Amount: "+amount)
		print("Scholarship Description: "+des)
		'''
		print(wadd)
		print(contact)
		print(add)
		print(dline)
		print(awards)
		print(amount)
		print(des)
