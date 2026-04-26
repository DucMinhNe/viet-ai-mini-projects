# Anomaly Detector

This project identifies unusual points in a small time-series dataset using a rolling average, rolling standard deviation, and z-score threshold.

## What It Shows

- Time-series data loading
- Rolling baseline calculation
- Z-score anomaly scoring
- Simple alert generation

## Run

```bash
python3 anomaly-detector/main.py
```

## Example Use Cases

- Detecting traffic spikes
- Monitoring product metrics
- Flagging unusual transaction volume
- Finding sensor readings that deserve investigation

## Notes

This project intentionally uses a transparent statistical method. In a production system, this could be extended with seasonality handling, robust statistics, or machine learning models.
