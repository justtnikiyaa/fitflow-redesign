# FitFlow Redesign

A full-scale redesign of the **FitFlow** fitness tracking app using human-centered design (HCI) principles and a modern, high-performance technology stack.

Repository: [https://github.com/justtnikiyaa/fitflow-redesign.git](https://github.com/justtnikiyaa/fitflow-redesign.git)

---

## Tech Stack Summary

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend** | React Native (iOS / Android / Web) | Cross-platform mobile UI with native performance |
| **Backend** | Node.js + NestJS | Scalable, modular enterprise API gateway & business logic |
| **AI Service** | Python + FastAPI | Microservice for ML model inference and computer vision |
| **Primary Database** | PostgreSQL | Relational storage for user profiles, workouts, and transactions |
| **Real-time Database** | Firebase Firestore | Real-time synchronization for community feed and social chats |
| **Authentication** | Firebase Authentication | Secure multi-provider auth (OAuth, Email/Password, JWT) |
| **Cache & Queues** | Redis | In-memory caching, rate-limiting, and background task queues |

---

## Key Features

- 🤖 **AI-Powered Personalized Workout Plans**: Adaptive training regimens calculated using individual biometric data, recovery metrics, and workout history.
- 📸 **Camera-Based Nutrition Logging**: Computer-vision powered meal logging that recognizes food items from photos and automatically estimates macronutrients and calories.
- 👥 **Real-Time Social Community**: Activity sharing feeds, friend challenges, peer encouragement, and leaderboard interactions powered by real-time Firestore sync.
- 📊 **Interactive Progress Dashboards**: Visual analytics tracking body composition, strength milestones, and cardiovascular trends over time.

---

## Folder Structure

```
fitflow-redesign/
├── frontend/             # React Native app
│   ├── src/
│   │   ├── screens/      # Application screens & views
│   │   ├── components/   # Reusable UI components
│   │   ├── navigation/   # Stack & tab navigators
│   │   └── services/     # API clients & state integration
│   └── package.json
├── backend/              # NestJS API Gateway & Core Service
│   ├── src/
│   │   ├── modules/      # Feature modules (workouts, nutrition, users)
│   │   ├── auth/         # Firebase Auth guards & RBAC
│   │   └── main.ts       # Application entry point
│   └── package.json
├── ai-service/           # Python FastAPI ML Microservice
│   ├── app/
│   │   ├── models/       # PyTorch/TFLite/ONNX inference pipelines
│   │   ├── routers/      # FastAPI route controllers
│   │   └── main.py       # ASGI app entry point
│   └── requirements.txt
├── docs/                 # Project documentation & design records
│   ├── architecture-diagram.png
│   ├── tech-stack-summary.md
│   ├── comparison-matrix.md
│   └── ADR.md
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml        # GitHub Actions CI pipeline
└── README.md
```

---

## Setup & Running Services

### 1. Frontend (React Native)
```bash
cd frontend
npm install
# For iOS:
npx pod-install
npm run ios
# For Android:
npm run android
# For Web / Expo (if configured):
npm start
```

### 2. Backend (NestJS)
```bash
cd backend
npm install
# Set up environment variables (.env)
npm run start:dev
```
Backend API will be available at `http://localhost:3000`.

### 3. AI Service (Python FastAPI)
```bash
cd ai-service
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
FastAPI interactive docs (Swagger) will be available at `http://localhost:8000/docs`.

---

## Documentation

- [Architecture Diagram](docs/architecture-diagram.png)
- [Tech Stack Summary](docs/tech-stack-summary.md)
- [Tech Stack Comparison Matrix](docs/comparison-matrix.md)
- [Architecture Decision Record (ADR)](docs/ADR.md)
