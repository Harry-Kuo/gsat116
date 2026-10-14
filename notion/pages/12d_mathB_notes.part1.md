<callout icon="🧭">
	向量、機率統計、排列組合的題目整理成下方的「🧩 經典題型與解題技巧」：先從題目的關鍵字認出題型，再照做法解題，每一型都附例題、解答和考過的題目。
	後面依單元整理必背公式、解題流程和容易錯的地方。標「考卷附」的公式，考卷最後會附上，但還是要熟到不用查。
	每個觀念最後列出前兩週每日練習中全國答對率最低的題目，點進去可以看題目、答案與解析。
</callout>
## 🧩 經典題型與解題技巧
看到題目先找關鍵字，認出是下面哪一型，再照那一型的做法解；點開題型名稱可以看做法、例題、解答和考過的題目。
### 平面向量
<details>
<summary>① 線性組合：解出係數，看點在哪裡</summary>
	**🔍 看到**：$`\overrightarrow{OP}=\alpha\overrightarrow{OA}+\beta\overrightarrow{OB}`$；「P 在三角形內部」「P 在平行四邊形內」「哪些 A、B 是可能的」。
	**🛠️ 做法**
	1. 寫成坐標，列出 $`\alpha`$、$`\beta`$ 的聯立方程式解出來。
	2. P 在直線 AB 上 ⇔ $`\alpha+\beta=1`$。
	3. P 在 $`\triangle OAB`$ 內部或邊上 ⇔ $`\alpha\ge0`$、$`\beta\ge0`$、$`\alpha+\beta\le1`$；在 OA、OB 所張的平行四邊形內 ⇔ $`0\le\alpha\le1`$、$`0\le\beta\le1`$。
	**✏️ 例題**：$`\overrightarrow{OP}=\dfrac{1}{3}\overrightarrow{OA}+\dfrac{1}{2}\overrightarrow{OB}`$，P 在 $`\triangle OAB`$ 的內部嗎？
	**💡 解答**：兩個係數都是正的，而且 $`\dfrac{1}{3}+\dfrac{1}{2}=\dfrac{5}{6}<1`$，所以 P 在 $`\triangle OAB`$ 的內部。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81b5af68dc319cdcafd8"/>　全國答對率 52%
	- <mention-page url="https://app.notion.com/p/3ecee100984f814dbe53d46b161566f1"/>　全國答對率 76%
	- <mention-page url="https://app.notion.com/p/3ecee100984f81d0a6a3e74016569986"/>　全國答對率 19%
</details>
<details>
<summary>② 分點與交點：同一點用兩種方法表示</summary>
	**🔍 看到**：「$`AP:PB=m:n`$」「兩條線段的交點」「角平分線」「重心」「D 在直線 AB 上」。
	**🛠️ 做法**
	1. 分點：$`AP:PB=m:n`$ ⇒ $`\overrightarrow{OP}=\dfrac{n\overrightarrow{OA}+m\overrightarrow{OB}}{m+n}`$，離哪個點近，那個點的係數就大。
	2. 交點：設交點在第一條線上的比例是 s、在第二條線上的比例是 t，兩種寫法的係數對應相等，解出 s、t。
	3. 角平分線把對邊分成兩鄰邊的比；「D 在直線 AB 上」可能是內分點，也可能是外分點，兩種都要考慮。
	**✏️ 例題**：$`\triangle ABC`$ 中，D 在 $`\overline{BC}`$ 上，$`BD:DC=1:2`$。用 $`\overrightarrow{AB}`$、$`\overrightarrow{AC}`$ 表示 $`\overrightarrow{AD}`$。
	**💡 解答**：$`\overrightarrow{AD}=\dfrac{2\overrightarrow{AB}+\overrightarrow{AC}}{3}=\dfrac{2}{3}\overrightarrow{AB}+\dfrac{1}{3}\overrightarrow{AC}`$（D 離 B 比較近，所以 $`\overrightarrow{AB}`$ 的係數比較大）。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81ac8a75e3e4e7e41945"/>　全國答對率 38%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81d497d6dac9441513c2"/>　全國答對率 36%
	- <mention-page url="https://app.notion.com/p/3ebee100984f81068a04c9917745a881"/>　全國答對率 25%
	- <mention-page url="https://app.notion.com/p/3ebee100984f81719a26ec44a6d3a1fb"/>　全國答對率 28%
