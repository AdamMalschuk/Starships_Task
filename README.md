# Starships ETL task

### Goal

- Extract the starships data from the "SWAPI" (Star Wars API).
- Combine the starships pilot data with the characters data on out mongodb database (reference character object ID).
- Add the combined data to a new mongodb collection.

#### Side Notes

- The code has unit tests and a query test using the unit test framework in its own file to check the ETL pipeline was successful. 
- The code is stateless so can be rerun as many times as needed.
- The code uses a locally hosted mongodb database that already has characters loaded into their own collection.
