# AK–HDPST v17.0.1 — AK高次元射影構造理論

> **AK-OS v1.0.1：高次元数学探索のための「オペレーティングシステム（Operating System）」**  
> **Core（中核）**：体上の 1 次元・構成的パーシステンス（constructible 1D persistence）における証明済み範囲  
> **[Spec]（仕様）**：監査可能な、打ち切り後（post-truncation）の非膨張（non-expansive）拡張・探索ポリシー

本リポジトリは **AK–HDPST v17.0.1** を収録します。本プロジェクトは、ナビエ–ストークス、BSD、リーマン予想、FLT 等の「大問題の解決器」を主張するものではありません。代わりに、**明確な範囲（Scope）・予算（δ）・監査成果物（Artifacts）** を備えた **証明志向の探索OS（AK-OS）** として位置づけます。

付随プロジェクト **AK_AP（Arithmetic Programs）v1.0.1** は、同じOSの枠組みを用い、算術モジュライ空間上での **閉世界キャリブレーション（closed-world calibration）** を実施します。既知定理を **外部入力（boundary inputs）** として採用し、OS の整合性と監査性を検証します。

**強い保証（Strong guarantees）は Core 範囲に厳密に限定** されます。Core 以外の要素はすべて **[Spec]** として明示し、監査対象として扱います。

---

## このリリースに含まれるファイル構造

```text
.
├─ OLD/                                  # 戒めとしての旧版アーカイブ（陳腐化・過剰主張を含み得る）
│  └─ ...                                # 過去スナップショット（v1.x–v16.x）
├─ AK–HDPST_v17.0.1/
│  ├─ AK_HPDST_v17.0.1.tex               # XeLaTeX 原稿（本文）
│  └─ AK_HPDST_v17.0.1.pdf               # コンパイルPDF（本文）
└─ AK–Arithmetic_Programs_v1.0.1/
   ├─ AK–Arithmetic Programs v1.0.1.tex  # XeLaTeX 原稿（付属：算術プログラム）
   └─ AK–Arithmetic Programs v1.0.1.pdf  # コンパイルPDF（付属）
```

---

## AK-OS v1.0.1 マニフェスト

### これは何か

- **ではない**：大予想（ナビエ–ストークス／BSD／RH／FLT／ラングランズ等）の証明主張。  
- **である**：以下を中核部品とする **探索のためのモジュラーOS**。
  - 正確な打ち切り作用 `T_tau`（「バー削除」）
  - フィルター付きリフト `C_tau`（filtered quasi-isomorphism（f.q.i.）まで）
  - **δ台帳（δ-ledger）**：誤差・非可換・モデル差分の予算管理（alg / disc / meas）
  - **塔診断** `(mu_collapse, nu_collapse)`：極限でのみ現れる不可視の破綻（Type IV）検出
  - **窓（window）ごとのゲート**（B–Gate⁺ / Overlap Gate）— すべて **打ち切り後** に評価
  - 探索レイヤ **HDPS**（High-Dimensional Projection Search）— **[Spec]**：妥当性地図（Map of Validity）を構築

### Core と [Spec] の分離（v17.0.1 規約）

- **Core（中核：証明済み／形式化候補）**
  - 体 `k` 上の **1パラメータ・構成的パーシステンス**
  - 正確な打ち切り `T_tau`：長さ `<= tau` のバーを削除する反射的局所化、冪等、interleaving 距離で 1-Lipschitz
  - フィルター付きリフト `C_tau`（f.q.i.まで）と整合：
    - `P_i(C_tau F) ≅ T_tau(P_i F)`（パーシステンス層での同型）
  - 一方向ブリッジ（`D^b(k-mod)` において、振幅 `<=1` かつ t-exact 実現の下）：
    - `PH1(F)=0  ⇒  Ext^1(R(F), k)=0`
  - **塔診断** `(mu_collapse, nu_collapse)` を **打ち切り後** に定義し、Type IV（不可視欠陥）を検出
  - 窓（window）単位のゲート（B–Gate⁺）と重なり整合（Overlap Gate）
  - 予算（δ）と監査成果物に基づく運用規約（run manifest / artifacts / checksums）