</details>
<details>
<summary>③ 面積比：看線性組合的係數</summary>
	**🔍 看到**：$`\overrightarrow{AP}=a\overrightarrow{AB}+b\overrightarrow{AC}`$，問 $`\triangle ABP`$、$`\triangle ACP`$、$`\triangle BCP`$ 的面積或面積比。
	**🛠️ 做法**
	1. P 在 $`\triangle ABC`$ 內部時：$`\triangle ABP=b\cdot\triangle ABC`$、$`\triangle ACP=a\cdot\triangle ABC`$、$`\triangle BCP=(1-a-b)\cdot\triangle ABC`$。
	2. 記法：$`\triangle ABP`$ 和 $`\triangle ABC`$ 同底 AB，面積比＝高的比＝P、C 到直線 AB 的距離比，就是 $`\overrightarrow{AC}`$ 的係數 b。
	**✏️ 例題**：$`\overrightarrow{AP}=\dfrac{1}{4}\overrightarrow{AB}+\dfrac{1}{2}\overrightarrow{AC}`$，求 $`\triangle ABP:\triangle ACP:\triangle BCP`$。
	**💡 解答**：$`\dfrac{1}{2}:\dfrac{1}{4}:\left(1-\dfrac{1}{4}-\dfrac{1}{2}\right)=\dfrac{1}{2}:\dfrac{1}{4}:\dfrac{1}{4}=2:1:1`$。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3ecee100984f81d0a6a3e74016569986"/>　全國答對率 19%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81d497d6dac9441513c2"/>　全國答對率 36%
</details>
<details>
<summary>④ 內積的三種算法</summary>
	**🔍 看到**：求 $`\overrightarrow{a}\cdot\overrightarrow{b}`$ 或夾角；「圓上兩點」「已知三邊長」。
	**🛠️ 做法**
	1. 有坐標：$`\overrightarrow{a}\cdot\overrightarrow{b}=a_1b_1+a_2b_2`$。
	2. 有長度和夾角：$`\overrightarrow{a}\cdot\overrightarrow{b}=|\overrightarrow{a}||\overrightarrow{b}|\cos\theta`$。
	3. 只有三邊長：$`\overrightarrow{OA}\cdot\overrightarrow{OB}=\dfrac{OA^2+OB^2-AB^2}{2}`$（就是餘弦定理）。
	**✏️ 例題**：半徑 5 的圓上有 A、B 兩點，$`AB=6`$，O 是圓心。求 $`\overrightarrow{OA}\cdot\overrightarrow{OB}`$。
	**💡 解答**：$`\overrightarrow{OA}\cdot\overrightarrow{OB}=\dfrac{5^2+5^2-6^2}{2}=\dfrac{14}{2}=7`$。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3ebee100984f81779eecf9a2b90df1fa"/>　全國答對率 44%
	- <mention-page url="https://app.notion.com/p/3ebee100984f8111805be96f20c157f2"/>　全國答對率 38%
	- <mention-page url="https://app.notion.com/p/3ecee100984f815fb1efff3c648fdc7e"/>　全國答對率 42%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81ac8a75e3e4e7e41945"/>　全國答對率 38%
</details>
<details>
<summary>⑤ 垂直、平行：翻成內積和倍數</summary>
	**🔍 看到**：「垂直」「直角」「平行」「向量和直線垂直」。
	**🛠️ 做法**
	1. 垂直 ⇔ 內積為 0；平行 ⇔ 一個向量是另一個的實數倍。
	2. 直線 $`ax+by=c`$ 的法向量是 $`(a,b)`$、方向向量是 $`(b,-a)`$；斜率 m 的直線，方向向量是 $`(1,m)`$。
	3. 內積的式子可以移項、提出相同的向量：$`\overrightarrow{AB}\cdot\overrightarrow{AC}=\overrightarrow{AB}\cdot\overrightarrow{AD}`$ ⇒ $`\overrightarrow{AB}\cdot(\overrightarrow{AD}-\overrightarrow{AC})=\overrightarrow{AB}\cdot\overrightarrow{CD}=0`$。
	**✏️ 例題**：向量 $`(k,2)`$ 和直線 $`y=3x+1`$ 垂直，求 k。
	**💡 解答**：直線的方向向量是 $`(1,3)`$，$`(k,2)\cdot(1,3)=k+6=0`$ ⇒ $`k=-6`$。
	**⚠️ 小心**：「向量和直線垂直」是和直線的方向向量內積為 0；和法向量是「平行」。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3e9ee100984f819babc3ebf90a17717c"/>　全國答對率 19%
	- <mention-page url="https://app.notion.com/p/3ebee100984f81068a04c9917745a881"/>　全國答對率 25%
	- <mention-page url="https://app.notion.com/p/3f3ee100984f81a88b8cd6a7850bd849"/>　全國答對率 43%
