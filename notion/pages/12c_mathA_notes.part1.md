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
<summary>⑦ 最大值、最小值：三角不等式、柯西不等式</summary>
	**🔍 看到**：「$`|\overrightarrow{a}+\overrightarrow{b}|`$ 的最大值」「$`x^2+y^2=4`$ 時 $`3x+4y`$ 的最大值」「點在圓上，求某個式子的範圍」。
	**🛠️ 做法**
	1. 三角不等式 $`|\overrightarrow{a}+\overrightarrow{b}|\le|\overrightarrow{a}|+|\overrightarrow{b}|`$，兩向量同方向才取得到等號；方向受限制時改用坐標，讓每個分量各自取到最大。
	2. 柯西不等式 $`(ax+by)^2\le(a^2+b^2)(x^2+y^2)`$，等號在 $`(x,y)`$ 和 $`(a,b)`$ 平行時成立。
	**✏️ 例題**：$`x^2+y^2=4`$ 時，$`3x+4y`$ 的最大值是多少？
	**💡 解答**：$`(3x+4y)^2\le(3^2+4^2)(x^2+y^2)=25\times4=100`$，所以 $`3x+4y\le10`$；$`(x,y)=\left(\dfrac{6}{5},\dfrac{8}{5}\right)`$ 時取到最大值 10。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3ebee100984f81fabd31e8fe2399d945"/>　全國答對率 26%
	- <mention-page url="https://app.notion.com/p/3ecee100984f819ca2bdffbaf1af319e"/>　全國答對率 5%
</details>
<details>
<summary>⑧ 面積：兩向量所張的三角形</summary>
	**🔍 看到**：「兩向量所張的三角形（平行四邊形）面積」「$`2\overrightarrow{a}+\overrightarrow{b}`$ 與 $`\overrightarrow{a}+2\overrightarrow{b}`$ 所張的面積」。
	**🛠️ 做法**
	1. $`\overrightarrow{a}=(a_1,a_2)`$、$`\overrightarrow{b}=(b_1,b_2)`$ 所張平行四邊形的面積 $`=|a_1b_2-a_2b_1|`$，三角形是它的一半。
	2. 行列式可以像乘法一樣展開：$`\det(p\overrightarrow{a}+q\overrightarrow{b},r\overrightarrow{a}+s\overrightarrow{b})=(ps-qr)\det(\overrightarrow{a},\overrightarrow{b})`$。
	**✏️ 例題**：$`\overrightarrow{a}=(3,1)`$、$`\overrightarrow{b}=(1,2)`$ 所張三角形的面積是多少？
	**💡 解答**：$`\dfrac{1}{2}|3\times2-1\times1|=\dfrac{5}{2}`$。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3ecee100984f81a1b607e78ae7be9a33"/>　全國答對率 31%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81d497d6dac9441513c2"/>　全國答對率 36%
</details>
<details>
<summary>⑨ 沒有坐標的圖形：選兩個基底向量</summary>
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
### 空間向量
<details>
<summary>① 立體圖形放上坐標</summary>
	**🔍 看到**：正立方體、長方體、四面體，問向量、外積、夾角或距離。
	**🛠️ 做法**
	1. 一個頂點放在原點，三條互相垂直的稜放在 x、y、z 軸上。
	2. 正立方體各頂點的坐標只由 0 和邊長組成，寫出坐標後就能用內積、外積計算。
	**✏️ 例題**：邊長 1 的正立方體，O 是一個頂點，求體對角線 $`\overrightarrow{OG}=(1,1,1)`$ 和稜 $`\overrightarrow{OA}=(1,0,0)`$ 夾角的餘弦值。
	**💡 解答**：$`\cos\theta=\dfrac{(1,1,1)\cdot(1,0,0)}{\sqrt{3}\times1}=\dfrac{1}{\sqrt{3}}=\dfrac{\sqrt{3}}{3}`$。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3ebee100984f8174bfa2f7e5946b81d8"/>　全國答對率 57%
	- <mention-page url="https://app.notion.com/p/3ebee100984f819fa3faf9fe22599261"/>　全國答對率 35%
	- <mention-page url="https://app.notion.com/p/3f3ee100984f81c18d82e841933da8bd"/>　全國答對率 69%
