from pathlib import Path
import pandas as pd, numpy as np

out = Path(__file__).resolve().parents[1] / "data/raw/trips.csv"
out.parent.mkdir(parents=True, exist_ok=True)

n = 500
rng = np.random.default_rng(42)

df = pd.DataFrame({
    "ride_id": np.arange(1, n+1),
    "pickup_ts": pd.to_datetime("2024-01-01") + pd.to_timedelta(rng.integers(0, 1440, n), unit="m"),
    "dropoff_ts": pd.to_datetime("2024-01-01") + pd.to_timedelta(rng.integers(10, 2880, n), unit="m"),
    "passenger_count": rng.integers(1, 5, n),
    "trip_distance": np.round(rng.uniform(0.5, 20.0, n), 2),
    "fare_amount": np.round(rng.uniform(5, 80, n), 2),
    "tip_amount": np.round(rng.uniform(0, 15, n), 2),
    "payment_type": rng.choice(["card", "cash", "wallet"], n, p=[0.6, 0.3, 0.1]),
})
df.to_csv(out, index=False)
print(f"Wrote {out}")