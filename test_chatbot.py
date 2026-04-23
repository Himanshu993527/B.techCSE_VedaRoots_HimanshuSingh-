#!/usr/bin/env python3
import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_chatbot():
    """Test the chatbot API endpoint"""
    base_url = "http://127.0.0.1:5000"
    
    print("Testing VedaRoots Chatbot API...")
    print(f"HF Token exists: {'Yes' if os.getenv('HF_TOKEN') else 'No'}")
    
    # Test 1: Simple GET request
    try:
        print("\n1. Testing GET request...")
        response = requests.get(f"{base_url}/api/chat?q=hello", timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"GET Request Error: {e}")
    
    # Test 2: POST request with message
    try:
        print("\n2. Testing POST request...")
        payload = {
            "message": "What is Tulsi?",
            "history": []
        }
        response = requests.post(
            f"{base_url}/api/chat",
            json=payload,
            headers={'Content-Type': 'application/json'},
            timeout=30
        )
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"POST Request Error: {e}")
    
    # Test 3: Check if chatbot page loads
    try:
        print("\n3. Testing chatbot page...")
        response = requests.get(f"{base_url}/chatbot.html", timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Page loads: {'Yes' if response.status_code == 200 else 'No'}")
    except Exception as e:
        print(f"Page Load Error: {e}")

if __name__ == "__main__":
    test_chatbot()
