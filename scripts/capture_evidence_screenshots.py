#!/usr/bin/env python3
"""Capture evidence screenshots for NDR V1.1 Word report."""

import asyncio
import os
from pathlib import Path

from playwright.async_api import async_playwright

OUT_DIR = Path("/workspace/assets/evidence_screenshots")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# id, url, wait_selector (optional), clip height, note
TARGETS = [
    {
        "id": "S-01",
        "url": "https://www.secrss.com/articles/79613",
        "wait": "text=23.6",
        "full_page": False,
        "height": 1400,
    },
    {
        "id": "S-02",
        "url": "https://www.qianxin.com/report/detail/rid/62",
        "wait": "text=22.5",
        "full_page": False,
        "height": 1200,
    },
    {
        "id": "S-03",
        "url": "https://www.secrss.com/articles/58067",
        "wait": "text=3.5",
        "full_page": False,
        "height": 1200,
    },
    {
        "id": "S-04",
        "url": "https://www.zscaler.com/blogs/security-research/threatlabz-report-threats-delivered-over-encrypted-channels",
        "wait": "text=87.2",
        "full_page": False,
        "height": 1600,
    },
    {
        "id": "S-05",
        "url": "https://almanac.httparchive.org/en/2024/security",
        "wait": "text=98%",
        "full_page": False,
        "height": 1800,
        "scroll": True,
    },
    {
        "id": "S-06",
        "url": "https://www.grandviewresearch.com/industry-analysis/network-detection-response-ndr-market-report",
        "wait": "text=3.77",
        "full_page": False,
        "height": 1400,
    },
    {
        "id": "S-07",
        "url": "https://www.marketsandmarkets.com/Market-Reports/network-detection-and-response-market-236524642.html",
        "wait": "text=5.82",
        "full_page": False,
        "height": 1400,
    },
    {
        "id": "S-10",
        "url": "https://www.dwcon.cn/post/3410",
        "wait": "text=NDR",
        "full_page": False,
        "height": 1400,
    },
]


async def capture_one(page, target: dict) -> Path:
    out = OUT_DIR / f"{target['id']}.png"
    url = target["url"]
    print(f"  Capturing {target['id']}: {url}")

    await page.goto(url, wait_until="domcontentloaded", timeout=60000)
    await page.wait_for_timeout(2500)

    if target.get("wait"):
        try:
            await page.wait_for_selector(target["wait"], timeout=15000)
        except Exception:
            print(f"    Warning: selector not found for {target['id']}")

    if target.get("scroll"):
        # Scroll to HTTPS section on HTTP Archive
        for y in [0, 800, 1600, 2400]:
            await page.evaluate(f"window.scrollTo(0, {y})")
            await page.wait_for_timeout(400)

    viewport = page.viewport_size or {"width": 1280, "height": 720}
    height = min(target.get("height", 1200), 3000)

    await page.screenshot(
        path=str(out),
        full_page=target.get("full_page", False),
        clip={
            "x": 0,
            "y": 0,
            "width": viewport["width"],
            "height": height,
        },
    )
    print(f"    Saved {out} ({out.stat().st_size // 1024} KB)")
    return out


async def main():
    results = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1280, "height": 900},
            locale="zh-CN",
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
        )
        page = await context.new_page()

        for target in TARGETS:
            try:
                path = await capture_one(page, target)
                results[target["id"]] = path
            except Exception as e:
                print(f"    FAILED {target['id']}: {e}")
                results[target["id"]] = None

        await browser.close()

    ok = sum(1 for v in results.values() if v)
    print(f"\nDone: {ok}/{len(TARGETS)} screenshots captured -> {OUT_DIR}")
    return results


if __name__ == "__main__":
    asyncio.run(main())
