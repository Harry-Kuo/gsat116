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
	**🧩 經典題型與解題技巧**：在本頁最上方的「機率」。
	**⚠️ 容易錯的地方**
	- 「A 之中有多少比例是 B」是條件機率，分母是 A，不是全體。
	- 獨立和互斥不同。
	- 貝氏定理的分母要把所有會得到這個結果的情況都加進來，不能只算其中一條路徑。
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
	- 標準差 $`\sigma=\sqrt{\dfrac{1}{n}\sum_{i=1}^{n}(x_i-\mu)^2}=\sqrt{\dfrac{1}{n}\sum_{i=1}^{n}x_i^2-\mu^2}`$（考卷附）；標準化 $`z=\dfrac{x-\mu}{\sigma}`$，標準化後的資料平均是 0、標準差是 1。
	- 相關係數 r 介於 $`-1`$ 和 1 之間，等於兩組資料標準化之後，對應乘積的平均（公式考卷附）。
	**🧭 解題流程**
	1. 看散布圖：點越接近一條直線，$`|r|`$ 越接近 1；斜向右上 $`r>0`$、右下 $`r<0`$。
	2. 用迴歸直線預測：把 x 代入 $`y-\mu_y=r\cdot\dfrac{\sigma_y}{\sigma_x}(x-\mu_x)`$。
	**🧩 經典題型與解題技巧**：在本頁最上方的「數據分析」。
	**⚠️ 容易錯的地方**
	- 標準差只受乘除影響，加減常數不會改變。
	- 相關係數不受單位換算（乘正數）影響。
	- 由 x 預測 y 和由 y 預測 x 是兩條不同的迴歸直線。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3ebee100984f8112a954f8f1e377146e"/>　全國答對率 15%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f817e95f8c1c7d01bc2c6"/>　全國答對率 35%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f8151b4bdf9662e73dce5"/>　全國答對率 46%
</details>