- **[Spec]（仕様：監査可能だが仮定・実装依存）**
  - 分野固有の実現（算術／PDE／フカヤ／ラングランズ等）— 必ず Core のガード下
  - HDPS：Terrain Cells、Hunter / Mapper / Lifter、妥当性地図
  - PF/BC（射影公式／基底変換）比較器（after-collapse）、Mirror / Transfer、A/B ソフト可換
  - 定量ヒューリスティクスと探索戦略（すべて δ台帳で監査）

**原則**：[Spec] はすべて「打ち切り後に非膨張（post-truncation non-expansive）」であること（本プロジェクトの意味で）を要求し、δ台帳と塔診断で監査可能でなければなりません。

---

## v17.0.1 の要点（v17.0 からの文書・監査パッチ）

v17.0.1 は主として **監査可能性と境界明確化** のためのパッチです（Core の射程拡張ではありません）。

- 参照・ラベル衛生：重複ラベル、未解決参照、誤参照の解消
- Core / [Spec] の明示：proof sketch の [Spec] 明記、宣言化、誤読を防ぐ文言統一
- 「標準事実」の最小文献アンカー：飛躍判定を容易にする
- Type IV 診断の表現を正規化：`DiagZero` を中核の合否表現として統一

---

## Core：基本部品（v17.0.1）

### 1) 打ち切り `T_tau` とリフト `C_tau`

- `T_tau`：バー長 `<= tau` を削除する正確打ち切り（反射的局所化）
- `C_tau`：チェイン層でのリフト（f.q.i.まで）
- 整合条件（パーシステンス層）：
  - `P_i(C_tau F) ≅ T_tau(P_i F)`

### 2) 一方向ブリッジ `PH1 ⇒ Ext1`（Core）

Core が保持するブリッジは **一方向のみ** です。

- 条件：`D^b(k-mod)` 上、t-exact 実現、振幅 `<= 1`（amplitude <= 1）
- 結論：`PH1(F)=0  ⇒  Ext^1(R(F), k)=0`
- 注意：**逆向き（Ext1 ⇒ PH1）は大域では主張しない**。局所的・条件付きの逆向きは [Spec] として明示する（例：E1-degenerate window 等）。

### 3) 塔診断 `(mu_collapse, nu_collapse)` と `DiagZero`

v17.0.1 は Type IV（不可視欠陥）を塔診断で扱います。

- `(mu_collapse, nu_collapse)`：打ち切り後の比較写像（比較極限）から導く核／余核の診断量
- `DiagZero := (mu_collapse, nu_collapse) = (0,0)`
  - `DiagZero` は「尾部同型（tail isomorphism）」「不可視欠陥なし」の正規表現として使用

### 4) B–Gate⁺（窓単位・打ち切り後ゲート：Core）

右開窓 `W=[u,u')` としきい値 `tau` に対し、**B–Gate⁺ が合格（pass）** するための中核条件：

1. `PH1(C_tau F | W) = 0`
2. `Ext^1(R(C_tau F | W), k) = 0`（適格性：振幅 `<=1` 等が成立する範囲のみ）
3. `DiagZero`（つまり `(mu_collapse, nu_collapse)=(0,0)`）
4. 予算条件：`gap_tau > sum_delta`（δ台帳の合算に対して安全余裕がある）

B–Gate⁺ は **「崩壊契約（collapse contract）」** の実体であり、Core の合否判定はすべてこの規約に従います。

### 5) Overlap Gate（重なり整合ゲート：Core）

窓 `W_a` と `W_b` の重なり上で、打ち切り後に整合性を強制します：

- 重なり上の距離（interleaving 等） `<= sum_delta_ab`
- 予算余裕 `gap_tau > sum_delta_ab`
- `DiagZero`

目的：窓ごとの証明片（証明・監査・成果物）を貼り合わせ、整合した全体像へ昇格させる。

---

## AK_AP（Arithmetic Programs）v1.0.1：閉世界キャリブレーション（付属）

