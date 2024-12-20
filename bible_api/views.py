from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .serializers import QuestionSerializer, GuidanceResponseSerializer
from ai_agents import get_biblical_guidance
import logging

# Set up logging
logger = logging.getLogger(__name__)

class HealthCheckView(APIView):
    def get(self, request):
        return JsonResponse({
            "status": "online",
            "message": "His Word API is running",
            "endpoints": {
                "/": "API documentation",
                "/api/guidance": "POST - Get biblical guidance for your question"
            }
        })

class GuidanceView(APIView):
    def post(self, request):
        try:
            serializer = QuestionSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(
                    {"error": "Please provide a valid question"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            question = serializer.validated_data['question']
            if not question.strip():
                return Response(
                    {"error": "Question cannot be empty"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            logger.info(f"Processing guidance request for question: {question}")
            result = get_biblical_guidance(question)

            response_serializer = GuidanceResponseSerializer(data={
                "success": True,
                "guidance": result["guidance"],
                "scenario": result["scenario"],
                "analysis": result["analysis"]
            })
            
            if response_serializer.is_valid():
                return Response(response_serializer.data)
            else:
                logger.error(f"Response serialization error: {response_serializer.errors}")
                return Response(
                    {"error": "Error formatting response"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        except Exception as e:
            logger.error(f"Error processing guidance request: {str(e)}")
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
