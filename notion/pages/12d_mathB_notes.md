<callout icon="🧭">
	依單元整理必背公式、解題流程和容易錯的地方。標「考卷附」的公式，考卷最後會附上，但還是要熟到不用查。
	每個觀念最後列出前兩週每日練習中全國答對率最低的題目，點進去可以看題目、答案與解析。
</callout>
## 數與函數
<details>
<summary>**數與式、指數對數**</summary>
	<callout icon="💡">
		絕對值是「距離」；指數、對數先化成同底再比較；$`\ln`$ 與 $`e`$ 用在連續複利，$`\log`$ 值範圍要會估。
	</callout>
	**📌 必背**
	- 指數律（$`a>0`$）：$`a^m\cdot a^n=a^{m+n}`$、$`(a^m)^n=a^{mn}`$、$`a^0=1`$、$`a^{-n}=\dfrac{1}{a^n}`$、$`a^{m/n}=\sqrt[n]{a^m}`$。
	- 對數：$`\log_a b=x`$ ⇔ $`a^x=b`$；$`\log(MN)=\log M+\log N`$、$`\log\left(\dfrac{M}{N}\right)=\log M-\log N`$、$`\log(M^k)=k\cdot\log M`$。
	- 自然對數 $`\ln x=\log_e x`$（$`e\approx2.718`$），運算規則和 $`\log`$ 相同；$`\ln\left(\dfrac{a}{b}\right)=\ln a-\ln b`$。
	- 換底：$`\log_a b=\dfrac{\log b}{\log a}`$。
	- 位數：正數 N 的整數部分是 k 位數 ⇔ $`k-1\le\log N<k`$。
	- 絕對值：$`|x-a|`$ 是數線上 x 到 a 的距離；$`|x-a|\le r`$ ⇔ $`a-r\le x\le a+r`$。
	**🧭 解題流程**
	1. 成長或衰退模型：每期變成原來的 $`(1+r)`$ 倍，n 期後是 $`A_0\cdot(1+r)^n`$；求期數就兩邊取對數。
	2. 比較大小：化成同底；底數 $`>1`$ 時遞增，$`0<\text{底數}<1`$ 時遞減。
	3. 估算：用考卷附的對數值，$`\log5=1-\log2`$。
	**⚠️ 容易錯的地方**
	- 每期成長 4%，n 期後是乘 $`(1.04)^n`$，不是乘 $`(1+0.04n)`$。
	- $`\ln\left(\dfrac{135}{100}\right)=\ln135-\ln100`$，不是 $`\ln(135-100)`$：對數把除法變成減法。
	- 對數的真數一定要大於 0。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3ebee100984f81c0bacff062d239b83b"/>　全國答對率 31%
	- <mention-page url="https://app.notion.com/p/3ebee100984f81188ea8e4660944b6f3"/>　全國答對率 39%
	- <mention-page url="https://app.notion.com/p/3ebee100984f8197a24def50f8556556"/>　全國答對率 45%
</details>
<details>
<summary>**多項式與函數圖形**</summary>
	<callout icon="💡">
		二次函數配方找頂點；三次函數看對稱中心；多項式用「代特殊值」與除法原理最快。
	</callout>
	**📌 必背**
	- 除法原理：$`f(x)=g(x)\cdot q(x)+r(x)`$，餘式的次數比除式低；餘式定理：$`f(x)`$ 除以 $`x-a`$ 的餘式是 $`f(a)`$。
	- 二次函數配方：$`y=a(x-h)^2+k`$，頂點 $`(h,k)`$；$`a>0`$ 開口向上。
	- $`ax^2+bx+c=0`$：判別式 $`b^2-4ac`$ 決定實根個數；兩根和 $`=-\dfrac{b}{a}`$、兩根積 $`=\dfrac{c}{a}`$。
	- 三次函數 $`y=ax^3+bx^2+cx+d`$ 的圖形對稱於點 $`\left(-\dfrac{b}{3a},f\left(-\dfrac{b}{3a}\right)\right)`$。
	**🧭 解題流程**
	1. 求函數值或係數：代特殊值（$`x=0`$、1、$`-1`$）最快。
	2. 解多項式不等式：因式分解 → 在數線上標出根 → 由最高次項係數決定最右邊的正負，往左依次變號。
	3. 兩個圖形的交點：兩個函數相減，交點的 x 坐標就是相減後方程式的實根。
	**⚠️ 容易錯的地方**
	- 偶次重根的兩側正負號相同，不會變號。
	- 限定範圍內的最大值、最小值，要比較頂點和兩個端點。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3e9ee100984f816c91cccb2cd09bd14f"/>　全國答對率 22%
	- <mention-page url="https://app.notion.com/p/3ebee100984f812ca482d61f1a52e171"/>　全國答對率 29%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81e085fbfca5ff068baf"/>　全國答對率 35%
