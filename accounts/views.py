import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def read_json(request):
    try:
        return json.loads(request.body or b"{}")
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None

@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Use POST"}, status=405)
    data = read_json(request)
    if data is None:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    user = authenticate(request, username=data.get("username", ""), password=data.get("password", ""))
    if user is None:
        return JsonResponse({"error": "Invalid username or password"}, status=401)
    login(request, user)
    return JsonResponse({"message": "Login successful", "username": user.username})

@csrf_exempt
def logout_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Use POST"}, status=405)
    logout(request)
    return JsonResponse({"message": "Logout successful"})

@csrf_exempt
def register_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Use POST"}, status=405)
    data = read_json(request)
    if data is None:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    username = str(data.get("username", "")).strip()
    password = str(data.get("password", ""))
    email = str(data.get("email", "")).strip()
    first_name = str(data.get("first_name", "")).strip()
    last_name = str(data.get("last_name", "")).strip()
    if not username or not password:
        return JsonResponse({"error": "Username and password are required"}, status=400)
    if User.objects.filter(username=username).exists():
        return JsonResponse({"error": "Username already exists"}, status=409)
    user = User.objects.create_user(username=username, password=password, email=email,
                                    first_name=first_name, last_name=last_name)
    return JsonResponse({"message": "Registration successful", "username": user.username}, status=201)
