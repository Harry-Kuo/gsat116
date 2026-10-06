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
	- 乘法公式：$`(a\pm b)^3=a^3\pm3a^2b+3ab^2\pm b^3`$；$`a^3\pm b^3=(a\pm b)(a^2\mp ab+b^2)`$。
	- 分母有理化：$`\dfrac{1}{\sqrt{a}+\sqrt{b}}=\dfrac{\sqrt{a}-\sqrt{b}}{a-b}`$（分子、分母同乘 $`\sqrt{a}-\sqrt{b}`$）。
	- 算幾不等式：$`a\ge0`$、$`b\ge0`$ 時 $`\dfrac{a+b}{2}\ge\sqrt{ab}`$，等號在 $`a=b`$ 時成立；兩數的和固定時，相等時乘積最大；乘積固定時，相等時和最小。
	- 科學記號：正數都能寫成 $`a\times10^n`$（$`1\le a<10`$，n 是整數），$`\log(a\times10^n)=n+\log a`$；n 決定位數，$`\log a`$（介於 0 和 1 之間）決定首位數字。
	- 指數函數 $`y=a^x`$ 的圖形都在 x 軸上方、通過 $`(0,1)`$；對數函數 $`y=\log_a x`$ 的圖形都在 y 軸右側、通過 $`(1,0)`$；兩者對稱於直線 $`y=x`$。$`a>1`$ 時兩者都遞增，$`0<a<1`$ 時都遞減。
	- 複利：本金 P、年利率 r，一年複利 n 次，t 年後本利和 $`P\left(1+\dfrac{r}{n}\right)^{nt}`$；連續複利（n 趨近無限大）是 $`Pe^{rt}`$。
	- 平均成長率：各期成長率是 $`r_1`$、$`r_2`$、…、$`r_n`$ 時，平均成長率 $`=\sqrt[n]{(1+r_1)(1+r_2)\cdots(1+r_n)}-1`$（幾何平均，不是算術平均）。
	- 對數尺度：pH 差 1，$`[\mathrm{H^+}]`$ 差 10 倍；分貝差 10，聲音強度差 10 倍；芮氏地震規模差 1，振幅差 10 倍、能量約差 32 倍。題目給公式時，把兩個式子相減最快。
	**🧭 解題流程**
	1. 成長或衰退模型：每期變成原來的 $`(1+r)`$ 倍，n 期後是 $`A_0\cdot(1+r)^n`$；求期數就兩邊取對數。
	2. 比較大小：化成同底；底數 $`>1`$ 時遞增，$`0<\text{底數}<1`$ 時遞減。
	3. 估算：用考卷附的對數值，$`\log5=1-\log2`$。
	**⚠️ 容易錯的地方**
	- 每期成長 4%，n 期後是乘 $`(1.04)^n`$，不是乘 $`(1+0.04n)`$。
	- $`\ln\left(\dfrac{135}{100}\right)=\ln135-\ln100`$，不是 $`\ln(135-100)`$：對數把除法變成減法。
	- 對數的真數一定要大於 0。
	- 算幾不等式要兩數都不是負的，而且等號要能成立，最大值或最小值才取得到。
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
	- 三次函數的局部近似：用綜合除法連續除以 $`x-h`$，把 $`f(x)`$ 寫成 $`a(x-h)^3+b(x-h)^2+c(x-h)+d`$，圖形在 $`x=h`$ 附近近似直線 $`y=c(x-h)+d`$。
	- 每個三次函數都是 $`y=ax^3+px`$ 的圖形平移而來（把對稱中心移到原點）；x 很大或很小時，圖形的走勢由最高次項決定。
	- 數線上的分點：A、B 的坐標是 a、b，P 在 $`\overline{AB}`$ 上且 $`\overline{AP}:\overline{PB}=m:n`$，則 P 的坐標 $`=\dfrac{na+mb}{m+n}`$；內插法就是用分點公式估計兩個已知數值之間的值。
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
	- 廣義角的三角比：終邊在第一象限時三者都是正的；第二象限只有 $`\sin`$ 是正的；第三象限只有 $`\tan`$ 是正的；第四象限只有 $`\cos`$ 是正的。
	- 極坐標 $`[r,\theta]`$：到原點的距離是 r，從 x 軸正向逆時針轉 $`\theta`$；換成直角坐標是 $`(r\cos\theta,r\sin\theta)`$，反過來 $`r=\sqrt{x^2+y^2}`$。
	- 週期現象：頻率是週期的倒數，$`y=a\sin(bx+c)+d`$ 的頻率 $`=\dfrac{|b|}{2\pi}`$（每單位時間完成幾次循環）。
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
	- $`\sum`$ 的性質：$`\sum_{k=1}^{n}(a_k+b_k)=\sum_{k=1}^{n}a_k+\sum_{k=1}^{n}b_k`$；$`\sum_{k=1}^{n}c\cdot a_k=c\sum_{k=1}^{n}a_k`$；$`\sum_{k=1}^{n}c=nc`$。
	- 數學歸納法：先驗證 $`n=1`$ 成立，再證明「$`n=k`$ 成立 ⇒ $`n=k+1`$ 也成立」，就能推得所有正整數 n 都成立。
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
	- 對稱點：$`(a,b)`$ 對 x 軸是 $`(a,-b)`$，對 y 軸是 $`(-a,b)`$，對原點是 $`(-a,-b)`$，對直線 $`y=x`$ 是 $`(b,a)`$。
	- 圓的切線和通過切點的半徑垂直；從圓外一點可以作兩條切線，兩條切線段一樣長。
	- 二元一次不等式 $`ax+by+c>0`$ 表示直線某一側的半平面：代一個不在直線上的點（常用原點）檢查。
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
	- 正射影：$`\overrightarrow{a}`$ 在 $`\overrightarrow{b}`$ 上的正射影 $`=\dfrac{\overrightarrow{a}\cdot\overrightarrow{b}}{|\overrightarrow{b}|^2}\overrightarrow{b}`$；夾角 $`\cos\theta=\dfrac{\overrightarrow{a}\cdot\overrightarrow{b}}{|\overrightarrow{a}||\overrightarrow{b}|}`$；兩向量平行 ⇔ 一個是另一個的實數倍。
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
<details>
<summary>**排列組合**</summary>
	<callout icon="💡">
		相鄰的先綁成一塊再排；分組分派先滿足「每組都要有」的條件，再用補集扣掉不合的情形。
	</callout>
	**📌 必背**
	- 加法原理（分類）、乘法原理（分步）。
	- 排列 $`\dfrac{n!}{(n-k)!}`$；組合 $`C(n,k)=\dfrac{n!}{k!(n-k)!}`$；有相同物的排列 $`\dfrac{n!}{p!\cdot q!\cdots}`$。
	- k 個相同的東西分給 n 個人（可以有人沒分到）：$`C(n+k-1,k)`$ 種。
	- k 個位置、每個位置都有 m 種選擇：$`m^k`$ 種（重複排列）。
	- 取捨原理（排容原理）：$`n(A\cup B)=n(A)+n(B)-n(A\cap B)`$；$`n(A\cup B\cup C)=n(A)+n(B)+n(C)-n(A\cap B)-n(B\cap C)-n(C\cap A)+n(A\cap B\cap C)`$。
	- 二項式定理：$`(a+b)^n`$ 展開式的第 $`k+1`$ 項是 $`C(n,k)\cdot a^{n-k}\cdot b^k`$；$`C(n,0)+C(n,1)+\cdots+C(n,n)=2^n`$，$`C(n,k)=C(n,n-k)`$。
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
	- 期望值 $`E=x_1p_1+x_2p_2+\cdots+x_np_n`$（每個可能的值乘上它的機率再相加）。
	- 貝氏定理：$`P(A\mid B)=\dfrac{P(A)\cdot P(B\mid A)}{P(A)\cdot P(B\mid A)+P(A')\cdot P(B\mid A')}`$；分子是「A 發生而且得到 B」這條路徑的機率，分母是所有會得到 B 的路徑機率總和。
	- 主觀機率也要符合機率的性質（每個事件的機率介於 0 和 1 之間，所有可能情形的機率和為 1）；客觀機率由大量資料的相對次數估計。
	**🧭 解題流程**
	1. 列聯表：設一個未知數把表格填滿（每列、每行的和要對），再把題目的條件翻成方程式或不等式。
	2. 多階段的試驗：畫樹狀圖，路徑相乘、不同路徑相加。
	3. 「至少一次」：1 減去「一次都沒有」。
	**⚠️ 容易錯的地方**
	- 「A 之中有多少比例是 B」是條件機率，分母是 A，不是全體。
	- 獨立和互斥不同。
	- 貝氏定理的分母要把所有會得到這個結果的情況都加進來，不能只算其中一條路徑。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3ebee100984f81a3abb5db65d758d976"/>　全國答對率 23%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f8151a00cd7d71344c3ab"/>　全國答對率 24%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81e99cc2c578aaa7b5ac"/>　全國答對率 35%
</details>