</details>
<details>
<summary>**三角函數與三角測量**</summary>
	<callout icon="💡">
		$`y=a\sin(bx+c)+d`$ 看振幅、週期與平移；解三角形用正弦、餘弦定理。
	</callout>
	**📌 必背**
	- 特殊角：$`\sin30^{\circ}=\dfrac{1}{2}`$、$`\sin45^{\circ}=\dfrac{\sqrt{2}}{2}`$、$`\sin60^{\circ}=\dfrac{\sqrt{3}}{2}`$；$`\sin^2\theta+\cos^2\theta=1`$。
	- 弧度：$`\pi=180^{\circ}`$；扇形弧長 $`s=r\theta`$、面積 $`=\dfrac{1}{2}r^2\theta`$。
	- 正弦定理 $`\dfrac{a}{\sin A}=2R`$、餘弦定理 $`c^2=a^2+b^2-2ab\cos C`$（考卷附）；三角形面積 $`=\dfrac{1}{2}ab\sin C`$。
	- $`y=a \sin(bx+c)+d`$：振幅 $`|a|`$、週期 $`\dfrac{2\pi}{|b|}`$、上下平移 d。
	- 仰角、俯角：視線和水平線的夾角；方位角：從正北順時針量到目標方向的角。
	**🧭 解題流程**
	1. 測量題：先畫圖，把已知的長度和角度標在三角形上，再選正弦或餘弦定理。
	2. 週期現象（潮汐、日照、摩天輪）：由最高、最低點求振幅和中線，由一個完整週期的時間求 b。
	**⚠️ 容易錯的地方**
	- 已知兩邊和其中一邊的對角時，可能有兩個三角形。
	- 週期是 $`\dfrac{2\pi}{|b|}`$；f 在一段時間內都是正的、兩端是 0，這段時間是半個週期。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81bebf5ac997601bf0a7"/>　全國答對率 29%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81a8b83af5a5686c84e1"/>　全國答對率 32%
	- <mention-page url="https://app.notion.com/p/3ebee100984f81d89011dfb6651e3315"/>　全國答對率 37%
</details>
<details>
<summary>**數列、遞迴與規律**</summary>
	<callout icon="💡">
		等差看公差、等比看公比；遞迴式找「平移後成等比」的形式；週期規律用最小公倍數。
	</callout>
	**📌 必背**
	- 等差數列 $`a_n=a_1+(n-1)d`$、$`S_n=\dfrac{n(a_1+a_n)}{2}`$；等比數列 $`a_n=a_1\cdot r^{n-1}`$、$`S_n=\dfrac{a_1(1-r^n)}{1-r}`$（考卷附）。
	- $`1+2+\ldots+n=\dfrac{n(n+1)}{2}`$；$`1^2+2^2+\ldots+n^2=\dfrac{n(n+1)(2n+1)}{6}`$。
	**🧭 解題流程**
	1. 遞迴式 $`a_{n+1}=p\cdot a_n+q`$（$`p\ne1`$）：解 $`c=pc+q`$ 得到 c，則 $`a_n-c`$ 是公比 p 的等比數列，會趨近 c（$`|p|<1`$ 時）。
	2. 週期規律：兩個週期 p、q 同時回到起點，要經過 p、q 的最小公倍數。
	3. 找規律：列出前幾項，看差或比。
	**⚠️ 容易錯的地方**
	- 第 1 項是 $`a_1`$ 還是 $`a_0`$ 要看清楚，項數會差一個。
	- 公比 $`r=1`$ 時不能用等比級數公式。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81b394b0ee51f8e8e52b"/>　全國答對率 11%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81ffa945d6b2051d54f2"/>　全國答對率 27%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81088b94e1f659c05487"/>　全國答對率 29%