</details>
<details>
<summary>⑥ 正射影：投影長＝內積÷長度</summary>
	**🔍 看到**：「正射影」「投影長」「在某個方向的分量」「投影到一條直線上」。
	**🛠️ 做法**
	1. $`\overrightarrow{a}`$ 在 $`\overrightarrow{b}`$ 方向的正射影長 $`=\dfrac{|\overrightarrow{a}\cdot\overrightarrow{b}|}{|\overrightarrow{b}|}`$；正射影 $`=\dfrac{\overrightarrow{a}\cdot\overrightarrow{b}}{|\overrightarrow{b}|^2}\overrightarrow{b}`$。
	2. 兩個方向互相垂直時，向量在這兩個方向的正射影長，平方相加等於向量長度的平方。
	**✏️ 例題**：$`\overrightarrow{a}=(3,4)`$ 在 $`\overrightarrow{b}=(1,1)`$ 方向的正射影長和正射影各是什麼？
	**💡 解答**：$`\overrightarrow{a}\cdot\overrightarrow{b}=7`$、$`|\overrightarrow{b}|=\sqrt{2}`$。正射影長 $`=\dfrac{7}{\sqrt{2}}=\dfrac{7\sqrt{2}}{2}`$；正射影 $`=\dfrac{7}{2}(1,1)=\left(\dfrac{7}{2},\dfrac{7}{2}\right)`$。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3ebee100984f8152ac4ec9d3635fd46c"/>　全國答對率 8%
	- <mention-page url="https://app.notion.com/p/3ecee100984f81eb8383fae5505f7083"/>　全國答對率 12%
</details>
<details>
<summary>⑦ 長度的最大值：每個分量各自取最大</summary>
	**🔍 看到**：「$`|\overrightarrow{v}+\overrightarrow{AB}|`$ 的最大值」「坐標都在某個範圍內」。
	**🛠️ 做法**
	1. 把向量寫成坐標，每個分量能各自調整時，讓每個分量的絕對值都取到最大。
	2. 用「兩個長度相加」估出來的上界，只有兩向量同方向時才取得到，常常達不到。
	**✏️ 例題**：$`\overrightarrow{u}=(x,y)`$，$`-1\le x\le1`$、$`-1\le y\le1`$。$`|(3,-2)+\overrightarrow{u}|`$ 的最大值是多少？
	**💡 解答**：$`(3,-2)+\overrightarrow{u}=(3+x,-2+y)`$：取 $`x=1`$、$`y=-1`$ 得 $`(4,-3)`$，長度是 5，最大值就是 5。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3ebee100984f81fabd31e8fe2399d945"/>　全國答對率 26%
</details>
<details>
<summary>⑧ 沒有坐標的圖形：選兩個基底向量</summary>
	**🔍 看到**：三角形、梯形、正六邊形的邊長、夾角或內積，題目沒有給坐標。
	**🛠️ 做法**
	1. 選兩個不平行的向量當基底（例如 $`\overrightarrow{AB}`$、$`\overrightarrow{AC}`$），其他向量都用它們表示。
	2. 先算好 $`|\overrightarrow{AB}|^2`$、$`|\overrightarrow{AC}|^2`$、$`\overrightarrow{AB}\cdot\overrightarrow{AC}`$ 三個數，求長度、角度時都用它們展開。
	3. 也可以直接把圖形放上坐標平面：一個頂點放原點、一邊放在 x 軸上。
	**✏️ 例題**：$`\triangle ABC`$ 中，$`AB=6`$、$`AC=5`$、$`\cos A=\dfrac{3}{4}`$，M 是 $`\overline{BC}`$ 的中點。求 AM 的長。
	**💡 解答**：$`\overrightarrow{AM}=\dfrac{1}{2}(\overrightarrow{AB}+\overrightarrow{AC})`$，$`\overrightarrow{AB}\cdot\overrightarrow{AC}=6\times5\times\dfrac{3}{4}=\dfrac{45}{2}`$。$`|\overrightarrow{AM}|^2=\dfrac{1}{4}\left(36+25+2\times\dfrac{45}{2}\right)=\dfrac{106}{4}`$，所以 $`AM=\dfrac{\sqrt{106}}{2}`$。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81ac8a75e3e4e7e41945"/>　全國答對率 38%
	- <mention-page url="https://app.notion.com/p/3ecee100984f817fb36bf2962c0f0778"/>　全國答對率 27%
	- <mention-page url="https://app.notion.com/p/3ebee100984f8111805be96f20c157f2"/>　全國答對率 38%
