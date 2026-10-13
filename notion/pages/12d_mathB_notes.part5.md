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
	**🧩 經典題型與解題技巧**
	先從題目的關鍵字認出是哪一型，再照那一型的做法解；點開可以看例題、解答和考過的題目。
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
	**⚠️ 容易錯的地方**
	- 標準差只受乘除影響，加減常數不會改變。
	- 相關係數不受單位換算（乘正數）影響。
	- 由 x 預測 y 和由 y 預測 x 是兩條不同的迴歸直線。
	**📝 代表題**（前兩週做過、全國答對率最低的題目）
	- <mention-page url="https://app.notion.com/p/3ebee100984f8112a954f8f1e377146e"/>　全國答對率 15%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f817e95f8c1c7d01bc2c6"/>　全國答對率 35%
	- <mention-page url="https://app.notion.com/p/3e9ee100984f8151b4bdf9662e73dce5"/>　全國答對率 46%
</details>
