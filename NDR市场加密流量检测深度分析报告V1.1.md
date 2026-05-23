# NDR 市场加密流量方向深度分析报告 V1.1

**（2022–2024 历史数据 + 2026–2030 市场预测 · 证据标注版）**

| 项目 | 内容 |
|------|------|
| 报告版本 | V1.1（基于 V1.0 修订，全部关键数据附公开来源链接） |
| 报告日期 | 2026 年 5 月 |
| 修订说明 | 修正 10 处数据口径/年份错误，删除 3 处无法验证数据，新增证据索引与截图采集指引 |
| 适用场景 | NDR 2.0 版本加密流量分析需求可行性验证 |

---

## 摘要

本报告聚焦全球及中国 NDR（Network Detection & Response，网络检测与响应）市场中 **加密流量检测**（Encrypted Traffic Detection, ETD）细分方向的发展态势。所有关键统计数据均标注来源机构、报告编号、公开链接及证据等级。

### 核心发现（均已公开验证）

| 维度 | 关键数据 | 证据等级 | 来源 |
|------|---------|---------|------|
| 中国 NDR 市场 | 2024 年 **23.6 亿元**，同比 **-0.9%** | ✅ 已验证 | IDC Doc # CHC52196225 |
| 全球 NDR 市场 | 2025 年 **37.7 亿美元** | ✅ 已验证 | Grand View Research |
| 全球 NDR 预测 | 2030 年 **58.2 亿美元**，CAGR **9.6%** | ✅ 已验证 | MarketsandMarkets |
| 加密流量威胁 | **87.2%** 攻击经 TLS/SSL 通道投递（+10.3% YoY） | ✅ 已验证 | Zscaler ThreatLabz 2024 |
| 恶意软件占比 | 加密威胁中 **86.5%** 为恶意软件 | ✅ 已验证 | Zscaler ThreatLabz 2024 |
| HTTPS 普及 | **98%** Web 请求使用 HTTPS | ✅ 已验证 | HTTP Archive Web Almanac 2024 |
| TLS 1.3 采用 | **73%** 站点使用 TLS 1.3 | ✅ 已验证 | HTTP Archive Web Almanac 2024 |
| 技术趋势 | 加密流量检测成为 NDR 核心趋势 | ✅ 已验证 | IDC Doc # CHC52196225 |

> **V1.1 删除项说明**：V1.0 中 CR5=56.5%、ETD CAGR=32%、金融 NDR 渗透率 68%、2027 年突破 60 亿元等数据因无公开权威出处，本版已删除。

---

## 一、中国 NDR 市场规模与格局（2022–2024）

### 1.1 市场规模变化趋势

**数据来源**：IDC《中国网络威胁检测与响应市场份额》系列报告

| 年份 | 市场规模 | 同比增速 | 来源 | 证据链接 |
|------|---------|---------|------|---------|
| 2022 | **3.5 亿美元**（约 24.2 亿元人民币¹） | **+13.7%** | IDC Doc # CHC50358323 | [安全内参](https://www.secrss.com/articles/58067) |
| 2023 | **23.8 亿元人民币** | **+1.6%** | IDC Doc # CHC50964624 | [奇安信](https://www.qianxin.com/report/detail/rid/62) |
| 2024 | **23.6 亿元人民币** | **-0.9%** | IDC Doc # CHC52196225 | [安全内参](https://www.secrss.com/articles/79613) |

¹ 按 2022 年汇率约 6.9 折算，仅供横向参考。

**【数据冲突标注】**

| 机构 | 2022 年规模 | 差异说明 |
|------|-----------|---------|
| IDC | 3.5 亿美元（出货量统计） | **本报告采用** |
| 华经产业研究院 | 25.48 亿元 | 厂商调研口径，约高 5% |
| 数世咨询 | 24.64 亿元 | 18 家厂商调研，约高 2% |

> 📸 **截图建议 S-03**：安全内参 IDC 2022 报告「3.5 亿美元 +13.7%」段落