</details>
### 排列組合
<details>
<summary>① 先分類、再分步</summary>
	**🔍 看到**：情況可以分成幾種、彼此不會同時發生（例如「3 種都是基本材料／2 種基本、1 種進階／其他」）；或一件事要分好幾個步驟才能完成。
	**🛠️ 做法**
	1. 先列出所有類別，確認彼此不重疊、也沒有遺漏。
	2. 每一類用乘法原理算（各步驟的方法數相乘），各類再相加。
	3. 題目說「結果相同只算一種」時，要數的是「不同的結果」，不是選法。
	**✏️ 例題**：從 4 位男生、3 位女生中選出正、副班長各 1 人，兩人必須同性別，有幾種選法？
	**💡 解答**：兩位都是男生：$`4\times3=12`$ 種；兩位都是女生：$`3\times2=6`$ 種（正、副有分別，要排順序）。共 $`12+6=18`$ 種。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3e9ee100984f816f8934d9befa3b9356"/>　全國答對率 56%
	- <mention-page url="https://app.notion.com/p/3ecee100984f81108960df82708d4bac"/>　全國答對率 7%
</details>
<details>
<summary>② 有系統地列舉：固定一個，由小到大</summary>
	**🔍 看到**：條件和數的性質有關（完全平方數、倍數、等差、不等式），或是條件很多、情況不多，套不上公式。
	**🛠️ 做法**
	1. 先固定一個變數（例如先決定 a），由小到大逐一列出另一個變數能取的值。
	2. 數字題先依性質分類，例如把 1～9 寫成「平方數 × 剩下的部分」，三數乘積是完全平方數 ⇔ 剩下的部分相乘是完全平方數。
	3. 列完檢查有沒有重複，以及最大、最小的情況有沒有漏掉。
	**✏️ 例題**：擲兩顆骰子，點數分別是 a、b，滿足 $`ab\ge20`$ 的情況有幾種？
	**💡 解答**：$`a\le3`$ 時 $`ab\le18`$，不可能。$`a=4`$：$`b=5,6`$，2 種；$`a=5`$：$`b=4,5,6`$，3 種；$`a=6`$：$`b=4,5,6`$，3 種。共 8 種。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3ecee100984f81af806fce513f553532"/>　全國答對率 13%
	- <mention-page url="https://app.notion.com/p/3ecee100984f8108ab76f1c6493c5620"/>　全國答對率 61%
	- <mention-page url="https://app.notion.com/p/3ecee100984f8107b22ecf3e171338ad"/>　全國答對率 72%
</details>
<details>
<summary>③ 特殊的先處理：指定位置、有限制的人</summary>
	**🔍 看到**：「0 不能在首位」「甲不排第一」「老師站正中間」「歌唱要排在鋼琴之後」。
	**🛠️ 做法**
	1. 先安排有限制的位置或人，再排其他沒有限制的。
	2. 限制很多、分類太麻煩時，改用「全部 − 不符合」（見⑪）。
	**✏️ 例題**：用 0、1、2、3、4 組成數字不重複的三位數，共有幾個？其中偶數有幾個？
	**💡 解答**：百位不能是 0：$`4\times4\times3=48`$ 個。偶數先看個位：個位是 0 時 $`4\times3=12`$ 個；個位是 2 或 4 時，百位不能是 0 也不能和個位相同，$`2\times3\times3=18`$ 個。偶數共 $`12+18=30`$ 個。
	**⚠️ 小心**：個位和百位都有限制時，要分「個位是 0」「個位不是 0」兩類，因為百位能選的個數不一樣。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3ecee100984f81108960df82708d4bac"/>　全國答對率 7%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f819f9f77ce572588caf8"/>　全國答對率 60%
