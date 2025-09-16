# AK–HDPST v16.0 — AK 高次元射影構造理論

高次元射影と制御された障害除去による関手的崩壊のための、二層・監査可能な証明フレームワーク。

- Core: 体上の1次元構成可能パーシステンスにおける機械検証可能な主張
- [Spec]: 切り詰め後に非膨張で安全な拡張（明示的・監査可能な仮定付き）

リポジトリの状態: 参照API・実行プロトコル・監査成果物を備えた研究用フレームワーク。強い保証は以下の Core 範囲に限定。

シンプルなフロー（測定順序）:
t  →  パーシステンス `P_i`  →  切り詰め `T_tau`  →  比較/監査
```

---

## v16.0 の新機能（v15.0 比）

- ウィンドウ化インフラ
  - Overlap Gate の強化（ウィンドウ化、崩壊後のグルーイング；オーバーラップ上の Čech–Ext¹ 無サイクル性；オーバーラップ上の δ 予算）
  - Window Stack（WinFib）：グロタンディーク・ファイブレーション風のブックキーピング足場
  - 安定性バンド：τ スイープとタワー監査のためのバンド検知；バンドに基づく堅牢なゲーティング
- セーフティと監査
  - ウィンドウ毎の B–Gate⁺ 安全マージン；Restart/Summability により証明書を大域的に貼り合わせ
  - δ 台帳の標準化と層化：アルゴリズム（Mirror–Collapse と A/B 残差を含む）、離散化、測定
  - 標準実行スキーマのフィールド：overlap_checks、spectral_policy（昇順；op/fro ノルム）、spectral_bounds、Lambda_len 監査、phi_iso_tail
- 診断と比較器
  - タワー診断（μ, ν）：切り詰め後の核/余核を形式化；不可視な Type IV 障害（有限段は OK、極限で崩れる）
  - PF/BC 崩壊後比較器（`T_tau` 適用後のウィンドウ上で射影公式/基底変換を評価）
  - 非入れ子トーション反射子に対する A/B ソフト可換ポリシー（加法的 Δ_comm 予算）
- 量的構造
  - 長さスペクトル作用素 `Lambda_len`（ウィンドウ付きクリップド長多重集合；切り詰め後の同型不変）
  - トロピカル/弱群崩壊ツール [Spec]：ウィンドウ付きエネルギー優越の収縮；バー基底上の群作用プロキシ
- ドメイン・フック [Spec]
  - Fukaya 作用フィルトレーション・パイプライン（継続 1-Lipschitz；ストップ追加は削除型；(μ, ν) によるタワー安定性）
  - 三層（Gal → Trans → Funct）のラングランズ風ゲート（ウィンドウ化レイヤ核と PF/BC 監査）
- 形式テストスイート（IMRN/AiM 対応）
  - T14 Overlap Gate グルーイング；T15 長さスペクトル監査；T7 飽和ゲート；T10 A/B テスト；T13 δ 予算加法性；T11 Restart/Summability

---

## 目次

- 概要
- 対象範囲と保証
- Core（可証）と [Spec]（監査可能）の内容
- 概念とコンポーネント
- インストール
- クイックスタート（CLI と Python API）
- 設定（`run.yaml`）
- ワークフローと例
- 更新ポリシー（許可される操作）
- 監査と成果物
- コマンドリファレンス
- Python API リファレンス（抜粋）
- ロードマップ
- コントリビュート
- 引用と参考文献
- ライセンス
- 付録：用語チートシート

---

## 概要

AK–HDPST v16.0 は、以下を明確に分離する証明指向フレームワークです。
- Core: 体上の構成可能 1D パーシステンスにおける、証明済みで機械検証可能な保証
- [Spec]: 切り詰め後に非膨張で、完全に監査される運用拡張（δ 台帳、オーバーラップ・グルーイング、安定性バンド）

すべての比較は、ウィンドウ化された単層プロトコル（切り詰め後）に従います:
t → パーシステンス `P_i` → `T_tau` → 比較/監査

これにより、測度的安定性、透明な失敗モード（例：Type IV）、再現可能なパイプラインが保証されます。

---

## 対象範囲と保証（Core）

強い主張は以下に限定:
- 一パラメータ、体 k 上の構成可能パーシステンス
- 正確な Serre 反射子 `T_tau`（長さ ≤ τ のバーを削除）；正確・冪等・1‑Lipschitz（インタリービング/ボトルネック）
- フィルタ付き持ち上げ `C_tau`（フィルタ付き疑似同型（f.q.i.）まで）で `P_i(C_tau F) ≅ T_tau(P_i F)`
- 片方向ブリッジのみ：t‑正確・振幅 ≤ 1 の実現の下で `PH1(F)=0 ⇒ Ext1(R(F), k)=0`（逆は主張しない）
- 切り詰め後の比較写像からのタワー診断 `(mu, nu)`；不可視な極限失敗（Type IV）を検知
- ウィンドウ化ゲーティング：B–Gate⁺（PH1/Ext1/(μ,ν)/セーフティマージン）と Overlap Gate（崩壊後の局所から大域）

主張しないこと:
- `PH1 ⇔ Ext1` の大域同値
- BSD、RH、Navier–Stokes などへの言及（[Spec] レベルのプロトコルを超えない）
- 構成可能性の範囲外や多パラメータへの保証

---

## Core と [Spec] の内容

Core（可証）:
- 正確な切り詰め `T_tau` と 1‑Lipschitz 安定性
- フィルタ付き持ち上げ `C_tau`（f.q.i. まで）
- 片方向 PH1 ⇒ Ext1（振幅 ≤ 1）
- タワー診断 `(mu,nu)`、τ スイープ、安定性バンド
- B–Gate⁺（安全マージン）と Overlap Gate（オーバーラップ上の Čech–Ext¹）
- Restart/Summability によるウィンドウ別証明書の大域貼り合わせ
- 長さスペクトルの正当性（クリップド長多重集合；切り詰め後の同型不変）

[Spec]（監査可能・切り詰め後に非膨張）:
- PF/BC 崩壊後比較器（固有/滑らか + 体係数）
- Mirror/Transfer の δ 制御可換（自然 2‑セル；加法的、後処理で非増加）
- 非入れ子反射子の A/B ソフト可換ポリシー（Δ_comm を δ 台帳へ）
- トロピカル/弱群の崩壊プロキシ
- 三層ラングランズ・ゲート（Gal/Trans/Funct）
- 作用フィルトレーション付き Fukaya 実現（継続 1‑Lipschitz；ストップ追加は削除型）

---

## 概念とコンポーネント

- `T_tau`（正確な切り詰め）
  - 長さ ≤ τ のバーを削除する正確な反射的局所化
  - 冪等；インタリービング/ボトルネックに対して 1‑Lipschitz
- `C_tau`（フィルタ付き持ち上げ；f.q.i. まで）
  - 連鎖レベルの持ち上げで `P_i(C_tau F) ≅ T_tau(P_i F)`
- 崩壊ゲート（B–Gate⁺）
  - 各ウィンドウで：PH1(F)=0；Ext1(R(F),k)=0（振幅 ≤ 1 のときのみ対象）；μ=ν=0；安全余裕 `gap_tau > Σ delta`
- Overlap Gate（崩壊後）
  - オーバーラップ上の切り詰め後局所同値；Čech–Ext¹ 無サイクル性；オーバーラップ上の δ 予算；安定性バンド確認
- タワー診断
  - `T_tau` 後の比較写像に対し `(mu, nu)` = 核/余核の一般繊維次元；`(mu,nu)≠(0,0)` で Type IV
- 安定性バンド
  - τ スイープ；バンド検出；`(mu,nu)=(0,0)` が連続 τ 範囲で安定なゲーティング
- PF/BC 崩壊後比較器 [Spec]
  - t における対象毎の PF/BC 計算 → パーシステンスへ輸送 → `T_tau` 適用 → ウィンドウで比較
- Mirror/Transfer の可換性 [Spec]
  - 自然 2‑セル `Mirror ∘ C_tau ⇒ C_tau ∘ Mirror` と一様な δ(i,τ)；パイプラインで加法的；後処理で非増加
- A/B ソフト可換 [Spec]
  - 非入れ子反射子向け；Δ_comm ≤ η をテスト；不合格時はフォールバック順序へ、Δ_comm を δ 台帳へ記録
- 長さスペクトル作用素 `Lambda_len`
  - ウィンドウ付きクリップド長の固有値（順序なし多重集合）は、クリップド・バーコード長に一致；切り詰め後の同型不変

---

## インストール

```bash
# 1) クローン
git clone https://github.com/your-org/ak-hdpst.git
cd ak-hdpst

