import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Dealer, Review

def dealer_json(dealer):
    return {"id": dealer.id, "name": dealer.name, "city": dealer.city, "state": dealer.state,
            "address": dealer.address, "phone": dealer.phone, "website": dealer.website}

def home_view(request):
    dealers = Dealer.objects.all().order_by("state", "name")
    return render(request, "home.html", {"dealers": dealers})

def dealers_list(request):
    return JsonResponse({"dealers": [dealer_json(d) for d in Dealer.objects.all().order_by("id")]})

def dealers_by_state(request, state):
    qs = Dealer.objects.filter(state__iexact=state).order_by("name")
    return JsonResponse({"state": state, "dealers": [dealer_json(d) for d in qs]})

def dealer_detail(request, dealer_id):
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    return JsonResponse({"dealer": dealer_json(dealer)})

def dealer_reviews(request, dealer_id):
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    reviews = dealer.reviews.order_by("-created_at")
    return JsonResponse({"dealer_id": dealer.id, "reviews": [
        {"id": r.id, "name": r.name, "review": r.review, "sentiment": r.sentiment,
         "created_at": r.created_at.isoformat()} for r in reviews
    ]})

@csrf_exempt
def create_review(request, dealer_id):
    if request.method != "POST":
        return JsonResponse({"error": "Use POST"}, status=405)
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    try:
        data = json.loads(request.body or b"{}")
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    body = str(data.get("review", "")).strip()
    name = str(data.get("name", "Guest")).strip() or "Guest"
    if not body:
        return JsonResponse({"error": "Review text is required"}, status=400)
    sentiment = classify_sentiment(body)
    review = Review.objects.create(dealer=dealer, name=name, review=body, sentiment=sentiment,
                                   user=request.user if request.user.is_authenticated else None)
    return JsonResponse({"message": "Review created", "id": review.id, "sentiment": sentiment}, status=201)

def classify_sentiment(text):
    positive = {"fantastic", "great", "excellent", "good", "amazing", "wonderful", "helpful", "love"}
    negative = {"bad", "poor", "terrible", "awful", "worst", "hate", "rude", "slow"}
    words = {w.strip(".,!?;:").lower() for w in text.split()}
    score = len(words & positive) - len(words & negative)
    return "positive" if score > 0 else ("negative" if score < 0 else "neutral")

def analyze_review(request):
    if request.method != "POST":
        return JsonResponse({"error": "Use POST"}, status=405)
    try:
        data = json.loads(request.body or b"{}")
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    text = str(data.get("review", data.get("text", "")))
    return JsonResponse({"review": text, "sentiment": classify_sentiment(text)})

def car_makes(request):
    return JsonResponse({"car_makes": [
        {"make": "Toyota", "models": ["Camry", "Corolla", "RAV4"]},
        {"make": "Honda", "models": ["Civic", "Accord", "CR-V"]},
        {"make": "Ford", "models": ["F-150", "Escape", "Mustang"]},
        {"make": "Chevrolet", "models": ["Malibu", "Equinox", "Silverado"]}
    ]})