</details>
<details>
<summary>④ 相鄰：先綁成一塊再排</summary>
	**🔍 看到**：「相鄰」「排在一起」「同類的排在一起」。
	**🛠️ 做法**
	1. 把要相鄰的看成一塊，和其他的一起排。
	2. 再乘上塊內的排法。
	**✏️ 例題**：甲、乙、丙、丁、戊 5 人排成一列，甲、乙相鄰的排法有幾種？
	**💡 解答**：甲乙綁成一塊，和丙、丁、戊共 4 個單位：$`4!=24`$ 種；塊內有甲乙、乙甲 2 種。共 $`24\times2=48`$ 種。
	**⚠️ 小心**：「5、6 相鄰，而且 6、7 相鄰」表示 5、6、7 連成一塊，6 一定在中間，塊內只有 567、765 兩種，不是 $`3!`$ 種。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3e9ee100984f819f9f77ce572588caf8"/>　全國答對率 60%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f812b89e5fa2f45fd676d"/>　全國答對率 36%
</details>
<details>
<summary>⑤ 不相鄰：先排其他的，再插空隙</summary>
	**🔍 看到**：「不相鄰」「互不相鄰」「任兩個都不相鄰」「中間至少隔一個」。
	**🛠️ 做法**
	1. 先排沒有限制的 m 個，會產生 $`m+1`$ 個空隙（含兩端）。
	2. 不能相鄰的 k 個分別放進不同的空隙：相異的人依序挑空隙，$`(m+1)\times m\times\cdots`$（k 個數相乘）；相同的東西只要選空隙，$`C(m+1,k)`$ 種。
	**✏️ 例題**：3 位男生、3 位女生排成一列，女生互不相鄰的排法有幾種？
	**💡 解答**：男生先排：$`3!=6`$ 種，產生 4 個空隙；3 位女生依序挑空隙：$`4\times3\times2=24`$ 種。共 $`6\times24=144`$ 種。
	**⚠️ 小心**：「兩人不相鄰」也可以用「全部 − 相鄰」；但「三人兩兩不相鄰」不能只扣掉「三人連在一起」，要用插空隙。選位置也一樣：10 棟大樓選 3 棟、互不相鄰，先放好沒選的 7 棟，產生 8 個空隙，$`C(8,3)=56`$ 種。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3ecee100984f81adb056d93b0c76d679"/>　全國答對率 50%
	- <mention-page url="https://app.notion.com/p/3ecee100984f81e39e52df1c0cbb6660"/>　全國答對率 23%
</details>
<details>
<summary>⑥ 有相同物的排列、走捷徑</summary>
	**🔍 看到**：「相同的球」「顏色的排法」「字母有重複」「只能向右、向上走」。
	**🛠️ 做法**
	1. n 個東西中有 p 個相同、q 個相同……，排法有 $`\dfrac{n!}{p!\,q!\cdots}`$ 種（相同的東西互換位置，排法不變）。
	2. 方格走捷徑：向右 m 步、向上 n 步，就是把 m 個「右」和 n 個「上」排成一列，$`\dfrac{(m+n)!}{m!\,n!}`$ 種。
	3. 必須經過某一點：分成前後兩段，兩段的走法相乘。
	**✏️ 例題**：從 $`(0,0)`$ 走到 $`(4,3)`$，每一步只能向右或向上走一格，有幾種走法？如果必須經過 $`(2,1)`$ 呢？
	**💡 解答**：4 個「右」、3 個「上」排成一列：$`\dfrac{7!}{4!\,3!}=35`$ 種。經過 $`(2,1)`$：前段 $`\dfrac{3!}{2!\,1!}=3`$ 種，後段向右 2 步、向上 2 步，$`\dfrac{4!}{2!\,2!}=6`$ 種，共 $`3\times6=18`$ 種。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3ecee100984f81e39e52df1c0cbb6660"/>　全國答對率 23%
</details>
<details>
<summary>⑦ 順序已經固定：只要選，不用排</summary>
	**🔍 看到**：「由小到大」「遞增」「$`a<b<c`$」「甲要排在乙的前面（不一定相鄰）」。
	**🛠️ 做法**
	1. 順序固定的 k 個東西，選出它們（或它們的位置）就決定了排法：$`C(n,k)`$ 種，選完只有 1 種排法。
	2. n 人排成一列、其中 k 人的先後順序固定：$`\dfrac{n!}{k!}`$ 種。
	**✏️ 例題**：甲、乙、丙、丁、戊 5 人排成一列，甲要排在乙的前面（不一定相鄰），有幾種排法？
	**💡 解答**：每一種排法把甲、乙對調就得到另一種，兩種之中恰好一種是甲在前：$`\dfrac{5!}{2!}=60`$ 種。
	**⚠️ 小心**：題目寫「遞增」「遞減」時，先找一定在某個位置的數（例如最大的數一定在遞增和遞減的交界），再決定其他數放哪一邊。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3ebee100984f81ec9148fe2ab2c04a0d"/>　全國答對率 44%
	- <mention-page url="https://app.notion.com/p/3ebee100984f81599ed3ff603420889d"/>　全國答對率 38%
