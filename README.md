# 🌞🌧️🌳🌸 Daily Holiday Viewer: MediaWiki Action API Application

The **Daily Holiday Viewer** is a Flask-based application that fetches and displays holiday observances for specific dates using Wikipedia's MediaWiki Action API. It allows users to explore cultural and historical holidays, search for specific dates, and contribute new holiday entries to a test Wikipedia page.

---

## 📋 Table of Contents

1. [App Overview](#app-overview)
2. [Architecture Overview](#architecture-overview)
3. [Dependencies](#dependencies)
4. [How It Works](#how-it-works)
5. [Step-by-Step Guide](#step-by-step-guide)
6. [MediaWiki API Endpoints](#mediawiki-api-endpoints)
7. [Next Steps](#next-steps)

---

## 🌍 App Overview

The **Daily Holiday Viewer** enables users to:

- 📅 View holidays and observances for today or any specific date.
- 🔍 Search for holidays by month and day.
- ✍️ Log in to add new holidays to a test Wikipedia page.
- 🎨 Experience a clean and responsive UI built with Bootstrap and Materialize icons.

---

## 🔧 Architecture Overview

The application uses a **Python Flask backend** to handle routes and API requests. It integrates with the **MediaWiki API** to fetch holiday data and dynamically renders templates using Jinja2. The frontend leverages **Bootstrap** for responsive design and **jQuery** for interactive elements like link management.

---

## 📦 Dependencies

- **Flask**: Web framework for handling routes and rendering templates.
- **Requests**: Python library for making HTTP requests to the MediaWiki API.
- **Bootstrap**: Provides a modern and responsive UI.
- **jQuery**: Enables dynamic interactions and link updates.
- **Material Icons**: Adds intuitive navigation and action icons.

---

## 💡 How It Works

1. **Homepage**: Displays holidays for today’s date by default.
2. **Search**: Users can select a date to retrieve holidays for that day.
3. **Add Holidays**: Authenticated users can add new holidays to a test page.
4. **Dynamic Rendering**: Backend fetches data and renders it into the templates using Jinja2.

---

## 🛠️ Step-by-Step Guide

### **1️⃣ Set Up the Flask Application**

- **File**: `app.py`  
  Initialize the Flask app with routes for:
  - 📅 Displaying holidays.
  - 🔍 Searching for holidays.
  - 🔑 Logging in to Wikipedia.
  - ✍️ Adding new holidays.

---

### **2️⃣ Define Base Layout**

- **File**: `templates/layout.html`  
  Create a base HTML layout with:
  - 🎨 **Bootstrap** for responsive design.
  - 🖼️ **Materialize icons** for navigation and actions.

---

### **3️⃣ List Holidays**

- **File**: `templates/index.html`  
  Fetch holidays from Wikipedia using the **MediaWiki Action API**.  
  Display the holidays for:
  - 📅 **Today’s date**.
  - 📅 **User-selected date** (optional).

---

### **4️⃣ Add Search Functionality**

- **File**: `templates/search.html`  
  Add a search form allowing users to:
  - 📆 **Select a month**.
  - 📆 **Select a day**.  
    Fetch and display holidays for the specified date.

---

### **5️⃣ Add New Holidays**

- **File**: `templates/add.html`  
  Allow authenticated users to:
  - ✍️ Add holidays to a test page on Wikipedia using the **API:Edit** endpoint.
  - ✨ Highlight added holidays in **bold**.

---

### **6️⃣ Login to Wikipedia**

- **File**: `templates/login.html`  
  Authenticate users with the **API:ClientLogin** endpoint.

---

### **7️⃣ Styling**

- **File**: `static/style.css`  
  Apply custom CSS for:
  - 🎨 A visually appealing UI.
  - 📱 Mobile-friendly responsiveness.

---

## 🌐 MediaWiki API Endpoints

### **1️⃣ API:Parse**

- Retrieve section data and content for holidays.

### **2️⃣ API:ClientLogin**

- Authenticate users for adding holidays.

### **3️⃣ API:Edit**

- Add new holidays to a test Wikipedia page.

---

## 🚀 Next Steps

**Expand Features**  
🌟 Add user accounts and permissions for better user management.  
📊 Integrate analytics to track popular holidays and user activity.

**Enhance Visualization**  
📈 Use charts or timelines to visualize holidays by:  
📅 Date.  
🗂️ Category.

**Improve API Integration**  
🔄 Implement caching to reduce API calls for frequently accessed holidays.
