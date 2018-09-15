# Week 4

## PTV API
I had applied for access to the official PTV API which is documented on [Swagger UI](https://timetableapi.ptv.vic.gov.au/swagger/ui/index)

The API allows fetching for real time information about platform departures on a specific stop. 

There is a DEPARTURES endpoint which can give the data in the following format.

```json
{
  "departures": [
    {
      "stop_id": 0,
      "route_id": 0,
      "run_id": 0,
      "direction_id": 0,
      "disruption_ids": [
        0
      ],
      "scheduled_departure_utc": "2018-09-15T08:31:35.793Z",
      "estimated_departure_utc": "2018-09-15T08:31:35.793Z",
      "at_platform": true,
      "platform_number": "string",
      "flags": "string",
      "departure_sequence": 0
    }
  ],
  "stops": {},
  "routes": {},
  "runs": {},
  "directions": {},
  "disruptions": {},
  "status": {
    "version": "string",
    "health": 0
  }
}
```
After getting access, I attempted to perform a simple GET request to fetch the data in real time.

*GET* /v3/departures/route_type/{route_type}/stop/{stop_id}

```
route_type = 0, //For a train
stop_id = FLINDERS_STOP_ID
```

## Challenges

Getting the Flinders Street Stop ID was a challenge as the PTV website "stop_id" did not correspond to the API. Hence, the API would give out *no content* response. 

It was after calling the *GET* /v3/search/{search_term} with __search_term = flinders__ that I could find the correct stop ID.

## Outcome

![alt text](https://fit2082.github.io/28809033_RESEARCH_NOTEBOOK/images/app_initial_demo.gif "App Demo MyStation")

## Android App
By the end of this week, I had a basic app working which fetched data from the API. It could figure out what train line departed next from a certain platform. 

This meant that once the app starts communicating with the Raspberry PI, it will be able to feed in the platform numbers into existing code framework and be able to display and speak out the departures information.

There were the following problems solved to build the application
* PTV API Requests were made using Google's library Volley
* API Data Models were created
* JSON parsing and Java object mapping using GSON.
* Accessibility testing using the Android's built in text to speech tool.


## Reflection

I assumed that the API communications would've been really smooth sailing however turned out to be a tussle with the documentation not being accurate and comprehensive. There is even a notice on the PTV website suggesting no support for the API will be provided. The app turned out to be a challenge but in the end it was quite rewarding to get to the outcome.







