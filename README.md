# 🏃‍♂️ Garmin NLP Workouts — Full Stack App

This project converts **natural language workout descriptions** (e.g. “4 × 8min @ HM pace with 2min jog recovery”) into **structured Garmin workouts** that can be uploaded to your Garmin Connect account.



https://github.com/user-attachments/assets/84cc5d19-a4db-4b22-9e3c-16879d75a60d



Built with:
- 🧠 **FastAPI (Python)** backend — parses text and communicates with Garmin Connect  
- 💡 **Gemini API** — interprets workout text into structured JSON  
- ⚛️ **Next.js (React)** frontend — clean UI to input text and trigger workout creation

---

## 🧩 Project Structure

```

garmin-workouts-mcp/
│
├── backend/                  # FastAPI app
│   ├── app.py               # API entry point (server)
│   ├── create_workout_from_text.py
│   ├── main.py
│   └── ...
│
├── frontend/                 # Next.js app
│   ├── app/
│   │   ├── page.js
│   │   ├── layout.js
│   │   └── globals.css
│   ├── package.json
│   └── ...
│
├── .gitignore
└── README.md

```

---

## ⚙️ Environment Setup

### 1. Clone the repository

```bash
git clone https://github.com/brahimi73837/garmin-workout-full-stack.git
cd garmin-workouts-full-stack
````

---

### 2. Backend Setup (FastAPI)

#### Create a virtual environment

```bash
cd backend
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or venv\Scripts\activate  # Windows
```

#### Install dependencies

```bash
pip install fastapi garth fastmcp python-dotenv google-generativeai
```

#### Set environment variables

Create a `.env` file inside `backend/`:

```
GEMINI_API_KEY=your_gemini_api_key_here
GARMIN_EMAIL=your_garmin_email
GARMIN_PASSWORD=your_garmin_password
```

#### Run the server

```bash
uvicorn main:app --reload
```

By default, the backend runs at:
👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

You can test health:

```
GET http://127.0.0.1:8000/health
```

Expected response:

```json
{ "status": "ok" }
```

---

### 3. Frontend Setup (Next.js)

Open another terminal window:

```bash
cd frontend
npm install
npm run dev
```

or 
```bash
cd frontend
next dev
```

The frontend runs at:
👉 **[http://localhost:3000](http://localhost:3000)**

---

## 🧠 How It Works

1. You enter a natural-language workout (e.g. `4 x 8min @ HM pace with 2min recovery`)
2. The frontend sends a POST request to the backend `/create-workout` endpoint.
3. The backend uses Gemini to generate structured workout JSON.
4. The workout is automatically uploaded to Garmin Connect.
5. The UI shows the created `workoutId` and a link to view it on Garmin.

---

## 📬 Example API Call (via Postman)

**Endpoint:**

```
POST http://127.0.0.1:8000/create-workout
```

**Body (JSON):**

```json
{
  "text": "20min warmup\n4 x 8min @ HM pace with 2min jog recovery\n10min cooldown"
}
```

**Response:**

```json
{
  "status": "success",
  "result": {
    "workoutId": "1350279627"
  }
}
```

---

## 🧰 Tech Stack


| Layer      | Technology                |
| ------------ | --------------------------- |
| Backend    | FastAPI, Python 3.13      |
| AI Parsing | Gemini API                |
| Frontend   | Next.js 15 + Tailwind CSS |

---
