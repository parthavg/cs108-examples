from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Profile, StatusMessage
from .models import *
from.forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm
import random
from django.shortcuts import redirect
from django.urls import reverse



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
        profiles = Profile.objects.all()

        # select one profile at random
        p = random.choice(profiles)
        return p

class CreateProfileView(CreateView):
    '''Create a new Quote object and store in database.'''

    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"


class UpdateProfileView(UpdateView):
    '''Update a profile object and store it in the database'''
    
    form_class = UpdateProfileForm
    template_name = "mini_fb/update_profile_form.html"
    queryset = Profile.objects.all()


def post_status_message(request, pk):
    '''
    Process a form submission to post a new status message.
    '''

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateStatusMessageForm(request.POST or None, request.FILES or None)

        profile = Profile.objects.get(pk=pk)

        if form.is_valid():

            # create the StatusMessage object with the data in the CreateStatusMessageForm
            status_message = form.save(commit=False) # don't commit to database yet
            image = form.save(commit=False)
            # find the profile that matches the `pk` in the URL

            # attach FK profile to this status message
            status_message.profile = profile
            image.profile = profile
            # check if the form is valid, save object to database 
        

                    
            image.save() #store to the database 
            status_message.save()
        else:
            print("Error: the form was not valid")


    # redirect the user to the show_profile_page view
    url = reverse('show_profile_page', kwargs={'pk': pk})
    return redirect(url)
    


class DeleteStatusMessageView(DeleteView):
    '''Delete a status message object and store it in the database'''
    
    template_name = "mini_fb/delete_status_form.html"
    queryset = StatusMessage.objects.all()

    def get_context_data(self, **kwargs):
        #obtain default context data dictionary by calling get_context_data
        context = super(DeleteStatusMessageView, self).get_context_data(**kwargs)
        #find status message object we are trying to delete 
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_message_pk'])
        #Add this to the context data dictionary 
        context['St_Mg'] = st_msg
        return context

    def get_object(self):

        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_message_pk']

        # find the StatusMessage object, and return it

        return StatusMessage.objects.get(pk=self.kwargs['status_message_pk'])

    def get_success_url(self):

        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']

        url = reverse('show_profile_page', kwargs={'pk': profile_pk})
        return (url)


class ShowNewsFeedView(DetailView):
    "Display news feed"
    model = Profile
    template_name = "mini_fb/show_news_feed.html"
    context_object_name = "profile"


class ShowPossibleFriendsView(DetailView):
    "Show Possible friends for profile"

    model = Profile
    template_name = "mini_fb/show_possible_friends.html"
    context_object_name = "profile"

def add_friend(request, profile_pk, friend_pk):
        '''process the add_friend request, to add a friend for a given profile'''
    
        #find the Profile object which is adding the friend, and store it into a variable
        profile_ob_pk = Profile.objects.get(pk= profile_pk)
        #find the Profile object of the friend to add, and store it into another variable
        friend_ob_pk = Profile.objects.get(pk= friend_pk)
        #add that friend’s Profile into the profile.friends object (using the method add).
        profile_ob_pk.friends.add(friend_ob_pk)
        #save the profile object
        profile_ob_pk.save()
        return redirect(reverse('show_profile_page', kwargs={'pk':profile_pk}))






