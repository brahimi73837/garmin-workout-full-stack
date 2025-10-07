# #!/usr/bin/env python3
# """
# Script to create a Garmin Connect workout from a text description
# using Gemini to generate the structured workout JSON.
# """

# import os
# import json
# import re
# import google.generativeai as genai
# from garmin_workouts_mcp import main

# MODEL = "gemini-2.5-flash"


# # -----------------------------
# # FUNCTIONS
# # -----------------------------
# def create_workout_from_text(text: str):
#     """Convert text workout to structured JSON and upload to Garmin."""

#     # 1️⃣ Login to Garmin
#     main.login()

#     # 2️⃣ Generate prompt using repo function
#     prompt_dict = main.generate_workout_data_prompt.fn(text)
#     prompt_text = prompt_dict["prompt"]

#     # 3️⃣ Query Gemini API
#     gemini_api_key = os.environ.get("GEMINI_API_KEY")
#     if not gemini_api_key:
#         raise ValueError("GEMINI_API_KEY environment variable not set")

#     genai.configure(api_key=gemini_api_key)

#     # --------------------------------------------------------------------------

#     model = genai.GenerativeModel(MODEL)

#     response = model.generate_content(prompt_text)

#     # Extract the text content from the response
#     workout_json_str_raw = response.text

#     # --- NEW: Extract JSON from markdown code block if present ---
#     # Use a regular expression to find the content within ```json ... ```
#     match = re.search(r"```json\s*(.*?)\s*```", workout_json_str_raw, re.DOTALL)
#     if match:
#         workout_json_str = match.group(1).strip()
#     else:
#         # If no markdown block is found, assume the raw response is the JSON
#         workout_json_str = workout_json_str_raw.strip()
#     # ------------------------------------------------------------

#     try:
#         workout_json = json.loads(workout_json_str)
#     except json.JSONDecodeError as e:
#         print("Failed to parse JSON from Gemini response:")
#         print(workout_json_str_raw)  # Print the raw response for debugging
#         raise e

#     # 4️⃣ Upload workout to Garmin
#     result = main.upload_workout.fn(workout_json)
#     return result


# # -----------------------------
# # MAIN
# # -----------------------------
# if __name__ == "__main__":
#     text_workout = """
#     10min Z3
#     2 min rest
#     4x1500m + 3x200
#     1500m on HM pace
#     200m progressive to the max rec 200m
#     set rest 2min
#     rest btw 1500m is Z0
#     """

#     result = create_workout_from_text(text_workout)
#     print("Workout uploaded successfully:", result)
