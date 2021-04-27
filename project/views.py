from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import CreateListingForm, UpdatePosterForm, CreateReviewForm, CreateProfileForm
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse


class PostersPageView(ListView):
    '''Showing a list of all Posters.'''
    model = Poster                                      # retrieve Poster objects from database
    template_name = "project/show_all_posters.html"     # delegate the display to this template
    context_object_name = "posters"                     # use this variable name in the template

    def get_context_data(self, **kwargs):
        context = super(PostersPageView, self).get_context_data(**kwargs)
        context['categories'] = CATEGORY_CHOICES
        return context

class PostersCategoryPageView(ListView):
    '''Showing a list of all Posters.'''
    model = Poster                                      # retrieve Poster objects from database
    template_name = "project/show_all_posters.html"     # delegate the display to this template
    context_object_name = "posters"                     # use this variable name in the template

    def get_context_data(self, **kwargs):
        context = super(PostersCategoryPageView, self).get_context_data(**kwargs)
        context['categories'] = CATEGORY_CHOICES
        return context

    def get_queryset(self, **kwargs):
        return Poster.objects.filter(category = self.kwargs['type'])


class PosterPageView(DetailView):
    '''Showing a list of an individual Poster.'''       
    model = Poster                                      # retrieve Poster objects from database
    template_name = "project/show_poster_page.html"     # delegate the display to this template
    context_object_name = 'posters'                     # use this variable name in the template

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(PosterPageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateReviewForm() 
        context['create_review_form'] = form
        # return this context dictionary
        return context

class ProfilePageView(DetailView):
    "obtain data for one Profile record, then deleguate work to show_profile.html to display Profile."
    model = Profile
    template_name = "project/show_profile.html"
    context_object_name = "profile"

class CreateListView(CreateView):
    '''create a new poster object and store it in the database'''
    model = Poster                                         #which model to create
    form_class = CreateListingForm                         # which form to use to create the list
    template_name = "project/create_list_form.html"        # delegate display to this template


class CreateProfileView(CreateView):
    '''create a new poster object and store it in the database'''
    model = Profile                                        #which model to create
    form_class = CreateProfileForm                         # which form to use to create the list
    template_name = "project/create_profile_form.html"     # delegate display to this template


class UpdatePosterView(UpdateView):
    '''update an existing poster object and store it in the database'''
    model = Poster                                         # which model to update
    form_class = UpdatePosterForm                          # which form to use to update the poster 
    template_name = "project/update_poster_form.html"      # delegate the display to this template


def post_review_message(request, pk):
    '''
    Process a form submission to post a new user review.
    '''

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateReviewForm(request.POST or None)

    if form.is_valid():

            # create the Review object with the data in the CreateReviewForm
            review = form.save(commit=False) # don't commit to database yet

            # find the poster that matches the `pk` in the URL
            poster = Poster.objects.get(pk=pk)

            # attach FK profile to this status message
            review.poster = poster

            # now commit to database
            review.save()
    else:
            print("Error: the form was not valid")
            print(form.errors)

    # redirect the user to the show_profile_page view
    url = reverse('show_poster_page', kwargs={'pk': pk})
    return redirect(url)


class DeleteReviewView(DeleteView):
        '''A view to delete a user review and store it in database'''  

        template_name = "project/delete_review_form.html"
        queryset =  Review.objects.all()

        def get_context_data(self, **kwargs):
            #obtain default context data dictionary by calling get_context_data
            context = super(DeleteReviewView, self).get_context_data(**kwargs)
            #find review object we are trying to delete 
            review = Review.objects.get(pk=self.kwargs['review_pk'])
            #Add this to the context data dictionary 
            context['review'] = review
            return context

        def get_object(self):

            # read the URL data values into variables
            poster_pk = self.kwargs['poster_pk']
            review_pk = self.kwargs['review_pk']

            # find the Review object, and return it

            return Review.objects.get(pk=self.kwargs['review_pk'])

        def get_success_url(self):
            '''Return a URL to be redirected to after the delete''' 
            # get the pk for this review
            poster_pk = self.kwargs['poster_pk'] 
            
            url = reverse('show_poster_page', kwargs={'pk': poster_pk})
            return (url)
 

class SearchView(ListView):
    '''Showing a list of all Posters.'''
    model = Poster                                      # retrieve Poster objects from database
    template_name = "project/search.html"     # delegate the display to this template
    context_object_name = "posters"                     # use this variable name in the template

def get_queryset(self):
    '''Return a QuerySet of Poster objects.'''

    # check for HTTP parameters in the HTTP GET request
    if 'search_text' in self.request.GET:
        search_text = self.request.GET['search_text']

        return Poster.objects.filter(text__contains=search_text)

    # default: no query was provided:
    return None