AK_AP は、AK-OS の運用を **真偽が既知の世界** で校正するための付属プログラムです。

- `M_Weil`：有限体 Weil world（Deligne 系結果を外部入力として扱う）
- `M_FLT`：FLT world（Frey データ／Wiles–Taylor 系結果を外部入力として扱う）

重要：AK_AP は **新証明を主張しない**。既知定理と整合する形で、OS のゲート／台帳／診断が「正しく振る舞う」ことを確認するための **閉世界検査** である。

### v17.0.1 との整合ルール（必須）

- **B–Gate⁺ は v17.0.1 Core 定義を専用** とする（窓・打ち切り後・予算・`DiagZero`）。
- 算術固有の計測（欠陥ポテンシャル等）は
  - **[Spec] 計測** または **プレゲート（sanity check）** として扱う
  - δ台帳に記録する
  - B–Gate⁺ を暗黙に再定義しない

---

## 本プロジェクトの読み方

- **数学として**：定理級の主張は Core のみ。[Spec] は監査可能だが仮定・実装依存。
- **ソフトウェア設計として**：打ち切り優先（truncation-first）の安定性、予算管理、失敗診断を統合した探索OS。
- **AI×人間協働として**：成果を再実行・批判可能にする（run manifest＋成果物＋台帳）ことを最優先する。

---

## 実行プロトコル（概念）

比較・判定はすべて打ち切り後の順序で実施します：

```text
t  →  persistence P_i  →  truncation T_tau  →  compare / audit / gate / map_validity
```

---

## インストール（例示：実装リポジトリ依存）

```bash
git clone https://github.com/your-org/ak-hdpst.git
cd ak-hdpst
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[all]"
```

> 注意：実際のパッケージ構成・コマンド名・extras はリポジトリ実装に依存します。  
> 本 README は OS と監査契約を説明するもので、コード骨格は環境により異なり得ます。

---

## クイックスタート（例示）

### 最小CLI実行

```bash
# run 設定（例）
cp examples/v17.0.1/minimal/run.yaml ./run.yaml

# 窓ごとの after-truncation パイプラインを実行
akhdpst run run.yaml

# ゲート判定、塔診断、δ台帳を窓単位で確認
akhdpst audit out/artifacts --by-window
```

### 最小 Python API（例示）

```python
from akhdpst.core import T_tau, C_tau
from akhdpst.gate import b_gate_plus
from akhdpst.tower import audit_tower

F = ...   # filtered object / persistence を読み込み
tau = 0.15
W = (0.0, 0.5)  # 右開窓を便宜上ペアで表現

# パーシステンス層で打ち切り
P1_trunc = T_tau(F.persistence(1), tau)

# フィルター付きリフト（f.q.i.まで）
F_trunc = C_tau(F, tau)

# 塔診断（打ち切り後）
mu, nu = audit_tower(tower=[...], tau=tau, degree=1)

# ゲート判定（窓単位）
ok = b_gate_plus(
    F=F,
    window=W,
    tau=tau,
    mu=mu,
    nu=nu,
    gap_tau=0.03,
    sum_delta=0.011,
)
```

---

## 設定（`run.yaml`）— v17.0.1 の要点（例示）

```yaml
meta:
  name: "demo-v17.0.1"
  seed: 1337
  version: "17.0.1"
  author: "your-name"

data:
  input: "data/example.h5"
  backend: "bars"       # bars | chain
  degrees: [0, 1]

windows:
  - label: "w0"
    range: [0.0, 0.5)   # 右開；MECE；被覆は監査対象
  - label: "w1"
    range: [0.5, 1.0)

truncation:
  tau: 0.15
  lift: "C_tau"
  reflector: "T_tau"

gate:
  require:
    PH1_zero: true
    Ext1_zero: true         # 適格（振幅<=1 等）が成立する範囲のみ使用
    DiagZero: true          # (mu_collapse, nu_collapse) = (0,0)
    gap_tau_gt_sum_delta: true
  safety_margin:
    gap_tau: 0.03

audit:
  outputs: ["bars", "ledger", "tower", "gate", "checksums"]
  checksums: "sha256"

output:
  dir: "out/artifacts"
  overwrite: false
```

