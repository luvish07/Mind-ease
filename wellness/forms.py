from django import forms


FORM_INPUT_CLASS = "w-full px-4 py-2 text-sm border border-[#E8E3DD] rounded-xl focus:outline-none focus:border-[#3B5848] bg-[#FBF9F6]"


class GratitudeForm(forms.Form):
    gratitude = forms.CharField(
        label="",
        max_length=160,
        widget=forms.TextInput(
            attrs={
                "class": FORM_INPUT_CLASS,
                "placeholder": "One thing you're grateful for today...",
            }
        ),
    )


class DepressionRiskForm(forms.Form):
    GENDER_CHOICES = [("female", "Female"), ("male", "Male")]
    PLATFORM_CHOICES = [
        ("All Platforms", "All Platforms"),
        ("Facebook", "Facebook"),
        ("Instagram", "Instagram"),
        ("TikTok", "TikTok"),
        ("YouTube", "YouTube"),
    ]
    WELLBEING_CHOICES = [
        ("Healthy", "Healthy"),
        ("Moderate", "Moderate"),
        ("At Risk", "At Risk"),
    ]
    INTERACTION_CHOICES = [
        ("high", "High"),
        ("medium", "Medium"),
        ("low", "Low"),
    ]
    SLEEP_QUALITY_CHOICES = [
        ("Good", "Good"),
        ("Fair", "Fair"),
        ("Poor", "Poor"),
    ]

    age = forms.IntegerField(min_value=10, max_value=30, widget=forms.NumberInput(attrs={"class": FORM_INPUT_CLASS}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={"class": FORM_INPUT_CLASS}))
    daily_social_media_hours = forms.FloatField(
        min_value=0,
        max_value=24,
        label="Daily social media hours",
        widget=forms.NumberInput(attrs={"class": FORM_INPUT_CLASS, "step": "0.5"}),
    )
    platform_usage = forms.ChoiceField(
        choices=PLATFORM_CHOICES,
        label="Most used platform",
        widget=forms.Select(attrs={"class": FORM_INPUT_CLASS}),
    )
    sleep_hours = forms.FloatField(
        min_value=0,
        max_value=24,
        widget=forms.NumberInput(attrs={"class": FORM_INPUT_CLASS, "step": "0.5"}),
    )
    screen_time_before_sleep = forms.FloatField(
        min_value=0,
        max_value=12,
        label="Screen time before sleep",
        widget=forms.NumberInput(attrs={"class": FORM_INPUT_CLASS, "step": "0.5"}),
    )
    academic_performance = forms.IntegerField(
        min_value=1,
        max_value=5,
        label="Academic performance",
        widget=forms.NumberInput(attrs={"class": FORM_INPUT_CLASS}),
    )
    physical_activity = forms.IntegerField(
        min_value=1,
        max_value=5,
        label="Physical activity",
        widget=forms.NumberInput(attrs={"class": FORM_INPUT_CLASS}),
    )
    social_interaction_level = forms.ChoiceField(
        choices=INTERACTION_CHOICES,
        label="Social interaction level",
        widget=forms.Select(attrs={"class": FORM_INPUT_CLASS}),
    )
    sleep_quality = forms.ChoiceField(
        choices=SLEEP_QUALITY_CHOICES,
        widget=forms.Select(attrs={"class": FORM_INPUT_CLASS}),
    )
    digital_wellbeing_flag = forms.ChoiceField(
        choices=WELLBEING_CHOICES,
        label="Digital wellbeing",
        widget=forms.Select(attrs={"class": FORM_INPUT_CLASS}),
    )
