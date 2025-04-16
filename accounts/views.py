# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# This view handles the user registration process
def register_view(request):
    if request.method == 'POST':  # If the form is submitted
        form = UserCreationForm(request.POST)  # Create the form with the submitted data
        if form.is_valid():  # If the form data is valid
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log the user in immediately after registration
            messages.success(request, 'Registration successful!')  # Display a success message
            return redirect('home')  # Redirect the user to the home page
        else:
            # If there are errors in the form, display them as error messages
            for error in form.errors:
                messages.error(request, form.errors[error])
    else:
        form = UserCreationForm()  # If it's a GET request, just show an empty form
    return render(request, 'registration/register.html', {'form': form})  # Render the registration page with the form

# This view handles user login
def login_view(request):
    if request.method == 'POST':  # If the form is submitted
        form = AuthenticationForm(request, data=request.POST)  # Create the login form with the submitted data
        if form.is_valid():  # If the form data is valid
            username = form.cleaned_data.get('username')  # Get the username from the form
            password = form.cleaned_data.get('password')  # Get the password from the form
            user = authenticate(username=username, password=password)  # Check if the user exists and the password is correct
            if user is not None:  # If authentication is successful
                login(request, user)  # Log the user in
                messages.info(request, f"You are now logged in as {username}.")  # Display a success message
                return redirect('home')  # Redirect the user to the home page
            else:
                messages.error(request, "Invalid username or password.")  # If login failed, show an error message
        else:
            messages.error(request, "Invalid username or password.")  # If the form data is invalid, show an error message
    form = AuthenticationForm()  # If it's a GET request, show an empty login form
    return render(request, 'registration/login.html', {'form': form})  # Render the login page with the form

# This view logs the user out
@login_required  # Ensure the user is logged in before they can log out
def logout_view(request):
    if request.method == 'POST' or request.method == 'GET':  # Handle both POST and GET requests
        logout(request)  # Log the user out
        messages.info(request, "You have successfully logged out.")  # Show a logout success message
        return render(request, 'registration/logout.html')  # Render the logout page

# This view displays the user's profile, but the user must be logged in to access it
@login_required  # Ensure the user is logged in to view their profile
def profile_view(request):
    return render(request, 'registration/profile.html')  # Render the profile page
