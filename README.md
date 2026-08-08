# Python Programming Lab 011 🐍

**3 Assignments + Automated Daily Submissions via GitHub Actions**

![Python](https://img.shields.io/badge/Python-3.10-blue) ![Lab](https://img.shields.io/badge/Lab-011-orange) ![Automated](https://img.shields.io/badge/Automated-Yes-green)

---

## 📋 Overview

3 Python assignments with automated daily submissions (3 days) via GitHub Actions. Each includes full documentation, automated testing, and CI/CD workflows.

---

## 🎯 Assignments

### **Problem 1: Shopping Bill Calculator** 💳
- Input: Customer name, 3 items with prices
- Logic: Calculate total → 10% discount if > Rs. 3000
- Output: Formatted receipt
- [📖 Details](./README_problem1_shopping_bill.md)

### **Problem 2: Student Performance Calculator** 📊
- Input: Student info, 5 subject marks
- Logic: Calculate percentage → Assign grade (6 levels)
- Output: Professional report card
- [📖 Details](./README_problem2_student_performance.md)

### **Problem 3: Utility Toolkit** 🛠️
- 6 Interactive calculators: Temperature, Area, Interest, BMI
- Menu-driven interface
- Input validation included
- [📖 Details](./README_problem3_utility_toolkit.md)

---

## 🤖 Automation

Each workflow includes:
- ✅ Syntax validation
- ✅ Execution testing
- ✅ Logic verification
- ✅ Submission reports
- ✅ Artifact tracking (30 days)

**Default**: Daily 9:00 AM UTC (2:30 PM IST) for 3 consecutive days

---

## 🚀 Quick Start

```bash
# 1. Test locally
python problem1_shopping_bill.py
python problem2_student_performance.py
python problem3_utility_toolkit.py

# 2. Push to GitHub
git add .
git commit -m "Lab 011 assignments"
git push origin main

# 3. View submissions
GitHub → Actions tab → Select workflow
```

---

## 📁 Files Included

- 3 Python files (assignments)
- 3 README files (documentation)
- 3 Workflow files (automation)
- Setup guides

---

## 📖 Documentation

| File | Purpose |
|------|---------|
| README_problem1_shopping_bill.md | Shopping Bill details |
| README_problem2_student_performance.md | Student Calc details |
| README_problem3_utility_toolkit.md | Toolkit details |
| SETUP_GUIDE.md | Workflow setup |
| QUICK_REFERENCE.md | Quick lookup |

---

## ⚙️ Customize

Change submission time in `.github/workflows/problemX-submission.yml`:

```yaml
schedule:
  - cron: '0 6 * * *'  # 6 AM UTC (11:30 AM IST)
  - cron: '0 9 * * *'  # 9 AM UTC (2:30 PM IST) - Default
  - cron: '0 12 * * *' # 12 PM UTC (5:30 PM IST)
```

---

## ✅ Checklist

- [ ] All Python files created
- [ ] Files tested locally
- [ ] Pushed to GitHub
- [ ] Actions enabled
- [ ] Day 1-3 submissions verified

---

**Status**: Ready ✅ | **Last Updated**: August 2026

For detailed setup, see [SETUP_GUIDE.md](./SETUP_GUIDE.md)
