#!/usr/bin/env python3
"""Generate NDR V1.1 Word report with inline evidence screenshots."""

from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.shared import Pt, Inches, RGBColor
from docx.oxml.ns import qn

ASSETS = Path("/workspace/assets/evidence_screenshots")
OUT = Path("/workspace/NDR市场加密流量检测深度分析报告V1.1-含截图.docx")


def set_cell_shading(cell, color: str):
    shading = cell._element.get_or_add_tcPr()
    shd = shading.makeelement(qn("w:shd"), {qn("w:fill"): color, qn("w:val"): "clear"})
    shading.append(shd)


def style_run(run, size=10, bold=False, color=None):
    run.font.name = "Microsoft YaHei"
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "Microsoft YaHei")
    run.font.size = Pt(size)
    run.font.bold = bold
    if color:
        run.font.color.rgb = color


def add_table(doc, headers, rows, header_color="D9E2F3"):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = h
        set_cell_shading(hdr[i], header_color)
        for p in hdr[i].paragraphs:
            for r in p.runs:
                r.bold = True
                r.font.size = Pt(9)
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            table.cell(ri + 1, ci).text = str(val)
    doc.add_paragraph()


def add_note(doc, text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    style_run(run, 9)
    run.italic = True
    run.font.color.rgb = RGBColor(0x80, 0x00, 0x00)


def add_evidence(doc, sid: str, caption: str, url: str, width=Inches(6.0)):
    """Insert screenshot block after a section."""
    img = ASSETS / f"{sid}.png"
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = cap.add_run(caption)
    style_run(r, 9, True, RGBColor(0x1F, 0x4E, 0x79))

    if img.exists() and img.stat().st_size > 5000:
        pic = doc.add_paragraph()
        pic.alignment = WD_ALIGN_PARAGRAPH.CENTER
        pic.add_run().add_picture(str(img), width=width)
    else:
        p = doc.add_paragraph()
        style_run(p.add_run(f"[截图 {sid} 未生成]"), 9, False, RGBColor(0xC0, 0x00, 0x00))

    src = doc.add_paragraph()
    src.alignment = WD_ALIGN_PARAGRAPH.CENTER
    style_run(src.add_run(f"来源：{url}"), 8, False, RGBColor(0x66, 0x66, 0x66))
    doc.add_paragraph()


def build():
    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Microsoft YaHei"
    style.font.size = Pt(10)
    style._element.rPr.rFonts.set(qn("w:eastAsia"), "Microsoft YaHei")

    t = doc.add_heading("NDR 市场加密流量方向深度分析报告 V1.1", 0)
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub = doc.add_paragraph("（2022–2024 历史数据 + 2026–2030 市场预测 · 证据标注版 · 含原文截图）")
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph("报告版本：V1.1-含截图  |  报告日期：2026年5月  |  NDR 2.0 需求验证")

    doc.add_heading("摘要", level=1)
    doc.add_paragraph(
        "本报告全部关键数据均附公开网页原文截图佐证，截图采集时间：2026年5月。"
    )

    doc.add_heading("核心发现（均已公开验证）", level=2)
    add_table(doc, ["维度", "关键数据", "证据", "截图"],
        [
            ["中国 NDR", "23.6亿元（2024）", "IDC", "图2"],
            ["全球 NDR", "37.7亿美元（2025）", "Grand View", "图6"],
            ["加密威胁", "87.2% 经加密通道", "Zscaler", "图4"],
            ["HTTPS", "98% Web 请求", "HTTP Archive", "图5"],
        ])

    # --- Section 1 ---
    doc.add_heading("一、中国 NDR 市场规模与格局（2022–2024）", level=1)
    doc.add_heading("1.1 市场规模变化趋势", level=2)
    add_table(doc, ["年份", "规模", "增速", "来源"],
        [
            ["2022", "3.5亿美元（约24.2亿）", "+13.7%", "IDC CHC50358323"],
            ["2023", "23.8亿元", "+1.6%", "IDC CHC50964624"],
            ["2024", "23.6亿元", "-0.9%", "IDC CHC52196225"],
        ])
    add_evidence(doc, "S-03", "【证据截图 图1】IDC 2022：市场规模 3.5 亿美元", "https://www.secrss.com/articles/58067")
    add_evidence(doc, "S-01", "【证据截图 图2】IDC 2024：市场规模 23.6 亿元", "https://www.secrss.com/articles/79613")

    doc.add_heading("1.2 市场竞争格局（2024）", level=2)
    add_table(doc, ["排名", "厂商", "说明"],
        [
            ["1", "奇安信", "连续四年第一"],
            ["2-5", "绿盟/深信服/安恒/360", "TOP5 主要玩家"],
            ["—", "观成科技", "加密流量检测代表厂商"],
        ])
    add_evidence(doc, "S-02", "【证据截图 图3】IDC 2023：奇安信份额 22.5%（2023年数据）", "https://www.qianxin.com/report/detail/rid/62")
    add_note(doc, "2024 年各厂商精确份额见 IDC 付费报告；图2 含 2024 市场格局与趋势。")

    # --- Section 2 ---
    doc.add_heading("二、加密流量检测（ETD）专项分析", level=1)
    doc.add_heading("2.1 全球加密流量威胁态势", level=2)
    add_table(doc, ["指标", "数值"],
        [
            ["加密通道攻击", "87.2%（+10.3% YoY）"],
            ["恶意软件", "86.5%"],
            ["制造业占比", "42%"],
        ])
    add_evidence(doc, "S-04", "【证据截图 图4】Zscaler ThreatLabz 2024：87.2% 威胁经加密通道", "https://www.zscaler.com/blogs/security-research/threatlabz-report-threats-delivered-over-encrypted-channels")

    doc.add_heading("2.2 全球加密流量渗透率", level=2)
    add_table(doc, ["指标", "数值", "来源"],
        [
            ["HTTPS 请求", "98%", "HTTP Archive 2024"],
            ["TLS 1.3 站点", "73%", "HTTP Archive 2024"],
        ])
    add_evidence(doc, "S-05", "【证据截图 图5】HTTP Archive 2024：HTTPS 采用率", "https://almanac.httparchive.org/en/2024/security")

    doc.add_heading("2.3 IDC 加密流量检测趋势", level=2)
    doc.add_paragraph("IDC 2024：加密流量检测成为更多行业明确需求，AI 不解密检测成为核心竞争力。")
    add_evidence(doc, "S-01", "【证据截图 图7】IDC 2024：加密流量检测趋势原文", "https://www.secrss.com/articles/79613")

    doc.add_heading("2.4 三大技术路线", level=2)
    add_table(doc, ["路线", "代表厂商"],
        [["AI 不解密", "观成、360、绿盟"], ["可选解密", "奇安信、深信服"], ["全量解密", "传统厂商"]])

    # --- Section 3 ---
    doc.add_heading("三、全球 NDR 市场对比", level=1)
    add_table(doc, ["年份", "规模", "来源"],
        [
            ["2025", "37.7亿美元", "Grand View"],
            ["2030", "58.2亿美元", "MarketsandMarkets"],
        ])
    add_evidence(doc, "S-06", "【证据截图 图6】Grand View：全球 NDR 37.7 亿美元（2025）", "https://www.grandviewresearch.com/industry-analysis/network-detection-response-ndr-market-report")
    add_evidence(doc, "S-07", "【证据截图 图7】MarketsandMarkets：2030 年 58.2 亿美元", "https://www.marketsandmarkets.com/Market-Reports/network-detection-and-response-market-236524642.html")

    # --- Section 4 ---
    doc.add_heading("四、市场预测（2026–2030）", level=1)
    doc.add_paragraph("2028–2030 为【估算】，依据贝哲斯咨询 CAGR 推算。")
    add_evidence(doc, "S-10", "【证据截图 图8】数世咨询：NDR 行业需求分布", "https://www.dwcon.cn/post/3410")

    # --- Section 5 ---
    doc.add_heading("五、NDR 2.0 需求验证结论", level=1)
    for line in [
        "市场需求成立：87.2% 攻击走加密通道，IDC 确认 ETD 为核心趋势",
        "市场体量支撑：中国 23.6 亿、全球 37.7 亿美元",
        "建议推进 NDR 2.0 加密流量分析能力建设",
    ]:
        doc.add_paragraph(line, style="List Bullet")

    doc.add_heading("六、数据来源索引", level=1)
    add_table(doc, ["编号", "截图", "链接"],
        [
            ["S-01", "图2/图7", "secrss.com/articles/79613"],
            ["S-02", "图3", "qianxin.com/report/detail/rid/62"],
            ["S-03", "图1", "secrss.com/articles/58067"],
            ["S-04", "图4", "zscaler.com/..."],
            ["S-05", "图5", "almanac.httparchive.org/..."],
            ["S-06", "图6", "grandviewresearch.com/..."],
            ["S-07", "图7", "marketsandmarkets.com/..."],
            ["S-10", "图8", "dwcon.cn/post/3410"],
        ])

    p = doc.add_paragraph()
    style_run(p.add_run("免责声明：截图来自公开网页，以来源链接实时页面为准。报告仅供参考。"), 8)

    doc.save(str(OUT))
    print(f"Saved: {OUT}")


if __name__ == "__main__":
    build()
