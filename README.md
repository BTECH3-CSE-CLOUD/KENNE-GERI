# KENNE-GERI
# The project is found in the Master branch
1) Project Setup
    Django project (restaurant_reservation) and app (reservations) created.
    Packages installed: Django, Django REST Framework.
    Security:
        SECRET_KEY is set (change for production).
        DEBUG = True (set to False for production).
        ALLOWED_HOSTS includes localhost and 127.0.0.1.
    Project structure:
        restaurant_reservation/ (project)
        reservations/ (app)
        venv/ (virtual environment)
2) Data Modeling
    Models:
        Table: number, seats.
        Reservation: user, table, date, time, guests.
        Comment: user, reservation, text, created_at.
    Relationships:
        One reservation belongs to a table.
        Users can post multiple comments.
        Reservations and comments are linked to users.
3) API Endpoints
    Create Reservation:
        POST /api/reservations/
        List Reservations by Table:
        GET /api/reservations/?table=<table_id>
        Post a Comment:
        POST /api/comments/
4) Validation and Frontend API Call
    Validation:
        Comments must not be empty (checked in serializer).
        Example React API Calls:
            // Add a reservation
            axios.post('/api/reservations/', {
                user: 1, // user ID
                table: 2, // table ID
                date: '2024-07-01',
                time: '19:00',
                guests: 4
            });

            // Filter reservations by table
            axios.get('/api/reservations/?table=2');

            // Submit a comment
            axios.post('/api/comments/', {
                user: 1, // user ID
                reservation: 3, // reservation ID
                text: 'Great service!'
            });

To run this project, install all depencies and  run the server with "python manage.py runserver". Then access the admin at /admin/ to manage users, tables, and reservations. It is possible to use the API endpoints as showned above.
