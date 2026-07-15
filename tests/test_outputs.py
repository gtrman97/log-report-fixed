import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def load_report() -> dict:
    assert REPORT_PATH.is_file(), "/app/report.json must exist as a regular file"

    try:
        report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError("/app/report.json must contain valid JSON") from exc

    return report


def test_success_criterion_1_report_schema():
    """Success criterion 1: report is valid JSON with the required schema."""
    report = load_report()

    assert isinstance(report, dict)
    assert set(report.keys()) == {
        "total_requests",
        "unique_ips",
        "top_path",
    }

    assert type(report["total_requests"]) is int
    assert type(report["unique_ips"]) is int
    assert type(report["top_path"]) is str


def test_success_criterion_2_total_requests():
    """Success criterion 2: total_requests equals the number of non-empty log entries."""
    report = load_report()
    assert report["total_requests"] == 6


def test_success_criterion_3_unique_ips():
    """Success criterion 3: unique_ips equals the number of distinct client IP addresses."""
    report = load_report()
    assert report["unique_ips"] == 3


def test_success_criterion_4_top_path():
    """Success criterion 4: top_path is the most frequently requested path."""
    report = load_report()
    assert report["top_path"] == "/index.html"