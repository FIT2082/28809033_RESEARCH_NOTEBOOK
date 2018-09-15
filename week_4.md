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


