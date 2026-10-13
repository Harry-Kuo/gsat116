<callout icon="🧭">
	依單元整理必背公式、解題流程和容易錯的地方。標「考卷附」的公式，考卷最後會附上，但還是要熟到不用查。
	向量、機率統計、排列組合另外整理了「🧩 經典題型與解題技巧」：先從題目的關鍵字認出題型，再照做法解題，每一型都附例題、解答和考過的題目。
	每個觀念最後列出前兩週每日練習中全國答對率最低的題目，點進去可以看題目、答案與解析。
</callout>
## 數與函數
<details>
<summary>**數與式、指數對數**</summary>
	<callout icon="💡">
		指數、對數先化成同底，再比較指數；高斯記號 $`[x]`$ 要一個一個代值確認。
	</callout>
	**📌 必背**
	- 指數律（$`a>0`$）：$`a^m\cdot a^n=a^{m+n}`$、$`(a^m)^n=a^{mn}`$、$`a^0=1`$、$`a^{-n}=\dfrac{1}{a^n}`$、$`a^{m/n}=\sqrt[n]{a^m}`$。
	- 對數的定義：$`\log_a b=x`$ ⇔ $`a^x=b`$（$`a>0`$、$`a\ne1`$、$`b>0`$）。
	- 運算：$`\log_a(MN)=\log_a M+\log_a N`$；$`\log_a\left(\dfrac{M}{N}\right)=\log_a M-\log_a N`$；$`\log_a(M^k)=k\cdot\log_a M`$。
	- 換底：$`\log_a b=\dfrac{\log b}{\log a}`$；$`\log_a b\cdot\log_b c=\log_a c`$。
	- 位數：正數 N 的整數部分是 k 位數 ⇔ $`k-1\le\log N<k`$；首位數字看 $`\log N`$ 的小數部分。
	- 絕對值：$`|x-a|`$ 是數線上 x 到 a 的距離；$`|x-a|\le r`$ ⇔ $`a-r\le x\le a+r`$。
	- 乘法公式：$`(a\pm b)^3=a^3\pm3a^2b+3ab^2\pm b^3`$；$`a^3\pm b^3=(a\pm b)(a^2\mp ab+b^2)`$。
	- 分母有理化：$`\dfrac{1}{\sqrt{a}+\sqrt{b}}=\dfrac{\sqrt{a}-\sqrt{b}}{a-b}`$（分子、分母同乘 $`\sqrt{a}-\sqrt{b}`$）。
	- 算幾不等式：$`a\ge0`$、$`b\ge0`$ 時 $`\dfrac{a+b}{2}\ge\sqrt{ab}`$，等號在 $`a=b`$ 時成立；兩數的和固定時，相等時乘積最大；乘積固定時，相等時和最小。
	- 科學記號：正數都能寫成 $`a\times10^n`$（$`1\le a<10`$，n 是整數），$`\log(a\times10^n)=n+\log a`$；n 決定位數，$`\log a`$（介於 0 和 1 之間）決定首位數字。
	- 指數函數 $`y=a^x`$ 的圖形都在 x 軸上方、通過 $`(0,1)`$；對數函數 $`y=\log_a x`$ 的圖形都在 y 軸右側、通過 $`(1,0)`$；兩者對稱於直線 $`y=x`$。$`a>1`$ 時兩者都遞增，$`0<a<1`$ 時都遞減。
	- 按比例成長或衰退：每期變成 r 倍，n 期後是 $`A_0\cdot r^n`$；半衰期是 T 的物質，經過時間 t 剩下 $`A_0\cdot\left(\dfrac{1}{2}\right)^{t/T}`$。
	**🧭 解題流程**
	1. 比較大小：先化成同底的指數或對數；底數 $`>1`$ 時函數遞增，$`0<\text{底數}<1`$ 時遞減。
	2. 解指數方程式：令 $`t=a^x`$（$`t>0`$），換成多項式方程式；解完檢查 t 是不是正的。
	3. 解對數方程式：先寫出「真數 $`>0`$」的條件，合併成一個對數再去掉 $`\log`$，最後回代檢查。
	**⚠️ 容易錯的地方**
	- 底數介於 0 和 1 之間時，兩邊取指數或對數後，不等號要變向。
	- 對數的真數一定要大於 0，解出來的值要回代檢查。
	- 考卷附 $`\log2\approx0.3010`$、$`\log3\approx0.4771`$、$`\log5\approx0.6990`$、$`\log7\approx0.8451`$，估算時直接用。
	- 算幾不等式要兩數都不是負的，而且等號要能成立，最大值或最小值才取得到。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3e9ee100984f817baa22ebc185144228"/>　全國答對率 31%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f813ab42bd08747fa6eda"/>　全國答對率 41%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f813a9baafa5b8a72d880"/>　全國答對率 44%
