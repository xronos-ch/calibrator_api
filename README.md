# Calibrator API

This project provides a Dockerized Flask API for running the `calibrator` tool, a command-line utility for 14C calibration. The API allows users to run the `calibrator` tool with specified parameters and receive the output in JSON format.

## Project Structure

```
calibrator_api/
├── Dockerfile
├── LICENCE
├── Makefile
├── app.py
├── bin
├── data
│   └── intcal20.14c
├── docker-compose.yml
├── include
│   ├── cal_curve.h
│   ├── cal_date.h
│   ├── cal_date_list.h
│   ├── json.hpp
│   ├── sigma_range.h
│   ├── uncal_date.h
│   └── uncal_date_list.h
├── lib
│   └── calibrator_mac
├── requirements.txt
└── src
    ├── cal_curve.cpp
    ├── cal_date.cpp
    ├── cal_date_list.cpp
    ├── main.cpp
    ├── sigma_range.cpp
    ├── uncal_date.cpp
    └── uncal_date_list.cpp
```

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Building and Running the Application

1. **Clone the repository**:

   ```bash
   git clone https://github.com/xronos-ch/calibrator_api.git
   cd calibrator_api
   ```

2. **Build and start the services**:

   ```bash
   docker-compose up --build --no-cache
   ```

3. **Access the API**:

   Open your browser or use `curl` to access the API endpoint:

   ```bash
   curl "http://localhost:8000/run_calibrator?b=5000&s=50"
   ```

### Entering the Container

If you need to enter the running container:

```bash
docker-compose exec web /bin/bash
```

## API Endpoint

### `/run_calibrator`

**Method**: GET

**Parameters**:
- `b` (required): bp - BP value.
- `s` (required): std - Standard deviation.

**Example**:
```bash
curl "http://localhost:8000/run_calibrator?b=5000&s=50"
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.