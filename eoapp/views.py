from django.shortcuts import render
def home(request):
	if request.GET.get("num"):
		num=int(request.GET.get("num"))
		if num%2==0:
			res="even"
		else:
			res="odd"
		msg="number : "+str(num)+"and result : "+res
		return render(request,"home.html",{"msg":msg})
	else:
		return render(request,"home.html")