</details>
<details>
<summary>**多項式與二次函數**</summary>
	<callout icon="💡">
		多項式看首項係數與對稱中心；二次函數先配方找頂點。
	</callout>
	**📌 必背**
	- 除法原理：$`f(x)=g(x)\cdot q(x)+r(x)`$，餘式 $`r(x)`$ 的次數比除式 $`g(x)`$ 低。
	- 餘式定理：$`f(x)`$ 除以 $`x-a`$ 的餘式是 $`f(a)`$；因式定理：$`f(a)=0`$ ⇔ $`x-a`$ 是 $`f(x)`$ 的因式。
	- 二次函數配方：$`y=a(x-h)^2+k`$，頂點 $`(h,k)`$；$`a>0`$ 開口向上、最小值 k。
	- $`ax^2+bx+c=0`$：判別式 $`b^2-4ac`$ 決定實根個數；兩根和 $`=-\dfrac{b}{a}`$、兩根積 $`=\dfrac{c}{a}`$。
	- 三次函數 $`y=ax^3+bx^2+cx+d`$ 的圖形對稱於點 $`\left(-\dfrac{b}{3a},f\left(-\dfrac{b}{3a}\right)\right)`$。
	- 三次函數的局部近似：用綜合除法連續除以 $`x-h`$，把 $`f(x)`$ 寫成 $`a(x-h)^3+b(x-h)^2+c(x-h)+d`$，圖形在 $`x=h`$ 附近近似直線 $`y=c(x-h)+d`$。
	- 每個三次函數都是 $`y=ax^3+px`$ 的圖形平移而來（把對稱中心移到原點）；x 很大或很小時，圖形的走勢由最高次項決定。
	- 數線上的分點：A、B 的坐標是 a、b，P 在 $`\overline{AB}`$ 上且 $`\overline{AP}:\overline{PB}=m:n`$，則 P 的坐標 $`=\dfrac{na+mb}{m+n}`$；內插法就是用分點公式估計兩個已知數值之間的值。
	**🧭 解題流程**
	1. 求餘式：除式是一次式就代值；除式是二次式，設餘式為 $`px+q`$，再代入兩個根解聯立。
	2. 解多項式不等式：因式分解 → 在數線上標出所有根 → 最右邊的正負由最高次項係數決定，往左每過一個根變號一次。
	3. 兩個函數圖形的交點：把兩個函數相減，交點的 x 坐標就是相減後方程式的實根。
	**⚠️ 容易錯的地方**
	- 偶次重根的兩側正負號相同，不會變號。
	- 二次函數在限定範圍內的最大值、最小值，要比較頂點和兩個端點。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3e9ee100984f8164bacee08cc8299630"/>　全國答對率 20%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81ac9148d78230b6143c"/>　全國答對率 28%
	- <mention-page url="https://app.notion.com/p/3ebee100984f8103afbfedcdd9d820cc"/>　全國答對率 31%
