🏃‍♂️ Garmin Workout Creator (AI-Powered)

Create Garmin workouts instantly from plain text using **Google Gemini** and upload them directly to **Garmin Connect**.


## 🚀 How It Works

All you have to do is:

1. Set up your `.env` file:

   ```bash
   GARMIN_EMAIL=
   GARMIN_PASSWORD=
   GEMINI_API_KEY=
   ```
2. Open `create_workout_from_text.py` and modify this part:

   ```python
   text_workout = """
   PASTE YOUR WORKOUT HERE!!!!!!!!!!!!
   """
   ```
3. Run it:

   ```bash
   python3 create_workout_from_text.py
   ```
4. Wait for the upload message:
   ✅ “Workout uploaded successfully!”

Then check your workout on Garmin Connect:
👉 [https://connect.garmin.com/modern/workouts](https://connect.garmin.com/modern/workouts)


## ⚙️ Setup Instructions

### 1️⃣ Install dependencies

```bash
pip install garth fastmcp python-dotenv google-generativeai
```

### 2️⃣ Copy `.env.example` → `.env` and fill in your credentials

### 3️⃣ Run the script

```bash
python3 create_workout_from_text.py
```
or alternatively run:
```bash
dotenv run -- python create_workout_from_text.py
```

----

## 🧠 Example

```python
text_workout = """
10min Z3
2 min rec
15x250m at 10k pace 150m jog
"""
```

In less than **15 seconds**, the script:

* Logs into Garmin Connect
* Uses **Gemini** to convert your text into a structured JSON
* Uploads it automatically
* You can then edit or schedule it in Garmin Connect.