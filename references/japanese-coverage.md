# Japanese-related SW source coverage audit

**Requirement:** Consider *every* original `sw-*` file containing `Japanese`, `日本`, `日式`, `日剧`, `轻小说`, `ラノベ`, `坂元裕二`, `小津安二郎` or `起承转合`. A match means **review**, not automatic inclusion in the novel skill. This index uses exact text searches on the supplied archive, then editorial classification.

## Substantive adaptations

| Source | Japanese-related material | Use |
|---|---|---|
| `sw-japanese-screenwriting/SKILL.md` and `reference.md` | Ten Japanese creator methods and Arai; structure-first versus character/fragment-first, diaries, everyday deviations, comic correction, constrained premises, theme discovered late | **Deep integration** in `japanese-methods.md` and `light-novel-craft.md` |
| `sw-series-case-studies/SKILL.md` §9 and `reference-asia.md` §9 | Sakamoto Yuji relationship-centered film screenplay analysis, micro-scenes, repeating motifs, dates and object meanings | **Deep integration** as prose-specific relationship and time techniques; no copy of film ratio targets |
| `sw-story-structure/SKILL.md` §6 | `起承转合` as Chinese theatre/four-movement lens, which overlaps with a Japanese adaptation in `sw-japanese-screenwriting` | **Selective comparison**; do not claim both uses or three acts are identical |
| `sw-genre-anatomy/SKILL.md` relevant genre-mixing mentions | General genre structure, even where Japanese media could be relevant | **General genre lens**; not an independent Japanese doctrine |
| `sw-series-engine-bible/SKILL.md` and `reference.md` | Citation to Sakamoto relationship sample in cross-method materials | **Case-study cross-reference**, not additional source rules |
| `sw-workflow/SKILL.md`, `reference.md`, `terms.md` | Japanese methods routing, Japanese term preservation, writing-system references | **Glossary and routing** only; avoid screenplay format mandates |

## Reviewed but deliberately excluded from active prose rules

| Source | Reason |
|---|---|
| `sw-format-adaptation/SKILL.md` and `reference.md` | Japanese `柱`, `ト書き`, `セリフ` are screenplay formatting terms. Preserve as context but don't draft novels in that format. |
| `sw-chinese-series-practice/*` | References to Japanese series length and historical examples of Japanese wartime adversaries are context, not Japanese fiction-writing methods. |
| `sw-korean-french-screenwriting/SKILL.md` | Refers to companion Japanese skill, but substantive methods inside concern Korean and French creators; adapt on their own merits. |
| `sw-truby-anatomy/SKILL.md` | Occurrence of `起承转合` is cross-structural comparison; not evidence of Japanese authorship. |
| `sw-series-case-studies/reference.md` | Mostly linking notes about Sakamoto example; substantive analysis is in `SKILL.md` and `reference-asia.md`. |

## Nuance

- Do not treat any reference to Japanese *screenplay notation* or television production as evidence of how Japanese novels must be written.
- Do not treat `起承转合` as solely Japanese: this Chinese four-part literary expression shares terminology with Japanese `起承転結` but has varied histories and uses.
- Several supplied sources mention absent sibling skills (`ozu-screenplay-style`). Their contents are not present in the archive, so they cannot be synthesized as if read.
- The old skill `sw-sitcom-comedy` is fully considered for light novel comedy regardless of whether its core text uses a Japanese keyword. The *boke/tsukkomi* bridge is our prose adaptation of character-comedy relationships and Japanese screenwriting discussions.

## Reproducible source locations

The following listing records exact file/line occurrences of the search vocabulary. Incidental historical references are included to demonstrate that they were considered rather than silently dropped.

### `sources/sw/sw-chinese-series-practice/source-skill.md` (2 matching lines)

- Line 3: description: Mainland-Chinese TV-series craft, documents and production chain (国产剧创作体系与制片链) — the China layer parallel to the Japanese and Korean/French skills. Distilled from...
- Line 119: **B. 张明智（制片方评审口径，p0067）**：**① 故事大纲**（时间、地点、主要人物、人物关系、剧情发展；"完全可以判断故事有没有别致的闪光点，有没有新意"）→ **② 分集梗概**（"可以看出全剧的篇章结构，矛盾的起承转合，以及**每一集戏的'戏眼'**"；多人合写时"**更具有凝聚全篇的重要意义**"）→ **③ 分集剧本**（"主体...

### `sources/sw/sw-chinese-series-practice/reference-cases.md` (2 matching lines)

