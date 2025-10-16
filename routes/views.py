from django.shortcuts import render
from .models import Airport
from .forms import AirportRouteForm, SearchNthNodeForm

# Create your views here.

def flight_routes_view(request):
    #initializze forms and variables
    route_form = AirportRouteForm()
    search_form = SearchNthNodeForm()
    nth_node_result = None
    search_error = None

    # to Find Nth Node
    if 'search_submit' in request.POST:
        search_form = SearchNthNodeForm(request.POST)
        if search_form.is_valid():
            start_airport = search_form.cleaned_data['start_airport']
            n_level = search_form.cleaned_data['n_level']
            position = search_form.cleaned_data['position']
            
            # the traversal logic
            current_node = start_airport
            found = True
            for i in range(n_level):
                try:
                    # Find the next child in the chain
                    current_node = current_node.children.get(position=position)
                except Airport.DoesNotExist:
                    # If any child is not found, stop and show an error
                    search_error = f"No {i+1}-level '{position}' node found."
                    found = False
                    break
            
            if found:
                nth_node_result = current_node

    # for adding a new route
    if 'add_route_submit' in request.POST:
        route_form = AirportRouteForm(request.POST)
        if route_form.is_valid():
            route_form.save()
            route_form = AirportRouteForm() # Reset form after saving

    # longest route: order by duration descending and take the first
    longest_route = Airport.objects.filter(duration__isnull=False).order_by('-duration').first()

    # shortest route: order by duration ascending and take the first
    shortest_route = Airport.objects.filter(duration__isnull=False).order_by('duration').first()
    
    context = {
        'route_form': route_form,
        'search_form': search_form,
        'nth_node_result': nth_node_result,
        'search_error': search_error,
        'longest_route': longest_route,
        'shortest_route': shortest_route,
        'all_airports': Airport.objects.all(),
    }
    
    return render(request, 'main.html', context)