</details>
<details>
<summary>② 外積：同時垂直兩個向量，算面積</summary>
	**🔍 看到**：「同時垂直」「法向量」「空間中三角形或平行四邊形的面積」。
	**🛠️ 做法**
	1. $`\overrightarrow{a}\times\overrightarrow{b}=(a_2b_3-a_3b_2,a_3b_1-a_1b_3,a_1b_2-a_2b_1)`$，同時垂直 $`\overrightarrow{a}`$ 和 $`\overrightarrow{b}`$。
	2. $`|\overrightarrow{a}\times\overrightarrow{b}|`$ 是 $`\overrightarrow{a}`$、$`\overrightarrow{b}`$ 所張平行四邊形的面積，三角形是一半。
	3. 算完驗算：外積和 $`\overrightarrow{a}`$、$`\overrightarrow{b}`$ 的內積都要是 0。
	**✏️ 例題**：求 $`\overrightarrow{a}=(1,2,0)`$、$`\overrightarrow{b}=(0,1,3)`$ 所張平行四邊形的面積。
	**💡 解答**：$`\overrightarrow{a}\times\overrightarrow{b}=(6,-3,1)`$，驗算 $`(6,-3,1)\cdot(1,2,0)=0`$、$`(6,-3,1)\cdot(0,1,3)=0`$。面積 $`=\sqrt{36+9+1}=\sqrt{46}`$。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3f3ee100984f81c18d82e841933da8bd"/>　全國答對率 69%
	- <mention-page url="https://app.notion.com/p/3ebee100984f8174bfa2f7e5946b81d8"/>　全國答對率 57%
	- <mention-page url="https://app.notion.com/p/3ecee100984f8179bbd1f9c236e8f6e7"/>　全國答對率 18%
</details>
<details>
<summary>③ 求平面：法向量加一點</summary>
	**🔍 看到**：「過三點的平面」「包含直線 L 而且和直線 M 平行」「和某個平面垂直」。
	**🛠️ 做法**
	1. 在平面上找兩個不平行的方向，外積得到法向量 $`(a,b,c)`$，再代一點：$`a(x-x_0)+b(y-y_0)+c(z-z_0)=0`$。
	2. 平面包含直線 ⇒ 直線的方向在平面上；平面和直線平行 ⇒ 法向量和直線的方向垂直；兩平面垂直 ⇒ 兩個法向量垂直。
	**✏️ 例題**：求過 $`A(1,0,0)`$、$`B(0,2,0)`$、$`C(0,0,3)`$ 三點的平面方程式。
	**💡 解答**：$`\overrightarrow{AB}=(-1,2,0)`$、$`\overrightarrow{AC}=(-1,0,3)`$，外積 $`=(6,3,2)`$。過 A：$`6(x-1)+3y+2z=0`$，也就是 $`6x+3y+2z=6`$。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3ecee100984f81fb89f7e54aad095144"/>　全國答對率 38%
	- <mention-page url="https://app.notion.com/p/3ecee100984f8179bbd1f9c236e8f6e7"/>　全國答對率 18%
	- <mention-page url="https://app.notion.com/p/3ebee100984f811d989ae3842bda27e4"/>　全國答對率 24%
</details>
<details>
<summary>④ 點到平面的距離</summary>
	**🔍 看到**：「點到平面的距離」「到三個平面的距離都是 6」「兩平行平面的距離」。
	**🛠️ 做法**
	1. 點 $`(x_0,y_0,z_0)`$ 到 $`ax+by+cz+d=0`$ 的距離 $`=\dfrac{|ax_0+by_0+cz_0+d|}{\sqrt{a^2+b^2+c^2}}`$。
	2. 拿掉絕對值時，用題目的條件（坐標的正負、點在平面的哪一側）決定裡面是正還是負。
	**✏️ 例題**：求點 $`(1,2,3)`$ 到平面 $`2x-y+2z=1`$ 的距離。
	**💡 解答**：$`\dfrac{|2\times1-2+2\times3-1|}{\sqrt{4+1+4}}=\dfrac{5}{3}`$。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3e9ee100984f8151880dc9cc5d74f53e"/>　全國答對率 33%
	- <mention-page url="https://app.notion.com/p/3ebee100984f811d989ae3842bda27e4"/>　全國答對率 24%
