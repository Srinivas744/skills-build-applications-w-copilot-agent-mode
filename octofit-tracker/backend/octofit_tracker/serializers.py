from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard
from bson import ObjectId

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for field_name, field_value in data.items():
            if isinstance(field_value, ObjectId):
                data[field_name] = str(field_value)
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for field_name, field_value in data.items():
            if isinstance(field_value, ObjectId):
                data[field_name] = str(field_value)
        return data

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for field_name, field_value in data.items():
            if isinstance(field_value, ObjectId):
                data[field_name] = str(field_value)
        return data

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for field_name, field_value in data.items():
            if isinstance(field_value, ObjectId):
                data[field_name] = str(field_value)
        return data

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for field_name, field_value in data.items():
            if isinstance(field_value, ObjectId):
                data[field_name] = str(field_value)
        return data