</details>
<details>
<summary>⑧ 可以重複選：每一次都有 m 種</summary>
	**🔍 看到**：「可以重複」「抽 k 次、每次 1 個」「每封信投入任一個郵筒」「每個人任選一項」。
	**🛠️ 做法**
	1. 先分清楚「誰在選」：每一個選擇者（每封信、每一次）都有 m 種選擇，共 $`m^k`$ 種。
	2. k 封信投入 m 個郵筒是 $`m^k`$ 種，不是 $`k^m`$ 種。
	3. 每個郵筒至少一封：先把信分堆，再把各堆分給郵筒。
	**✏️ 例題**：4 封不同的信投入 3 個不同的郵筒，有幾種投法？如果每個郵筒至少一封呢？
	**💡 解答**：每封信都有 3 種選擇：$`3^4=81`$ 種。每個郵筒至少一封：4 封信分成 2、1、1 三堆，選出同一堆的 2 封有 $`C(4,2)=6`$ 種；三堆分給 3 個郵筒有 $`3!=6`$ 種。共 $`6\times6=36`$ 種。
	**⚠️ 小心**：可以重複、但不管順序的「選取」不能用 $`m^k`$：例如從 10 種口味選兩球（可以同口味），要分「兩球不同口味 $`C(10,2)=45`$ 種」和「同口味 10 種」，共 55 種。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81e99cc2c578aaa7b5ac"/>　全國答對率 35%
	- <mention-page url="https://app.notion.com/p/3ebee100984f81d884d8e7777827bd06"/>　全國答對率 8%
	- <mention-page url="https://app.notion.com/p/3ecee100984f815c8e1de2730f47040b"/>　全國答對率 29%
</details>
<details>
<summary>⑨ 相同的東西分給不同的人：隔板法</summary>
	**🔍 看到**：「相同的球分給幾個人」「$`x+y+z=10`$ 的非負整數解」「每人至少分到幾個」。
	**🛠️ 做法**
	1. k 個相同的東西分給 n 個人（可以有人沒分到）：把 k 個「○」和 $`n-1`$ 個隔板「｜」排成一列，$`\dfrac{(k+n-1)!}{k!\,(n-1)!}`$ 種。
	2. 每人至少 r 個：先每人發 r 個，剩下的再用隔板。
	**✏️ 例題**：10 顆相同的糖果分給甲、乙、丙三人，每人至少 2 顆，有幾種分法？
	**💡 解答**：先每人發 2 顆，剩下 4 顆任意分給 3 人：4 個「○」和 2 個「｜」排成一列，$`\dfrac{6!}{4!\,2!}=15`$ 種。
</details>
<details>
<summary>⑩ 分組、分派：組有沒有名字？</summary>
	**🔍 看到**：「分成兩組」「平分成甲、乙兩組」「分派到兩個部門」「每組都要有……」。
	**🛠️ 做法**
	1. 組有名字（甲組、研發部門、A 教室）：依序選人，$`C(n,a)\times C(n-a,b)\times\cdots`$。
	2. 組沒有名字、又有幾組人數一樣：再除以這幾組的排列數，例如平均分成 3 組要除以 $`3!`$。
	3. 每組有特別的條件（例如每組要有 1 名翻譯）：先分有條件的人，再分其他人；「至少一個」用補集。
	**✏️ 例題**：6 人分到 A、B、C 三間教室，每間 2 人，有幾種分法？如果只是分成 3 組、每組 2 人呢？
	**💡 解答**：分到教室：$`C(6,2)\times C(4,2)\times C(2,2)=15\times6\times1=90`$ 種。3 組沒有名字，三組互換不算新的分法：$`90\div3!=15`$ 種。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81038983e339acb3508a"/>　全國答對率 25%
	- <mention-page url="https://app.notion.com/p/3ebee100984f8194a4edd6ee7756347c"/>　全國答對率 35%
</details>