</details>
## 坐標、向量與空間
<details>
<summary>**直線與坐標幾何**</summary>
	<callout icon="💡">
		斜角與斜率、平行線距離、點到直線距離；面積問題把圖形放在坐標上算。
	</callout>
	**📌 必背**
	- 斜率 $`m=\dfrac{y_2-y_1}{x_2-x_1}=\tan\theta`$；平行 ⇔ 斜率相等；垂直 ⇔ 斜率乘積 $`=-1`$（都不是鉛直線時）。
	- 點到直線 $`ax+by+c=0`$ 的距離 $`=\dfrac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}`$；平行線距離 $`=\dfrac{|c_1-c_2|}{\sqrt{a^2+b^2}}`$。
	- 線段的中垂線：通過中點，斜率是線段斜率的負倒數。
	- 圓 $`(x-h)^2+(y-k)^2=r^2`$；圓心到直線的距離 $`d<r`$ 交兩點、$`d=r`$ 相切、$`d>r`$ 不相交。
	- 頂點在原點、另兩點 $`(x_1,y_1)`$、$`(x_2,y_2)`$ 的三角形面積 $`=\dfrac{1}{2}|x_1y_2-x_2y_1|`$。
	**🧭 解題流程**
	1. 先畫圖，把點、線放到坐標平面上，再決定用斜率、距離還是面積公式。
	2. 平分面積的直線：先算總面積的一半，判斷直線會和哪一條邊相交，再設交點坐標列式。
	**⚠️ 容易錯的地方**
	- 斜率乘積 $`=-1`$ 不適用於鉛直線。
	- 等腰三角形要分情況，並排除三點共線。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3ebee100984f81998baae9a7346164f5"/>　全國答對率 16%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f814685bad8e308f9baad"/>　全國答對率 17%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81bebf5ac997601bf0a7"/>　全國答對率 29%
</details>
<details>
<summary>**平面向量**</summary>
	<callout icon="💡">
		$`\overrightarrow{OP}=\alpha\overrightarrow{OA}+\beta\overrightarrow{OB}`$ 解出 $`\alpha`$、$`\beta`$ 再看範圍；係數都在 0 到 1 之間時 P 落在平行四邊形內。
	</callout>
	**📌 必背**
	- 向量的坐標：$`\overrightarrow{AB}=(x_B-x_A,y_B-y_A)`$；長度 $`|(a,b)|=\sqrt{a^2+b^2}`$。
	- 線性組合：$`\overrightarrow{OP}=\alpha\overrightarrow{OA}+\beta\overrightarrow{OB}`$；$`\alpha+\beta=1`$ ⇔ P 在直線 AB 上；$`0\le\alpha\le1`$ 且 $`0\le\beta\le1`$ ⇔ P 在 OA、OB 所張的平行四邊形內（含邊界）。
	- 分點：$`AP:PB=m:n`$ ⇒ $`\overrightarrow{OP}=\dfrac{n\overrightarrow{OA}+m\overrightarrow{OB}}{m+n}`$。
	- 內積 $`\overrightarrow{a}\cdot\overrightarrow{b}=a_1b_1+a_2b_2=|\overrightarrow{a}||\overrightarrow{b}|\cos\theta`$；$`\overrightarrow{a}\perp\overrightarrow{b}`$ ⇔ $`\overrightarrow{a}\cdot\overrightarrow{b}=0`$。
	**🧭 解題流程**
	1. 把向量寫成坐標，列出 $`\alpha`$、$`\beta`$ 的聯立方程式解出係數，再看係數的範圍判斷位置。
	2. 求長度的最大值：讓兩個分量的絕對值同時最大（各分量可以分開調整時）。
	**⚠️ 容易錯的地方**
	- 三角不等式 $`|\overrightarrow{a}+\overrightarrow{b}|\le|\overrightarrow{a}|+|\overrightarrow{b}|`$ 只是上界，兩向量不同方向時達不到。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3ebee100984f81fabd31e8fe2399d945"/>　全國答對率 26%
	- <mention-page url="https://app.notion.com/p/3ebee100984f81719a26ec44a6d3a1fb"/>　全國答對率 28%
	- <mention-page url="https://app.notion.com/p/3ebee100984f8111805be96f20c157f2"/>　全國答對率 38%
