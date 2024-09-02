# Brit Item Management Application

This is a Python-based web application for managing items, using FastAPI as the backend framework and MongoDB Atlas as the database. The application is containerized using Docker and deployed on an AWS EC2 instance.

## Features

- **User Authentication**: Users can create a new account and log in using JWT tokens.
- **Item Management**: Authenticated users can add items with names and prices, view a list of their items, and see a summary of the total price of all items.
- **MongoDB Atlas**: The application uses MongoDB Atlas as the database to store users and items.
- **Docker**: The application is containerized using Docker for easy deployment.

## Setup

### Prerequisites

- Python 3.10 or later
- MongoDB Atlas account with a cluster set up
- Docker installed on your system
- An AWS EC2 instance running Amazon Linux 2 or Ubuntu

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sahanasanu/Brit-item-management.git
   cd Brit-item-management
