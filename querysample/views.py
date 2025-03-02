from django.shortcuts import render
from django.http import JsonResponse

from .models import Sate, City

from .forms import CountriesForm
# Create your views here.

def drop_down_list(request):
    # Define the template file to render
    templatefile = "querysample/countries.html" 
    # Create an instance of the CountriesForm
    countries_form = CountriesForm()
    
    # Check if the request method is POST
    if request.method == "POST":
        # Bind the form with the POST data
        countries_form = CountriesForm(request.POST)
        # Validate the form data
        if countries_form.is_valid():  # Note: corrected 'is_valide' to 'is_valid'
            # Save the form data to the database
            countries_form.save()
            # Return a JSON response indicating success
            return JsonResponse({'success': True})

    # Render the template with the form, whether it's valid or not
    return render(request, templatefile, {'countries_form': countries_form})


def load_states(request):
    # Get the country_id from the GET request parameters
    country_id = request.GET.get('country_id')
    print(country_id)  # Print the country_id for debugging purposes
    
    # Query the State model to get states related to the specified country
    states = Sate.objects.filter(country_id=country_id).values('id', 'name')
    
    # Return the list of states as a JSON response
    return JsonResponse(list(states), safe=False)


def load_cities(request):
    # Get the state_id from the GET request parameters
    state_id = request.GET.get('state_id')
    
    # Query the City model to get cities related to the specified state
    cities = City.objects.filter(state_id=state_id).values('id', 'name')
    
    # Return the list of cities as a JSON response
    return JsonResponse(list(cities), safe=False)