# 2) 環境作成
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3) インストール
pip install -e ".[all]"     # 追加機能: [viz], [lean], [coq]
```

---

## クイックスタート

### 最小 CLI 実行

```bash
# 実行設定の用意
cp examples/v16/minimal/run.yaml ./run.yaml

# パイプラインの実行（ウィンドウ化・切り詰め後）
akhdpst run run.yaml

# ウィンドウ毎のゲート判定と δ 台帳を確認
akhdpst audit out/artifacts
```

### 最小 Python API

```python
from akhdpst.core import T_tau, C_tau
from akhdpst.gate import collapse_admissible, b_gate_plus
from akhdpst.tower import audit_tower, detect_stability_band
from akhdpst.compare import pf_bc_compare_after_collapse
from akhdpst.length import lambda_len

# フィルタ付き連鎖複体または次数別パーシステンスをロード
F = ...  # ユーザがロード

# tau で切り詰め（パーシステンスとフィルタ付き持ち上げ）
tau = 0.15
P_trunc = {i: T_tau(F.persistence(i), tau) for i in [0,1]}
F_trunc = C_tau(F, tau)  # f.q.i. まで

# ゲート確認（片方向ブリッジは t-正確・振幅<=1 のときのみ使用）
ok_gate = collapse_admissible(
    F, realization="Db(k-mod)", t_exact=True, amplitude_leq_1=True
)

