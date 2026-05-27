# config.py
# Central location for all configuration settings

# File paths
DATA_PATH = 'Teen_Mental_Health.csv'
MODEL_PATH = 'depression_model.pkl'
SCALER_PATH = 'feature_scaler.pkl'
ENCODER_PATH = 'gender_encoder.pkl'

# Model parameters
RANDOM_STATE = 42
TEST_SIZE = 0.2
N_ESTIMATORS = 100
MAX_DEPTH = 10

# Feature lists
NUMERICAL_FEATURES = [
    'age', 'daily_social_media_hours', 'sleep_hours',
    'screen_time_before_sleep', 'academic_performance',
    'physical_activity'
]

CATEGORICAL_FEATURES = [
    'gender', 'platform_usage', 'digital_wellbeing_flag','social_interaction_level', 'sleep_quality'
]

ALL_FEATURES = NUMERICAL_FEATURES + [
    f'{col}_encoded' for col in CATEGORICAL_FEATURES
]

# Target column
TARGET_COLUMN = 'depression_label'