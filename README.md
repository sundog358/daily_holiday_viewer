# 🌞🌧️🌳🌸 Sun & Rain Works: MediaWiki Action API Holidays Viewer Application

The **Holidays Viewer** is a Flask-based application that fetches holiday observances for a specified date from Wikipedia. It provides features such as searching for holidays, displaying them in a clean user interface, and allowing authenticated users to add holidays to a test page on Wikipedia.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [File Structure](#file-structure)
6. [Step-by-Step Guide](#step-by-step-guide)
7. [MediaWiki API Endpoints](#mediawiki-api-endpoints)
8. [Next Steps](#next-steps)

---

## 🌍 Overview

The **Holiday Viewer** allows users to:

- 📅 View holidays and observances for today or any specified date.
- 🔍 Search holidays by month and day.
- ✍️ Log in to add new holidays (restricted to a test page on Wikipedia).
- 🎨 Leverage Bootstrap and custom styling for a visually appealing interface.

---

## ✨ Features

- **Fetch Holiday Data**: Retrieve holidays and observances from Wikipedia for a specific date.
- **Search Functionality**: Input a custom date (month and day) to find holidays.
- **Add New Holidays**: Authenticated users can add new holidays, highlighted in bold for distinction.
- **Responsive Design**: A clean and responsive UI using Bootstrap.
- **Dynamic Links**: Automatically updates holiday links to point to Wikipedia pages and open in a new tab.

---

## 🛠️ Technologies Used

- **Python 3**: Backend programming.
- **Flask**: Lightweight web framework.
- **Bootstrap**: Frontend styling.
- **jQuery**: For link updates and interactivity.
- **MediaWiki Action API**: To interact with Wikipedia data.
- **Materialize Icons**: For icons.

---

## 📝 Installation

### **1️⃣ Clone the Repository**

```
git clone https://github.com/sundog358/holidays-viewer.git
cd holidays-viewer
```

### 2️⃣ Set Up the Python Environment

Install Flask and dependencies:

`pip install flask requests`

### 3️⃣ Run the Application

Start the Flask app:

`python app.py`

- Open your browser and navigate to: http://127.0.0.1:5000/

# 📁 File Structure: Holidays Viewer Application

```
holiday-viewer/
├── app.py                 # Main application file
├── templates/             # HTML template files
│   ├── layout.html        # Base layout for all pages
│   ├── index.html         # Displays holidays
│   ├── login.html         # Login page
│   ├── add.html           # Add holiday form
│   └── search.html        # Search holidays page
├── static/                # Static files
│   ├── style.css          # Custom styling
│   └── update-links.js    # jQuery script to update Wikipedia links
```

# 🛠️ Step-by-Step Guide

## **1️⃣ Set Up the Flask Application**

- **File**: `app.py`
- Initialize the Flask app with routes for:
  - 📅 Displaying holidays.
  - 🔍 Searching for holidays.
  - 🔑 Logging in to Wikipedia.
  - ✍️ Adding new holidays.

---

## **2️⃣ Define Base Layout**

- **File**: `templates/layout.html`
- Create a base HTML layout with:
  - 🎨 **Bootstrap** for responsive design.
  - 🖼️ **Materialize icons** for navigation and actions.

---

## **3️⃣ List Holidays**

- **File**: `templates/index.html`
- Fetch holidays from Wikipedia using the **MediaWiki Action API**.
- Display the holidays for:
  - 📅 **Today's date**.
  - 📅 **User-selected date** (optional).

---

## **4️⃣ Add Search Functionality**

- **File**: `templates/search.html`
- Add a search form allowing users to:
  - 📆 **Select a month**.
  - 📆 **Select a day**.
- Fetch and display holidays for the specified date.

---

## **5️⃣ Add New Holidays**

- **File**: `templates/add.html`
- Allow authenticated users to:
  - ✍️ Add holidays to a test page on Wikipedia using the **API:Edit** endpoint.
  - ✨ Highlight added holidays in **bold**.

---

## **6️⃣ Login to Wikipedia**

- **File**: `templates/login.html`
- Authenticate users with the **API:ClientLogin** endpoint.

---

## **7️⃣ Styling**

- **File**: `static/style.css`
- Apply custom CSS for:
  - 🎨 A visually appealing UI.
  - 📱 Mobile-friendly responsiveness.

---

### 🚀 Next Steps

Expand Features

🌟 Add user accounts and permissions for better user management.

📊 Integrate analytics to track popular holidays and user activity.
Enhance Visualization

📈 Use charts or timelines to visualize holidays by:

📅 Date.
🗂️ Category.

Improve API Integration

🔄 Implement caching to reduce API calls for frequently accessed holidays.
