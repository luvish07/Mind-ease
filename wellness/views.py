from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import DepressionRiskForm, GratitudeForm
from .ml_service import get_predictor
from .models import GratitudeEntry


def home(request):
    gratitude_form = GratitudeForm()
    risk_form = DepressionRiskForm()
    prediction_result = None

    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "gratitude":
            gratitude_form = GratitudeForm(request.POST)
            if gratitude_form.is_valid():
                GratitudeEntry.objects.create(text=gratitude_form.cleaned_data["gratitude"])
                messages.success(request, "Thank you for sharing your light today. Keep it with you.")
                return redirect(f"{reverse('wellness:home')}#tools")

        if form_type == "risk":
            risk_form = DepressionRiskForm(request.POST)
            if risk_form.is_valid():
                prediction_result = get_predictor().predict(risk_form.cleaned_data)

    latest_entry = GratitudeEntry.objects.first()

    context = {
        "gratitude_form": gratitude_form,
        "risk_form": risk_form,
        "prediction_result": prediction_result,
        "latest_gratitude": latest_entry.text if latest_entry else "",
        "stats": [
            {
                "value": "1 in 5",
                "label": "Adults",
                "description": "Experience a mental health condition each year globally.",
            },
            {
                "value": "50%",
                "label": "Of Lifetime Illness",
                "description": "Begins by age 14, making early awareness vital.",
            },
            {
                "value": "10 Min",
                "label": "Daily Practice",
                "description": "Of mindfulness can drastically reduce stress and anxiety levels.",
            },
        ],
        "crisis_contacts": [
            {"region": "Mauritius", "contact": "Contact a friend"},
            
            {"region": "International", "contact": "Befrienders Worldwide"},
        ],
        "resources": [
            
            {"name": "Mental Health Foundation", "url": "https://www.mentalhealth.org.uk"},
            {"name": "WHO Resources", "url": "https://www.who.int"},
        ],
    }
    return render(request, "wellness/home.html", context)
