# Technology Stack Summary: FitFlow Redesign

**Project:** FitFlow Fitness Tracking App Redesign (HCI Lab Exercise 05)  
**Institution:** SLIIT — BSc (Hons) in Information Technology — Year 3, Semester 2  
**Module:** IT3060 – Human Computer Interaction  

---

## 1. Executive Summary & Context

FitFlow, a mid-sized health-tech startup fitness tracking application, suffered a drop in retention rates and app store ratings (declining from 4.6 to 3.8 stars). User research revealed that **68% of users abandoned the app shortly after onboarding** due to tedious manual nutrition logging, generic non-adaptive workout routines, and social isolation during fitness journeys. 

To overcome these user pain points and fulfill the requirements of personas **Alex Rivera** (busy professional needing quick, adaptive workouts) and **Priya Singh** (beginner seeking social accountability), the FitFlow redesign adopts a modern, polyglot microservice architecture:
- **Mobile Client:** React Native (cross-platform iOS, Android, and Web)
- **Core Backend / API Gateway:** Node.js + NestJS
- **AI / Computer Vision Microservice:** Python + FastAPI
- **Databases:** PostgreSQL (Relational/Health Data) + Firebase Firestore (Real-Time Social Dynamics)
- **Authentication:** Firebase Authentication
- **Caching & Rate Limiting:** Redis

---

## 2. Frontend Analysis & Evaluation (Activity 1)

### 2.1 Candidate Comparison Across Key Criteria

| Evaluation Criteria | React Native | Flutter | Kotlin Multiplatform (KMP) | Swift / SwiftUI |
| :--- | :--- | :--- | :--- | :--- |
| **Development Speed** | **Very High** (Fast Refresh, vast npm ecosystem, shared JS/TS logic) | High (Hot Reload, Dart widget tree) | Moderate (Shared business logic, separate native UIs) | Moderate (iOS only, requires duplicate Android work) |
| **Code Reusability** | **High (85–90%)** across iOS, Android, and Web (via React Native for Web) | High (90%+) across mobile/web/desktop | Moderate (50–70%, primarily logic, not UI) | Very Low (0% for Android/Web; iOS/macOS only) |
| **Runtime Performance** | **High** (New Architecture: Fabric renderer + TurboModules + JSI, 60–120 FPS) | High (Skia/Impeller direct rendering engine) | **Native** (Compiles directly to native bytecode) | **Native** (Best iOS performance and memory efficiency) |
| **Ecosystem & Libraries**| **Massive** (npm ecosystem, Reanimated 3, Gesture Handler, Expo modules) | Strong & growing (pub.dev), but fewer enterprise third-party SDKs | Growing, but limited UI ecosystem | Rich iOS-specific ecosystem (HealthKit, CoreML) |
| **Learning Curve** | **Low to Moderate** (Ubiquitous JavaScript/TypeScript and React paradigm) | Moderate (Requires learning Dart language & widget paradigm) | High (Requires Kotlin expertise, Gradle, and native iOS tooling) | Low for iOS devs, High overall (Swift/SwiftUI + separate Kotlin for Android) |
| **Web Compatibility** | **Excellent** (React Native for Web allows identical component sharing) | Good (CanvasKit rendering, larger initial bundle sizes) | Moderate (Kotlin/Wasm is still maturing) | None (Requires separate Web technology like React) |
| **AI/ML Integration** | **High** (TensorFlow Lite, ONNX Runtime Mobile, OpenCV bindings) | Moderate (tflite_flutter, but plugin maintenance varies) | Moderate (Requires native platform bridging) | **Very High** on iOS (CoreML/Vision), but zero Android support |
| **Real-Time Features** | **High** (First-class Firebase SDK, WebSockets, Socket.io) | High (Firebase FlutterFire, WebSockets) | Moderate (Native WebSocket implementations) | High (Native WebSockets, Firebase iOS SDK) |
| **Maintenance Cost** | **Low** (Single codebase, single team skill set in TypeScript) | Low to Moderate (Single codebase, specialized Dart engineers) | Moderate to High (Requires Kotlin + Swift engineers) | **Very High** (Requires two separate engineering teams) |
| **Security & Privacy** | **High** (Encrypted SQLite/Keychain, Hermes bytecode compilation) | High (Compiled native binaries) | **Very High** (Native platform security models) | **Very High** (Native iOS Secure Enclave & Keychain) |

### 2.2 Suitability for FitFlow & Final Frontend Recommendation
- **Decision:** **React Native** (with TypeScript and Expo/Reanimated 3).
- **Justification:** FitFlow requires simultaneous iOS and Android deployment with an intuitive, fluid user experience (60–120 fps micro-animations) to engage users like Alex and Priya. React Native offers native hardware camera integration for computer-vision food logging, seamless integration with Firebase for real-time social feeds, and shared TypeScript types with the NestJS backend, maximizing engineering velocity and reducing maintenance overhead for a mid-sized team.

---

## 3. Backend, Database & Authentication Analysis (Activity 2)

### 3.1 Backend Framework Comparison

