# 📐 數學A

<callout icon="🧭">數學A 100 分鐘：單選 6 題×5、多選 6 題×5、選填 5 題×5（全對才給分）＋混合題或非選 15 分。</callout>

> 第 3 週上課前補齊：各單元必考觀念、常見題型與解題流程。

## 🎯 觀念大綱

### 數與函數
- **數與式、指數對數**：指數、對數先化成同底，再比較指數；高斯記號 [x] 要一個一個代值確認。
- **多項式與二次函數**：多項式看首項係數與對稱中心；二次函數先配方找頂點。
- **三角函數**：先畫出單位圓或函數圖形，再判斷範圍與交點；倍角公式要熟。
- **數列與級數**：等差看中項、等比看公比；遞迴式試著找出「平移後成等比」的形式。

### 幾何與向量
- **坐標幾何（直線、圓、不等式區域）**：把條件畫在坐標平面上；點到直線距離與圓的切割、弦長公式是核心。
- **向量與空間**：內積判斷垂直與夾角，外積或行列式算面積與體積；比例分點用向量表示最快。
- **矩陣**：矩陣乘法先算小次方找規律；線性組合可以把未知向量拆成已知向量。

### 機率統計與計數
- **機率與統計**：期望值＝Σ（值×機率）；條件機率＝交集／條件；迴歸直線與標準化分數是常考。
- **排列組合**：先分類再計數，注意「相同結果」只算一次；綁在一起的排列先排區塊。

## 📝 第 1 週每日練習（含解析）

<details><summary>Day 1｜機率、函數與矩陣</summary>

<details><summary>📝 115 學測數學A 第 1 題（全國答對率 84%）</summary>

![題目]({{SITE}}/img/mathA/115-01.webp)

<details><summary>看答案與解析</summary>

**答案：2**
💡 期望值＝Σ（獎金×機率）。兩次都「吉」機率 1/9、兩次都「祥」機率 1/9。
P(吉吉)＝(1/3)(1/3)＝1/9，P(祥祥)＝1/9，其他情況 0 元。
期望值＝180×(1/9)＋90×(1/9)＝20＋10＝30（元）→ 答案 (2)

</details>

