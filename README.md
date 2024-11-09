# Movie Booking System

This is a Python-based Movie Booking System using **Tkinter** for the GUI and **MySQL** for database management. The application allows users to register, book tickets, view available movies, and more, all with a simple graphical interface.

## Features

- **User Registration**: Users can register with details like ID, Name, Age, Gender, Phone, and Movie choice.
- **Movie Details**: Admins can add details about movies, including the movie name, cast, genre, and other information.
- **Booking**: Users can book movie tickets, view the available showrooms, and choose from various facilities (like AC, Snacks, etc.).
- **Show Details**: Admins can add show details, including the show time, date, and available facilities.
- **Update and Modify**: Users can modify their booking details if needed (e.g., change name, age, or phone number).
- **Search**: Users can search for their bookings using the unique ID.
- **Booking Details**: Displays booking details like room number, date, show time, and available facilities.

## Tech Stack

- **Python 3.x**
- **Tkinter** (GUI)
- **MySQL** (Database)
- **Random** (For assigning random room numbers)

## Setup Instructions

### Prerequisites

- Python 3.x installed on your local machine.
- MySQL server running with a database called `project`.

### Steps to Set Up

1. **Clone the Repository**
   ```bash
   git clone https://github.com/bhuvanika1102/online-ticket-booking.git
   cd movie-booking-system
2. **Install Dependencies**

Ensure that the following Python libraries are installed:

pymysql: Used for MySQL database connection.
tkinter: Used for the GUI.
You can install the dependencies using pip:

bash
```
pip install pymysql
```
Note: tkinter comes pre-installed with Python, so you don’t need to install it separately.

3. **Set Up MySQL Database**

Open your MySQL client (e.g., MySQL Workbench, Command Line).

Create a new database called `project`.

```sql
CREATE DATABASE project;
```
4. **Create the following tables inside the project database:**

Table 1: booking

```sql

CREATE TABLE booking (
    idno INT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender CHAR(1),
    phone VARCHAR(20),
    movie_name VARCHAR(255)
);
```
Table 2: showdetails

```sql
CREATE TABLE showdetails (
    show_time VARCHAR(50),
    show_date DATE,
    facility VARCHAR(255),
    snacks VARCHAR(255)
);
```
Table 3: movie

```sql
CREATE TABLE movie (
    movie_id INT PRIMARY KEY,
    hero VARCHAR(255),
    heroine VARCHAR(255),
    director VARCHAR(255),
    singer VARCHAR(255),
    movie_name VARCHAR(255),
    genre VARCHAR(255)
);
```
Table 4: booking_details

```sql
CREATE TABLE booking_details (
    idno INT,
    room_no VARCHAR(10),
    date DATE,
    show_time VARCHAR(50),
    facility VARCHAR(255),
    PRIMARY KEY (idno)
);
```
5.. **Running the Application**

After setting up the database and dependencies, you can run the application.

```bash
python ticket_booking.py
```
This will launch the GUI, allowing you to register, book tickets, view movie details, and more.
