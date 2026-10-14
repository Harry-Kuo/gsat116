<details>
<summary>⑧ 兩平面的夾角、三垂線定理</summary>
	**🔍 看到**：四面體、積木，問兩平面的夾角或垂直關係。
	**🛠️ 做法**
	1. 兩平面的夾角用法向量算最穩：$`\cos\theta=\dfrac{|\overrightarrow{n_1}\cdot\overrightarrow{n_2}|}{|\overrightarrow{n_1}||\overrightarrow{n_2}|}`$（取銳角）。
	2. 圖形容易看出來時，在兩個平面上各作一條垂直交線的直線（交在同一點），兩線的夾角就是兩面角。
	3. 三垂線定理：$`\overline{PA}`$ 垂直平面 E 於 A，E 上的直線 L 垂直 $`\overline{AB}`$ 於 B，則 $`\overline{PB}\perp L`$。
	**✏️ 例題**：求平面 $`x+y=1`$ 和平面 $`y+z=2`$ 的夾角（取銳角）。
	**💡 解答**：法向量 $`(1,1,0)`$、$`(0,1,1)`$：$`\cos\theta=\dfrac{|0+1+0|}{\sqrt{2}\times\sqrt{2}}=\dfrac{1}{2}`$，夾角是 $`60^{\circ}`$。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3ecee100984f81bda13efc28e56fb6f2"/>　全國答對率 64%
	- <mention-page url="https://app.notion.com/p/3ecee100984f81a9be12f8f4ce63af2c"/>　全國答對率 38%
</details>
### 機率
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
### 數據分析
<details>
<summary>① 百分位數、中位數：先算是第幾個</summary>
	**🔍 看到**：「第 k 百分位數」「中位數」「四分位數」，資料用人數表或次數分配表給。
	**🛠️ 做法**
	1. 資料由小到大排好，算 $`n\times\dfrac{k}{100}`$：不是整數就取下一個整數那一個；是整數 m 就取第 m 個和第 $`m+1`$ 個的平均。
	2. 用人數表時，一路累加人數，看第幾個落在哪一組。
	3. 只有部分資料加分時，要重新確認排序，注意加分範圍的邊界。
	**✏️ 例題**：30 筆資料由小到大排好，第 25 百分位數、中位數各是第幾筆？
	**💡 解答**：$`30\times\dfrac{25}{100}=7.5`$，不是整數，取第 8 筆。$`30\times\dfrac{50}{100}=15`$，是整數，取第 15、16 筆的平均。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81819f80d7df87db6ea2"/>　全國答對率 58%
	- <mention-page url="https://app.notion.com/p/3ebee100984f81aaad5fcdffb7b37f2f"/>　全國答對率 70%
	- <mention-page url="https://app.notion.com/p/3ebee100984f8194a4edd6ee7756347c"/>　全國答對率 35%
</details>
<details>
<summary>② 資料一起乘、一起加：線性變換</summary>
	**🔍 看到**：「每人的分數乘 0.8 再加 20 分」「單位換算」「T 分數」「每個值都是另一組的 0.5 倍」。
	**🛠️ 做法**
	1. 平均數、中位數、百分位數都跟著變：$`\mu_y=a\mu_x+b`$。
	2. 標準差只受乘法影響：$`\sigma_y=|a|\sigma_x`$，加減常數不會改變標準差。
	3. 相關係數：$`a>0`$ 不變，$`a<0`$ 變號；迴歸直線的斜率要用 $`r\cdot\dfrac{\sigma_y}{\sigma_x}`$ 重新算。
	**✏️ 例題**：某班數學平均 50 分、標準差 10 分。每個人的分數 x 都改成 $`1.2x+10`$，新的平均和標準差是多少？
	**💡 解答**：平均 $`=1.2\times50+10=70`$ 分；標準差 $`=1.2\times10=12`$ 分（加 10 分不影響標準差）。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3ecee100984f8112b82ad879ed506ec8"/>　全國答對率 46%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f812ea705fb18286fc721"/>　全國答對率 44%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f817e95f8c1c7d01bc2c6"/>　全國答對率 35%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81e4a395c4ff05381c7d"/>　全國答對率 22%
</details>
<details>
<summary>③ 標準化：比較在不同組裡的位置</summary>
	**🔍 看到**：「標準化」「標準分數」「T 分數」「數學和英文，哪一科的表現比較好」。
	**🛠️ 做法**
	1. $`z=\dfrac{x-\mu}{\sigma}`$：z 越大，在自己那一組的位置越前面；標準化後的資料，平均是 0、標準差是 1。
	2. T 分數 $`=50+10z`$。
	**✏️ 例題**：數學平均 60 分、標準差 12 分，某生考 72 分；英文平均 70 分、標準差 5 分，他考 78 分。哪一科的相對表現比較好？
	**💡 解答**：數學 $`z=\dfrac{72-60}{12}=1`$；英文 $`z=\dfrac{78-70}{5}=1.6`$。英文的 z 比較大，相對表現比較好。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3e9ee100984f812ea705fb18286fc721"/>　全國答對率 44%
