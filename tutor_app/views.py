from django.shortcuts import render, redirect
from .models import Tutor, Course

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        education = request.POST.get('education')
        expertise = request.POST.get('expertise')
        
        # Check if username already exists
        if Tutor.objects.filter(username=username).exists():
            error_message = "Username already exists."
            return render(request, 'register.html', {'error_message': error_message})

        # Create the tutor object
        tutor = Tutor.objects.create(username=username, password=password, name=name, education=education, expertise=expertise)
        
        # Redirect to login page
        return redirect('login')
    
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if username exists
        try:
            tutor = Tutor.objects.get(username=username)
        except Tutor.DoesNotExist:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})

        # Check if password matches
        if tutor.password != password:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
        
        # Set session for logged in user
        request.session['tutor_id'] = tutor.id
        
        # Redirect to profile page
        return redirect('profile')
    
    return render(request, 'login.html')

def logout(request):
    # Clear session
    request.session.clear()
    return redirect('login')

def profile(request):
    # Check if tutor is logged in
    tutor_id = request.session.get('tutor_id')
    if not tutor_id:
        return redirect('login')

    # Get tutor object
    tutor = Tutor.objects.get(id=tutor_id)

    # Get courses created by the tutor
    courses = Course.objects.filter(tutor=tutor)

    return render(request, 'profile.html', {'tutor': tutor, 'courses': courses})

def create_course(request):
    # Check if tutor is logged in
    tutor_id = request.session.get('tutor_id')
    if not tutor_id:
        return redirect('login')

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        video_url = request.POST.get('video_url')
        
        # Get tutor object
        tutor = Tutor.objects.get(id=tutor_id)
        
        # Create the course
        Course.objects.create(tutor=tutor, title=title, description=description, video_url=video_url)
        
        # Redirect to profile page
        return redirect('profile')
    
    return render(request, 'create_course.html')
