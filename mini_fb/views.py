from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Profile, StatusMessage
from .models import *
from.forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm
import random
from django.shortcuts import redirect
from django.urls import reverse

def post_status_message(request, pk):
    '''
    Process a form submission to post a new status message.
    '''

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateStatusMessageForm(request.POST or None)

        if form.is_valid():

            # create the StatusMessage object with the data in the CreateStatusMessageForm
            status_message = form.save(commit=False) # don't commit to database yet

            # find the profile that matches the `pk` in the URL
            profile = Profile.objects.get(pk=pk)

            # attach FK profile to this status message
            status_message.profile = profile

            # now commit to database
            status_message.save()

    # redirect the user to the show_profile_page view
    url = reverse('show_profile_page', kwargs={'pk': pk})
    return redirect(url)

class ShowAllProfilesView(ListView):
    "Shows a listing of all the various profiles"
    model = Profile
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "profiles"


class ShowProfilePageView(DetailView):
    "obtain data for one Profile record, then deleguate work to a template show_profile_page.html to display that Profile."
    model = Profile
    template_name = "mini_fb/show_profile_page.html"
    context_object_name = "profile"

def get_context_data(self, **kwargs):
    '''Return the context data (a dictionary) to be used in the template.'''

    # obtain the default context data (a dictionary) from the superclass; 
    # this will include the Profile record to display for this page view
    context = super(ShowProfilePageView, self).get_context_data(**kwargs)
    # create a new CreateStatusMessageForm, and add it into the context dictionary
    form = CreateStatusMessageForm() 
    context['create_status_form'] = form
    # return this context dictionary
    return context


class RandomShowProfilePageView(DetailView):
    "obtain data for one Profile record, then deleguate work to a template show_profile_page.html to display that Profile."
    model = Profile
    template_name = "mini_fb/show_profile_page.html"
    context_object_name = "profile"

    def get_object(self):
        '''Select one profile at random for display in the show_profile_page.html'''

        #obtain all profiles using object manager 
        mini_fb = Profile.objects.all()

        # select one profile at random
        p = random.choice(mini_fb)
        return p

class CreateProfileView(CreateView):
    '''Create a new Quote object and store in database.'''

    model = Profile #which model to create
    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"

class UpdateProfileView(UpdateView):

    form_classs = UpdateProfileForm
    template_name = "mini_fb/update_profile_form.html"
    queryset = Profile.objects.all()


class DeleteStatusMessageView(DeleteView):
 
    template_name = "mini_fb/update_profile_form.html"
    queryset = Profile.objects.all()
    #success_url = "../../all" # once you have deleted your status

    def get_success_url(self):
        '''Return the URL we should be redirected to after the delete.'''

        # get the primary key for this status
        pk = self.kwargs.get('pk')
        StatusMessage = StatusMessage.objects.filter(pk=pk).first() #get one object from QuerySet

        # find the person associated with the status message

        # reverse to show the profile page for that status message
        Profile = StatusMessage.Profile
        return reverse('Profile', kwargs={'pk':Profile.pk})