</details>
<details>
<summary>④ 標準差的意義：只知道平均和標準差能推出什麼</summary>
	**🔍 看到**：「標準差」「每一筆都在某個範圍內」「全距」「每一次都一樣嗎」。
	**🛠️ 做法**
	1. 標準差是每筆資料和平均的差，平方後取平均再開根號，表示資料分散的程度。
	2. 如果每筆資料都在 $`\mu-d`$ 到 $`\mu+d`$ 之間，標準差一定 $`\le d`$；所以標準差比 d 大，就一定有資料落在這個範圍外。
	3. 只知道平均和標準差，不能推出全距、中位數或某一筆資料的值。
	**✏️ 例題**：資料 2、4、6、8 的平均和標準差各是多少？
	**💡 解答**：平均 $`=5`$；和平均的差是 $`-3`$、$`-1`$、1、3，平方的平均 $`=\dfrac{9+1+1+9}{4}=5`$，標準差 $`=\sqrt{5}`$。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3e9ee100984f8151b4bdf9662e73dce5"/>　全國答對率 46%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f817e95f8c1c7d01bc2c6"/>　全國答對率 35%
</details>
<details>
<summary>⑤ 迴歸直線：一定通過平均點</summary>
	**🔍 看到**：「迴歸直線」「最適直線」「用 x 預測 y」「由迴歸直線反推標準差」。
	**🛠️ 做法**
	1. $`y-\mu_y=r\cdot\dfrac{\sigma_y}{\sigma_x}(x-\mu_x)`$，一定通過 $`(\mu_x,\mu_y)`$；x 代平均數，預測出來的就是 y 的平均數。
	2. 已知斜率、r 和 $`\sigma_x`$，可以反推 $`\sigma_y=\dfrac{\text{斜率}\times\sigma_x}{r}`$。
	3. 用 x 預測 y、用 y 預測 x，是兩條不同的直線。
	**✏️ 例題**：$`\mu_x=10`$、$`\mu_y=50`$、$`\sigma_x=2`$、$`\sigma_y=6`$、$`r=0.5`$。寫出 y 對 x 的迴歸直線，並預測 $`x=12`$ 時的 y。
	**💡 解答**：斜率 $`=0.5\times\dfrac{6}{2}=1.5`$，迴歸直線是 $`y-50=1.5(x-10)`$。$`x=12`$ 時 $`y=50+1.5\times2=53`$。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3ebee100984f8141b93ec620318a8082"/>　全國答對率 36%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f817e95f8c1c7d01bc2c6"/>　全國答對率 35%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f81e4a395c4ff05381c7d"/>　全國答對率 22%
</details>
<details>
<summary>⑥ 相關係數：看散布圖，換單位不影響</summary>
	**🔍 看到**：「散布圖」「相關係數」「完全正相關」「換了單位以後」。
	**🛠️ 做法**
	1. 點越集中在一條直線附近，$`|r|`$ 越接近 1；由左下往右上 $`r>0`$，由左上往右下 $`r<0`$。
	2. 一組資料是另一組乘上正數再加常數 ⇒ $`r=1`$（完全正相關）。
	3. 兩組資料各自乘正數、加常數，r 都不變；r 接近 0 只表示沒有「線性」關係。
	**✏️ 例題**：身高的單位從公分換成公尺，身高和體重的相關係數會改變嗎？
	**💡 解答**：不會。公分換成公尺是每個身高都乘 0.01（正數），相關係數不變。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3e9ee100984f817e95f8c1c7d01bc2c6"/>　全國答對率 35%
	- <mention-page url="https://app.notion.com/p/3ecee100984f81eb8383fae5505f7083"/>　全國答對率 12%
</details>
<details>
<summary>⑦ 取對數後成一直線：還原成指數關係</summary>
	**🔍 看到**：「把 t 取對數後畫散布圖」「點 $`(s,\log t)`$ 大致在一條直線上」。
	**🛠️ 做法**：從圖讀出直線 $`\log t=ms+k`$，再還原：$`t=10^{ms+k}=10^k\cdot(10^m)^s`$；選項寫成 $`t^2=10^s`$ 這類形式時，兩邊取對數比對斜率。
	**✏️ 例題**：點 $`(s,\log t)`$ 大致落在通過 $`(0,1)`$、$`(1,3)`$ 的直線上，t 和 s 的關係是什麼？
	**💡 解答**：直線是 $`\log t=2s+1`$，所以 $`t=10^{2s+1}=10\times100^s`$。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3ebee100984f815a835ae7bd241deb3a"/>　全國答對率 51%
</details>
<details>
<summary>⑧ 讀表格、讀圖：先看單位和定義</summary>
	**🔍 看到**：統計表、次數分配表、長條圖，或是兩組資料合併成一組。
	**🛠️ 做法**
	1. 先確認單位（千人、萬人、百分比）和每一欄的意思，再判斷選項。
	2. 判斷「可能／不可能」：找一個符合條件的例子，或用總數、最大值、最小值的限制排除。
	**📝 考過的題目**
	- <mention-page url="https://app.notion.com/p/3ebee100984f8112a954f8f1e377146e"/>　全國答對率 15%
	- <mention-page url="https://app.notion.com/p/3ecee100984f81708df7f5ee7ed91fd9"/>　全國答對率 76%
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
