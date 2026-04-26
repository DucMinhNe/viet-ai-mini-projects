import csv
import statistics
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "traffic.csv"
WINDOW_SIZE = 5
Z_SCORE_THRESHOLD = 3.0


def load_points(path):
    with path.open(newline="", encoding="utf-8") as file:
        rows = csv.DictReader(file)
        return [(row["date"], int(row["visits"])) for row in rows]


def detect_anomalies(points, window_size=WINDOW_SIZE, threshold=Z_SCORE_THRESHOLD):
    anomalies = []

    for index in range(window_size, len(points)):
        date, value = points[index]
        history = [visits for _, visits in points[index - window_size:index]]
        baseline = statistics.mean(history)
        spread = statistics.pstdev(history) or 1.0
        z_score = (value - baseline) / spread

        if abs(z_score) >= threshold:
            anomalies.append({
                "date": date,
                "value": value,
                "baseline": baseline,
                "z_score": z_score,
            })

    return anomalies


def main():
    points = load_points(DATA_PATH)
    anomalies = detect_anomalies(points)

    print("Anomaly Report")
    print(f"Total points: {len(points)}")
    print(f"Detected anomalies: {len(anomalies)}\n")

    for anomaly in anomalies:
        direction = "spike" if anomaly["z_score"] > 0 else "drop"
        print(
            f"- {anomaly['date']}: {direction} "
            f"value={anomaly['value']} "
            f"baseline={anomaly['baseline']:.1f} "
            f"z={anomaly['z_score']:.2f}"
        )


if __name__ == "__main__":
    main()