### 1.2 市场竞争格局（2024）

**数据来源**：IDC Doc # CHC52196225（2025 年 6 月发布）

2024 年中国 NDR 市场主要玩家（按 IDC 公开 PR 排序）：

| 排名 | 厂商 | 公开信息 | 证据链接 |
|------|------|---------|---------|
| 1 | **奇安信** | 连续四年市场份额第一 | [奇安信](https://www.qianxin.com/report/detail/rid/89) |
| 2 | **绿盟科技** | TOP5 主要玩家 | [安全内参](https://www.secrss.com/articles/79613) |
| 3 | **深信服科技** | TOP5 主要玩家 | 同上 |
| 4 | **安恒信息** | TOP5 主要玩家（与深信服并列第三） | 同上 |
| 5 | **360 数字安全集团** | TOP5 主要玩家 | 同上 |
| — | **观成科技** | IDC 加密流量检测代表厂商；报告含独立章节 | [IDC 目录页](https://my.idc.com/research/viewtoc.jsp?containerId=CHC52196225) |

**2023 年已知精确份额（供历史参考）**：

- 奇安信：**22.5%**，连续三年第一（IDC 2023 报告）
- 来源：[奇安信 IDC 2023 报告页](https://www.qianxin.com/report/detail/rid/62)
- 📸 **截图建议 S-02**

> ⚠️ **V1.1 修正说明**：V1.0 将 22.5% 标注为 2024 年数据，实为 **2023 年**数据。2024 年各厂商精确份额仅在 IDC 付费报告内披露，公开 PR 未给出百分比，**本版不再引用未经截图佐证的精确份额**。

> 📸 **截图建议 S-01 / S-09**：安全内参 IDC 2024 份额图；或 IDC 付费报告份额表（Doc # CHC52196225）

---

## 二、加密流量检测（ETD）专项分析

### 2.1 全球加密流量威胁态势

**数据来源**：Zscaler ThreatLabz《2024 Encrypted Attacks Report》（2024 年 12 月 5 日）

**研究范围**：2023 年 10 月 – 2024 年 9 月，Zscaler 云拦截 **321 亿**次加密攻击

| 指标 | 数值 | 证据等级 | 原文链接 |
|------|------|---------|---------|
| 加密通道攻击占比 | **87.2%**（全部拦截攻击） | ✅ | [Zscaler 博客](https://www.zscaler.com/blogs/security-research/threatlabz-report-threats-delivered-over-encrypted-channels) |
| 同比增幅 | **+10.3%** | ✅ | 同上 |
| 恶意软件占加密威胁 | **86.5%** | ✅ | 同上 |
| XSS 攻击增幅 | **+110.2%** YoY | ✅ | 同上 |
| 加密挖矿/劫持增幅 | **+122.9%** YoY | ✅ | 同上 |
| 制造业攻击占比 | **42%**（第一大目标行业） | ✅ | [GlobeNewswire](https://www.globenewswire.com/news-release/2024/12/05/2992083/0/en/Zscaler-Finds-Over-87-of-Cyberthreats-Hide-in-Encrypted-Traffic-Reinforcing-Need-For-Zero-Trust.html) |
| 制造业攻击次数 | **135 亿**次（2023.10–2024.9） | ✅ | [Zscaler 博客](https://www.zscaler.com/blogs/security-research/threatlabz-report-threats-delivered-over-encrypted-channels) |

> ⚠️ **口径说明**：上述 87.2% 基于 Zscaler 云拦截样本，代表其客户群威胁分布，**不等同于全球全量网络攻击统计**。

> 📸 **截图建议 S-04**：Zscaler 博客 5 Key Findings 段落

### 2.2 全球加密流量渗透率

**V1.1 修正**：V1.0 逐年趋势表（2022–2025）因来源不统一已删除，改为引用 HTTP Archive 与 Google 权威数据。

| 指标 | 数值 | 数据来源 | 证据链接 |
|------|------|---------|---------|
| HTTPS 请求占比（移动端） | **98%** | HTTP Archive Web Almanac 2024 | [链接](https://almanac.httparchive.org/en/2024/security) |
| HTTPS 站点占比 | **96%** | HTTP Archive Web Almanac 2024 | 同上 |
| TLS 1.3 站点占比 | **73%**（桌面） | HTTP Archive Web Almanac 2024 | 同上 |
| Google 全球流量加密率 | **~96%** | Google Transparency Report | [链接](https://transparencyreport.google.com/https/certificates) |

> 📸 **截图建议 S-05**：HTTP Archive Figure 11.1（98% HTTPS 请求）

### 2.3 IDC 关于加密流量检测的趋势判断（定性 · 高价值）

**2024 年 IDC 原文**（Doc # CHC52196225）：

> 「**加密流量检测成为更多行业的明确需求**，利用 AI 实现不解密状态下的流量威胁检测成为技术提供商核心竞争力之一。」

**2022 年 IDC 原文**（Doc # CHC50358323）：

> 「提升加密流量检测模型的丰富度和准确性任重而道远……通过规则匹配、指纹识别、模型训练等多种手段检测加密流量中的恶意威胁。」

- 证据链接：[安全内参 IDC 2024 PR](https://www.secrss.com/articles/79613) · [安全内参 IDC 2022 PR](https://www.secrss.com/articles/58067)
- 📸 **截图建议 S-08**

### 2.4 加密流量检测三大技术路线

| 技术路线 | 技术原理 | 代表厂商（IDC/公开资料） |
|---------|---------|------------------------|
| **AI 不解密检测** | TLS 元数据、JA3 指纹、流量行为特征 + AI/ML | 观成科技、360、绿盟科技 |
| **可选解密** | 对可疑流量选择性解密，平衡检测与隐私 | 奇安信、深信服 |
| **全量解密** | 中间人方式解密 TLS，完整内容检测 | 传统安全厂商 |

> 来源：IDC 2024 PR 厂商点名 + 行业公开资料；竞品能力需 PoC 实测验证。

### 2.5 观成科技：ETD 赛道代表厂商

| 维度 | 公开信息 | 证据状态 |
|------|---------|---------|
| IDC 定位 | 2024 年 IDC NDR 报告加密流量检测代表厂商 | ✅ [安全内参](https://www.secrss.com/articles/79613) |
| 产品 | 瞰云-加密威胁智能检测系统（ENS） | 📸 厂商公开资料 |
| 技术 | AI 多模型 + 流行为特征，支持冰蝎/Cobalt Strike 等加密工具检测 | [腾讯云社区](https://cloud.tencent.com/developer/article/2631616) |

> ⚠️ V1.0 中「连续三年 100% 增长」「60 余项专利」「100 家客户」等数据来自企查查转载，**本版降级为待核实信息**，需厂商官方白皮书佐证。

---

## 三、全球 NDR 市场对比分析

### 3.1 全球 NDR 市场规模

| 年份 | 市场规模 | CAGR | 来源 | 证据链接 |
|------|---------|------|------|---------|
| 2024 | **33.4 亿美元** | — | MarketsandMarkets | [链接](https://www.marketsandmarkets.com/Market-Reports/network-detection-and-response-market-236524642.html) |
| 2025 | **37.7 亿美元** | — | Grand View Research | [链接](https://www.grandviewresearch.com/industry-analysis/network-detection-response-ndr-market-report) |
| 2030（预测） | **58.2 亿美元** | **9.6%**（2025–2030） | MarketsandMarkets | 同上 |
| 2033（预测） | **80.8 亿美元** | **10.1%**（2026–2033） | Grand View Research | 同上 |

> ⚠️ **数据冲突标注**：Grand View（2033 终点）与 MarketsandMarkets（2030 终点）预测口径不同，**不可合并为单一预测曲线**。

> 📸 **截图建议 S-06 / S-07**

### 3.2 区域市场（定性）

| 区域 | 公开信息 | 证据状态 |
|------|---------|---------|
| 北美 | 全球最大区域市场 | 📸 需 Grand View/M&M 区域章节截图 |
| 亚太 | 增长最快区域，中国为主要驱动力 | MarketsandMarkets PR |
| 中国 | 增速高于全球平均（IDC 2023：23.8 亿 vs 全球 ~9–10% CAGR） | 间接推算 |

---

## 四、市场预测（2026–2030）

### 4.1 中国 NDR 市场预测

**【估算】** 以下 2028–2030 年数据基于贝哲斯咨询 CAGR 18.6% 等比推算，**非 IDC 官方预测**。

| 年份 | 市场规模（亿元） | 同比增速 | 依据 |
|------|---------------|---------|------|
| 2026 | 31.5 | +18.6% | 贝哲斯咨询 |
| 2027 | 37.5 | +19.0% | 贝哲斯咨询 |
| 2028 | 44.5 | +18.7% | 【估算】 |
| 2029 | 53.0 | +19.1% | 【估算】 |
| 2030 | 63.0 | +18.9% | 【估算】 |

- 来源：[格隆汇转载](https://m.gelonghui.com/p/901401)
- 推算公式：\( V_{n+1} = V_n \times (1 + CAGR) \)

### 4.2 ETD 细分市场

**V1.1 修正**：V1.0 中 ETD CAGR=32%、2024 年 5.1 亿元等精确数字 **无公开权威出处，已全部删除**。

**可引用的定性判断**：

1. IDC 2024：加密流量检测成为更多行业明确需求（✅ 已验证）
2. 数世咨询：金融、运营商、地方政府、互联网、监管机构为 NDR 需求前五行业（[链接](https://www.dwcon.cn/post/3410)）
3. ETD 细分市场规模 **暂无权威公开量化数据**，待 IDC 专项报告或厂商财报披露

---

## 五、发展趋势与 NDR 2.0 需求验证结论

### 5.1 核心增长驱动因素（附证据）

| 驱动因素 | 数据/定性支撑 | 证据 |
|---------|-------------|------|
| 加密流量普及 | 98% Web 请求 HTTPS | HTTP Archive 2024 |
| 威胁隐蔽化 | 87.2% 攻击走加密通道 | Zscaler 2024 |
| AI 不解密检测 | IDC 列为 2024 核心竞争力 | IDC CHC52196225 |
| 合规政策 | 《数据安全法》《个人信息保护法》 | 政策法规 |
| 云原生流量 | IDC：东西向/云上全流量检测需求增长 | IDC PR |
| GenAI 赋能 | IDC：AI 智能体提升 NDR 运营效率 | IDC CHC52196225 |

### 5.2 热点赛道

- **AI 不解密检测**：IDC 2024 点名代表厂商（360、观成、绿盟）
- **云原生 NDR**：阿里云、华为云、腾讯云（IDC 2024 PR）
- **NDR + 数据安全融合**：API 安全、敏感数据检测（IDC 2024 PR）
- **GenAI 赋能 NDR**：大模型告警分析、钓鱼检测（IDC 2024 PR）

### 5.3 潜在增长机会（定性）

| 行业 | 公开依据 | 证据状态 |
|------|---------|---------|
| 金融 | 数世咨询：NDR 需求占比前五 | ✅ |
| 运营商/政府 | 数世咨询：NDR 需求占比前五 | ✅ |
| 医疗 | 勒索攻击频发（Zscaler 行业报告） | 定性 |
| 中小企业 | 云化部署模式（IDC 2022：市场下沉趋势） | 定性 |
| 信创 | 国产化替代（行业共识） | 定性 |

> ⚠️ V1.0「金融 NDR 渗透率 68%」已删除（无公开出处）。

### 5.4 NDR 2.0 需求验证结论

基于上述 **已验证数据**，NDR 2.0 加密流量分析功能具备明确市场需求：

1. **市场体量支撑**：中国 NDR 23.6 亿（2024），全球 37.7 亿美元（2025），赛道规模可观
2. **威胁驱动明确**：87.2% 攻击经加密通道，86.5% 为恶意软件
3. **技术方向清晰**：IDC 确认 AI 不解密检测为核心竞争力
4. **竞品窗口存在**：观成科技等专精厂商已获 IDC 点名，360/绿盟/奇安信/深信服均在布局
5. **待补充项**：竞品 PoC 实测、IDC 2024 精确份额截图、ETD 细分量化

---

## 六、证据附件与截图采集清单

| 编号 | 截图内容 | URL | 对应章节 |
|------|---------|-----|---------|
| S-01 | IDC 2024 市场规模 + 份额图 | https://www.secrss.com/articles/79613 | 1.1, 1.2 |
| S-02 | 奇安信 22.5%（2023）段落 | https://www.qianxin.com/report/detail/rid/62 | 1.2 |
| S-03 | IDC 2022 3.5 亿美元段落 | https://www.secrss.com/articles/58067 | 1.1 |
| S-04 | Zscaler 87.2% 关键发现 | https://www.zscaler.com/blogs/security-research/threatlabz-report-threats-delivered-over-encrypted-channels | 2.1 |
| S-05 | HTTP Archive HTTPS 98% | https://almanac.httparchive.org/en/2024/security | 2.2 |
| S-06 | Grand View 37.7 亿美元 | https://www.grandviewresearch.com/industry-analysis/network-detection-response-ndr-market-report | 3.1 |
| S-07 | MarketsandMarkets 2030 预测 | https://www.marketsandmarkets.com/Market-Reports/network-detection-and-response-market-236524642.html | 3.1 |
| S-08 | IDC 加密流量检测趋势段落 | https://www.secrss.com/articles/79613 | 2.3 |
| S-09 | IDC 2024 厂商份额表（付费） | IDC Doc # CHC52196225 | 1.2 |
| S-10 | 数世咨询 NDR 行业分布 | https://www.dwcon.cn/post/3410 | 4.2, 5.3 |

---

## 七、数据来源索引

| # | 机构 | 报告 | 编号 | 链接 |
|---|-----|------|------|------|
| 1 | IDC | 中国网络威胁检测与响应市场份额，2022 | CHC50358323 | https://www.secrss.com/articles/58067 |
| 2 | IDC | 中国网络威胁检测与响应市场份额，2023 | CHC50964624 | https://www.qianxin.com/report/detail/rid/62 |
| 3 | IDC | 中国 GenAI 赋能的网络威胁检测与响应市场份额，2024 | CHC52196225 | https://www.secrss.com/articles/79613 |
| 4 | Zscaler | ThreatLabz 2024 Encrypted Attacks Report | — | https://www.zscaler.com/blogs/security-research/threatlabz-report-threats-delivered-over-encrypted-channels |
| 5 | HTTP Archive | Web Almanac 2024 - Security | — | https://almanac.httparchive.org/en/2024/security |
| 6 | Google | Transparency Report - HTTPS | — | https://transparencyreport.google.com/https/certificates |
| 7 | Grand View Research | Network Detection And Response Market | — | https://www.grandviewresearch.com/industry-analysis/network-detection-response-ndr-market-report |
| 8 | MarketsandMarkets | Network Detection and Response Market | TC 9581 | https://www.marketsandmarkets.com/Market-Reports/network-detection-and-response-market-236524642.html |
| 9 | 数世咨询 | NDR 能力指南 | — | https://www.dwcon.cn/post/3410 |
| 10 | 贝哲斯咨询 | NDR 市场规模及未来发展走向 | — | https://m.gelonghui.com/p/901401 |

---

## 免责声明

本报告 V1.1 数据均来源于公开渠道，经逐项公开网页交叉验证。标注【估算】的数据已说明推算依据，不得作为精确投资决策依据。精确厂商份额等数据需 IDC 付费报告原文截图佐证。报告仅供参考，不构成投资建议。

**关联文档**：`NDR2.0可行性调研-数据证据索引与核验清单.md`（含逐条核验详情）
