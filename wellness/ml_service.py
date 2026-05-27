from functools import lru_cache
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from django.conf import settings


MODEL_DIR = Path(settings.BASE_DIR) / "models"

NUMERICAL_FEATURES = [
    "age",
    "daily_social_media_hours",
    "sleep_hours",
    "screen_time_before_sleep",
    "academic_performance",
    "physical_activity",
]

CATEGORICAL_FEATURES = [
    "gender",
    "platform_usage",
    "digital_wellbeing_flag",
    "social_interaction_level",
    "sleep_quality",
]


class DepressionRiskPredictor:
    def __init__(self, model_dir=MODEL_DIR):
        self.model_dir = Path(model_dir)
        self.model = joblib.load(self.model_dir / "depression_model.pkl")
        self.scaler = joblib.load(self.model_dir / "scaler.pkl")
        self.feature_names = joblib.load(self.model_dir / "feature_names.pkl")
        self.encoders = {
            feature: joblib.load(self.model_dir / f"{feature}_encoder.pkl")
            for feature in CATEGORICAL_FEATURES
        }

    def predict(self, cleaned_data):
        # 1. Get model's raw probability
        frame = pd.DataFrame([cleaned_data])
        for feature in CATEGORICAL_FEATURES:
            frame[f"{feature}_encoded"] = self.encoders[feature].transform([str(frame[feature].iloc[0])])[0]

        values = {}
        for feature in self.feature_names:
            values[feature] = frame[feature].iloc[0]

        prediction_frame = pd.DataFrame([values], columns=self.feature_names).astype(float)
        prediction_frame[NUMERICAL_FEATURES] = self.scaler.transform(prediction_frame[NUMERICAL_FEATURES])

        model_probability = float(self.model.predict_proba(prediction_frame)[0][1])

        # 2. Calculate rule-based risk score
        rule_score = self._calculate_rule_score(cleaned_data)

        # 3. Blend model probability and rule-based score
        # We'll give the rule score a 60% weight and the model probability 40%
        hybrid_score = (rule_score * 0.6) + (model_probability * 0.4)

        # 4. Determine final risk level based on the hybrid score
        risk_level = self._risk_level(hybrid_score)
        summary = self._summary(hybrid_score)

        # If the hybrid score is low, the confidence should be high (1 - probability)
        if risk_level == "Low Risk":
            confidence = 1 - model_probability
        else:
            confidence = model_probability

        return {
            "risk_level": risk_level,
            "summary": summary,
            "model_confidence": round(confidence * 100, 1),
        }

    def _calculate_rule_score(self, data):
        score = 0
        # Rule 1: Very low sleep hours (e.g., <= 3)
        if data.get("sleep_hours", 8) <= 3:
            score += 0.4
        # Rule 2: Very high social media usage (e.g., >= 5 hours)
        if data.get("daily_social_media_hours", 0) >= 5:
            score += 0.3
        # Rule 3: Poor sleep quality
        if data.get("sleep_quality") == "Poor":
            score += 0.3
        # Rule 4: Low academic performance
        if data.get("academic_performance") == "Poor":
            score += 0.2
        
        # Normalize score to be between 0 and 1
        return min(score, 1.0)

    def _risk_level(self, score):
        if score >= 0.5:
            return "High Risk"
        if score >= 0.25:
            return "Moderate Risk"
        return "Low Risk"

    def _summary(self, score):
        if score >= 0.5:
            return "The analysis indicates a combination of factors that significantly increase risk."
        if score >= 0.25:
            return "The analysis found some factors that may suggest an elevated risk."
        return "The analysis suggests a lower-risk profile based on the provided answers."


@lru_cache(maxsize=1)
def get_predictor():
    return DepressionRiskPredictor()
