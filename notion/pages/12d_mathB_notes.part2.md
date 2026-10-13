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
	- 正射影：$`\overrightarrow{a}`$ 在 $`\overrightarrow{b}`$ 上的正射影 $`=\dfrac{\overrightarrow{a}\cdot\overrightarrow{b}}{|\overrightarrow{b}|^2}\overrightarrow{b}`$；夾角 $`\cos\theta=\dfrac{\overrightarrow{a}\cdot\overrightarrow{b}}{|\overrightarrow{a}||\overrightarrow{b}|}`$；兩向量平行 ⇔ 一個是另一個的實數倍。
	**🧭 解題流程**
	1. 把向量寫成坐標，列出 $`\alpha`$、$`\beta`$ 的聯立方程式解出係數，再看係數的範圍判斷位置。
	2. 求長度的最大值：讓兩個分量的絕對值同時最大（各分量可以分開調整時）。
	**🧩 經典題型與解題技巧**
	先從題目的關鍵字認出是哪一型，再照那一型的做法解；點開可以看例題、解答和考過的題目。
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
	- 二元一次方程組可以寫成 $`AX=B`$：$`\det A\ne0`$ 時恰有一組解 $`X=A^{-1}B`$；$`\det A=0`$ 時無解或有無限多組解。
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
	- 空間坐標：點 $`(x,y,z)`$ 在 xy 平面上的投影是 $`(x,y,0)`$；兩點距離 $`=\sqrt{(x_1-x_2)^2+(y_1-y_2)^2+(z_1-z_2)^2}`$。
	- 經緯度換成空間坐標：球心在原點、半徑 R，z 軸指向北極、x 軸指向赤道和本初子午線的交點；北緯 $`\theta`$、東經 $`\varphi`$ 的點是 $`(R\cos\theta\cos\varphi,R\cos\theta\sin\varphi,R\sin\theta)`$。
	- 長方體表面上兩點的最短路徑：把長方體展開成平面，兩點連成直線；不同的展開方式要比較，取最短的。
	- 空間中兩直線的關係：相交、平行、歪斜（不平行也不相交）；直線垂直一個平面 ⇔ 直線垂直這個平面上兩條相交的直線。
	- 平面上的比例：相似圖形對應邊成比例，面積比是邊長比的平方；例如 A 系列紙張（A3、A4）的長寬比是 $`\sqrt{2}:1`$，對摺後比例不變。
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
