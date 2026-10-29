# 📊 Bellabeat Data Analysis Case Study

## 🎯 Executive Summary
This case study is part of the **Google Data Analytics Professional Certificate**. The primary objective is to analyze smart device usage data from non-Bellabeat devices (Fitbit) to uncover consumer habits, identify growth opportunities, and provide high-level strategic recommendations for **Bellabeat**, a high-tech manufacturer of health-focused products for women.

The project follows Google’s data analysis framework: **Ask, Prepare, Process, Analyze, Share, and Act**.

---

## 🛠️ Tech Stack & Methodology
* **Data Processing & Analysis:** SQL (PostgreSQL)
* **Data Visualization:** Data Storytelling / Custom Dashboards (Tableau)
* **Framework:** Google Data Analytics 6-Step Process
* **Dataset:** FitBit Fitness Tracker Data (Public Domain via Kaggle)

---

## 🔍 Key Findings (Analyze & Share)

### 1. Market Segmentation (User Profiles)
Analysis revealed a clear polarization in the market across 33 distinct users:
* **Active Users (Active & Highly Active):** **51.5%** of the sample.
* **Inactive Users (Sedentary & Lightly Active):** **48.5%** of the sample.

> **Visual Choice:** *Pie / Donut Chart* to highlight market composition instantly for executive decision-making.

### 2. Weekly Habits & Trends
Daily activity is non-linear across the week:
* **Peak Days:** **Tuesdays and Saturdays** showed the highest average step counts (~8,950 steps).
* **Motivation Dip:** Step counts drop significantly on **Thursdays and Fridays** (~7,800 steps).
* **Active Rest:** **Sundays** register the lowest step volume (7,627 steps) but maintain low overall sedentary levels, indicating light domestic or recreational movement.

> **Visual Choice:** *Line Chart* to display time-series continuity and identify weekly behavior rhythms.

### 3. Hourly Activity Dynamics
Aggregating activity into 6-hour time blocks demonstrated clear movement windows:
* **Afternoon (12:00 - 17:59):** Peak activity window averaging **513 steps/hour**, outperforming Morning (381 steps/hr) and Evening (368 steps/hr).

> **Visual Choice:** *Vertical Bar Chart* to compare block magnitudes directly and establish action windows.

---

## 🚀 Strategic Recommendations (Act)

Based on the statistical evidence, the following **Dual Marketing and Product Strategy** is recommended for Bellabeat leadership:

1. **Adaptive App Experience (Feature Personalization):**
   * **For Inactive Profiles (48.5%):** Implement a *Wellness & Habits Mode* focused on gamification, daily streak achievements, and gentle movement prompts.
   * **For Active Profiles (51.5%):** Enable a *Performance Mode* offering advanced metric analysis, intensity tracking, and recovery/hormonal health correlation.

2. **Time-Targeted Push Notifications:**
   * **Vespertine Engagement:** Schedule automated hydration, mindfulness, and movement reminders between **13:00 and 16:00** (Afternoon window) to engage users during peak activity.
   * **Mid-Week Reactivation:** Trigger encouraging notifications or challenges on **Thursdays and Fridays** to prevent habit drop-off prior to the weekend.

3. **"Active Rest" Weekend Marketing Campaign:**
   * Position Bellabeat devices (*Leaf*, *Time*, *Ivy*) not just as gym trackers, but as holistic lifestyle companions. Normalize and celebrate light Sunday activities (yoga, walks, home wellness), promoting overall health over strict step quotas.

---

## 📂 Repository Structure
├── sql/
│   └── consultas_bellabeat.sql    # PostgreSQL scripts (Queries & CTEs)
├── data/                          # Processed dataset files
├── README.md                      # Executive Case Study Summary
└── LICENSE                        # MIT License


---

## 👨‍💻 Author
**Diego Vidaurre**  
*Systems Engineer & Data Analyst*  
[LinkedIn Profile](YOUR_LINKEDIN_URL_HERE) | [GitHub Portfolio](https://github.com/YOUR_GITHUB_USERNAME)
