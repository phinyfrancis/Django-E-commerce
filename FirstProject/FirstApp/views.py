from FirstApp.models import Itemlist, Rolereq, User, Userorder
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from FirstApp.forms import ItemsForm, OrderForm, Pfupd, Rlupd, usgform, Rltype,Chgepwd
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from FirstProject import settings
# Create your views here.
def home(request):
    return render(request,'app/home.html')

def about(request):
    return render(request,'app/about.html')

def contact(request):
    return render(request,'app/contact.html')

def login(request):
    return render(request,'app/login.html')

def usrreg(request):
    if request.method == "POST":
        d = usgform(request.POST)
        if d.is_valid():
            d.save()
            return redirect('/login')
    d=usgform()
    return render(request,'app/userregister.html',{'t':d})

@login_required
def order(request):
    a = Itemlist.objects.all()
    if request.method == "POST":
        q = OrderForm(request.POST)
        if q.is_valid():
            q.save()
            messages.success(request,"Order placed Successfully, Order again for more")
    q = OrderForm()
    return render(request,'app/order.html',{'a':q,'items':a})

@login_required
def orderaccept(request):
    y = Userorder.objects.all()
    t = User.objects.all()
    return render(request,'app/orderaccept.html',{'q':y,'c':t})

@login_required
def od(request,m):
    r=Userorder.objects.get(id=m)
    if request.method=="POST":
        messages.info(request,"Order Completed")
        r.delete()
        return redirect('/oc')
    e=OrderForm(instance=r)
    return render(request,'app/od.html',{'a':e})


@login_required
def additems(request):
    if request.method == "POST":
        k = ItemsForm(request.POST,request.FILES)
        if k.is_valid():
            k.save()
            messages.success(request,"Item added Successfully")
            return redirect('/additems')
    k=ItemsForm(request.FILES)        
    return render(request,'app/additems.html',{'r':k})

@login_required
def rolereq(request):
    p = Rolereq.objects.filter(ud_id=request.user.id).count()
    if request.method == "POST":
        k = Rltype(request.POST,request.FILES)
        if k.is_valid():
            y = k.save(commit=False)
            y.ud_id = request.user.id
            y.uname = request.user.username
            y.is_checked = 0
            print(y)
            y.save()
    k = Rltype()
    return render(request,'app/rolereq.html',{'d':k, 'c':p})

@login_required
def gveperm(request):
    u = User.objects.all()
    r = Rolereq.objects.all()
    d={}
    for n in u:
        for m in r:
            if n.is_superuser == 1 or n.id != m.ud_id :
                continue
            else:
                d[m.id] = m.Uname, m.rltype, n.role,n.id,m.id
    return render(request,'app/gvpl.html',{'h':d.values()})

@login_required
def gvupd(request,t):
    y = Rolereq.objects.get(ud_id=t)
    d = User.objects.get(id=t)
    if request.method == "POST":
        n = Rlupd(request.POST,instance=d)
        if n.is_valid():
            n.save()
            y.is_checked = 1
            y.save()
            return redirect('/gvper')
    n = Rlupd(instance=d)
    return render(request,'app/gvepermission.html',{'c':n})

@login_required
def gvdel(request,m):
    r = Rolereq.objects.get(id=m)
    a = User.objects.get(id = r.ud_id)
    if request.method == "POST":
        a.role=1
        r.delete()
        a.save()
        messages.success(request,"{} Request Deleted Successfully".format(a.username))
        return redirect('/gvper')
    n = Rlupd(instance=r)
    return render(request,'app/gvdel.html',{'a':n})

@login_required
def pfle(request):
    y = User.objects.get(id=request.user.id)
    return render(request,'app/profile.html',{'q':y})

@login_required
def pfupd(request):
	t = User.objects.get(id=request.user.id)
	if request.method == "POST":
		pfl = Pfupd(request.POST,request.FILES,instance=t)
		if pfl.is_valid():
			pfl.save()
			return redirect('/pfle')
	pfl = Pfupd(instance=t)
	return render(request,'app/profileupdate.html',{'u':pfl})


@login_required
def feedback(request):
    if request.method == "POST":
        sd = request.POST['snmail'].split(',')
        sm = request.POST['sub']
        mg = request.POST['msg']
        rt = settings.EMAIL_HOST_USER
        dt = send_mail(sm,mg,rt,sd)
        if dt == 1:
            return redirect('/')
    return render(request,'app/feedback.html')

@login_required
def changepwd(request):
	if request.method == "POST":
		k = Chgepwd(user=request.user,data=request.POST)
		if k.is_valid():
			k.save()
			return redirect('/login')
	k = Chgepwd(user=request)
	return render(request,'app/changepwd.html',{'t':k})

