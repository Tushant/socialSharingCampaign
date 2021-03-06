from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect, Http404

# Create your views here.
from .forms import EmailForm, JoinForm
from .models import Join


def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""
	return ip




#str(user_id)[:11].replace('-', '').lower()
import uuid

def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
	#ref_id = '9f16a22615'
	try:
		id_exists = Join.objects.get(ref_id=ref_id)
		get_ref_id()
	except:
		return ref_id



def share(request, ref_id):
	#print ref_id
	try:
		join_obj = Join.objects.get(ref_id=ref_id)
		friends_referred = Join.objects.filter(friend=join_obj)
		count = join_obj.referral.all().count()
		print count
		ref_url = settings.SHARE_URL + str(join_obj.ref_id)

		context = {"ref_id": join_obj.ref_id, "count": count, "ref_url": ref_url}
		template = "share.html"
		return render(request, template, context)
	except:
		raise Http404



def home(request):
	try:
		join_id = request.session['join_id_ref']
		obj = Join.objects.get(id=join_id)
	except:
		obj = None

	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit=False)
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email=email)
		if created:
			new_join_old.ref_id = get_ref_id()
			# add our friend who referred us to our join model or a related
			if not obj == None:
				new_join_old.friend = obj
			new_join_old.ip_address = get_ip(request)
			new_join_old.save()
		
		#print all "friends" that joined as a result of main sharer email
		#print Join.objects.filter(friend=obj).count()
		#print obj.referral.all().count()

		#redirect here
		return HttpResponseRedirect("/%s" %(new_join_old.ref_id))

	context = {"form": form}
	template = "home.html"
	return render(request, template, context)




























'''
# Create your views here.
def home(request):


	# This is using normal forms
	# form = EmailForm(request.POST or None)
	# if form.is_valid():
	# 	email = form.cleaned_data['email']
	# 	print email #prints the email that is entered on the email field 
	# 	new_join, created = Join.objects.get_or_create(email=email) #prints the email from the database and if the email is created then returns True else False 
	# 	print new_join
	# 	print created
	# 	if created:
	# 		print 'New email is created %s' %(new_join) 



	# This is now using models form
	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit=False)
		print new_join
		#There might be other operation to be done so we are not saving it now so commit is false
		email = form.cleaned_data['email']
		print email #prints the email that is entered on the email field 
		new_join_old, created = Join.objects.get_or_create(email=email)  #This and above code(cleaned_data) will not allow same email(will be unique) 
		if created:
			new_join_old.ref_id = get_ref_id()
			new_join_old.ip_address = get_ip(request) #new_join.ip_address means it is taking the value from the model`s ip_address where the ip of requested user is stored so request parameter is used
			new_join_old.save()

	context = {"form":form}
	template = "base.html"
	return render(request,template,context)
'''	