[到練習網站作答]({{SITE}}/#/item/ma115-01)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0q054344158947111283/03-115%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e5%8d%b7.pdf)

</details>
<details><summary>📝 115 學測數學A 第 2 題（全國答對率 55%）</summary>

![題目]({{SITE}}/img/mathA/115-02.webp)

<details><summary>看答案與解析</summary>

**答案：1**
💡 直接代入：f(−20)＝10＋8＝18，f(0)＝9＋9＝18，f(1)＝9＋10＝19。
[a] 是「不超過 a 的最大整數」。
f(−20)＝[√119]＋[√79]＝10＋8＝18（10²＝100 ≤ 119 < 121，8²＝64 ≤ 79 < 81）
f(0)＝[√99]＋[√99]＝9＋9＝18
f(1)＝[√98]＋[√100]＝9＋10＝19
所以 f(−20)＝f(0) < f(1) → 答案 (1)

</details>

[到練習網站作答]({{SITE}}/#/item/ma115-02)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0q054344158947111283/03-115%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e5%8d%b7.pdf)

</details>
<details><summary>📝 115 學測數學A 第 7 題（全國答對率 74%）</summary>

![題目]({{SITE}}/img/mathA/115-07.webp)

<details><summary>看答案與解析</summary>

**答案：3,4**
💡 兩條直線交於 (1,−1)，可行區域在兩線下方，落在第三、第四象限。
2x−y−3>0 ⇔ y<2x−3；x＋2y＋1<0 ⇔ y<−(x＋1)/2，兩線交於 (1,−1)。
第一象限：y>0 但 y<−(x＋1)/2<0，不可能。
第二象限：x<0 時 y<2x−3<−3，y 不可能為正。
第三象限：例 (−1,−10) 兩式皆成立 ✓
第四象限：例 (2,−5) 兩式皆成立 ✓
x 軸（y＝0）：需 x>3/2 且 x<−1，矛盾。
→ 答案 (3)(4)

</details>

[到練習網站作答]({{SITE}}/#/item/ma115-07)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0q054344158947111283/03-115%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e5%8d%b7.pdf)

</details>
<details><summary>📝 115 學測數學A 第 8 題（全國答對率 70%）</summary>

![題目]({{SITE}}/img/mathA/115-08.webp)

<details><summary>看答案與解析</summary>

**答案：2,5**
💡 A²＝2A＋I ⇒ Aⁿ⁺²＝2Aⁿ⁺¹＋Aⁿ；又 A²ⁿ＝(Aⁿ)²。
A²＝[[5,2],[2,1]]。
(1) b₂＝2、c₂＝2，不是 b₂<c₂ ✗
(2) 2A＋I＝[[5,2],[2,1]]＝A² ✓
(3) 由 (2) 得 Aⁿ⁺²＝2Aⁿ⁺¹＋Aⁿ，所以 cₙ₊₂＝2cₙ₊₁＋cₙ，不是 cₙ₊₁＋2cₙ ✗（例：c₄＝12，但 c₃＋2c₂＝9）
(4) Aⁿ(0,1)ᵀ＝(bₙ,dₙ)ᵀ；而 (bₙ₊₁,dₙ₊₁)ᵀ＝Aⁿ(A(0,1)ᵀ)＝Aⁿ(1,0)ᵀ＝(aₙ,cₙ)ᵀ，兩者不同 ✗
(5) A²ⁿ＝(Aⁿ)²，a₂ₙ＝aₙ²＋bₙcₙ，d₂ₙ＝cₙbₙ＋dₙ²，相減得 dₙ²−aₙ² ✓
→ 答案 (2)(5)

</details>

[到練習網站作答]({{SITE}}/#/item/ma115-08)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0q054344158947111283/03-115%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e5%8d%b7.pdf)

</details>
<details><summary>📝 115 學測數學A 第 13 題（全國答對率 73%）</summary>

![題目]({{SITE}}/img/mathA/115-13.webp)

<details><summary>看答案與解析</summary>

**答案：9,1,0**
💡 條件機率＝(碩士且通過)/(通過)＝(9/20)/(10/20)＝9/10。
學士且通過：(1/4)(1/5)＝1/20；碩士且通過：(3/4)(3/5)＝9/20。
P(碩士｜通過)＝(9/20)/(1/20＋9/20)＝9/10
→ 13-1＝9，13-2＝1，13-3＝0

</details>

[到練習網站作答]({{SITE}}/#/item/ma115-13)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0q054344158947111283/03-115%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e5%8d%b7.pdf)

</details>

</details>

<details><summary>Day 2｜指數、計數與向量</summary>

<details><summary>📝 115 學測數學A 第 3 題（全國答對率 41%）</summary>

![題目]({{SITE}}/img/mathA/115-03.webp)

<details><summary>看答案與解析</summary>

**答案：1**
💡 f(c₂)/f(c₁)＝a^(10/3)＝4，所以 a＝2^(3/5)；公比 f(8)/f(10)＝a^(−2)。
f(c₂)/f(c₁)＝a^(c₂−c₁)＝a^(10/3)＝4 ⇒ a＝4^(3/10)＝2^(6/10)＝2^(3/5)
等比數列 f(10), f(8), f(6) 的公比＝f(8)/f(10)＝a^(−2)＝2^(−6/5) → 答案 (1)

</details>

[到練習網站作答]({{SITE}}/#/item/ma115-03)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0q054344158947111283/03-115%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e5%8d%b7.pdf)

</details>
<details><summary>📝 115 學測數學A 第 4 題（全國答對率 56%）</summary>

![題目]({{SITE}}/img/mathA/115-04.webp)

<details><summary>看答案與解析</summary>

**答案：3**
💡 草藥 1 種＋食物 10 種＋藥水（1 基本 2 進階或 3 進階）390 種＝401。
分三類計算「不同的道具」：
① 3 種基本材料 → 一律同一種草藥：1 種
② 2 基本＋1 進階 → 由進階材料決定：10 種
③ 其他組合都是不同藥水：C(6,1)C(10,2)＋C(10,3)＝6×45＋120＝390 種
共 1＋10＋390＝401 → 答案 (3)
提醒：先確認「什麼情況會產生相同結果」，再決定用組合數還是直接數種類。

</details>

[到練習網站作答]({{SITE}}/#/item/ma115-04)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0q054344158947111283/03-115%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e5%8d%b7.pdf)

</details>
<details><summary>📝 115 學測數學A 第 9 題（全國答對率 44%）</summary>

![題目]({{SITE}}/img/mathA/115-09.webp)

<details><summary>看答案與解析</summary>

**答案：1,2,4**
💡 數學 T＝50＋(5/6)(S−60)，英文 T＝50＋(5/4)(S−60)；兩科換算比例不同。
(1) 英文 52 分：T＝50＋10×(−8/8)＝40 ✓
(2) 數學 T−S＝50＋(5/6)(S−60)−S＝−S/6 ≤ 0，T 不會超過原始成績 ✓
(3) ✗ 反例：乙（數80、英60）T 平均＝(66.7＋50)/2≈58.3；丙（數60、英76）T 平均＝(50＋70)/2＝60。乙原始平均 70 較高，T 平均反而較低。
(4) T≥40 ⇔ 數學 S≥48、英文 S≥52，數學及格分數較低 ✓
(5) 原始成績迴歸斜率＝r×12/8＝1.5r；T 分數兩科標準差都是 10，斜率＝r，一般不相同 ✗
→ 答案 (1)(2)(4)

</details>

[到練習網站作答]({{SITE}}/#/item/ma115-09)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0q054344158947111283/03-115%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e5%8d%b7.pdf)

</details>
<details><summary>📝 115 學測數學A 第 10 題（全國答對率 36%）</summary>

![題目]({{SITE}}/img/mathA/115-10.webp)

<details><summary>看答案與解析</summary>

**答案：1,5**
💡 △ABD 面積 8、△ABE 面積 3 ⇒ DE:EB＝5:3 ⇒ DC＝(5/3)AB。
(1) cos∠BAD＝(AB·AD)/(|AB||AD|)＝(2−30)/(√40·√26)＝−7/√65＝−7√65/65 ✓
(2) △ABD＝½|2×5−(−6)×1|＝8，不是 9 ✗
梯形 AB∥DC：設 DC＝k·AB，則 BE:ED＝1:k。△AED/△ABE＝k，3＋3k＝8 ⇒ k＝5/3。
(3) AC＝AD＋DC＝(1,5)＋(5/3)(2,−6)＝(13/3,−5)，AE＝(3/8)AC＝(13/8,−15/8) ✗
(4) 面積＝△ABD＋△BCD＝8＋(5/3)×8＝64/3，不是 65/3 ✗
(5) BC＝AC−AB＝(7/3,1)，|BC|＝√58/3≈2.54 < 8/3≈2.67 ✓
→ 答案 (1)(5)

</details>

[到練習網站作答]({{SITE}}/#/item/ma115-10)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0q054344158947111283/03-115%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e5%8d%b7.pdf)

</details>
<details><summary>📝 115 學測數學A 第 14 題（全國答對率 19%）</summary>

![題目]({{SITE}}/img/mathA/115-14.webp)

<details><summary>看答案與解析</summary>

**答案：1,4**
💡 直線方向向量 (1,b)，垂直 ⇒ a＋b²＝0 ⇒ a＋b＝−(b−½)²＋¼。
y＝bx−1 的方向向量為 (1,b)。(a,b) 與直線垂直 ⇒ (a,b)·(1,b)＝a＋b²＝0 ⇒ a＝−b²。
a＋b＝−b²＋b＝−(b−1/2)²＋1/4，最大值 1/4（b＝1/2 時）
→ 14-1＝1，14-2＝4

</details>

[到練習網站作答]({{SITE}}/#/item/ma115-14)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0q054344158947111283/03-115%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e5%8d%b7.pdf)

</details>

</details>

<details><summary>Day 3｜矩陣、坐標與多項式</summary>

<details><summary>📝 115 學測數學A 第 5 題（全國答對率 26%）</summary>

![題目]({{SITE}}/img/mathA/115-05.webp)

<details><summary>看答案與解析</summary>

**答案：5**
💡 A 把 (1,0,1) 送到 (1,0,1)……而 (1,0,−1) 被送到 0，解有無限多個且第二分量恆為 0。
(1,0,1)ᵀ＝(1,1,0)ᵀ＋(0,−1,1)ᵀ，所以 A(1,0,1)ᵀ＝(0,−1,1)ᵀ＋(1,1,0)ᵀ＝(1,0,1)ᵀ。
又 A(1,0,−1)ᵀ＝0，所以所有解為 v＝(1,0,1)ᵀ＋t(1,0,−1)ᵀ＝(1＋t, 0, 1−t)ᵀ。
（三個已知向量行列式＝2≠0，彼此獨立，A 的零空間就是 (1,0,−1) 方向。）
v 垂直 (0,1,0) ⇔ v₂＝0，而所有解的 v₂ 都是 0 → 有無窮多個 → 答案 (5)

</details>

[到練習網站作答]({{SITE}}/#/item/ma115-05)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0q054344158947111283/03-115%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e5%8d%b7.pdf)

</details>
<details><summary>📝 115 學測數學A 第 6 題（全國答對率 37%）</summary>

![題目]({{SITE}}/img/mathA/115-06.webp)

<details><summary>看答案與解析</summary>

**答案：2**
💡 分三種等腰情況，並排除三點共線；共 2 點。
AB＝√(3²＋4²)＝5，C 在 y＝−6 上。
① CA＝CB：C 在 AB 的中垂線 y＝(3/4)(x−1/2) 上，代 y＝−6 得 C(−15/2, −6)，1 點。
② AC＝AB＝5：(x−2)²＋16＝25 ⇒ x＝5 或 −1。但 (5,−6) 在直線 AB 上（三點共線，不成三角形），只剩 (−1,−6)，1 點。
③ BC＝AB＝5：(x＋1)²＋64＝25 無解。
共 2 點 → 答案 (2)。易錯點：忘了排除共線的情況。

</details>

[到練習網站作答]({{SITE}}/#/item/ma115-06)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0q054344158947111283/03-115%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e5%8d%b7.pdf)

</details>
<details><summary>📝 115 學測數學A 第 11 題（全國答對率 33%）</summary>

![題目]({{SITE}}/img/mathA/115-11.webp)

<details><summary>看答案與解析</summary>

**答案：2,4**
💡 (0,1) 永遠是交點；cos 是偶函數，所以 (a,b) 在 L_m 上 ⇔ (−a,b) 在 L₋ₘ 上。
(1) x＝0 時 cos0＝1＝m·0＋1，(0,1) 恆為交點，x 坐標不是負的 ✗
(2) b＝cos(πa/2)＝ma＋1 ⇒ cos(−πa/2)＝b 且 (−m)(−a)＋1＝b ✓
(3) cos(10π/3)＝cos(4π/3)＝−1/2 ≠ 1/2，該點不在 Γ 上 ✗
(4) cos(πx/2)＝−1 ⇒ x＝2＋4k；代入 −1＝mx＋1 ⇒ 1/m＝−x/2＝−(1＋2k)，是奇數 ✓
(5) 反例：m＝−1（過 (1,0)），交點有 x＝0、1、2 三個，是奇數個 ✗
→ 答案 (2)(4)

</details>

[到練習網站作答]({{SITE}}/#/item/ma115-11)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0q054344158947111283/03-115%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e5%8d%b7.pdf)

</details>
<details><summary>📝 115 學測數學A 第 12 題（全國答對率 28%）</summary>

![題目]({{SITE}}/img/mathA/115-12.webp)

<details><summary>看答案與解析</summary>

**答案：2,4**
💡 g＝f−2x³−2x，g 首項係數 −1；對稱中心 x＝−(二次項係數)/(3×首項係數)。
設 f＝x³＋px²＋qx＋r，則 g＝−x³＋px²＋(q−2)x＋r。
a₁＝−p/3，a₂＝p/3 ⇒ a₁＋a₂＝0 → (2) ✓
(1) f−g＝2x³＋2x＝2x(x²＋1)＝0 只有 x＝0，只交一點 ✗
(3) b₁＋b₂ 會隨 p、r 改變，無法唯一確定 ✗
(4) a₁＝a₂ ⇒ a₁＝0 ⇒ p＝0，b₁＝f(0)＝r＝g(0)＝b₂ ✓
(5) b₁−b₂＝(2q−2)a₁；取 q＝1、p≠0，b₁＝b₂ 但 a₁≠a₂ ✗
→ 答案 (2)(4)

</details>

[到練習網站作答]({{SITE}}/#/item/ma115-12)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0q054344158947111283/03-115%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e5%8d%b7.pdf)

</details>
<details><summary>📝 115 學測數學A 第 15 題（全國答對率 31%）</summary>

![題目]({{SITE}}/img/mathA/115-15.webp)

<details><summary>看答案與解析</summary>

**答案：3,2**
💡 b 是 a、c 的中點，三點共線 ⇒ log4b 是 log3a、log6c 的平均 ⇒ 16b²＝18ac。
a、b、c 等差 ⇒ b 是 a、c 的中點；三點共線 ⇒ 中間點的 y 值也是平均：
2log(4b)＝log(3a)＋log(6c) ⇒ 16b²＝18ac ⇒ 8b²＝9ac。
代 c＝2b−a：8b²＝9a(2b−a) ⇒ 8t²−18t＋9＝0（t＝b/a）⇒ t＝3/2 或 3/4。
a<b ⇒ t>1 ⇒ b/a＝3/2 → 15-1＝3，15-2＝2

</details>

[到練習網站作答]({{SITE}}/#/item/ma115-15)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0q054344158947111283/03-115%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e5%8d%b7.pdf)

</details>

</details>

<details><summary>Day 4｜綜合與挑戰題</summary>

<details><summary>📝 114 學測數學A 第 1 題（全國答對率 57%）</summary>

![題目]({{SITE}}/img/mathA/114-01.webp)

<details><summary>看答案與解析</summary>

**答案：5**
💡 獨立 ⇔ P(藍∩1號)＝P(藍)P(1號)：2/(9＋k)＝[5/(9＋k)]·[6/(9＋k)]。
總數 9＋k。P(藍)＝5/(9＋k)，P(1號)＝6/(9＋k)，P(藍且1號)＝2/(9＋k)。
獨立 ⇒ 2/(9＋k)＝30/(9＋k)² ⇒ 9＋k＝15 ⇒ k＝6 → 答案 (5)

</details>

[到練習網站作答]({{SITE}}/#/item/ma114-01)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0p056503510203248955/03-114%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e9%a1%8c.pdf)

</details>
<details><summary>📝 114 學測數學A 第 2 題（全國答對率 62%）</summary>

![題目]({{SITE}}/img/mathA/114-02.webp)

<details><summary>看答案與解析</summary>

**答案：2**
💡 兩三角形面積分別為 (2/3)a² 與 (3/4)a²，差 a²/12＝3。
L₁ 斜率 −4/3，y 截距 (4/3)a，面積＝½·a·(4/3)a＝(2/3)a²。
L₂ 斜率 −3/2，y 截距 (3/2)a，面積＝½·a·(3/2)a＝(3/4)a²。
面積差＝(3/4−2/3)a²＝a²/12＝3 ⇒ a²＝36 ⇒ a＝6 → 答案 (2)

</details>

[到練習網站作答]({{SITE}}/#/item/ma114-02)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0p056503510203248955/03-114%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e9%a1%8c.pdf)

</details>
<details><summary>📝 115 學測數學A 第 16 題（全國答對率 20%）</summary>

![題目]({{SITE}}/img/mathA/115-16.webp)

<details><summary>看答案與解析</summary>

**答案：3,5,2**
💡 f(x)＝−4x²＋1，P(0,1)；平移後頂點 (h,1＋2h) 過 (1/2,0) ⇒ h＝3/2。
Γ 過 (±1/2,0) 且頂點在 y 軸上：f(x)＝k(x²−1/4)，頂點 (0,−k/4) 在 y＝1＋2x ⇒ −k/4＝1 ⇒ k＝−4。P＝(0,1)。
平移後 y＝−4(x−h)²＋(1＋2h)，過 (1/2,0)：−4(1/2−h)²＋1＋2h＝0 ⇒ −4h²＋6h＝0 ⇒ h＝3/2（h＝0 與 P 重合，不合）。
Q＝(3/2,4)，PQ＝√((3/2)²＋3²)＝√45/2＝3√5/2
→ 16-1＝3，16-2＝5，16-3＝2

</details>

[到練習網站作答]({{SITE}}/#/item/ma115-16)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0q054344158947111283/03-115%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e5%8d%b7.pdf)

</details>
<details><summary>📝 114 學測數學A 第 7 題（全國答對率 66%）</summary>

![題目]({{SITE}}/img/mathA/114-07.webp)

<details><summary>看答案與解析</summary>

**答案：2,4**
💡 bₙ₊₁＝bₙ/3，b₁＝9/4；3ⁿaₙ＝[27＋3ⁿ(2n−3)]/4。
a₂＝(a₁＋1)/3＝1 → (1) ✗
b₂＝1−1＋3/4＝3/4 → (2) ✓
bₙ₊₁＝(aₙ＋n)/3−(n＋1)/2＋3/4＝(1/3)(aₙ−n/2＋3/4)＝bₙ/3，公比 1/3 → (3) ✗
aₙ＝(9/4)(1/3)ⁿ⁻¹＋n/2−3/4 ⇒ 3ⁿaₙ＝[27＋3ⁿ(2n−3)]/4，檢查 n 為奇數或偶數時分子都被 4 整除且為正 → (4) ✓
b₁₀＝(9/4)(1/3)⁹＝1/8748≈1.14×10⁻⁴ > 10⁻⁴ → (5) ✗
→ 答案 (2)(4)

</details>

[到練習網站作答]({{SITE}}/#/item/ma114-07)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0p056503510203248955/03-114%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e9%a1%8c.pdf)

</details>
<details><summary>📝 115 學測數學A 第 17 題（全國答對率 6%）</summary>

![題目]({{SITE}}/img/mathA/115-17.webp)

<details><summary>看答案與解析</summary>

**答案：3,1,1**
💡 設 ∠ACD＝θ，由 BC＝2BD 推得 sinθ＝1/4，k＝tanθ/tan3θ＝3/11。
以 A 為原點、AB 為 x 軸、AC 為 y 軸，設 AC＝c，∠ACD＝θ，則 ∠ACB＝3θ。
AD＝c·tanθ，AB＝c·tan3θ，BC＝c/cos3θ，BD＝c(tan3θ−tanθ)。
BC＝2BD ⇒ 1/cos3θ＝2·sin2θ/(cos3θ cosθ) ⇒ 1＝4sinθ ⇒ sinθ＝1/4。
tanθ＝1/√15，tan3θ＝(3tanθ−tan³θ)/(1−3tan²θ)＝11/(3√15)。
k＝AD/AB＝tanθ/tan3θ＝3/11 → 17-1＝3，17-2＝1，17-3＝1
這題全國答對率只有 6%，關鍵是把「角度倍數」和「邊長比例」都用 θ 表示。

</details>

[到練習網站作答]({{SITE}}/#/item/ma115-17)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0q054344158947111283/03-115%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e5%8d%b7.pdf)

</details>

</details>

<details><summary>Day 5｜計數、三角與數列</summary>

<details><summary>📝 114 學測數學A 第 3 題（全國答對率 60%）</summary>

![題目]({{SITE}}/img/mathA/114-03.webp)

<details><summary>看答案與解析</summary>

**答案：4**
💡 三類各自綑綁排 3!＝6 種順序，扣掉「歌唱排第一」的 2 種，剩 4 種。
同類綑綁：類別順序 3!＝6 種；類內排列 5!×4!×3!。
「歌唱在鋼琴之後或小提琴之後」⇔ 歌唱不是第一個，排除「歌唱、鋼琴、小提琴」與「歌唱、小提琴、鋼琴」2 種。
共 4×5!×4!×3! → 答案 (4)

</details>

[到練習網站作答]({{SITE}}/#/item/ma114-03)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0p056503510203248955/03-114%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e9%a1%8c.pdf)

</details>
<details><summary>📝 114 學測數學A 第 4 題（全國答對率 44%）</summary>

![題目]({{SITE}}/img/mathA/114-04.webp)

<details><summary>看答案與解析</summary>

**答案：3**
💡 對每個整數 x＝3~30，數 0<y<log₂x 的整數 y；log₂x 為整數時不含邊界。
x＝2：0 個；x＝3、4：各 1 個；x＝5~8：各 2 個（共 8）；x＝9~16：各 3 個（共 24）；x＝17~30：各 4 個（共 56）。
注意 x＝4、8、16 時 log₂x 是整數，y 取到邊界不算，所以 x＝4 只有 1 個、x＝8 只有 2 個、x＝16 只有 3 個。
總數＝0＋1＋1＋(2×4)＋(3×8)＋(4×14)＝2＋8＋24＋56＝90 → 答案 (3)

</details>

[到練習網站作答]({{SITE}}/#/item/ma114-04)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0p056503510203248955/03-114%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e9%a1%8c.pdf)

</details>
<details><summary>📝 114 學測數學A 第 8 題（全國答對率 48%）</summary>

![題目]({{SITE}}/img/mathA/114-08.webp)

<details><summary>看答案與解析</summary>

**答案：3,5**
💡 化簡指數得 (x−1)²＋y²＝4，是圓心 (1,0)、半徑 2 的圓。
2^(x²−3)＝2^(2x−y²) ⇒ x²−2x＋y²＝3 ⇒ (x−1)²＋y²＝4。
(1) x＝3 ⇒ y＝0，只有 1 個解 ✗
(2) 圓心不在原點，不對稱於原點（例 (3,0) 在圓上，(−3,0) 不在）✗
(3) 圓 ✓
(4) 圓心到 x＋y＝4 的距離＝3/√2>2，不相交 ✗
(5) x−y 最大值＝(1−0)＋2×√2＝1＋2√2 ✓
→ 答案 (3)(5)

</details>

[到練習網站作答]({{SITE}}/#/item/ma114-08)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0p056503510203248955/03-114%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e9%a1%8c.pdf)

</details>
<details><summary>📝 114 學測數學A 第 9 題（全國答對率 44%）</summary>

![題目]({{SITE}}/img/mathA/114-09.webp)

<details><summary>看答案與解析</summary>

**答案：2,4,5**
💡 b²≥4c>(b＋2)² ⇒ c>0 且 b<−1。
第一式有實根：b²−4c≥0；第二式無實根：(b＋2)²−4c<0。
(1) 4c>(b＋2)²≥0 ⇒ c>0 ✗
(2) b²≥4c>(b＋2)² ⇒ 4b＋4<0 ⇒ b<−1 ✓
(3) 反例 b＝−3、c＝2：(b＋1)²−4c＝4−8<0 無實根 ✗
(4) 判別式 (b＋2)²＋4c>0 ✓
(5) b<−1 ⇒ (b−2)²>b²≥4c，判別式>0 ✓
→ 答案 (2)(4)(5)

</details>

[到練習網站作答]({{SITE}}/#/item/ma114-09)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0p056503510203248955/03-114%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e9%a1%8c.pdf)

</details>
<details><summary>📝 114 學測數學A 第 13 題（全國答對率 48%）</summary>

![題目]({{SITE}}/img/mathA/114-13.webp)

<details><summary>看答案與解析</summary>

**答案：－,6,3**
💡 f(x)＝(x＋6)q(x)＋3，q(x)＝8−m(x＋6)²；令 t＝x＋6，f＝−mt³＋8t＋3。
q(x) 在 x＝−6 有最大值 8 ⇒ q(x)＝8−m(x＋6)²（m>0）。
f(x)＝(x＋6)[8−m(x＋6)²]＋3。令 t＝x＋6：f＝−mt³＋8t＋3，是奇函數再加 3。
對稱中心在 t＝0、y＝3，即 (−6, 3) → 13-1＝−，13-2＝6，13-3＝3

</details>

[到練習網站作答]({{SITE}}/#/item/ma114-13)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0p056503510203248955/03-114%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e9%a1%8c.pdf)

</details>

</details>

<details><summary>Day 6｜三角、向量與空間</summary>

<details><summary>📝 114 學測數學A 第 5 題（全國答對率 30%）</summary>

![題目]({{SITE}}/img/mathA/114-05.webp)

<details><summary>看答案與解析</summary>

**答案：1**
💡 cos2θ>cosθ ⇒ cosθ<−1/2；再配合 sinθ<0，得 π<θ<4π/3。
cos2θ>cosθ ⇔ 2cos²θ−cosθ−1>0 ⇔ (2cosθ＋1)(cosθ−1)>0 ⇒ cosθ<−1/2 ⇒ 2π/3<θ<4π/3。
sin2θ>sinθ ⇔ sinθ(2cosθ−1)>0；此範圍內 2cosθ−1<0 ⇒ sinθ<0 ⇒ π<θ<2π。
交集：π<θ<4π/3 ⇒ a＝1，b＝4/3，b−a＝1/3 → 答案 (1)

</details>

[到練習網站作答]({{SITE}}/#/item/ma114-05)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0p056503510203248955/03-114%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e9%a1%8c.pdf)

</details>
<details><summary>📝 114 學測數學A 第 6 題（全國答對率 35%）</summary>

![題目]({{SITE}}/img/mathA/114-06.webp)

<details><summary>看答案與解析</summary>

**答案：3**
💡 互相垂直 ⇒ |u−v|²＝|u|²＋|v|²；解出 |u|²＝1、|v|²＝4、|w|²＝10。
|u−v|²＝|u|²＋|v|²＝5；|v−w|²＝|v|²＋|w|²＝14；u−w＝(1,1,3) ⇒ |u|²＋|w|²＝11。
三式相加 ⇒ 平方和＝15 ⇒ |u|²＝1，|v|²＝4，|w|²＝10。
體積＝|u||v||w|＝√40＝2√10 → 答案 (3)

</details>

[到練習網站作答]({{SITE}}/#/item/ma114-06)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0p056503510203248955/03-114%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e9%a1%8c.pdf)

</details>
<details><summary>📝 114 學測數學A 第 10 題（全國答對率 38%）</summary>

![題目]({{SITE}}/img/mathA/114-10.webp)

<details><summary>看答案與解析</summary>

**答案：1,4,5**
💡 0<k<1 時在 [0,3] 有 4 個交點：x₁、1−x₁、2＋x₁、3−x₁。
要在 (0,1) 內有兩交點，必須 0<k<1 → (1) ✓；此時 (1,2) 內 sin 為負無交點，(2,3) 內又有兩點，共 4 個 → (2) ✗
x₂＝1−x₁ ⇒ x₁＋x₂＝1 → (3) ✗
PQ＝1−2x₁，QR＝(2＋x₁)−(1−x₁)＝1＋2x₁；2PQ＝QR ⇒ x₁＝1/6 ⇒ k＝sin(π/6)＝1/2 → (4) ✓
四個交點 x 坐標和＝6>5 → (5) ✓
→ 答案 (1)(4)(5)

</details>

[到練習網站作答]({{SITE}}/#/item/ma114-10)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0p056503510203248955/03-114%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e9%a1%8c.pdf)

</details>
<details><summary>📝 114 學測數學A 第 11 題（全國答對率 38%）</summary>

![題目]({{SITE}}/img/mathA/114-11.webp)

<details><summary>看答案與解析</summary>

**答案：3,4,5**
💡 角平分線分對邊：CP:PD＝BC:BD＝4:3；AP＝(2/7)AB＋(3/7)AC。
BD＝3，BC＝4 ⇒ CP:PD＝4:3 ⇒ CP＝(4/7)CD → (1) ✗
AP＝(3/7)AC＋(4/7)AD＝(2/7)AB＋(3/7)AC → (2) ✗
cos∠BAC＝(36＋25−16)/60＝3/4 → (3) ✓
sinA＝√7/4，△ABC＝15√7/4，△ACD＝15√7/8，△ACP＝(4/7)△ACD＝15√7/14 → (4) ✓
AP·AC＝(2/7)(6·5·3/4)＋(3/7)·25＝45/7＋75/7＝120/7 → (5) ✓
→ 答案 (3)(4)(5)

</details>

[到練習網站作答]({{SITE}}/#/item/ma114-11)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0p056503510203248955/03-114%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e9%a1%8c.pdf)

</details>
<details><summary>📝 114 學測數學A 第 14 題（全國答對率 33%）</summary>

![題目]({{SITE}}/img/mathA/114-14.webp)

<details><summary>看答案與解析</summary>

**答案：－,1,1**
💡 a,b,c 皆負，決定絕對值的正負號：4b＋3c＝−28、3b＋4c＝−35 ⇒ b＝−1、c＝−8。
到 E₁：|4b＋3c−2|/5＝6，b、c<0 ⇒ 4b＋3c−2＝−30 ⇒ 4b＋3c＝−28。
到 E₂：|3b＋4c＋5|/5＝6 ⇒ 3b＋4c＋5＝−30 ⇒ 3b＋4c＝−35。
解得 b＝−1，c＝−8。
到 E₃：|a＋2b＋2c＋2|/3＝6 ⇒ |a−16|＝18 ⇒ a＝−2（a<0）。
a＋b＋c＝−11 → 14-1＝−，14-2＝1，14-3＝1

</details>

[到練習網站作答]({{SITE}}/#/item/ma114-14)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0p056503510203248955/03-114%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e9%a1%8c.pdf)

</details>

</details>

<details><summary>Day 7｜統計、機率與圓</summary>

<details><summary>📝 114 學測數學A 第 12 題（全國答對率 22%）</summary>

![題目]({{SITE}}/img/mathA/114-12.webp)

<details><summary>看答案與解析</summary>

**答案：1,3,4,5**
💡 u＝100−x、v＝y/1000；線性轉換後迴歸直線跟著轉換：v＝2.09−0.0213u。
(1) 乙占比＝100−甲占比 ✓
(2) 1 奈米＝10⁻³ 微米，v＝y/1000，不是 1000y ✗
(3) u＝100−x 只是平移加反向，標準差不變 ✓
(4) v＝(21.3x−40)/1000＝(21.3(100−u)−40)/1000＝2.09−0.0213u ⇒ b＝2.09 ✓
(5) 新增的點剛好落在原迴歸線上（殘差 0），最小平方的條件不變，迴歸線不變 ✓
→ 答案 (1)(3)(4)(5)

</details>

[到練習網站作答]({{SITE}}/#/item/ma114-12)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0p056503510203248955/03-114%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e9%a1%8c.pdf)

</details>
<details><summary>📝 114 學測數學A 第 15 題（全國答對率 16%）</summary>

![題目]({{SITE}}/img/mathA/114-15.webp)

<details><summary>看答案與解析</summary>

**答案：4,0,5**
💡 第 3 次正面出現在第 3、4、5 次的機率分別 1/8、3/16、3/16，其餘 1/2。
前 3 次都正面：1/8 → 240 元
第 4 次才累積 3 正：C(3,2)(1/2)³·(1/2)＝3/16 → 320 元
第 5 次才累積 3 正：C(4,2)(1/2)⁴·(1/2)＝3/16 → 400 元
其餘：1−1/8−3/16−3/16＝1/2 → 480 元
期望值＝30＋60＋75＋240＝405 → 15-1＝4，15-2＝0，15-3＝5

</details>

[到練習網站作答]({{SITE}}/#/item/ma114-15)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0p056503510203248955/03-114%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e9%a1%8c.pdf)

</details>
<details><summary>📝 114 學測數學A 第 16 題（全國答對率 18%）</summary>

![題目]({{SITE}}/img/mathA/114-16.webp)

<details><summary>看答案與解析</summary>

**答案：2,4,5**
💡 由 O 到 L₁ 距離 1 解出 m＝3/4；L₂ 相切得半徑 13/5；弦長＝2√(r²−1)。
L₁：mx−y＋(1−3m)＝0，距離 |1−3m|/√(m²＋1)＝1 ⇒ 8m²−6m＝0 ⇒ m＝3/4（m＝0 時 L₁、L₂ 重合且與圓相切，不合）。
L₂：mx＋y−(1＋3m)＝0 與圓相切 ⇒ r＝(1＋9/4)/(5/4)＝13/5。
AB＝2√(r²−1)＝2√(144/25)＝24/5 → 16-1＝2，16-2＝4，16-3＝5

</details>

[到練習網站作答]({{SITE}}/#/item/ma114-16)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0p056503510203248955/03-114%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e9%a1%8c.pdf)

</details>
<details><summary>📝 114 學測數學A 第 17 題（全國答對率 14%）</summary>

![題目]({{SITE}}/img/mathA/114-17.webp)

<details><summary>看答案與解析</summary>

**答案：3,2**
💡 BD 平分 ∠ADC（等腰 AB＝BC），用餘弦定理得 AD、CD 都是 x²−6x＋7＝0 的根。
AC²＝9＋9−2·9·(−1/8)＝81/4 ⇒ AC＝9/2；cos∠BAC＝cos∠BCA＝3/4。
同弧所對圓周角相等：∠ADB＝∠ACB，∠BDC＝∠BAC，兩者都等於 α（cosα＝3/4）。
△ABD 餘弦定理：9＝AD²＋16−2·4·AD·(3/4) ⇒ AD²−6AD＋7＝0；同理 CD 也滿足此式。
托勒密：AC·BD＝AB·CD＋BC·AD ⇒ 18＝3(AD＋CD) ⇒ AD＋CD＝6，所以兩根 3±√2 分別是 AD、CD。
AD≤CD ⇒ CD＝3＋√2 → 17-1＝3，17-2＝2

</details>

[到練習網站作答]({{SITE}}/#/item/ma114-17)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0p056503510203248955/03-114%e5%ad%b8%e6%b8%ac%e6%95%b8%e5%ad%b8a%e8%a9%a6%e9%a1%8c.pdf)

</details>
<details><summary>📝 113 學測數學A 第 1 題（全國答對率 89%）</summary>

![題目]({{SITE}}/img/mathA/113-01.webp)

<details><summary>看答案與解析</summary>

**答案：2**
💡 半衰期 2 小時：4 小時後剩 (1/2)²＝1/4。
殘留量＝(1/2)^(t/2)。
3 小時：(1/2)^1.5≈0.35；4 小時：1/4 ✓；6 小時：1/8；8 小時：1/16；10 小時：1/32
→ 答案 (2)

</details>

[到練習網站作答]({{SITE}}/#/item/ma113-01)　[原卷 PDF](https://www.ceec.edu.tw/files/file_pool/1/0o051426180137211766/03-113%e5%ad%b8%e6%b8%ac%e6%95%b8a%e8%a9%a6%e9%a1%8c%e5%ae%9a%e7%a8%bf.pdf)

</details>

</details>

## ✍️ 老師筆記

（輪到本科上課前一週，會補上完整的必考觀念與趨勢分析。）
