# Technology Comparison & Weighted Decision Matrix

**Project:** FitFlow Fitness Tracking App Redesign (HCI Lab Exercise 05)  
**Module:** IT3060 – Human Computer Interaction  
**Activity 3:** Technology Comparison Matrix  

---

## 1. Methodology & Weighting Criteria

To objectively select the best technology stack for the FitFlow redesign, each candidate technology is evaluated using a **Weighted Decision Matrix**. 

- **Weights ($W$):** Scale from **1 (Lowest Importance)** to **5 (Highest Importance)** based on FitFlow's specific business and user needs (e.g., fast iteration for HCI testing, real-time social dynamics, camera-based AI vision, and high mobile performance).
- **Scores ($S$):** Evaluated from **1 (Poor)** to **5 (Exceptional)**.
- **Weighted Score ($WS$):** Calculated as $WS = \text{Score} \times \text{Weight}$.
- **Total Score:** $\sum (WS)$, where the highest total represents the most suitable technology.

---

## 2. Frontend Frameworks Weighted Decision Matrix

Evaluating mobile and cross-platform frameworks for FitFlow's client application:

| Criteria | Weight (1–5) | React Native | Flutter | Kotlin Multiplatform (KMP) | Swift / SwiftUI (iOS Native) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Development Speed & Hot Reload** | 5 | 5 (25) | 5 (25) | 3 (15) | 2 (10) |
| **Cross-Platform Code Reusability** | 5 | 5 (25) | 5 (25) | 3 (15) | 1 (5) |
| **Runtime Performance & 60fps UX** | 4 | 4 (16) | 4 (16) | 5 (20) | 5 (20) |
| **Ecosystem, UI Kits & Animation Support** | 4 | 5 (20) | 4 (16) | 3 (12) | 5 (20) |
| **Camera & Hardware Sensor Access** | 4 | 4 (16) | 4 (16) | 4 (16) | 5 (20) |
| **Web Compatibility (Code Sharing)** | 3 | 5 (15) | 3 (9) | 2 (6) | 1 (3) |
| **AI / ML Integration (TFLite / ONNX)** | 3 | 4 (12) | 3 (9) | 3 (9) | 5 (15) |
| **Learning Curve for Web/TS Devs** | 3 | 5 (15) | 3 (9) | 2 (6) | 2 (6) |
| **Maintenance Cost for Mid-Sized Team** | 4 | 5 (20) | 4 (16) | 3 (12) | 1 (4) |
| **Total Weighted Score (Max: 175)** | — | **164** | **141** | **111** | **103** |
| **Rank** | — | **1st (Selected)** | **2nd** | **3rd** | **4th** |

### Frontend Analysis & Justification
- **React Native (164 pts):** Emerges as the top choice. It allows near-complete code sharing between iOS, Android, and Web, enables smooth 60fps gesture-driven animations (via Reanimated 3), provides robust camera bindings for food logging, and leverages TypeScript for seamless type parity with the backend.
- **Flutter (141 pts):** Excellent UI engine, but Dart isolates the team from the TypeScript ecosystem, and Web support has larger bundle overhead.
- **Kotlin Multiplatform (111 pts) & Swift (103 pts):** While offering native performance, Swift requires maintaining a separate Android codebase, and KMP requires building distinct UI layers, doubling engineering costs for a mid-sized startup.

---

## 3. Backend Frameworks Weighted Decision Matrix

Evaluating backend technologies for FitFlow's API Gateway, Business Logic, and AI Services:

| Criteria | Weight (1–5) | Node.js + NestJS | Python + FastAPI | Go (Gin / Fiber) |
| :--- | :---: | :---: | :---: | :---: |
| **Modular Architecture & Maintainability** | 5 | 5 (25) | 4 (20) | 3 (15) |
| **Asynchronous I/O & Concurrency** | 5 | 5 (25) | 4 (20) | 5 (25) |
| **Machine Learning & CV Ecosystem** | 5 | 2 (10) | 5 (25) | 2 (10) |
| **Type Safety & Schema Validation** | 4 | 5 (20) | 5 (20) | 5 (20) |
| **Developer Velocity & Prototyping** | 4 | 5 (20) | 5 (20) | 3 (12) |
| **Microservice & Gateway Support** | 4 | 5 (20) | 4 (16) | 4 (16) |
| **Resource & Memory Footprint** | 3 | 3 (9) | 3 (9) | 5 (15) |
| **Total Weighted Score (Max: 150)** | — | **129** | **130** | **113** |
| **Role Assigned** | — | **Core Backend / Gateway** | **AI / ML Microservice** | **Alternative** |

