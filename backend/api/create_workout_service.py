import os
import json
import re
import logging
import google.generativeai as genai
from garmin_workouts_mcp import main

# Model name used in your existing script
MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

logger = logging.getLogger(__name__)

def create_workout_from_text(text: str):
    """
    Convert the text workout to structured JSON via Gemini and upload to Garmin.
    Returns the result from the upload (e.g. {"workoutId": "<id>"}).
    """
    # Ensure Garmin session
    main.login()

    # Get the prompt text using existing tool
    prompt_dict = main.generate_workout_data_prompt.fn(text)
    prompt_text = prompt_dict["prompt"]

    # Configure Gemini
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set")

    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel(MODEL)

    logger.info("Calling Gemini model: %s", MODEL)
    response = model.generate_content(prompt_text)
    workout_json_str_raw = response.text

    # Try to extract JSON inside ```json ... ``` code block, otherwise try to find JSON object
    match = re.search(r"```json\s*(.*?)\s*```", workout_json_str_raw, re.DOTALL)
    if match:
        workout_json_str = match.group(1).strip()
    else:
        # Fallback: attempt to grab the first top-level JSON object found
        json_match = re.search(r"(\{.*\})", workout_json_str_raw, re.DOTALL)
        if json_match:
            workout_json_str = json_match.group(1).strip()
        else:
            workout_json_str = workout_json_str_raw.strip()

    # Parse JSON
    try:
        workout_json = json.loads(workout_json_str)
    except json.JSONDecodeError:
        logger.error("Failed to parse JSON from Gemini response. Raw response:\n%s", workout_json_str_raw)
        raise

    # Upload using existing tool (keeps behaviour identical)
    result = main.upload_workout.fn(workout_json)
    return result
