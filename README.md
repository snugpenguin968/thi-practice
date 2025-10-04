# thi-practice
Simple TypeScript, React, Fast-API practice exercise

# Welcome to the Kudos Board Project! 👋

**Your Objective:** Your team's goal is to build a simple, full-stack web application that allows users to post and view short messages of appreciation ("kudos"). This is a pair-programming exercise designed to be completed in 90 minutes.

**Tech Stack:**
* **Frontend:** React with TypeScript
* **Backend:** Python with FastAPI

---

### Project Setup (After Cloning from GitHub)

You have just cloned the project which contains two folders: `client` and `server`. You will need to open two separate terminal windows or tabs to run both the backend and frontend servers simultaneously.

#### Backend Setup (In your first terminal)

1.  **Navigate to the Backend Folder:**
    ```bash
    cd server
    ```
2.  **Create and Activate Your Local Virtual Environment:** The `venv` folder is not shared on GitHub, so you must create your own. This keeps your project's Python packages separate from your computer's.
    ```bash
    # On macOS/Linux
    python3 -m venv venv && source venv/bin/activate
    
    # On Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```
    *You should see `(venv)` appear at the beginning of your terminal prompt.*

3.  **Install Dependencies:** The `requirements.txt` file in the folder is a list of all the packages this project needs. Install them with this command:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Backend Server:**
    ```bash
    uvicorn main:app --reload
    ```
    *Your backend is now running at `http://localhost:8000`.*

#### Frontend Setup (In your second terminal)

1.  **Navigate to the Frontend Folder:**
    ```bash
    cd client
    ```
2.  **Install Dependencies:** The `package.json` file lists all the JavaScript libraries needed. Install them by running:
    ```bash
    npm install
    ```
3.  **Start the Frontend Server:**
    ```bash
    npm start
    ```
    *Your React app is now running and should open automatically in your browser at `http://localhost:3000`.*

---

### The Data Model: Our "Contract"

To ensure the frontend and backend can communicate, every "Kudo" object must follow this structure. This is your contract!


{
  "id": 1,
  "author": "Alice",
  "message": "Great job on the presentation, Bob!",
  "timestamp": "2025-10-27T10:00:00Z",
  "upvotes": 0
}

* `id` (integer): A unique identifier for each kudo.
* `author` (string): The name of the person giving the kudo.
* `message` (string): The content of the kudo.
* `timestamp` (string): An ISO 8601 formatted timestamp of when the kudo was created.
* `upvotes` (integer): A count of upvotes (for an extra feature).

---

### Core Tasks

#### **Backend Task 1: Get All Kudos**

* **Goal:** Create the API endpoint that sends the list of all kudos to the frontend.
* **Database:** For this project, your "database" is just an in-memory Python list in `main.py`.
```python
# In main.py
db = [] # This is your database!
```
* **Endpoint:** `GET /kudos`
* **Success Response:** A `200 OK` status with a JSON array of Kudo objects, sorted with the newest first.

#### **Backend Task 2: Create a New Kudo**

* **Goal:** Create the API endpoint that receives data from the frontend form and adds a new kudo to the list.
* **Endpoint:** `POST /kudos`
* **Details:** The server is responsible for generating the `id`, `timestamp`, and setting `upvotes` to `0`.
* **Request Body:** The frontend will send a JSON object like this:
    ```json
    { "author": "Charlie", "message": "Thanks for the help debugging!" }
    ```
* **Success Response:** A `201 Created` status with the full Kudo object that was just created.

#### **Frontend Task 1: Display All Kudos**

* **Goal:** Build the React components to fetch and display the list of all kudos from the backend.
* **Functionality:**
    1.  When your app loads, use `useEffect` and `axios` to make a `GET` request to `http://localhost:8000/kudos`.
    2.  Store the returned array of kudos in state using `useState`.
    3.  Map over the array and render a separate component for each kudo, displaying its `message`, `author`, and `timestamp`.

#### **Frontend Task 2: Create a New Kudo Form**

* **Goal:** Build the React form for submitting a new kudo.
* **Functionality:**
    1.  Create a form with two controlled input fields (`author` and `message`) managed by `useState`.
    2.  On submit, use `axios` to make a `POST` request to `http://localhost:8000/kudos` with the form data.
    3.  After a successful post, clear the input fields and ensure the kudos list refreshes to show the new entry. (Hint: you may need to lift state up or pass a function down as a prop).

---

### Extra Features (If You Have Time!)

1.  **Delete a Kudo:** Add a `DELETE /kudos/{kudo_id}` endpoint and a delete button on the frontend.
2.  **Upvote a Kudo:** Add a `POST /kudos/{kudo_id}/upvote` endpoint and an upvote button on the frontend.
3.  **Auto-Refresh:** Use `setInterval` on the frontend to re-fetch the kudos list every 5 seconds.
