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
	**🧩 經典題型與解題技巧**
	先從題目的關鍵字認出是哪一型，再照那一型的做法解；點開可以看例題、解答和考過的題目。
	<details>
	<summary>① 古典機率：樣本空間要「等可能」</summary>
		**🔍 看到**：擲骰子、擲硬幣、從袋中抽球、隨機排成一列、隨機選取。
		**🛠️ 做法**
		1. $`P(A)=\dfrac{n(A)}{n(S)}`$，前提是每個樣本點出現的機會相等。
		2. 同色的球也要當成不同的球來數，才會等可能；分子、分母要用同一種數法（都考慮順序，或都不考慮）。
		**✏️ 例題**：袋中有 3 顆紅球、2 顆白球，一次取出 2 顆，兩顆同色的機率是多少？
		**💡 解答**：$`n(S)=C(5,2)=10`$；同色：$`C(3,2)+C(2,2)=3+1=4`$。機率 $`=\dfrac{4}{10}=\dfrac{2}{5}`$。
		**⚠️ 小心**：擲兩顆骰子，點數和有 2～12 共 11 種，但它們不是等可能，不能說和為 7 的機率是 $`\dfrac{1}{11}`$；要用 36 種有順序的結果來算，答案是 $`\dfrac{6}{36}=\dfrac{1}{6}`$。
		**📝 考過的題目**
		- <mention-page url="https://app.notion.com/p/3ecee100984f81aea0ebc60ffa46a628"/>　全國答對率 39%
		- <mention-page url="https://app.notion.com/p/3e9ee100984f81e99cc2c578aaa7b5ac"/>　全國答對率 35%
		- <mention-page url="https://app.notion.com/p/3ecee100984f8108ab76f1c6493c5620"/>　全國答對率 61%
		- <mention-page url="https://app.notion.com/p/3ecee100984f81af806fce513f553532"/>　全國答對率 13%
	</details>
	<details>
	<summary>② 「至少一次」：1 減去一次都沒有</summary>
		**🔍 看到**：「至少一次」「至少一個」「至少有一個停車場有空位」。
		**🛠️ 做法**：$`P(\text{至少一次})=1-P(\text{一次都沒有})`$；各次獨立時，一次都沒有＝每一次都失敗的機率相乘。
		**✏️ 例題**：投籃命中率 0.4，投 3 次（各次獨立），至少進 1 球的機率是多少？
		**💡 解答**：3 次都沒進：$`0.6^3=0.216`$。至少進 1 球：$`1-0.216=0.784`$。
		**📝 考過的題目**
		- <mention-page url="https://app.notion.com/p/3e9ee100984f8121aa5cfb72cbe5ecc2"/>　全國答對率 44%
		- <mention-page url="https://app.notion.com/p/3ebee100984f813d89d0fdb290bb8f05"/>　全國答對率 44%
	</details>
	<details>
	<summary>③ 獨立事件：機率相乘</summary>
		**🔍 看到**：「互不影響」「各次獨立」「已知 A、B 獨立，求未知數」「判斷兩事件是否獨立」。
		**🛠️ 做法**
		1. A、B 獨立 ⇔ $`P(A\cap B)=P(A)\cdot P(B)`$；幾個獨立的事件同時發生，就把機率相乘。
		2. 判斷獨立或求未知數：分別算出 $`P(A)`$、$`P(B)`$、$`P(A\cap B)`$，代進去檢查或列方程式。
		**✏️ 例題**：擲一顆公正骰子，A：點數是偶數，B：點數是 3 的倍數。A、B 獨立嗎？
		**💡 解答**：$`P(A)=\dfrac{1}{2}`$、$`P(B)=\dfrac{1}{3}`$；$`A\cap B=\{6\}`$，$`P(A\cap B)=\dfrac{1}{6}=\dfrac{1}{2}\times\dfrac{1}{3}`$，所以 A、B 獨立。
		**⚠️ 小心**：獨立和互斥不同：兩事件互斥（不會同時發生）、機率又都大於 0 時，一定不獨立。
		**📝 考過的題目**
		- <mention-page url="https://app.notion.com/p/3e9ee100984f8132b325ece6b258ed26"/>　全國答對率 57%
		- <mention-page url="https://app.notion.com/p/3e9ee100984f81d6a393c17ebac873fa"/>　全國答對率 37%
		- <mention-page url="https://app.notion.com/p/3ebee100984f81928c96f56085e89492"/>　全國答對率 43%
	</details>
	<details>
	<summary>④ 重複試驗：恰好 k 次、第 n 次才達成</summary>
		**🔍 看到**：「擲 n 次恰有 k 次正面」「玩 n 次至少中 2 次」「擲到第 4 次才累積 3 個正面」。
		**🛠️ 做法**
		1. 每次成功的機率是 p、各次獨立：n 次中恰好 k 次成功的機率 $`=C(n,k)\,p^k(1-p)^{n-k}`$（選出哪 k 次成功，乘上每一條路徑的機率）。
		2. 「第 n 次才累積到 k 次成功」＝前 $`n-1`$ 次恰好 $`k-1`$ 次成功，而且第 n 次成功。
		**✏️ 例題**：投籃命中率 0.6，投 3 次恰好進 2 球的機率是多少？
		**💡 解答**：選出哪 2 次進球：$`C(3,2)=3`$ 種；每一種的機率是 $`0.6^2\times0.4=0.144`$。所求 $`=3\times0.144=0.432`$。
		**⚠️ 小心**：「擲硬幣到第 5 次才出現第 2 個正面」：前 4 次恰 1 個正面，而且第 5 次是正面，機率 $`=C(4,1)\left(\dfrac{1}{2}\right)^4\times\dfrac{1}{2}=\dfrac{1}{8}`$，不是 $`C(5,2)\left(\dfrac{1}{2}\right)^5`$。
		**📝 考過的題目**
		- <mention-page url="https://app.notion.com/p/3e9ee100984f81d09880c2ea37de2bc3"/>　全國答對率 16%
		- <mention-page url="https://app.notion.com/p/3ebee100984f813d89d0fdb290bb8f05"/>　全國答對率 44%
	</details>
	<details>
	<summary>⑤ 多階段的試驗：畫樹狀圖</summary>
		**🔍 看到**：前一次的結果會影響下一次（抽後不放回、和前一次同色的機率是 $`\dfrac{1}{3}`$、機器人每次往某個方向移動），或是先選袋子再抽球。
		**🛠️ 做法**
		1. 畫樹狀圖：同一條路徑的機率相乘，符合條件的路徑再相加。
		2. 步驟很多時找規律或對稱：地位相同的位置，機率一定相等。
		**✏️ 例題**：甲袋有 2 紅 1 白、乙袋有 1 紅 2 白。擲一枚硬幣，正面從甲袋、反面從乙袋取 1 球，取到紅球的機率是多少？
		**💡 解答**：正面→紅：$`\dfrac{1}{2}\times\dfrac{2}{3}=\dfrac{1}{3}`$；反面→紅：$`\dfrac{1}{2}\times\dfrac{1}{3}=\dfrac{1}{6}`$。相加 $`=\dfrac{1}{3}+\dfrac{1}{6}=\dfrac{1}{2}`$。
		**📝 考過的題目**
		- <mention-page url="https://app.notion.com/p/3ecee100984f8123bf9fc07cda273d52"/>　全國答對率 69%
		- <mention-page url="https://app.notion.com/p/3ebee100984f81e29161cceb4cb0dea1"/>　全國答對率 49%
	</details>
	<details>
	<summary>⑥ 條件機率：在「已知的事件」裡面數</summary>
		**🔍 看到**：「已知……，則……的機率」「在……的條件下」「……之中，……占多少比例」。
		**🛠️ 做法**
		1. $`P(B\mid A)=\dfrac{P(A\cap B)}{P(A)}`$；等可能時直接在 A 裡面數：$`P(B\mid A)=\dfrac{n(A\cap B)}{n(A)}`$。
		2. 分母是「已經知道發生了」的事件，不是全體。
		**✏️ 例題**：擲兩顆公正骰子，已知點數和為 8，至少一顆是 6 點的機率是多少？
		**💡 解答**：點數和為 8 的有 $`(2,6)`$、$`(3,5)`$、$`(4,4)`$、$`(5,3)`$、$`(6,2)`$ 共 5 種，其中有 6 點的 2 種。所求 $`=\dfrac{2}{5}`$。
		**📝 考過的題目**
		- <mention-page url="https://app.notion.com/p/3ebee100984f812e8c2de7422ac7e7fb"/>　全國答對率 83%
		- <mention-page url="https://app.notion.com/p/3e9ee100984f81d6a393c17ebac873fa"/>　全國答對率 37%
		- <mention-page url="https://app.notion.com/p/3ebee100984f81a3abb5db65d758d976"/>　全國答對率 23%
		- <mention-page url="https://app.notion.com/p/3ebee100984f81928c96f56085e89492"/>　全國答對率 43%
		- <mention-page url="https://app.notion.com/p/3ecee100984f81e39e52df1c0cbb6660"/>　全國答對率 23%
	</details>
	<details>
	<summary>⑦ 貝氏定理：已知結果，反推原因</summary>
		**🔍 看到**：題目給「原因 → 結果」的機率（例如染病的人驗出陽性的機率），問「結果 → 原因」（驗出陽性的人真的染病的機率）。
		**🛠️ 做法**
		1. 畫兩層的樹狀圖：第一層是原因（染病／沒染病），第二層是結果（陽性／陰性）。
		2. $`P(\text{原因}\mid\text{結果})=\dfrac{\text{這條路徑的機率}}{\text{所有得到這個結果的路徑機率總和}}`$。
		**✏️ 例題**：某病的盛行率是 1%。檢驗時，有病的人 90% 呈陽性，沒病的人 10% 呈陽性。某人呈陽性，他真的有病的機率是多少？
		**💡 解答**：有病而且陽性：$`0.01\times0.9=0.009`$；沒病而且陽性：$`0.99\times0.1=0.099`$。所求 $`=\dfrac{0.009}{0.009+0.099}=\dfrac{0.009}{0.108}=\dfrac{1}{12}`$。
		**⚠️ 小心**：沒病的人比有病的人多很多，所以陽性的人大多是「沒病卻驗出陽性」；分母一定要把所有會得到這個結果的路徑都加進來。
		**📝 考過的題目**
		- <mention-page url="https://app.notion.com/p/3e9ee100984f819c9c53ccf38ac9e3ee"/>　全國答對率 73%
		- <mention-page url="https://app.notion.com/p/3ebee100984f81acaf0ec8661b6406c9"/>　全國答對率 53%
		- <mention-page url="https://app.notion.com/p/3ecee100984f816b9d22f56115d49737"/>　全國答對率 52%
		- <mention-page url="https://app.notion.com/p/3ecee100984f8158978ac407c5d9a556"/>　全國答對率 81%
	</details>
	<details>
	<summary>⑧ 列聯表：設一個未知數，把表格填滿</summary>
		**🔍 看到**：兩種分類交叉（有無近視 × 有無蛀牙、考數A × 考數B），題目給比例，或說「占多數」「占少數」。
		**🛠️ 做法**
		1. 畫一個兩列兩行的表格（再加上總和），設其中一格（通常是兩者都有的那一格）為 x。
		2. 用每一列、每一行的總和，把其他格都寫成 x 的式子。
		3. 把條件翻成方程式或不等式；「A 之中 B 占多數」就是 $`\dfrac{n(A\cap B)}{n(A)}>\dfrac{1}{2}`$。
		**✏️ 例題**：全班 40 人，20 人戴眼鏡、15 人參加球隊，兩者都沒有的有 12 人。戴眼鏡的人之中，參加球隊的占多少比例？
		**💡 解答**：設兩者都有的是 x 人：$`20+15-x=40-12`$ ⇒ $`x=7`$。所求 $`=\dfrac{7}{20}`$。
		**📝 考過的題目**
		- <mention-page url="https://app.notion.com/p/3e9ee100984f8151a00cd7d71344c3ab"/>　全國答對率 24%
		- <mention-page url="https://app.notion.com/p/3ebee100984f81a3abb5db65d758d976"/>　全國答對率 23%
		- <mention-page url="https://app.notion.com/p/3e9ee100984f8132b325ece6b258ed26"/>　全國答對率 57%
	</details>
	<details>
	<summary>⑨ 期望值：每個值乘上機率，再相加</summary>
		**🔍 看到**：「期望值」「平均可以得到」「平均要花多少錢」「平均抽到幾張」。
		**🛠️ 做法**
		1. 列出所有可能的值和它們的機率（機率加起來要等於 1），$`E=x_1p_1+x_2p_2+\cdots+x_np_n`$。
		2. 可以拆開算再相加：一次十連抽的期望張數 $`=9\times(\text{前九張每張的機率})+(\text{第十張的機率})`$；同樣的遊戲玩 n 次，期望值乘以 n。
		**✏️ 例題**：擲一顆公正骰子，擲出 6 點得 60 元、5 點得 30 元，其他點數得 0 元。期望值是多少？
		**💡 解答**：$`E=60\times\dfrac{1}{6}+30\times\dfrac{1}{6}+0\times\dfrac{4}{6}=10+5=15`$（元）。
		**📝 考過的題目**
		- <mention-page url="https://app.notion.com/p/3e9ee100984f815d8a6fc7fd79a65289"/>　全國答對率 84%
		- <mention-page url="https://app.notion.com/p/3e9ee100984f81d09880c2ea37de2bc3"/>　全國答對率 16%
		- <mention-page url="https://app.notion.com/p/3ebee100984f814faad9dcf2b1a5a640"/>　全國答對率 48%
		- <mention-page url="https://app.notion.com/p/3ecee100984f81d68325e589f5456239"/>　全國答對率 46%
		- <mention-page url="https://app.notion.com/p/3ebee100984f819fa3faf9fe22599261"/>　全國答對率 35%
	</details>
	<details>
	<summary>⑩ 抽後不放回：和順序無關，知道結果就看剩下的</summary>
		**🔍 看到**：「抽後不放回」「依序抽」「第 101 號抽中的機率」「前面的人已經抽走……」。
		**🛠️ 做法**
		1. 不知道前面的人抽到什麼時，每一個順位抽中的機率都一樣（抽籤不分先後）。
		2. 已經知道前面抽出的結果時，只看剩下的籤重新算。
		**✏️ 例題**：10 支籤中有 2 支有獎，10 人依序各抽 1 支、抽後不放回。第 3 個人抽中的機率是多少？如果已知前 2 人都沒抽中呢？
		**💡 解答**：不知道前面的結果時，第 3 個人和第 1 個人一樣，機率 $`=\dfrac{2}{10}=\dfrac{1}{5}`$。已知前 2 人都沒中：剩下 8 支、其中 2 支有獎，機率 $`=\dfrac{2}{8}=\dfrac{1}{4}`$。
		**📝 考過的題目**
		- <mention-page url="https://app.notion.com/p/3ebee100984f814faad9dcf2b1a5a640"/>　全國答對率 48%
	</details>
	**⚠️ 容易錯的地方**
	- 「A 之中有多少比例是 B」是條件機率，分母是 A，不是全體。
	- 獨立和互斥不同。
	- 貝氏定理的分母要把所有會得到這個結果的情況都加進來，不能只算其中一條路徑。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3ebee100984f81a3abb5db65d758d976"/>　全國答對率 23%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f8151a00cd7d71344c3ab"/>　全國答對率 24%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81e99cc2c578aaa7b5ac"/>　全國答對率 35%
</details>