- Line 150: - **一、抗日战争（前 18 集）**。第 1 集"**没有用叙述方式交待李云龙前史，而直接将他放到与坂田联队交战的战场上，以这一戏剧性场面中的动作来展现其人格**"；"**对手的强大无形中提升了李云龙的价值**"；降职为被服厂厂长，"**这种处理模式贯穿李云龙此后的军旅生涯**"。第 2–12 集"**李云龙的日本对手实力不断升级，从坂田联队到...
- Line 153: - **四、军事学院（26–30 集）**。双线（原样）："**主线为李云龙逐渐融入军事学院的学习生活；辅线为李云龙的婚外情。这两条线索都有着较完整的结构，以及起承转合。**"主线节拍：晚报到被罚扫马路（起）→ 捣乱课堂、顶撞教员（发展）→ 受院长批评后端正态度（转）→ 毕业论文宣读推向高潮 → **参加国庆阅兵的将军方阵作为"辉煌"的结局**。辅...

### `sources/sw/sw-chinese-series-practice/reference-rules.md` (2 matching lines)

- Line 39: | 22 | **战火四千金** | 电视剧，史晨风导演，编剧雷婷 | 1937 抗战 | 5 | 第二集（p0176–0178） | **"跪不跪"是最经济的舞台对抗**（一个身体姿态承担整场戏的权力博弈；父："**跪苍生，跪家国，你给我跪下！**"）；**给反方写足理由**——墨玉的"只认五个人"长白是全书最长的反方论述（"我就是我，我不是台北...
- Line 74: 满仓娘：这不是金斗吗，你从日本人那回来了？！

### `sources/sw/sw-chinese-series-practice/reference.md` (3 matching lines)

- Line 26: - **中篇连续剧**：**3 集以上、8 集之内**。"既适合每天放一集，又能集中在一天播放"；"日剧通常保持在 11 集左右的篇幅，也是因为这个缘故"。
- Line 99: 实例：《北京人在纽约》（感情纠葛＋异国生存）、《上海一家人》（旧上海商场奋斗＋与三个童年朋友的情爱纠葛，"既写了社会层面，又写了个人生活层面……使人物形象立体丰满起来"）。《亮剑》第四段落（26–30 集）把它写成明确的主辅两线：主线＝融入军事学院，辅线＝婚外情，两线各有完整的起承转合，并共同指向"**回归**"与"**迷途知返**"（张巍 p03...
- Line 115: | **外国剧** | **必须改结构的制度性原因**（p0042–0043）：日剧 11 集、美剧每周一集且可无限播下去（"故事走向是根据其收视率来调整"→开放结构），而"中国电视剧基本上都是全剧拍摄制作完毕……一次性完整地播出" | 置换背景、重设人物、调整剧情。成功：《家有儿女》（心理医生→儿童剧作家、女强人→主妇、多子女→**再婚重组家庭*...

### `sources/sw/sw-format-adaptation/source-skill.md` (5 matching lines)