| Criteria | Node.js + NestJS | Python + FastAPI | Go (Gin / Fiber) |
| :--- | :--- | :--- | :--- |
| **Architecture & Structure** | **Enterprise Modular** (Angular-inspired, DI, strict TypeScript decorators) | Lightweight / Declarative (Pydantic models, ASGI routing) | Minimalist (Requires manual project structuring) |
| **Throughput & Async I/O** | **High** (V8 event loop, non-blocking asynchronous I/O) | High (uvicorn/asyncio, Starlette core) | **Extreme** (Goroutines, minimal memory footprint) |
| **AI/ML & CV Ecosystem** | Moderate (Bridges via child processes or REST/gRPC) | **Industry Standard** (Direct PyTorch, TensorFlow, OpenCV, Hugging Face) | Low (Immature ML/CV ecosystem, usually calls Python) |
| **Type Safety & Maintainability** | **Excellent** (End-to-end TypeScript shared with React Native) | High (Python type hints + Pydantic validation) | **Excellent** (Statically typed compiled language) |
| **Developer Velocity** | **Very High** for CRUD, Auth, and Business Logic | **Very High** for ML services & API prototyping | Moderate (More boilerplate code required) |

**Recommendation:** A **Polyglot Microservice Architecture**:
1. **Node.js + NestJS** as the Primary API Gateway and Transactional Backend.
2. **Python + FastAPI** as the dedicated AI / Computer Vision Microservice for meal recognition and adaptive workout modeling.

---

### 3.2 Database Options Comparison

| Database | Data Model | Scalability & Query Performance | Health & Fitness Data Handling | Real-Time Support | Best Fit in FitFlow |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **PostgreSQL** | Relational (SQL + JSONB) | High read/write throughput, advanced B-tree/GIN indexing, ACID compliant | **Ideal:** Strict schema for user biometric history, workout logs, billing, and HIPAA/GDPR audit trails | Low (Requires LISTEN/NOTIFY or polling) | **Primary Database** |
| **Firebase Firestore**| NoSQL Document | Auto-scaling horizontal document store | Moderate: Less suited for complex analytical joins over time | **Native / Sub-second:** Real-time listeners and offline sync | **Real-Time Social Layer** |
| **MongoDB** | NoSQL Document | Good horizontal sharding, flexible schema | Good for flexible logs, but lacks native real-time mobile sync of Firestore | Moderate (Change streams require server connection) | Alternative, rejected for dual-engine |
| **AWS DynamoDB** | NoSQL Key-Value | Extreme single-digit ms latency at scale | Good for time-series logs, but query flexibility is constrained | Requires AWS AppSync / DynamoDB Streams | Overkill / Vendor lock-in |

**Recommendation:** **Hybrid Database Architecture (PostgreSQL + Firebase Firestore)**:
- **PostgreSQL:** Stores structured, relational, sensitive data (user accounts, biometric measurements, historical workout tracking, nutrition records, GDPR consent logs).
- **Firebase Firestore:** Powers the real-time social community feed, peer challenges, workout comments, and live group activity.

---

### 3.3 Authentication & Authorization Solutions

| Solution | Security & Compliance | Real-Time Sync | Mid-Sized Team Cost | Integration Complexity | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Firebase Auth** | **GDPR/HIPAA compliant**, secure token issuance, built-in rate limiting | Direct integration with Firestore rules | **Generous free tier**, highly cost-effective | **Very Low** (Out-of-the-box SDKs for React Native & Node.js) | **Recommended** |
| **Auth0** | Enterprise-grade compliance (HIPAA, SOC2, GDPR) | Webhook-based | Very expensive as monthly active users (MAU) scale | Moderate | Rejected (Cost barrier) |
| **AWS Cognito** | High compliance, IAM integration | Requires AppSync | Low base cost, complex pricing tiers | **High** (Steep learning curve, cumbersome UI/SDK) | Rejected (DX friction) |
| **Supabase Auth** | Strong (PostgreSQL RLS, open-source) | Realtime PostgreSQL | Moderate | Moderate (Requires tying into Supabase stack) | Alternative |

**Recommendation:** **Firebase Authentication** for turn-key multi-provider sign-in (Google, Apple, Email), zero password storage liabilities, and seamless JWT integration with NestJS guards.

---

## 4. Final Recommended Stack Table

| Layer | Technology | Version / Tooling | Justification & Role in FitFlow |
| :--- | :--- | :--- | :--- |
| **Mobile Client** | React Native | >= 0.74 (Expo SDK 51) | Cross-platform mobile UX, 60fps animations, native camera hardware access. |
| **API Gateway / Core** | NestJS (Node.js) | 10.x / Node 20 LTS | Structured modular architecture, TypeScript type safety, business logic. |
| **AI Microservice** | FastAPI (Python) | 0.110+ / Python 3.11 | Food image recognition (YOLO/OpenCV), adaptive AI workout generation. |
| **Relational Database** | PostgreSQL | 16.x | ACID compliance, strict health data schema, GDPR/HIPAA audit logs. |
| **Realtime Database** | Firebase Firestore | Cloud Firestore | Live community feed, friend challenges, real-time message sync, offline caching. |
| **Authentication** | Firebase Auth | v10+ SDK | Multi-provider OAuth, secure JWT verification via NestJS passport guards. |
| **Cache & Throttling** | Redis | 7.x | Leaderboard caching, frequent user metrics, API rate limiting. |
| **DevOps / CI** | GitHub Actions | Ubuntu Runner | Automated testing (`npm test`, `pytest`), linting, and continuous delivery. |
