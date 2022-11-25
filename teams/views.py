from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from teams.models import Team
from django.forms.models import model_to_dict

class TeamView(APIView):

    def post(self, request):
      
        team = Team.objects.create(**request.data)

        return Response(model_to_dict(team), 201)

    def get(self, request):

        teams = Team.objects.all()

        team_dict_list = [model_to_dict(team) for team in teams]

        return Response(team_dict_list)

class TeamDetailView(APIView):

    def get(self, request, team_id):

        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({'message': 'Team not found'}, 404)

        return Response(model_to_dict(team))

    def patch(self, request, team_id):
        
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({'message': 'Team not found'}, 404)
        
        for key, value in request.data.items():
            setattr(team, key, value)

        team.save()

        return Response(model_to_dict(team), 200)

    def delete(self, request, team_id):

        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({'message': 'Team not found'}, 404)
        
        team.delete()

        return Response(status=204)
