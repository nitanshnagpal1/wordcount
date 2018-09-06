from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request,'home.html',{'HI':'<p>BYE</p>'})
	
def count(request):
	fulltext=request.GET['fulltext']
	wordcount=fulltext.split()
	wordd={}
	for word in wordcount:
		if word in wordd:
			wordd[word]+=1
		else:
			wordd[word]=1
	wordd=wordd.items()
	wordd=sorted(wordd,key=operator.itemgetter(1),reverse=True)
	return render(request,'count1.html',{"word":len(wordcount),"word1":fulltext,"word2":wordd})
	
def about(request):
	return render(request,'about.html')