# タワー診断（tau ごと）；安定性バンド
mu, nu = audit_tower(tower=[F0, F1, F2, F_inf], tau=tau, degrees=[0,1])
bands = detect_stability_band(tower=[F0, F1, F2, F_inf], degree=1, tau_sweep=[0.1,0.15,0.2])

# PF/BC 崩壊後比較器（ウィンドウ化、T_tau 後）
ok_pfbc = pf_bc_compare_after_collapse(
    obj_left="Rf_*(A⊗f^*B)", obj_right="Rf_*A ⊗ B",
    window=("w0", [0.0, 0.5]), tau=tau
)

# 長さスペクトル監査（ウィンドウ付きクリップド長多重集合）
eig = lambda_len(P_trunc[1], window=(0.0, tau))
```

---

## 設定（`run.yaml`）— v16.0 スキーマの要点

```yaml
meta:
  name: "demo-v16.0"
  seed: 1337
  version: "16.0"
  author: "your-name"

data:
  input: "data/example.h5"
  backend: "bars"       # bars | chain
  degrees: [0, 1]

windows:
  # 右開区間; MECE（相互排他かつ完全）; ウィンドウ被覆は監査される
  - label: "w0"
    range: [0.0, 0.5)
  - label: "w1"
    range: [0.5, 1.0)

truncation:
  tau: 0.15
  lift: "C_tau"         # フィルタ付き持ち上げ（f.q.i. まで）
  reflector: "T_tau"    # パーシステンスでの正確な切り詰め

overlap_checks:
  local_equiv: true      # 切り詰め後の局所同値（予算内）
  cech_ext1_ok: true     # オーバーラップ上の Čech–Ext¹ 無サイクル性
  stability_band_ok: true