</details>
<details>
<summary>**三角函數**</summary>
	<callout icon="💡">
		先畫出單位圓或函數圖形，再判斷範圍與交點；倍角公式要熟。
	</callout>
	**📌 必背**
	- 特殊角：$`\sin30^{\circ}=\dfrac{1}{2}`$、$`\sin45^{\circ}=\dfrac{\sqrt{2}}{2}`$、$`\sin60^{\circ}=\dfrac{\sqrt{3}}{2}`$；$`\sin^2\theta+\cos^2\theta=1`$；$`\tan\theta=\dfrac{\sin\theta}{\cos\theta}`$。
	- 弧度：$`\pi=180^{\circ}`$；扇形弧長 $`s=r\theta`$、面積 $`=\dfrac{1}{2}r^2\theta`$（$`\theta`$ 用弧度）。
	- 和角公式（考卷附）；倍角：$`\sin2\theta=2 \sin\theta\cos\theta`$，$`\cos2\theta=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta`$。
	- 正弦定理 $`\dfrac{a}{\sin A}=\dfrac{b}{\sin B}=\dfrac{c}{\sin C}=2R`$、餘弦定理 $`c^2=a^2+b^2-2ab\cos C`$（考卷附）；三角形面積 $`=\dfrac{1}{2}ab\sin C`$。
	- $`y=a \sin(bx+c)+d`$：振幅 $`|a|`$、週期 $`\dfrac{2\pi}{|b|}`$、上下平移 d。
	- 疊合：$`a \sin x+b \cos x=\sqrt{a^2+b^2}\cdot\sin(x+\varphi)`$，最大值 $`\sqrt{a^2+b^2}`$、最小值 $`-\sqrt{a^2+b^2}`$。
	- 廣義角的三角比：終邊在第一象限時三者都是正的；第二象限只有 $`\sin`$ 是正的；第三象限只有 $`\tan`$ 是正的；第四象限只有 $`\cos`$ 是正的。
	- 極坐標 $`[r,\theta]`$：到原點的距離是 r，從 x 軸正向逆時針轉 $`\theta`$；換成直角坐標是 $`(r\cos\theta,r\sin\theta)`$，反過來 $`r=\sqrt{x^2+y^2}`$。
	- 半角公式：$`\sin^2\dfrac{\theta}{2}=\dfrac{1-\cos\theta}{2}`$、$`\cos^2\dfrac{\theta}{2}=\dfrac{1+\cos\theta}{2}`$。
	- $`y=\sin x`$、$`y=\cos x`$ 的週期是 $`2\pi`$、值域是 $`-1\le y\le1`$；$`y=\tan x`$ 的週期是 $`\pi`$。
	**🧭 解題流程**
	1. 解三角方程式或不等式：用倍角或疊合化成同一個三角函數 → 解出 $`\sin\theta`$ 或 $`\cos\theta`$ 的範圍 → 在單位圓上找出對應的角。
	2. 解三角形：已知兩角一邊、兩邊一對角用正弦定理；已知三邊、兩邊夾角用餘弦定理。
	3. 測量題：先畫出三角形，標出已知的邊和角，再選正弦或餘弦定理。
	**⚠️ 容易錯的地方**
	- 已知兩邊和其中一邊的對角時，可能有兩個三角形，要檢查。
	- 週期是 $`\dfrac{2\pi}{|b|}`$，不是 $`2\pi\cdot|b|`$。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3e9ee100984f812c957aca6d2b910481"/>　全國答對率 6%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f8166aa0bfcef9349cb6f"/>　全國答對率 14%
	- <mention-page url="https://app.notion.com/p/3ebee100984f81ee83b4faead4fb02d8"/>　全國答對率 21%