### Backend Analysis & Justification
- **NestJS (129 pts):** Ideal for the Core API Gateway due to its enterprise modular architecture, out-of-the-box Dependency Injection, robust Firebase Auth guard integration, and TypeScript type-sharing with the React Native client.
- **FastAPI (130 pts):** Highest score for ML/AI workloads. Python’s native support for PyTorch, OpenCV, and YOLO makes FastAPI the undisputed choice for the dedicated AI microservice handling computer vision food logging and adaptive workout generation.
- **Go (113 pts):** Highly performant with low memory footprint, but lacks native machine learning libraries and requires more boilerplate code.

---

## 4. Database Solutions Weighted Decision Matrix

Evaluating database technologies for FitFlow's transactional health records and real-time social features:

| Criteria | Weight (1–5) | PostgreSQL | Firebase Firestore | MongoDB | AWS DynamoDB |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **ACID Compliance & Data Integrity** | 5 | 5 (25) | 2 (10) | 3 (15) | 3 (15) |
| **Real-Time Data Synchronization** | 5 | 2 (10) | 5 (25) | 3 (15) | 3 (15) |
| **Complex Health & Metric Queries** | 5 | 5 (25) | 2 (10) | 3 (15) | 2 (10) |
| **Mobile Offline Persistence** | 4 | 2 (8) | 5 (20) | 2 (8) | 2 (8) |
| **Scalability & Low Latency** | 4 | 4 (16) | 4 (16) | 4 (16) | 5 (20) |
| **Total Weighted Score (Max: 115)** | — | **84** | **81** | **69** | **68** |
| **Role Assigned** | — | **Primary Health DB** | **Real-Time Social DB** | Rejected | Rejected |

### Database Justification: Hybrid Approach
- **PostgreSQL** secures the top score for transactional integrity, structured health records, user billing, and HIPAA/GDPR auditability.
- **Firebase Firestore** dominates in real-time listeners and automatic mobile offline caching for social feeds, chats, and challenges.
- **Decision:** A **Hybrid Database** architecture utilizing PostgreSQL for core transactional records and Firestore for real-time social engagement.

---

## 5. Authentication Solutions Weighted Decision Matrix

| Criteria | Weight (1–5) | Firebase Auth | Auth0 | AWS Cognito | Supabase Auth |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Ease of Integration with Mobile** | 5 | 5 (25) | 4 (20) | 2 (10) | 4 (20) |
| **Security & Regulatory Compliance** | 5 | 5 (25) | 5 (25) | 5 (25) | 4 (20) |
| **Cost Effectiveness for Mid-Sized Team**| 4 | 5 (20) | 2 (8) | 4 (16) | 4 (16) |
| **Social & Multi-Provider Support** | 4 | 5 (20) | 5 (20) | 3 (12) | 4 (16) |
| **Total Weighted Score (Max: 90)** | — | **90** | **73** | **63** | **72** |
| **Rank** | — | **1st (Selected)** | **2nd** | **4th** | **3rd** |

---

## 6. Final Recommended Stack Table

| Component | Selected Technology | Alternative Considered | Primary Justification |
| :--- | :--- | :--- | :--- |
| **Frontend** | **React Native (Expo)** | Flutter, Swift, KMP | High velocity, 60fps micro-animations, single TS codebase for iOS/Android/Web. |
| **Core Backend** | **Node.js + NestJS** | Go, Django, Express | Modular DI architecture, TypeScript end-to-end type safety, high I/O throughput. |
| **AI Microservice** | **Python + FastAPI** | Flask, Node.js Workers | Industry-standard PyTorch/OpenCV support, async ASGI performance. |
| **Primary Database** | **PostgreSQL** | MongoDB, DynamoDB | ACID guarantees, complex time-series queries, strict HIPAA/GDPR data integrity. |
| **Realtime Database** | **Firebase Firestore** | WebSockets, Supabase | Sub-second real-time social feed sync, native offline mobile caching. |
| **Authentication** | **Firebase Auth** | Auth0, AWS Cognito | Turn-key OAuth integration, cost-effective scaling, seamless token verification. |
| **Cache & Throttling** | **Redis** | Memcached | In-memory leaderboard ranking (sorted sets), fast session and token caching. |
| **CI / CD** | **GitHub Actions** | GitLab CI, CircleCI | Integrated directly with GitHub repository, automated multi-service test pipeline. |
