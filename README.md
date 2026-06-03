# Youth Center Management System
### Rosh Pinna Local Municipality - Youth Center

A web-based information system developed for the Rosh Pinna Youth Center, designed to replace fragmented Excel files and WhatsApp groups with a centralized, data-driven platform for managing ~600 young residents aged 18-35.

---

## The Problem

The Youth Center had no central information system. Youth data was scattered across separate Excel files, WhatsApp groups, and government reports. The coordinator could not proactively identify students, track life-stage changes, or send targeted messages — relying entirely on youth reaching out themselves.

---

## Solution

A centralized management system that allows the Youth Center to:

- **Onboard new youth** digitally upon completing 12th grade, including life-stage selection (military service, gap year, studies, etc.)
- **Track life-stage status** - military, student, employed — and update it over time
- **Manage service requests**- open, assign, track, and document responses
- **Send targeted messages** based on status (students, discharged soldiers, employed youth)
- **View segmented data** -breakdowns by status, participation rates, and trends to support budget planning
- **Verify residency** before issuing services

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Database | MySQL |
| Frontend | HTML, CSS |
| Architecture | MVC, REST |

---

## Project Structure

```
youth-center-management-system/
├── app.py                  # Main Flask application & routes
├── db_connection.py        # Database connection
├── request.py              # Service request logic
├── response.py             # Response handling
├── youth.py                # Youth data logic
├── create_db_mySql/
│   └── db.sql              # Database schema
├── templates/
│   ├── layout.html
│   ├── login.html
│   ├── my_requests.html
│   ├── open_request.html
│   └── profile.html
└── static/
```

---

## Key Features

- **Youth profiles** - centralized records with contact info, life-stage status, and history
- **Digital onboarding** - structured intake form replacing manual Excel entry
- **Request management** - open, assign, and track service requests with full audit trail
- **Role-based access** - coordinator vs. student-worker views
- **Status-based communication** - targeted outreach by life stage

---

## Background

This project was developed as part of an Industrial Engineering & Management course at Ariel University (Information Systems Analysis).  
The system was designed following stakeholder interviews with the Youth Center coordinator and local youth residents, field observations, and a formal requirements analysis process.

**Team:** Gil Hatiel, Roni Fahima, Roi Ashkenazi
