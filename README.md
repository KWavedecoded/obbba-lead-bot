# 🏢 OBBBA Lead Bot: Automated R&D Tax Credit Sourcing

본 프로젝트는 2026년 7월 4일 마감인 미국 **OBBBA(One Big Beautiful Bill Act)** 법안의 수혜 대상을 자동 발굴하고, 기업의 R&D 활동을 AI로 분석하여 고가치 비즈니스 리드를 생성합니다.

## 🏗️ System Architecture


```mermaid
graph TD
    A[Target Data: Crunchbase/GitHub] -->|Sourcing| B(Tavily Search API)
    B -->|R&D Activity Context| C[Gemini AI Decision Logic]
    C -->|OBBBA Eligibility Score| D{Python Scoring Filter}
    D -->|Qualified Lead| E[leads_database.csv]
    E -->|Automated Reporting| F[CPA Partner Integration]