---

## 監査成果物（概念）

```text
out/artifacts/
  bars/
    w0_deg1_trunc.json
    w1_deg1_trunc.json
  ledger/
    ledger_w0.json
    ledger_w1.json
  tower/
    phi_maps_w0_deg1.json     # 比較写像、(mu,nu)、tail フラグ等
  gate/
    gate_w0.json
    gate_w1.json
  run.yaml
  audit_summary.json
  checksums.txt
```

- `bars/`：窓×次数ごとの打ち切りバーコード
- `ledger/`：δ台帳（alg / disc / meas）
- `tower/`：比較写像と塔診断 `(mu_collapse, nu_collapse)`、tail/同型フラグ
- `gate/`：B–Gate⁺、必要なら Overlap Gate の結果
- `audit_summary.json`：窓横断の集計
- `checksums.txt`：再現性のための SHA256

---

## 更新ポリシー（打ち切り後）

単調性／安定性の主張はすべて **`T_tau` 適用後** に限定して述べます。

| 更新種別        | 例（例示）                                                     | 保証（`T_tau` 後）                                      |
|----------------|----------------------------------------------------------------|---------------------------------------------------------|
| 削除型         | 制約追加、保守的収縮、制御平均化                              | 選択した打ち切り後指標に対して単調非増加               |
| ε-継続         | interleaving 境界の下での小さなホモトピー                     | 1-Lipschitz 安定；ε を δ台帳へ記録                      |
| 包含型         | セル追加、領域拡大                                             | 安定性のみ（非膨張）；単調性は要求しない               |

注意：実現後のスペクトル指標は f.q.i. 不変量ではないため、v17.0.1 ではポリシー固定と予算化を必須とし、逸脱はログ化します。

---

## コントリビューション（方針）

- ドキュメント／コードとも **Core vs [Spec] を明示** すること。
- [Spec] は必ず：
  - （該当する場合）打ち切り後の非膨張テストを持ち、
  - δ台帳への記録を行うこと。
- 最小再現例（成果物＋チェックサム）を優先すること。

---

## 引用（テンプレート）

```text
AK–HDPST v17.0.1 / AK-OS v1.0.1:
AK高次元射影構造理論と崩壊ベース探索のためのOS。

Authors: Atsushi Kobayashi, et al.
Year: 2025
Repository / archive:（URL または DOI を記載）
```

---

## ライセンス

MIT（`LICENSE` 参照）。
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18029366.svg)](https://doi.org/10.5281/zenodo.18029366)
---

## 用語チートシート

- **1D構成的パーシステンス**：有限の臨界集合、窓内で点wise有限次元。
- **`T_tau`**：長さ `<= tau` のバーを削除する正確打ち切り；冪等；1-Lipschitz。
- **`C_tau`**：`T_tau` のフィルター付きリフト（f.q.i.まで）；`P_i(C_tau F) ≅ T_tau(P_i F)`。
- **`DiagZero`**：`(mu_collapse, nu_collapse)=(0,0)`；窓における「尾部障害なし／Type IV なし」。
- **B–Gate⁺（Core）**：窓ごとの after-collapse ゲート：
  - `PH1=0`
  - `Ext^1=0`（適格：振幅<=1 範囲）
  - `DiagZero`
  - 予算余裕 `gap_tau > sum_delta`
- **Overlap Gate（Core）**：重なり窓の整合ゲート（距離境界＋予算＋`DiagZero`）。
- **`(mu_collapse, nu_collapse)`**：打ち切り後の比較写像から導く塔診断；非ゼロは Type IV の信号。
- **HDPS（[Spec]）**：Core ガード下で妥当性地図（`Valid` / `Obstructed` / `Unknown`）を構築する探索レイヤ。
- **δ台帳（δ-ledger）**：アルゴリズム差、離散化誤差、計測誤差の予算管理ログ。
