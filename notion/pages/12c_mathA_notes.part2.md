<details>
<summary>**機率與統計**</summary>
	<callout icon="💡">
		$`\text{期望值}=\sum(\text{值}\times\text{機率})`$；$`\text{條件機率}=\dfrac{\text{交集}}{\text{條件}}`$；迴歸直線與標準化分數是常考。
	</callout>
	**📌 必背**
	- 古典機率 $`P(A)=\dfrac{n(A)}{n(S)}`$，前提是每個樣本點出現的機會相等。
	- $`P(A\cup B)=P(A)+P(B)-P(A\cap B)`$；$`P(A')=1-P(A)`$。
	- 條件機率 $`P(B\mid A)=\dfrac{P(A\cap B)}{P(A)}`$；乘法原理 $`P(A\cap B)=P(A)\cdot P(B\mid A)`$。
	- A、B 獨立 ⇔ $`P(A\cap B)=P(A)\cdot P(B)`$。
	- 期望值 $`E=x_1p_1+x_2p_2+\cdots+x_np_n`$。
	- 資料 $`y=ax+b`$：平均 $`\mu_y=a\cdot\mu_x+b`$、標準差 $`\sigma_y=|a|\cdot\sigma_x`$；$`a>0`$ 時相關係數不變，$`a<0`$ 時變號。
	- 迴歸直線 $`y-\mu_y=r\cdot\dfrac{\sigma_y}{\sigma_x}\cdot(x-\mu_x)`$，一定通過 $`(\mu_x,\mu_y)`$（考卷附）。
	- 貝氏定理：$`P(A\mid B)=\dfrac{P(A)\cdot P(B\mid A)}{P(A)\cdot P(B\mid A)+P(A')\cdot P(B\mid A')}`$；分子是「A 發生而且得到 B」這條路徑的機率，分母是所有會得到 B 的路徑機率總和。
	- 標準差 $`\sigma=\sqrt{\dfrac{1}{n}\sum_{i=1}^{n}(x_i-\mu)^2}=\sqrt{\dfrac{1}{n}\sum_{i=1}^{n}x_i^2-\mu^2}`$（考卷附）；標準化 $`z=\dfrac{x-\mu}{\sigma}`$，標準化後的資料平均是 0、標準差是 1。
	- 相關係數 r 介於 $`-1`$ 和 1 之間，等於兩組資料標準化之後，對應乘積的平均（公式考卷附）。
	- 第 k 百分位數：資料由小到大排，算 $`n\times\dfrac{k}{100}`$；不是整數就取下一個整數的位置，是整數 m 就取第 m 和第 $`m+1`$ 個的平均。
	- 主觀機率也要符合機率的性質（每個事件的機率介於 0 和 1 之間，所有可能情形的機率和為 1）；客觀機率由大量資料的相對次數估計。
	**🧭 解題流程**
	1. 多階段的機率：畫樹狀圖，同一條路徑相乘，不同路徑相加。
	2. 已知結果反推原因：$`P(\text{原因}\mid\text{結果})=\dfrac{\text{這條路徑的機率}}{\text{所有得到這個結果的路徑機率總和}}`$。
	3. 「至少一次」：用 1 減去「一次都沒有」。
	**⚠️ 容易錯的地方**
	- 獨立和互斥不同：兩事件互斥、機率又都大於 0 時，一定不獨立。
	- 標準差不受「加減常數」影響，只受「乘除」影響。
	- 相關係數接近 0，只表示沒有「線性」關係。
	- 貝氏定理的分母要把所有會得到這個結果的情況都加進來，不能只算其中一條路徑。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81d09880c2ea37de2bc3"/>　全國答對率 16%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81e4a395c4ff05381c7d"/>　全國答對率 22%
	- <mention-page url="https://app.notion.com/p/3ebee100984f8194a4edd6ee7756347c"/>　全國答對率 35%
</details>
<details>
<summary>**排列組合**</summary>
	<callout icon="💡">
		先分類再計數，注意「相同結果」只算一次；綁在一起的排列先排區塊。
	</callout>
	**📌 必背**
	- 加法原理（分類，各類不重疊）；乘法原理（分步）。
	- n 個不同的東西取 k 個排列：$`\dfrac{n!}{(n-k)!}`$；取 k 個的組合：$`C(n,k)=\dfrac{n!}{k!(n-k)!}`$。
	- 有相同物的排列：$`\dfrac{n!}{p!\cdot q!\cdots}`$。
	- k 個位置、每個位置都有 m 種選擇：$`m^k`$ 種（重複排列）。
	- k 個相同的東西分給 n 個人（可以有人沒分到）：$`C(n+k-1,k)`$ 種（排 k 個東西和 $`n-1`$ 個隔板）。
	- 二項式定理：$`(a+b)^n`$ 展開式的第 $`k+1`$ 項是 $`C(n,k)\cdot a^{n-k}\cdot b^k`$。
	- 取捨原理（排容原理）：$`n(A\cup B)=n(A)+n(B)-n(A\cap B)`$；$`n(A\cup B\cup C)=n(A)+n(B)+n(C)-n(A\cap B)-n(B\cap C)-n(C\cap A)+n(A\cap B\cap C)`$。
	- 二項式係數：$`C(n,0)+C(n,1)+\cdots+C(n,n)=2^n`$；$`C(n,k)=C(n,n-k)`$。
	**🧭 解題流程**
	1. 先決定分類還是分步；有限制條件的先處理（指定位置、相鄰、不相鄰）。
	2. 相鄰：先綁成一塊一起排，塊內再排；不相鄰：先排其他的，再插入空隙。
	3. 「至少」的問題用補集：全部減去不符合的。
	**⚠️ 容易錯的地方**
	- 分組時組與組沒有分別（例如平均分成兩組），要除以組數的排列數，避免重複計算。
	- 「每人至少一個」先每人發一個，剩下的再用隔板法分。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3ebee100984f8194a4edd6ee7756347c"/>　全國答對率 35%
	- <mention-page url="https://app.notion.com/p/3ebee100984f81ec9148fe2ab2c04a0d"/>　全國答對率 44%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f816f8934d9befa3b9356"/>　全國答對率 56%
</details>