</details>
<details>
<summary>**矩陣**</summary>
	<callout icon="💡">
		A 乘上一個行向量＝A 的各行依係數組合；反方陣把「輸入、輸出」對調。
	</callout>
	**📌 必背**
	- 矩陣乘法：AB 的第 $`(i,j)`$ 元＝A 的第 i 列和 B 的第 j 行對應相乘再相加；一般 $`AB\ne BA`$。
	- 二階方陣 $`A=\begin{bmatrix}a&b\\c&d\end{bmatrix}`$：$`ad-bc\ne0`$ 時 $`A^{-1}=\dfrac{1}{ad-bc}\cdot\begin{bmatrix}d&-b\\-c&a\end{bmatrix}`$。
	- A 乘上行向量 $`(x,y)^T=x\cdot(\text{A 的第 1 行})+y\cdot(\text{第 2 行})`$。
	**🧭 解題流程**
	1. 用矩陣表示「輸入 → 輸出」：$`AX=Y`$；已知輸出求輸入，就用反方陣 $`X=A^{-1}Y`$。
	2. 表格資料轉矩陣：先確認列、行各代表什麼，乘法的維度要對得上。
	**⚠️ 容易錯的地方**
	- 矩陣乘法不能交換順序。
	- $`ad-bc=0`$ 時沒有反方陣。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81e787b1ec2ab5179d8a"/>　全國答對率 62%
	- <mention-page url="https://app.notion.com/p/3ebee100984f815ea66dc95541f62852"/>　全國答對率 63%
	- <mention-page url="https://app.notion.com/p/3ebee100984f8174b24aee225ed6d2f5"/>　全國答對率 65%
</details>
<details>
<summary>**空間概念（經緯度、透視、截痕）**</summary>
	<callout icon="💡">
		緯度 $`\theta`$ 的緯線半徑是 $`R\cos\theta`$；大圓弧是球面最短路徑；透視圖的消失點與圓錐截痕類型要會判斷。
	</callout>
	**📌 必背**
	- 地球半徑 R，緯度 $`\theta`$ 的緯線半徑 $`=R\cos\theta`$。
	- 同一條經線上兩地的距離 $`=R\times\text{緯度差（弧度）}`$；赤道上兩地的距離 $`=R\times\text{經度差（弧度）}`$；同一條緯線上沿緯線走的距離 $`=R\cos\theta\times\text{經度差（弧度）}`$。
	- 球面上兩點之間的最短路徑，是通過這兩點的大圓上的劣弧。
	- 透視圖：和畫面平行的直線畫出來仍然平行；和畫面不平行的一組平行線，畫出來會交於同一個消失點。
	- 圓錐截痕：截面與軸線的夾角 $`\beta`$、圓錐半頂角 $`\alpha`$：$`\beta=90^{\circ}`$ 是圓、$`\alpha<\beta<90^{\circ}`$ 是橢圓、$`\beta=\alpha`$ 是拋物線、$`\beta<\alpha`$ 是雙曲線。
	**🧭 解題流程**
	1. 球面問題：畫出過地心的剖面（大圓）或緯線圓，再用弧長 $`s=r\theta`$ 或三角函數。
	2. 截痕問題：先判斷 $`\beta`$ 和 $`\alpha`$ 的大小關係，再對應截痕的種類。
	**⚠️ 容易錯的地方**
	- 除了赤道，緯線都不是大圓，沿緯線走不是最短路徑。
	- 經緯度的角度要換成弧度再乘半徑。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3ebee100984f8112ad26c2d753e9b73b"/>　全國答對率 15%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f8144a806f2ae3fb0eb10"/>　全國答對率 23%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81cd88f2d1876fcda574"/>　全國答對率 26%
