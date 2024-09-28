from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.http import JsonResponse

def login_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        clg_name = request.POST.get('college')
        phone_number = request.POST.get('phone')
        email = request.POST.get('email')

        # Check if the email already exists
        if UserDetails.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already exists. Please use a different email.'}, status=400)

        # Check if the phone number already exists
        if UserDetails.objects.filter(phone_number=phone_number).exists():
            return JsonResponse({'error': 'Phone number already exists. Please use a different phone number.'}, status=400)

        # Store email in session
        request.session['user_email'] = email  

        # Save user details to the database
        user_details = UserDetails(
            name=name,
            clg_name=clg_name,
            phone_number=phone_number,
            email=email
        )
        user_details.save()

        return JsonResponse({'success': 'User registered successfully!'}, status=200)

    return render(request, 'home_page.html')  # Render the form for GET request


# Assuming you already have QuizQuestion and UserDetailsMark models defined
def success_view(request):
    questions = QuizQuestion.objects.all()  # Fetch all QuizQuestion objects
    if request.method == "POST":
        total_marks = 0
        user_email = request.session.get('user_email')  # Get user email from session
        
        # Loop through each question and get the corresponding answer from the request
        for question in questions:
            answer = request.POST.get(f"question_{question.id}")  # Fetch the answer for the specific question
            print(answer)  # Get the answer submitted by the user
            if answer == question.answer:  # Compare with the correct answer
                total_marks += 1  # Increment marks for each correct answer

        # Save the total marks to the UserDetailsMark table
        UserDetailsMark.objects.update_or_create(email=user_email, defaults={'total_marks': total_marks})

        # Redirect to a success page or render a template with results
        return redirect('login')  # Replace with your success page URL

    return render(request, 'question_list.html', {'questions': questions})



def admin_login(request):
    # Get all user details
    user_details = UserDetails.objects.all()

    # Create a dictionary of user marks
    user_marks = {detail.email: detail.total_marks for detail in UserDetailsMark.objects.all()}

    # Sort users by highest marks
    sorted_users = sorted(user_details, key=lambda x: user_marks.get(x.email, 0), reverse=True)

    # Resulting sorted user details with their marks
    sorted_user_details = [(user, user_marks.get(user.email, 0)) for user in sorted_users]

    # Create a combined list of user details and marks
    combined_data = []
    for user, marks in sorted_user_details:  # Unpack the tuple
        combined_data.append({
            'name': user.name,
            'clg_name': user.clg_name,
            'phone_number': user.phone_number,
            'email': user.email,
            'total_marks': marks  # Use the unpacked marks variable
        })
    
    return render(request, 'admin_login.html', {'combined_data': combined_data})
