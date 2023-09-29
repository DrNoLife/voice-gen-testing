# Voice Synthesis Testing

This repository is dedicated to testing various methods of voice synthesis. The primary objective is to gain a deeper understanding of voice synthesis techniques and to offer code samples and projects that are both comprehensible and easily integrable into future projects.

## Technologies

- Python
- Flask

## Services

There are two distinct services/APIs created using Flask:
1. Service exposed via port `:5000`
2. Service exposed via port `:5001`

### Endpoints

1. **Service on :5001**  
   - **Endpoint**: `/text-to-speech`
   - **Method**: `POST`
   - **Data**: Form data with the key "text"

2. **Service on :5000**  
   - **Endpoint**: `/text-to-speech`
   - **Method**: `POST`
   - **Data**: JSON with a property named "text"

## Running the Services

To launch the services, navigate to the directory containing the `docker-compose` file and execute the following command:

```bash
docker-compose up --build
```


This will start both services, and they'll be accessible via the ports mentioned above.

---

Thank you for exploring this repository. Contributions and suggestions are always welcome!
