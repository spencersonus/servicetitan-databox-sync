# servicetitan-databox-sync  

This repository provides a Python module to authenticate with the ServiceTitan API using OAuth2 client credentials, pull inbound call data from the ServiceTitan Calls API, aggregate metrics by date, hour, and CSR name, and write the results to an Excel file.  

## Setup  

1. Clone the repo.  
2. Install dependencies: `pip install -r requirements.txt`.  
3. Set environment variables: `CLIENT_ID`, `CLIENT_SECRET`, `TENANT_ID`.  

## Usage  

Run the main script:  

```
python main.py
```  

This will fetch inbound and answered call data for today and yesterday, aggregate it, and create or overwrite `servicetitan_kpis.xlsx` in the current directory with a sheet named `Calls`.  

## Structure  

- `servicetitan/auth.py`: Handles OAuth2 client credentials flow.  
- `servicetitan/api.py`: Fetches call data and handles pagination.  
- `servicetitan/transform.py`: Aggregates call metrics by date, hour, and CSR.  
- `servicetitan/write.py`: Writes the aggregated dataframe to an Excel file.  
- `main.py`: Entry point to orchestrate the workflow.  
- `requirements.txt`: Lists Python dependencies.  

## Notes  

- The script fetches data for today and yesterday to avoid partial data for the current day.  
- The output Excel file will be overwritten on each run. 
