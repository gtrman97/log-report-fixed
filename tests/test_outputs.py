import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")


def load_report():
    assert REPORT_PATH.exists(), "missing /app/report.json"
    assert REPORT_PATH.is_file(), "/app/report.json is not a regular file"

    try:
        return json.loads(REPORT_PATH.read_text())
    except json.JSONDecodeError as exc:
        raise AssertionError(f"/app/report.json is not valid JSON: {exc}") from exc


def test_report_has_exact_schema():
    report = load_report()

    assert isinstance(report, dict), "report must be a JSON object"
    assert set(report) == {
        "total_requests",
        "unique_ips",
        "top_path",
    }, "report must contain exactly the required three keys"


def test_total_requests():
    report = load_report()

    assert type(report["total_requests"]) is int
    assert report["total_requests"] == 6


def test_unique_ips():
    report = load_report()

    assert type(report["unique_ips"]) is int
    assert report["unique_ips"] == 3


def test_top_path():
    report = load_report()

    assert type(report["top_path"]) is str
    assert report["top_path"] == "/index.html"