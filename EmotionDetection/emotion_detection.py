import requests # Import the requests library to handle HTTP requests
import json # Import the json library to allow json formatting

def emotion_detector(text_to_analyse): # Define a function named emotion_detector that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # URL of the emotion detector service
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # Set the headers required for the API request
    myobj = { "raw_document": { "text": text_to_analyse } } # Create a dictionary with the text to be analyzed
    
    response = requests.post(url, json = myobj, headers=headers) # Send a POST request to the API with the text and headers
    parsed_response = json.loads(response.text) # Format the response into json
    
    emotions = parsed_response['emotionPredictions'][0]['emotion'] # Navigate to the emotion data
    
    required_keys = ["anger", "disgust", "fear", "joy", "sadness"] # Create a list of the needed emotion keys
    result = {key: emotions[key] for key in required_keys if key in emotions} # Iterate through the json response to find required emotions and scores
    
    dominant = max(result, key=result.get) # Determine dominant emotion (highest score)
    result["dominant_emotion"] = dominant
    return result