- Line 3: description: Screenplay format, page craft, the writing process and adaptation (剧本格式/写作流程/改编) — merged from Wendy Henson (spec format rules), Richard Walter (page craft, revis...
- Line 102: **与 `sw-workflow` 的衔接**：阶段 5 的交付物按体例走——好莱坞式交 `.fountain` 文件，中文场号制与日式交纯文本，戏曲本子走戏曲 skill 的体例；story-bible 只记文件名与页数。
- Line 115: ### 日式剧本：柱・ト書き・セリフ
- Line 215: ### D. 日式（柱・ト書き・セリフ）
- Line 226: 按二之二的默认值：**全中文对白的项目用场号制，英文项目用好莱坞式／Fountain，日式只在明确要求时用；戏曲本子不在此列，走戏曲 skill 的体例**；并在交付件开头一句声明体例与折算方式。**不要因为没人可问就停下来。**

### `sources/sw/sw-format-adaptation/reference.md` (2 matching lines)

- Line 140: 场景标题写法因作者而异（`- LATER`、`-- DAY`、`, JAPANESE CASTLE`），三要素不变。
- Line 225: ### 10.4 日式剧本范例（柱・ト書き・セリフ）

### `sources/sw/sw-japanese-screenwriting/source-skill.md` (7 matching lines)

- Line 2: name: sw-japanese-screenwriting
- Line 3: description: Japanese (and other non-Hollywood) screenwriting methods (日本编剧方法/原创剧本实战) — distilled from ten Japanese directors and writers in ゼロからの脚本術; Kosawa Ryota (three acts...
- Line 6: # 日本编剧方法（Japanese Screenwriting Methods）
- Line 10: 日本原创剧本的实战路径，来源《从零开始做编剧：10 位日本金牌导演、编剧谈剧本》（泊贵洋编）、《故事创作大师班·国际卷》（荒井晴彦）。同一大师班中的韩国（吴胜郁、崔石焕）与法国（奥比坦）编剧见 `sw-korean-french-screenwriting`。与好莱坞体系的关系：**古泽良太、内田贤治、筧昌也承认三幕/起承转合是最有效结构但"探究好...
- Line 30: - **三幕＝起承转合**（古泽）：起厘清人物关系，承呈现矛盾冲突（**"承"精彩就能写出好剧本，"承"多则变化多**），转与合归并为高潮。摹写《七武士》剧本、给电视剧录像倒写成剧本是他的学习法。
- Line 128: ## 九、工作流程（原创日式剧本）
- Line 134: 5. **情节构想**（若写）：客观描写，写打动主人公的"事件"（微小亦可），不写"他这么想"；标起承转合；反转后回头补伏笔。

### `sources/sw/sw-japanese-screenwriting/reference.md` (2 matching lines)

- Line 1: # 日本编剧方法：情节构想范例与工作单
- Line 73: 原著雪山别墅密室杀人"太无聊搞不定"，角川春树"只要留题目随便改"；一个月想到把原著当戏中戏套"龙套追梦"主题；采访剧团培训班女孩一个月；参考《彗星美人》《日落大道》；W＝原著主角首字母/WOMEN/double V；记者招待会女孩甘当替罪羊换角色——"如果我不从他那里拿钱，你们都会相信我们是真正恋爱关系了吧"；"她在撒谎但眼泪是真实的"；创作过程...

### `sources/sw/sw-korean-french-screenwriting/source-skill.md` (2 matching lines)

- Line 10: 来源《故事创作大师班·国际卷》前四讲中的三位：吴胜郁（韩，《八月照相馆》《绿鱼》《无赖汉》）、崔石焕（韩，《王的男人》《港囧》）、弗雷德里克·奥比坦（法，《巴黎，我爱你》《特使》《偷情桥》）。日本的荒井晴彦与十位日本导演见 `sw-japanese-screenwriting`；好莱坞四讲见 `sw-american-case-studies` 与...
- Line 63: - 韩国电影史：翻译日本小说→本土小说→80 年代成人片（每拍四部换一个引进名额）→90 年代新类型→2006 完全开放仍年年有好片；"全球只有中韩印本土可抗衡"。

### `sources/sw/sw-series-case-studies/source-skill.md` (5 matching lines)

- Line 12: 只用一手文本。**凡剧本无幕标记、由分析者按篇幅与转折反推的幕界，一律标注"推断"。** 逐集表、幕页表、节拍表、线网格、长引文分三个文件：四部英语剧本集（West Wing／Sopranos／Downton／Fleabag）见 [reference.md]&#40;reference.md)；方法书里的 pilot 节拍表与 beat sheet 实物（...
- Line 27: | 对话驱动的关系剧 | 九（坂元裕二） |
- Line 217: ## 九、坂元裕二《花束般的恋爱》：对话驱动关系剧
- Line 221: > **注明媒介：这是一部电影剧本**（2021 年上映，导演土井裕泰；蕾克译，一頁 folio 2022.12）。**没有集、没有幕、没有 act out**，不能当剧集结构范本。放进本库的理由：作者是日本最重要的电视连续剧编剧之一（《东京爱情故事》《Mother》《最高の離婚》《カルテット》《大豆田とわ子と三人の元夫》），这是他"对话驱动关系剧...
- Line 291: > 《继承之战》的隐形幕判据、容器集、季形对称与结局工程见 `succession-series-writing`；国产剧分集大纲体量与审查节点见 `sw-chinese-series-practice`；日韩法编剧传统见 `sw-japanese-screenwriting` 与 `sw-korean-french-screenwriting`（...

### `sources/sw/sw-series-case-studies/reference-asia.md` (3 matching lines)

- Line 1: # 剧集案例库（三）：坂元裕二与卢熙京
- Line 5: ## 九、坂元裕二《花束般的恋爱》：场次统计表与五年时间线
- Line 7: > **媒介注明：这是一部电影剧本**（2021 年 1 月 29 日上映，导演土井裕泰，主演菅田将晖、有村架纯；蕾克译，广西师大出版社·一頁 folio 2022 年 12 月版，正文 35 千字）。**没有集、没有幕、没有 act out**，不能当剧集结构范本。放进本库的理由是作者是日本最重要的电视连续剧编剧之一（《东京爱情故事》《Mothe...

### `sources/sw/sw-series-case-studies/reference.md` (2 matching lines)

- Line 5: **体例**：英文文本的引文保留原文，下加一行中文说明；中文／中译本文本的引文用译文（坂元裕二《花束般的恋爱》蕾克译；卢熙京《世间最美丽的离别》小说化本刘悦译）。页码口径沿用各笔记：West Wing、Sopranos、Downton、Calvisi、Landau、Goldberg & Rabkin 为 PDF 页（`p00NN`）；Fleabag...
- Line 642: - 日韩两部文本（坂元裕二《花束般的恋爱》、卢熙京《世间最美丽的离别》）→ [reference-asia.md]&#40;reference-asia.md)

### `sources/sw/sw-series-engine-bible/source-skill.md` (1 matching lines)

- Line 46: - 语料：**Sopranos 剧本集**（Chase 前言＋pilot）、**Fleabag: The Scriptures**、**坂元裕二《花束般的恋爱》**（电影剧本）、**Succession S1–S4 剧本集**。

### `sources/sw/sw-story-structure/source-skill.md` (4 matching lines)

- Line 3: description: Story structure for screenplays and stage plays (故事结构) — merged from Syd Field's paradigm and plot points, Blake Snyder's Save the Cat beat sheet and board, Rober...
- Line 10: 本 skill 合并六种结构体系：悉德·菲尔德《电影剧本写作基础》（范式/情节点）、布莱克·斯奈德《救猫咪》（BS2 十五节拍、演示板）、罗伯特·麦基《故事》（结构层级、故事三角、激励事件、进展纠葛、危机高潮结局）、霍克斯特《编剧的十二条法则》（九节拍、A/B 故事）、尼尔·希克斯《编剧的核心技巧》（三幕＝吸引力/预期/满意、十要素）、陆军《编剧理...
- Line 115: **边界**：起承转合是小戏／独幕剧／戏曲的全剧结构层；长片与剧集只搬其局部手法（八种开头、加减乘除、高潮四病、结尾八法），不搬作骨架；戏曲项目见 `sw-chinese-opera-banqiang` 第二节。
- Line 117: ### 起承转合＝凤头猪肚豹尾

### `sources/sw/sw-workflow/source-skill.md` (5 matching lines)

- Line 46: | 5 | 初稿 | `sw-dialogue` ＋ `sw-format-adaptation`（格式与输出契约）＋ 参照类 skill | 剧本文件（好莱坞式交 `.fountain`，中文场号制或日式交纯文本，见 `sw-format-adaptation` 二之二）、页数、每日进度 | 页数在目标 ±15%；格式硬规则全过；对白遮名可辨 |
- Line 54: - `sw-japanese-screenwriting`、`sw-korean-french-screenwriting`：片段优先、主题后置、类型承诺、集体创作等替代路径；用户明确不走三幕经典设计时在阶段 1 就引入。
- Line 70: | 短片 / 小戏 / 独幕剧 | 1 → 2（用陆军起承转合与八法代替 BS2）→ 3 → 5 | 演示板缩到 10–15 卡；人物≤5；戏核必须先有 |
- Line 93: **参照类 skill 何时进入**：`succession-series-writing`（流媒体群像、隐形幕、季形对称、结局工程）从 S2 起作样板；`sw-series-case-studies`（West Wing 四幕、Sopranos pilot、Downton 多线、Fleabag 六集季、Calvisi 八个 pilot 节拍表、坂...
- Line 180: 3. **无对应物的词保留原词＋一句释义。** 国产特有词（戏眼、扣子、分集梗概、备案公示）与日式术语（柱、ト書き、決定稿）在任何语言下都不硬译，写成 `戏眼 (xìyǎn — the one-line core attraction of an episode)` 这样的形式。

### `sources/sw/sw-workflow/reference.md` (1 matching lines)

- Line 129: 5. `sw-format-adaptation` 第六节 格式诊断（按体例分四组：A 通用 12 问三种体例都跑，B 好莱坞式 7 问／C 中文场号制 8 问／D 日式 6 问只跑你采用的那一种）

### `sources/sw/sw-workflow/terms.md` (6 matching lines)

- Line 12: 4. **第五、六节的词没有英文对应**，任何语言下都**保留原词并附一句释义**，不要硬造对应物：写 `戏眼 (xìyǎn — the one-line core attraction of an episode)`、`ト書き (tosho — the action line of a Japanese script)`。
- Line 105: | slug line / scene heading | 场景头 | 中文场号制写作 `场次 地点 内/外 日/夜`；日式写作"柱" |
- Line 106: | action line | 动作描写 | 日式称 ト書き |
- Line 107: | parenthetical | 括注 | ⚠️ 英文 spec 忌滥用，中文与日式稿放宽 |
- Line 118: ## 五、日本术语（保留原词＋释义）
- Line 144: | 起承转合 | 中国传统叙事四段式，亦作"凤头猪肚豹尾" |

