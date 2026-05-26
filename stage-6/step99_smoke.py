"""Offline smoke test for Stage 6 URL policy helpers.

Run: python step99_smoke.py
"""

from __future__ import annotations

from browser_policy import normalize_space, validate_public_url


def expect(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_rejected(url: str) -> None:
    try:
        validate_public_url(url)
    except ValueError:
        return
    raise AssertionError(f"URL should be rejected: {url}")


def main() -> int:
    validate_public_url("https://example.com")
    validate_public_url("http://example.com/path")
    expect_rejected("file:///tmp/private.html")
    expect_rejected("https:///missing-host")
    expect(normalize_space("hello\n\n agent\tworld") == "hello agent world", "normalize_space failed")

    print("stage-6 smoke ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
