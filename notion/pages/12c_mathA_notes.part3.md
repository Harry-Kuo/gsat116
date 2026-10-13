<details>
<summary>**矩陣**</summary>
	<callout icon="💡">
		矩陣乘法先算小次方找規律；線性組合可以把未知向量拆成已知向量。
	</callout>
	**📌 必背**
	- 矩陣乘法：AB 的第 $`(i,j)`$ 元＝A 的第 i 列和 B 的第 j 行對應相乘再相加；一般 $`AB\ne BA`$。
	- 二階方陣 $`A=\begin{bmatrix}a&b\\c&d\end{bmatrix}`$：$`\det A=ad-bc`$；$`\det A\ne0`$ 時 $`A^{-1}=\dfrac{1}{ad-bc}\cdot\begin{bmatrix}d&-b\\-c&a\end{bmatrix}`$。
	- $`(AB)^{-1}=B^{-1}A^{-1}`$（順序相反）；$`\det(AB)=\det A\cdot\det B`$。
	- 聯立方程式寫成 $`AX=B`$：$`\det A\ne0`$ 時恰有一組解 $`X=A^{-1}B`$。
	- A 乘上行向量 $`(x,y,z)^T=x\cdot(\text{A 的第 1 行})+y\cdot(\text{第 2 行})+z\cdot(\text{第 3 行})`$。
	- 克拉瑪公式：$`\begin{cases}a_1x+b_1y=c_1\\a_2x+b_2y=c_2\end{cases}`$，令 $`\Delta=\begin{vmatrix}a_1&b_1\\a_2&b_2\end{vmatrix}`$、$`\Delta_x=\begin{vmatrix}c_1&b_1\\c_2&b_2\end{vmatrix}`$、$`\Delta_y=\begin{vmatrix}a_1&c_1\\a_2&c_2\end{vmatrix}`$；$`\Delta\ne0`$ 時恰有一組解 $`x=\dfrac{\Delta_x}{\Delta}`$、$`y=\dfrac{\Delta_y}{\Delta}`$。
	- $`\Delta=0`$ 時兩直線平行或重合：$`\Delta_x`$、$`\Delta_y`$ 至少一個不是 0 → 無解（平行）；$`\Delta_x=\Delta_y=0`$ → 無限多組解（重合）。
	- 三元一次聯立方程式：用消去法（對增廣矩陣做列運算）化成階梯形，再由最後一式往回代。
	- 平面上的線性變換：逆時針旋轉 $`\theta`$ 是 $`\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}`$；對 x 軸鏡射是 $`\begin{bmatrix}1&0\\0&-1\end{bmatrix}`$；對直線 $`y=x`$ 鏡射是 $`\begin{bmatrix}0&1\\1&0\end{bmatrix}`$；伸縮是 $`\begin{bmatrix}h&0\\0&k\end{bmatrix}`$；沿 x 方向推移是 $`\begin{bmatrix}1&k\\0&1\end{bmatrix}`$。
	- 線性變換 A 把圖形的面積變成 $`|\det A|`$ 倍；先做 A、再做 B 的合成變換是 $`BA`$（後做的寫在左邊）。
	- 二階轉移矩陣：元素都不是負數，每一行的和是 1；$`X_{n+1}=AX_n`$，所以 $`X_n=A^nX_0`$；穩定狀態 X 滿足 $`AX=X`$，且 X 的兩個元素和為 1。
	**🧭 解題流程**
	1. 求 $`A^n`$：先算 $`A^2`$、$`A^3`$，找出規律或週期。
	2. 已知 A 作用在幾個向量的結果：把要求的向量拆成這幾個向量的組合，再用 $`A(s\overrightarrow{u}+t\overrightarrow{v})=sA\overrightarrow{u}+tA\overrightarrow{v}`$。
	**⚠️ 容易錯的地方**
	- 矩陣乘法不能交換順序，左乘、右乘的結果不同。
	- 反方陣存在的條件是行列式不為 0。
	- 先旋轉再鏡射，和先鏡射再旋轉，結果通常不同：合成變換要注意乘的順序。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3e9ee100984f8178b788e0846f022e30"/>　全國答對率 26%
	- <mention-page url="https://app.notion.com/p/3ebee100984f81e8bfa5f3aa3d256408"/>　全國答對率 36%
	- <mention-page url="https://app.notion.com/p/3ebee100984f81bdab3fefa792c1d4e1"/>　全國答對率 38%
</details>
## 機率統計與計數