</details>
<details>
<summary>⑤ 投影點、垂足：設參數，再用垂直解</summary>
	**🔍 看到**：「投影點」「垂足」「最近的點」「和直線相交而且垂直」。
	**🛠️ 做法**
	1. 點到直線：直線上的點寫成參數式 $`P(t)`$，令 $`\overrightarrow{AP}`$ 和方向向量的內積為 0，解出 t。
	2. 點到平面：從點出發沿著法向量走，$`P(t)=A+t(a,b,c)`$，代入平面方程式解出 t。
	**✏️ 例題**：求原點在平面 $`x+2y+2z=9`$ 上的投影點。
	**💡 解答**：投影點是 $`(t,2t,2t)`$，代入：$`t+4t+4t=9`$ ⇒ $`t=1`$，投影點是 $`(1,2,2)`$。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3ecee100984f8109b358e713dfdbb83a"/>　全國答對率 33%
	- <mention-page url="https://app.notion.com/p/3ecee100984f814faf02c871f7475db6"/>　全國答對率 64%
	- <mention-page url="https://app.notion.com/p/3ebee100984f811d989ae3842bda27e4"/>　全國答對率 24%
</details>
<details>
<summary>⑥ 兩歪斜線：公垂線與距離</summary>
	**🔍 看到**：「歪斜線」「公垂線」「和兩條直線都相交而且垂直」「兩直線的距離」。
	**🛠️ 做法**
	1. 兩條線各寫成參數式 $`P(t)`$、$`Q(s)`$，令 $`\overrightarrow{PQ}`$ 同時和兩個方向向量垂直，解出 t、s，$`\overline{PQ}`$ 就是公垂線段。
	2. 或者：兩個方向向量的外積是公垂線的方向，兩條線上各取一點，連線向量在這個方向的正射影長就是距離。
	**✏️ 例題**：$`L_1`$：$`(t,0,0)`$，$`L_2`$：$`(1,s,2)`$（t、s 是實數）。求兩直線的距離。
	**💡 解答**：方向 $`(1,0,0)`$、$`(0,1,0)`$ 的外積是 $`(0,0,1)`$；兩線上各取 $`(0,0,0)`$、$`(1,0,2)`$，連線 $`(1,0,2)`$ 在 $`(0,0,1)`$ 方向的正射影長是 2，所以距離是 2。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3ebee100984f8110ac4eff251c2b45cd"/>　全國答對率 10%
</details>
<details>
<summary>⑦ 體積：三階行列式、底面積乘高</summary>
	**🔍 看到**：「平行六面體的體積」「三向量所張」「四面體的體積」「用體積反推點到平面的距離」。
	**🛠️ 做法**
	1. 平行六面體的體積 $`=|\overrightarrow{a}\cdot(\overrightarrow{b}\times\overrightarrow{c})|`$，就是三階行列式的絕對值；四面體是它的 $`\dfrac{1}{6}`$。
	2. 也可以用「底面積 × 高」；反過來，點到平面的距離 $`=\dfrac{3\times\text{四面體體積}}{\text{底面積}}`$。
	3. 三個向量互相垂直時，體積就是三個長度相乘。
	**✏️ 例題**：求 $`\overrightarrow{a}=(1,0,0)`$、$`\overrightarrow{b}=(1,2,0)`$、$`\overrightarrow{c}=(1,1,3)`$ 所張平行六面體的體積。
	**💡 解答**：$`\overrightarrow{b}\times\overrightarrow{c}=(6,-3,-1)`$，$`\overrightarrow{a}\cdot(\overrightarrow{b}\times\overrightarrow{c})=6`$，體積是 6。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81ad9d96d29f12416969"/>　全國答對率 35%
	- <mention-page url="https://app.notion.com/p/3ecee100984f819ca2bdffbaf1af319e"/>　全國答對率 5%
	- <mention-page url="https://app.notion.com/p/3ecee100984f81279e6be8bb5e9b061d"/>　全國答對率 21%
	- <mention-page url="https://app.notion.com/p/3ebee100984f81aab4c4dfd58910a693"/>　全國答對率 47%
</details>