spectral_policy:
  order: "ascending"     # 必須（v16.0）
  norm: "op"             # "op" または "fro"（必須）
spectral_bounds:
  lambda_min: 1.0e-8
  lambda_max: 1.0e+3
  lip_tol: 0.02

operations:
  steps:
    - type: "deletion"
      op: "dirichlet_restriction"
      args: { nodes: [1,5,7] }
      delta: { alg: 0.000, disc: 0.002, meas: 0.001 }
    - type: "epsilon"
      op: "continuation"
      args: { eps: 0.006 }
      delta: { alg: 0.006, disc: 0.002, meas: 0.001 }
    - type: "spec"
      op: "mirror_transfer"
      args: { delta_commutation: 0.010 }   # δ(i,τ)（Mirror×Collapse）
      delta: { alg: 0.010, disc: 0.000, meas: 0.000 }

spec:
  pf_bc_after_collapse: { enabled: true, delta_budget: 0.0 }
  ab_soft_commuting:
    enabled: true
    eta: 0.02            # 許容誤差
    fallback_order: ["birth_window", "length"]  # Δ_comm > η の場合

gate:
  require:
    PH1_zero: true
    Ext1_zero: true       # 振幅<=1 のときのみ使用
    mu_zero: true
    nu_zero: true
    gap_tau_gt_sum_delta: true
  safety_margin:
    gap_tau: 0.03

audit:
  outputs: ["bars", "spec", "ext", "phi", "Lambda_len"]
  checksums: "sha256"
  restart: "summability"

length_spectrum:
  degree: 1
  tau: 0.15
  audit: "hash"         # 小規模例では固有値を保存可

output:
  dir: "out/artifacts"
  overwrite: false
```

キー追加（v16.0）:
- `overlap_checks`（Overlap Gate — local_equiv, cech_ext1_ok, stability_band_ok）
- `spectral_policy.order="ascending"` と `norm="op"|"fro"`（必須）
- `spectral_bounds` と `lip_tol`
- `length_spectrum`（`Lambda_len` 監査）
- ステップ毎の δ 台帳；安全余裕の `gap_tau`
- `eta` とフォールバック順序付き A/B ソフト可換

---

## ワークフローと例

### 1) ウィンドウ化プロトコル（切り詰め後）

- 各右開ウィンドウに対して：
  - パーシステンスを計算
  - `T_tau` を適用
  - 写像を比較、`(mu,nu)` を算出し、δ 台帳を監査

```bash
akhdpst run examples/v16/windowed/run.yaml
akhdpst audit out/artifacts --by-window
```

### 2) Overlap Gate グルーイング（切り詰め後）

- オーバーラップするウィンドウ毎の要件：
  - 切り詰め後の局所同値（δ 予算内）
  - Čech–Ext¹ 無サイクル性（次数 1）
  - 安定性バンド条件（τ 付近の蓄積がない；`(mu,nu)=(0,0)`）

```bash
akhdpst gate overlap --run run.yaml --window w0,w1
```

### 3) τ スイープと安定性バンド

- τ グリッドで `(mu,nu)` を調べ、`(mu,nu)=(0,0)` が分割に安定なバンドを受理

```bash
akhdpst sweep tau --run run.yaml --degree 1 --grid "0.10:0.05:0.30"
```

### 4) PF/BC 崩壊後比較器 [Spec]

- `Rf_*(A⊗f^*B)` と `Rf_*A ⊗ B` を同一ウィンドウで `T_tau` 後に比較

```bash
akhdpst compare pf-bc --run run.yaml --window w0 --tau 0.15
```

### 5) A/B ソフト可換 [Spec]

- Δ_comm ≤ η をテスト；不合格ならフォールバック順序を採用し、Δ_comm を δ^{alg} として記録

```bash
akhdpst compare ab --run run.yaml --reflectors length birth_window --eta 0.02
```

### 6) 長さスペクトル監査（Lambda_len）

- ウィンドウ付きクリップド長多重集合を計算し、ハッシュ/固有値を保存

```bash
akhdpst audit lambda-len --dir out/artifacts --degree 1 --tau 0.15
```

---

## 更新ポリシー（切り詰め後）

| 更新タイプ     | 例                                                                      | 保証（`T_tau` 後）                                                   |
| ---           | ---                                                                     | ---                                                                  |
| 削除型        | ディリクレ制限；主座小行列；PSD Loewner 収縮；保守的平均；ストップ追加 | ウィンドウ付きパーシステンスのエネルギーとスペクトル指標に対して非増加 |
| ε‑連続変形    | 小さなホモトピー；インタリービングのシフト上限を満たす小ステップ         | 1‑Lipschitz（安定性）；ε を δ 台帳に記録                             |
| 包含型        | セル追加；境界条件の緩和；領域拡大                                       | 非膨張（安定性のみ）                                                 |

注意:
- スペクトル指標は `L(C_tau F)` 上で計算され、f.q.i. の不変量ではありません。v16.0 では固定の `spectral_policy`（順序/ノルム）と境界を `run.yaml` に必須とします。
- [Spec] 項目（PF/BC 比較器、Mirror/Transfer、A/B ポリシー、トロピカル系）は δ を台帳に記録し、ウィンドウ毎に B–Gate⁺ を通過する必要があります。

---

## 監査と成果物

```
out/artifacts/
  bars/
    w0_deg1_trunc.json
    w1_deg1_trunc.json
  spec/
    ledger_w0.json
    ledger_w1.json
  ext/
    w0_ext1.txt
  phi/
    maps_w0_deg1.h5         # 比較写像; (mu,nu); iso_tail フラグ
  lambda_len/
    w0_deg1_tau015.json     # 固有値またはハッシュ
  run.yaml
  audit_summary.json
  checksums.txt
