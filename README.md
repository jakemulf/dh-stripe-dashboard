# dh-stripe-dashboard

A sample application that creates a Deephaven dashboard to display data from Stripe's API.

## Components

* `Dockerfile`: The Dockerfile that extends the Deephaven server image to install the project dependencies
* `docker-compose.yml`: The docker-compose file that defines the local Dockerfile build, and the Deephaven application mode directory
* `requirements.txt`: The Python dependencies for the project
* `data/layouts/layout.json`: The pre-defined layout for the Deephaven IDE
* `data/app.d/`: The Deephaven application mode directory
  * `data/app.d/app.app`: The Deephaven application mode config file
  * `data/app.d/stripe_dashboard.py`: The Python script that pulls data from Stripe and creates the Deephaven plots

## Launch

Simply run

```
docker compose up
```

to launch the app, then go to http://localhost:10000 to view the app.