</details>
## 機率統計與計數
<details>
<summary>**排列組合**</summary>
	<callout icon="💡">
		相鄰的先綁成一塊再排；分組分派先滿足「每組都要有」的條件，再用補集扣掉不合的情形。
	</callout>
	**📌 必背**
	- 加法原理（分類）、乘法原理（分步）。
	- 排列 $`\dfrac{n!}{(n-k)!}`$；組合 $`C(n,k)=\dfrac{n!}{k!(n-k)!}`$；有相同物的排列 $`\dfrac{n!}{p!\cdot q!\cdots}`$。
	- k 個相同的東西分給 n 個人（可以有人沒分到）：$`C(n+k-1,k)`$ 種。
	**🧭 解題流程**
	1. 相鄰的先綁成一塊再排，塊內再排；不相鄰的先排其他人，再插空隙。
	2. 分組、分派：先滿足「每組都要有」的條件，再用補集扣掉不合的情形。
	**⚠️ 容易錯的地方**
	- 組與組沒有分別時要除以組數的排列數。
	- 「至少」的問題用補集比較快、不容易重複計算。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3ebee100984f81d884d8e7777827bd06"/>　全國答對率 8%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81038983e339acb3508a"/>　全國答對率 25%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81e99cc2c578aaa7b5ac"/>　全國答對率 35%
</details>
<details>
<summary>**機率**</summary>
	<callout icon="💡">
		獨立事件機率相乘；$`\text{條件機率}=\dfrac{\text{交集}}{\text{條件}}`$；列聯表先把各格用同一個未知數表示。
	</callout>
	**📌 必背**
	- 古典機率 $`P(A)=\dfrac{n(A)}{n(S)}`$（每個樣本點機會相等）；$`P(A')=1-P(A)`$。
	- $`P(A\cup B)=P(A)+P(B)-P(A\cap B)`$。
	- 條件機率 $`P(B\mid A)=\dfrac{P(A\cap B)}{P(A)}`$；A、B 獨立 ⇔ $`P(A\cap B)=P(A)\cdot P(B)`$。
	**🧭 解題流程**
	1. 列聯表：設一個未知數把表格填滿（每列、每行的和要對），再把題目的條件翻成方程式或不等式。
	2. 多階段的試驗：畫樹狀圖，路徑相乘、不同路徑相加。
	3. 「至少一次」：1 減去「一次都沒有」。
	**⚠️ 容易錯的地方**
	- 「A 之中有多少比例是 B」是條件機率，分母是 A，不是全體。
	- 獨立和互斥不同。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3ebee100984f81a3abb5db65d758d976"/>　全國答對率 23%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f8151a00cd7d71344c3ab"/>　全國答對率 24%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81e99cc2c578aaa7b5ac"/>　全國答對率 35%
</details>
<details>
<summary>**數據分析**</summary>
	<callout icon="💡">
		資料乘以 a 倍時標準差乘 $`|a|`$、相關係數不變（$`a>0`$）；迴歸直線過（平均, 平均），斜率 $`=r\cdot\dfrac{\sigma_y}{\sigma_x}`$；百分位數依定義找位置。
	</callout>
	**📌 必背**
	- 中位數、第 k 百分位數：資料由小到大排，算 $`n\times\dfrac{k}{100}`$；不是整數就取下一個整數的位置，是整數 m 就取第 m 和第 $`m+1`$ 個的平均。
	- 標準差、相關係數、迴歸直線的公式考卷附；迴歸直線一定通過 $`(\mu_x,\mu_y)`$，斜率 $`=r\cdot\dfrac{\sigma_y}{\sigma_x}`$。
	- 資料 $`y=ax+b`$：平均變成 $`a\cdot\mu_x+b`$、標準差變成 $`|a|\cdot\sigma_x`$；$`a>0`$ 時相關係數不變，$`a<0`$ 時變號。
	**🧭 解題流程**
	1. 看散布圖：點越接近一條直線，$`|r|`$ 越接近 1；斜向右上 $`r>0`$、右下 $`r<0`$。
	2. 用迴歸直線預測：把 x 代入 $`y-\mu_y=r\cdot\dfrac{\sigma_y}{\sigma_x}(x-\mu_x)`$。
	**⚠️ 容易錯的地方**
	- 標準差只受乘除影響，加減常數不會改變。
	- 相關係數不受單位換算（乘正數）影響。
	- 由 x 預測 y 和由 y 預測 x 是兩條不同的迴歸直線。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3ebee100984f8112a954f8f1e377146e"/>　全國答對率 15%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f817e95f8c1c7d01bc2c6"/>　全國答對率 35%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f8151b4bdf9662e73dce5"/>　全國答對率 46%
</details>