```

- `bars/`: ウィンドウ/次数毎の切り詰めバーコード
- `spec/`: δ 台帳（alg/disc/meas）＋ [Spec] 監査結果
- `ext/`: Ext¹ サマリ（振幅 ≤ 1 の場合のみ適格）
- `phi/`: 比較写像；`(mu,nu)`；`phi_iso_tail` の状態
- `lambda_len/`: クリップド長多重集合（固有値またはハッシュ）
- `audit_summary.json`: ゲート結果；オーバーラップ検査；安定性バンド
- `checksums.txt`: すべての成果物の SHA256

---

## コマンドリファレンス（CLI）

```bash
# 設定に従って実行
akhdpst run run.yaml

# 既存の実行ディレクトリを監査
akhdpst audit out/artifacts

# Overlap Gate チェック
akhdpst gate overlap --run run.yaml --window w0,w1

# ウィンドウ毎の B–Gate+
akhdpst gate check --run run.yaml --window w0

# τ スイープと安定性バンド
akhdpst sweep tau --run run.yaml --degree 1 --grid "0.10:0.05:0.30"

# PF/BC 崩壊後比較器
akhdpst compare pf-bc --run run.yaml --window w0 --tau 0.15

# A/B ソフト可換テスト
akhdpst compare ab --run run.yaml --reflectors length birth_window --eta 0.02

# タワー診断の出力
akhdpst diag tower --dir out/artifacts --degree 1

# 長さスペクトル監査
akhdpst audit lambda-len --dir out/artifacts --degree 1 --tau 0.15
```

---

## Python API リファレンス（抜粋）

```python
from akhdpst.core import T_tau, C_tau
from akhdpst.gate import collapse_admissible, b_gate_plus, overlap_gate_check
from akhdpst.tower import audit_tower, detect_stability_band
from akhdpst.compare import pf_bc_compare_after_collapse, ab_soft_commute
from akhdpst.length import lambda_len

# Overlap Gate
ok_overlap = overlap_gate_check(run="run.yaml", windows=["w0","w1"])