</details>
<details>
<summary>**數列與級數**</summary>
	<callout icon="💡">
		等差看中項、等比看公比；遞迴式試著找出「平移後成等比」的形式。
	</callout>
	**📌 必背**
	- 等差數列 $`a_n=a_1+(n-1)d`$；前 n 項和 $`S_n=\dfrac{n(a_1+a_n)}{2}`$（考卷附）。
	- 等比數列 $`a_n=a_1\cdot r^{n-1}`$；前 n 項和 $`S_n=\dfrac{a_1(1-r^n)}{1-r}`$，$`r\ne1`$（考卷附）。
	- $`1+2+\ldots+n=\dfrac{n(n+1)}{2}`$；$`1^2+2^2+\ldots+n^2=\dfrac{n(n+1)(2n+1)}{6}`$；$`1^3+2^3+\ldots+n^3=\left[\dfrac{n(n+1)}{2}\right]^2`$。
	- 三數成等差：中間項是兩旁的平均；三數成等比：中間項的平方＝兩旁的乘積。
	- $`\sum`$ 的性質：$`\sum_{k=1}^{n}(a_k+b_k)=\sum_{k=1}^{n}a_k+\sum_{k=1}^{n}b_k`$；$`\sum_{k=1}^{n}c\cdot a_k=c\sum_{k=1}^{n}a_k`$；$`\sum_{k=1}^{n}c=nc`$。
	**🧭 解題流程**
	1. 遞迴式 $`a_{n+1}=p\cdot a_n+q`$（$`p\ne1`$）：解 $`c=pc+q`$ 得到 c，則 $`a_{n+1}-c=p(a_n-c)`$，$`a_n-c`$ 是公比 p 的等比數列。
	2. 找規律：先列出 $`n=1`$、2、3、4 的值，看差或比，猜出一般項後再驗證。
	3. 數學歸納法：先驗證 $`n=1`$ 成立，再由 $`n=k`$ 成立推出 $`n=k+1`$ 也成立。
	**⚠️ 容易錯的地方**
	- 公比 $`r=1`$ 時不能用等比級數公式，前 n 項和是 $`n\cdot a_1`$。
	- 注意 $`\sum`$ 從 $`k=0`$ 還是 $`k=1`$ 開始，項數會差一個。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3e9ee100984f817baa22ebc185144228"/>　全國答對率 31%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f813ab42bd08747fa6eda"/>　全國答對率 41%
	- <mention-page url="https://app.notion.com/p/3ebee100984f812aa4afff4d03cc09b0"/>　全國答對率 46%
</details>
## 幾何與向量
<details>
<summary>**坐標幾何（直線、圓、不等式區域）**</summary>
	<callout icon="💡">
		把條件畫在坐標平面上；點到直線距離與圓的切割、弦長公式是核心。
	</callout>
	**📌 必背**
	- 斜率 $`m=\dfrac{y_2-y_1}{x_2-x_1}=\tan\theta`$（$`\theta`$ 是斜角）；兩直線平行 ⇔ 斜率相等；垂直 ⇔ 斜率乘積 $`=-1`$（兩條都不是鉛直線時）。
	- 點 $`(x_0,y_0)`$ 到直線 $`ax+by+c=0`$ 的距離 $`=\dfrac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}`$；兩平行線 $`ax+by+c_1=0`$、$`ax+by+c_2=0`$ 的距離 $`=\dfrac{|c_1-c_2|}{\sqrt{a^2+b^2}}`$。
	- 圓 $`(x-h)^2+(y-k)^2=r^2`$；圓心到直線的距離 d：$`d<r`$ 交兩點、$`d=r`$ 相切、$`d>r`$ 不相交；弦長 $`=2\sqrt{r^2-d^2}`$。
	- 線段的中垂線：通過中點，斜率是線段斜率的負倒數；中垂線上的點到兩端點等距。
	- $`ax+by+c>0`$ 表示直線某一側的區域：代一個不在直線上的點（常用原點）檢查。
	- 對稱點：$`(a,b)`$ 對 x 軸是 $`(a,-b)`$，對 y 軸是 $`(-a,b)`$，對原點是 $`(-a,-b)`$，對直線 $`y=x`$ 是 $`(b,a)`$。
	- 圓的切線和通過切點的半徑垂直；從圓外一點可以作兩條切線，兩條切線段一樣長。
	**🧭 解題流程**
	1. 先把條件畫在坐標平面上，再決定用距離、斜率還是代入。
	2. 求圓：圓心在某條直線上，就用參數設圓心，再用「圓心到切線的距離＝半徑」列方程式。
	3. 求面積：把多邊形切成三角形；頂點在原點、另兩點 $`(x_1,y_1)`$、$`(x_2,y_2)`$ 的三角形面積 $`=\dfrac{1}{2}|x_1y_2-x_2y_1|`$。
	**⚠️ 容易錯的地方**
	- 等腰、直角三角形要分「哪兩邊相等」「哪個角是直角」討論，並排除三點共線。
	- 斜率乘積 $`=-1`$ 不適用於鉛直線（斜率不存在）。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3e9ee100984f8132b384f4efbaaa7180"/>　全國答對率 18%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f8164bacee08cc8299630"/>　全國答對率 20%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81c88caae36526b6ad3e"/>　全國答對率 37%
</details>