# B–Gate+（ウィンドウ）
ok_bgate = b_gate_plus(
    window="w0",
    ph1_zero=True,
    ext1_zero=True,
    mu=0, nu=0,
    gap_tau=0.025,
    delta_sum=0.011
)

# Mirror/Transfer（δ 制御可換）
ok_mirror = ab_soft_commute(
    M=P_trunc[1], A="length", B="birth_window", eta=0.02, fallback=True
)

# PF/BC 比較器
ok_pfbc = pf_bc_compare_after_collapse(
    obj_left="Rf_*(A⊗f^*B)", obj_right="Rf_*A ⊗ B",
    window=("w0", [0.0, 0.5]), tau=0.15
)

# τ の安定性バンド検出
bands = detect_stability_band(tower=[...], degree=1, tau_sweep=[0.1,0.15,0.2])

# 長さスペクトル（固有値/ハッシュ）
L = lambda_len(P_trunc[1], window=(0.0, 0.15))  # eigs または hash
```

---

## ロードマップ

- 自動 τ スイープとバンド検出（堅牢な細分化；バンド単位ゲーティング）
- Overlap Gate の拡充（ナーブ API；単体タイプ別の受理）
- より豊富な Spec モジュール（数論/ラングランズ、PDE、Fukaya）と δ 制御
- 形式化の拡張（Lean/Coq）：`T_tau`、`(mu,nu)`、ゲート、PF/BC 輸送、A/B ポリシー
- ノートブック雛形（ウィンドウ別監査、δ 台帳/オーバーラップ可視化）

---

## コントリビュート

Issue と PR を歓迎します:
- Core と [Spec] を明確に区別（コード/ドキュメント）
- [Spec] 項目は「切り詰め後非膨張チェック + δ 台帳記録」を必須
- 最小例とテスト（T7, T10, T11, T13, T14, T15）を追加

開発コマンド:

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
mypy akhdpst
```

---

## 引用と参考文献

研究で AK–HDPST v16.0 を使用する場合は以下を引用してください:

```
AK–HDPST v16.0: Windowed Collapse, Overlap Gate, PF/BC After-Collapse, and Auditable Pipelines
Authors: ...
Year: 2025
URL: https://github.com/your-org/ak-hdpst
```

基礎文献:
- Crawley‑Boevey (2015): Decomposition of pointwise finite‑dimensional persistence modules
- Chazal, de Silva, Glisse, Oudot (2016): Structure and stability of persistence modules and barcodes

---

## ライセンス

本プロジェクトは MIT ライセンスで公開されています。詳細は `LICENSE` を参照してください。

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17130577.svg)](https://doi.org/10.5281/zenodo.17130577)
---

## 付録：用語チートシート

- 構成可能 1D パーシステンス：有限の臨界集合；有界ウィンドウでの点ごと有限次元
- `T_tau`：長さ ≤ τ のバーを削除する正確な切り詰め；冪等；1‑Lipschitz
- `C_tau`：`T_tau` のフィルタ付き持ち上げ（f.q.i. まで）；`P_i(C_tau F) ≅ T_tau(P_i F)`
- B–Gate⁺：PH1=0；Ext1=0（振幅 ≤ 1 のときのみ）；`(mu,nu)=(0,0)`；`gap_tau > Σ delta`
- Overlap Gate：崩壊後の局所から大域のグルーイング；オーバーラップ上の Čech–Ext¹；安定性バンド；δ オーバーラップ予算
- `(mu, nu)`：切り詰め後の比較写像における核/余核の一般繊維次元；非零なら Type IV
- 安定性バンド：`(mu,nu)=(0,0)` が τ 範囲でスイープに安定
- PF/BC 比較器：同一ウィンドウ/τ で `T_tau` 適用後に PF/BC を比較
- A/B ソフト可換：Δ_comm ≤ η をテスト；不合格ならフォールバックし、Δ_comm を δ^{alg} として記録
- Lambda_len：ウィンドウ付きクリップド長作用素；切り詰め後の同型不変
```
