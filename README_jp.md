# AK-HPDST v19.0.0

## AK High-Dimensional Projection Structural Theory
## AK高次元射影構造理論

> 複雑な数学的対象から必要な構造情報を抽出し、パーシステンスデータへ射影し、制御されたCollapse処理を行い、その結果・失敗・証拠・外部定理への接続を型付きで監査するための研究フレームワークです。

**著者:** Atsushi Kobayashi  
**リリース:** v19.0.0 - Threshold-Gap Metric Repair Release  
**位置づけ:** 証明済みの内部Core、条件付きInterface、限定Toy Bridge、探索基盤、明示的Non-Claimから構成される研究フレームワーク

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21330904.svg)](https://doi.org/10.5281/zenodo.21330904)

---

## 1. 初学者向け概要

AK-HPDSTは、複雑な数学的対象から選択した情報を、パーシステントホモロジーのプロファイルへ変換し、バーコードとして扱います。

バーコードは、barと呼ばれる区間の集まりです。

- 長いbarは、広い範囲で残り続ける特徴を表します。
- 短いbarは、短い範囲で消える特徴を表します。
- infinite barは、windowで切り取る前のプロファイルにおいて、無限に残り続ける特徴を表します。

AK-HPDSTは、短いbarを削除して、そのまま「難問を解いた」と判断する理論ではありません。

次の事項を一つずつ記録します。

1. どの外部数学対象を用いたか。
2. どのようにCoreが読めるデータへ変換したか。
3. どの次数、window、thresholdを選択したか。
4. どのbarを残し、どのbarを削除したか。
5. 比較誤差がある場合でも、その分類が安定しているか。
6. 必要な代表元、射、tower、証明artifactが存在するか。
7. 各主張がproved、conditional、operational、Spec、rejected、historicalのどれか。

最も重要な安全原則は次です。

```text
Core pass != 外部数学定理

別途Interface TheoremまたはBridge Theoremが証明された場合に限り、
Coreの結果を外部領域の結論へ移送できる。
```

したがって、AK-HPDSTは「難問を自動的に解く装置」ではなく、証明候補を構造化し、必要条件、証拠、失敗箇所、外部定理への接続を監査するためのproof-interface architectureです。

---

## 2. AK-HPDST v19.0.0でできること

v19.0.0は、宣言された仮定とデータ型の範囲内で、次の処理を行えます。

- 適切なfiltered objectを、構成可能な1-parameter persistence profileへ変換する。
- persistence profileを、指定したwindowへ制限する。
- 指定したthreshold以下の有限barを削除する。
- hard threshold deletionが、指定されたbottleneck distance誤差の下で安定かを判定する。
- exact comparisonとmetric comparisonを区別する。
- 修復済みpersistence profileを表すadmissible representativeを記録する。
- eligible realization regimeにおいて、次数1のpersistent vanishingからExt1 vanishingへの一方向の含意を用いる。
- directed towerと宣言されたapexを、実際のcomparison morphismで比較する。
- Type IV diagnosticsにより、terminal-genericなkernel defectとcokernel defectを検出する。
- local-to-global分析のためのoverlap、continuation、Restart recordを管理する。
- 単なる成功・失敗ではなく、失敗を型別に分類する。
- immutable manifest、Claim reference、proof-object record、replay dataを生成する。
- 人間やAIによる探索を活用しつつ、独立検証されるまで探索結果をproof verdictへ入れない。

実務的には、次の問いを整理するための枠組みです。

```text
複雑な対象から選択した構造情報を射影し、
Collapseし、比較し、監査する際に、
結果を解釈するための仮定や証拠を失わずに管理できるか。
```

---

## 3. v19.0.0が主張していないこと

このリリース単体では、次を証明していません。

- Navier-Stokes方程式の正則性。
- Riemann予想。
- Birch and Swinnerton-Dyer予想。
- ABC予想。
- Iwasawa main conjecture。
- Langlands correspondence。
- mirror symmetryまたはFukaya category equivalence。
- 暗号学的安全性定理。
- persistent homologyとExt群の普遍的同値。

特に、v19.0.0は次を無条件には主張しません。

```text
PH1 = 0 <-> Ext1 = 0
```

現在Coreで証明されている方向は、より限定された一方向です。

```text
Eval(1, W, tau; F) = 0
    -> Ext1(R(C(tau, W; F)), k) = 0
```

この含意を使うためには、少なくとも次が必要です。

- admissible representativeが存在する。
- 宣言されたrealizationが定義されている。
- 対象がeligible amplitude rangeに入る。
- 必要なedge identificationが証明されている。
- 関連artifactとClaim recordが揃っている。

逆方向は、v19.0.0 Coreには含まれません。

---

## 4. 主な処理フロー

```text
外部数学対象
        |
        v
宣言されたrealizationまたは1-parameter extraction
        |
        v
Core-readableなfiltered objectまたはpersistence object
        |
        v
Persistence profile P_i(F)
        |
        v
Window restriction Window(W, P_i(F))
        |
        v
Hard threshold deletion T_bar(tau)
        |
        v
Repaired evaluation Eval(i, W, tau; F)
        |
        +--> exact comparison
        +--> metric-gap-certified comparison
        +--> admissible representativeとeligible Ext1 edge
        +--> overlap、continuation、Restart record
        +--> tower comparisonとType IV diagnostics
        |
        v
B-Gate+とtyped audit
        |
        v
Core status: pass / reject / undefined / not_invoked
        |
        v
証明済みtransport theoremがある場合のみ外部結論へ接続
```

処理順序は固定です。

```text
persistence -> window -> threshold deletion
```

次の順序は、一般には同じではありません。

```text
persistence -> threshold deletion -> window
```

bounded windowで切り取ると、もともと長いbarやinfinite barが短い有限barになる場合があります。

したがって、別途commutation theoremがない限り、window処理を行った後にthreshold判定を行います。

---

## 5. 最小限の数学モデル

### 5.1 主な対象領域

Coreは主に次を扱います。

```text
体 k 上のconstructible one-parameter persistence module
```

簡単に言えば、次の性質を持つprofileです。

- 制御されたparameter値でのみ構造が変化する。
- 各parameterで有限次元のデータを持つ。
- bounded range内でcritical valueが無制限に集積しない。

wild、uncontrolled、infinite-rank、または本質的なmulti-parameter dataは、自動的にはCore-readableではありません。

外部データがこの形を持たない場合、別途extractionまたはInterface Theoremが必要です。

### 5.2 Window-first profile

filtered object `F`、監視次数 `i`、window `W`、threshold `tau`に対し、threshold処理前のprofileを次で表します。

```text
B(i, W; F) = Window(W, P_i(F))
```

repaired evaluationは次です。

```text
Eval(i, W, tau; F) = T_bar(tau, B(i, W; F))
```

同じ内容を展開すると次です。

```text
Eval(i, W, tau; F)
    = T_bar(tau, Window(W, P_i(F)))
```

### 5.3 Hard threshold deletion

各bar `I`に対して、次の処理を行います。

```text
if length(I) <= tau:
    Iを削除
else:
    Iを保持
```

infinite barは、bounded windowでclipされる前は保持されます。

同じthresholdを2回適用しても結果は変わりません。

```text
T_bar(tau, T_bar(tau, B)) = T_bar(tau, B)
```

2つのthresholdを順に適用した場合、より大きいthresholdを1回適用した結果と一致します。

```text
T_bar(sigma, T_bar(tau, B))
    = T_bar(max(sigma, tau), B)
```

ただし、hard deletionはstandard bottleneck metricの下でglobal non-expansiveではありません。

---

## 6. v19の中心修復: Threshold-Gap-Safe Stability

旧構成では、hard threshold deletionがbottleneck distanceを常に増加させないように読める表現が残っていました。

このglobal claimは誤りです。

barの長さが少し変わるだけでthresholdをまたぎ、retainedからdeleted、またはdeletedからretainedへ分類が変化する場合があるためです。

### 6.1 Threshold clearance

1つのbarcode `B`について、次を考えます。

```text
clear_tau(B)
    = tauと、Bに含まれる有限barの長さとの最小距離
```

有限barがない場合は次です。

```text
clear_tau(B) = infinity
```

複数の保護対象barcodeについては次です。

```text
gap_tau(B1, B2, ..., Bm)
    = min(clear_tau(B1), clear_tau(B2), ..., clear_tau(Bm))
```

### 6.2 修復後の安定性条件

次を仮定します。

```text
bottleneck_distance(B, C) <= epsilon
```

さらに、`B`と`C`の両方について、有限barの長さが次の範囲に入らないことを確認します。

```text
[tau - epsilon, tau + epsilon]
```

このとき次が成立します。

```text
bottleneck_distance(T_bar(tau, B), T_bar(tau, C)) <= epsilon
```

これはtwo-sided certificateです。

`B`だけ、または`C`だけを確認しても不十分です。

### 6.3 Ledger表現

比較誤差をmetric ledgerへ集約する場合、scalarized ledger valueは次を満たす必要があります。

```text
val_B(metric_defect) < gap_tau(protected_barcodes)
```

さらに次を証明または検証する必要があります。

```text
actual bottleneck discrepancy <= val_B(metric_defect)
```

ledgerに数値が記録されているだけでは不十分です。

その数値が、実際に比較するprofile間のbottleneck discrepancyを上から評価していることを、theorem、verified computation、または再構成可能なartifactで示す必要があります。

---

## 7. 各Coreの役割

以下の区分は、README上の説明用です。

正式な定義、証明、依存関係はMainおよび各Appendixが優先します。

### Core A - Persistence and barcode layer

Core-readableなpersistence profileを作成します。

```text
P_i(F)
```

そのprofileをbarcodeとして表現します。

**目的:** 選択した構造的挙動を、window処理、threshold処理、比較、監査が可能な形式へ変換すること。

### Core B - Windowed projection layer

profileを宣言されたwindowへ制限します。

```text
B(i, W; F) = Window(W, P_i(F))
```

**目的:** 全scaleを一括で扱うのではなく、制御されたparameter rangeを分析すること。

**注意:** bounded windowにより、infinite barが有限のclipped barへ変わる場合があります。

### Core C - Collapse layer

hard threshold deletionを適用します。

```text
Eval(i, W, tau; F) = T_bar(tau, B(i, W; F))
```

**目的:** threshold以下の有限barを削除し、repaired profileを得ること。

**注意:** 標準Coreではbarcode-level operationです。すべてのmorphismに作用するglobal exact functorであるとは主張しません。

### Core D - Comparison and metric-safety layer

比較には、次のいずれか1つのruntime modeを指定します。

- `exact`
- `metric_gap_certified`
- `not_compared`

#### exact

実際のequalityまたはpersistence-profile isomorphismが証明され、artifactで裏付けられている状態です。

#### metric_gap_certified

実際のdiscrepancy boundとtwo-sided threshold-gap certificateがある状態です。

#### not_compared

宣言されたscopeで比較推論を使用していない状態です。

必要な比較義務を`not_compared`で代替することはできません。

### Core E - Representative and Ext1-edge layer

admissible representativeを簡易表記で次のように書きます。

```text
C(tau, W; F)
```

これは、宣言された監視次数とequivalence strengthの範囲でrepaired profileを表します。

eligible regimeでは、次の一方向含意を使えます。

```text
Eval(1, W, tau; F) = 0
    -> Ext1(R(C(tau, W; F)), k) = 0
```

**目的:** persistent vanishingとderived-category statementを接続すること。

ただし、無条件の同値は主張しません。

### Core F - Tower and Type IV diagnostic layer

directed towerとdeclared apexを比較するために、実際のcomparison morphismが必要です。

```text
phi(i, W, tau):
    ColimProfile(i, W, tau; F_bullet)
        -> ApexProfile(i, W, tau; F_infinity)
```

source、target、kernel、cokernelがterminal-tameである場合、次を定義します。

```text
mu(i, W, tau) = terminal_generic_dimension(kernel(phi))
nu(i, W, tau) = terminal_generic_dimension(cokernel(phi))
```

監視対象がcleanである状態は次です。

```text
(mu_Collapse, nu_Collapse) = (0, 0)
```

これは、監視されたterminal-generic kernel defectとcokernel defectが検出されなかったことを意味します。

ただし、comparison morphism全体があらゆる意味でisomorphismであることまでは自動的に証明しません。

Type IV statusは次のいずれか1つです。

```text
not_invoked
undefined
certified_zero
obstructed
```

`not_invoked`または`undefined`の場合、数値pairを割り当てません。

### Core G - Gate, failure, and audit layer

`B-Gate+`は、必要な条件を相殺なしで統合します。

passには、状況に応じて次が必要です。

1. degree-one repaired vanishing。
2. valid comparison-mode record。
3. Ext1 clauseを使う場合のvalid Ext1 evidence。
4. Type IVがscope外なら`not_invoked`、使う場合はvalid artifact付きの`certified_zero`。
5. metric comparisonを使う場合のpassing metric budget。
6. required non-scalar obligationの充足。
7. complete and consistent manifest。
8. Claim Registerに適合したclaim use。

良好な数値marginがあっても、次を補うことはできません。

- representativeの欠落。
- morphismの欠落。
- eligibilityの欠落。
- terminal-tameness evidenceの欠落。
- 不適切なclaim status。
- proof artifactの欠落。
- artifact identityの不整合。

---

## 8. Failure taxonomy

複数のfailure typeが同時に成立する場合があります。

| Type | 意味 | 代表例 |
|---|---|---|
| Type I | Topological failure | `Eval(1, W, tau; F) != 0` |
| Type II | eligible regime内のcategorical failure | invokedかつwell-typedな`Ext1 != 0` |
| Type III | metric、comparison、representative、overlap、Restart、coherence failure | gap record失敗、comparison不正、required morphism欠落 |
| Type IV | tower-level terminal-generic obstruction | `(mu_Collapse, nu_Collapse) != (0, 0)` |
| Type V | claim status、provenance、identity、manifest failure | Spec、AI output、rejected claim、不完全recordをtheorem evidenceとして使用 |

必要な証拠が欠けている場合、通常のstatusは次です。

```text
undefined
```

次へ自動変換してはいけません。

```text
0
pass
not_invoked
not_compared
```

---

## 9. Claim discipline

すべてのstatementは、登録された強さの範囲でのみ使用します。

代表的なroleは次です。

- Core definition。
- Core theoremまたはlemma。
- metric-repair theorem。
- operational policy。
- Interface definitionまたはInterface theorem。
- Bridge candidate。
- Bridge Program。
- Bridge Theorem。
- toy bridge theorem。
- Search artifact。
- Companion template。
- Spec。
- explicit non-claim。
- deprecatedまたはrejected claim。

主要な原則は次です。

```text
Registration != proof
Spec != theorem
Bridge Program != Bridge Theorem
Toy Bridge != problem-specific Bridge Theorem
AI output != proof
Search result != theorem
Execution != proof
Replay success != mathematical truth
Manifest completeness != mathematical truth
Core pass != external theorem without a proved transport theorem
```

source、register、summary、implementation、old documentの内容が一致しない場合、新しいimmutable repairが発行されるまではweaker safe interpretationを採用します。

---

## 10. 文書構成

### Main - Chapter 1から8

Mainは、v19.0.0全体のcontractを定義します。

1. scope、claim discipline、metric-repair contract。
2. barcode metric、threshold deletion、gap-safe stability。
3. windowed evaluation、comparison record、representative。
4. eligible realizationと一方向の`PH1 -> Ext1` edge。
5. failure taxonomyとType IV diagnostics。
6. window logic、overlap、Restart、record-level gluing。
7. typed audit semanticsとCore sovereignty。
8. Core closureとexternal Interface boundary。

### Foundation Appendices AからG

- **A:** barcode metricとthreshold-gap repair。
- **B:** filtered representative。
- **C:** eligible realizationとcanonical Ext1 edge。
- **D:** tower diagnosticsとterminal-generic Type IV defect。
- **E:** window、overlap、Restart、gluing。
- **F:** typed obligation、status、dependency closure。
- **G:** canonical manifest schema、proof object、replayability。

### Technical Extension Appendices HからN

advisory indicator、discretization、measurement、controlled commutation、transfer ledger、quantale semantics、higher-categorical extensionを扱います。

これらは、証明済みCoreを暗黙に拡張しません。

### Problem Interface Appendices

外部領域がCoreへ接続するための型付き経路を定義します。

対象には次が含まれます。

- arithmetic interface。
- cyclotomic tower、Iwasawa tower interface。
- congruence interface。
- mirror、Fukaya-facing interface。
- normalization interface。
- Navier-Stokes exploration、soundness、proof-first program。

Interfaceは接続経路を定義するものであり、必要なtransport theoremが証明されない限り、外部数学定理ではありません。

### Search / Platform Appendices UからZ

次を管理します。

- human、AI、tool、platform agent。
- Hunter、Mapper、Lifter workflow。
- Bridge Program。
- validity map、certificate DAG。
- proof store。
- execution record、reproducibility record。

Searchは原則としてproposer-sideです。

Core verdictはverifier-side dataだけで決まります。

### Claim Register、CM、TB、Companion

- **CR-v19:** claim identity、status、permitted use、failure route、repair ancestry。
- **CM-v19:** 証明された強さを変えずに再利用するCore micro-theorem。
- **TB-v19:** 意図的に小さなsource categoryへ限定されたtoy bridge theorem。
- **Companion:** calibration、execution、record作成用template。theorem sourceではありません。

---

## 11. Repository guide

v19.0.0の典型的なrelease packageは次の構成です。

```text
.
├─ README.md
├─ README_JA.md
├─ AK_HPDST_v19_0_0_Part__Main.pdf
├─ AK_HPDST_v19_0_0_Appendix_Part_II__Foundation_Appendices.pdf
├─ AK_HPDST_v19_0_0_Appendix_Part_III__Technical_Extension_Appendices.pdf
├─ AK_HPDST_v19_0_0_Appendix_Part__IV__Problem_Interface_Appendices.pdf
├─ AK_HPDST_v19_0_0_Appendix_Part__V__Search_Platform_Appendices.pdf
├─ AK_HPDST_v19_0_0_Appendix_Part__Claim_Register.pdf
├─ AK_HPDST_v19_0_0_Appendix_Part__CM.pdf
├─ AK_HPDST_v19_0_0_Appendix_Part__TB.pdf
├─ AK_HPDST_v19_0_0_Appendix_Part__Companion.pdf
└─ OLD/
   └─ historical materials - non-normative and potentially incorrect
```

実際のpathはpackageまたはbranchにより異なる場合があります。

normative identityは、versioned source artifactとClaim Registerで管理します。

---

## 12. 推奨する読み順

初めて読む場合は、次の順番を推奨します。

1. このREADME。
2. Main Chapter 1 - scopeと安全原則。
3. Main Chapter 8 - 何が証明済みで、何が条件付きか。
4. Main Chapter 2、3 - window、threshold deletion、metric repair。
5. Main Chapter 4、5 - Ext1 edgeとtower diagnostics。
6. Appendix A - threshold-gap-safe stabilityの詳細証明。
7. CR-v19 - claim statusとpermitted use。
8. 目的領域に対応する各Appendix。

implementationまたはauditを行う場合は、Appendix F、G、U、Y、Z、およびCompanionも参照してください。

---

## 13. 小さな概念例

windowed barcodeに、次の有限bar lengthがあるとします。

```text
0.08, 0.21, 0.73
```

thresholdを次とします。

```text
tau = 0.20
```

hard deletionの結果は次です。

```text
0.08 -> deleted
0.21 -> retained
0.73 -> retained
```

ただし、`0.21`はthresholdに近い値です。

comparison errorによって長さが`0.20`未満へ変化する可能性がある場合、retained/deletedの分類は安定ではありません。

そのため、AK-HPDSTでは次の両方を要求します。

1. certified error bound `epsilon`。
2. `epsilon`より大きいtwo-sided threshold gap。

softwareがbarcodeを出力したという事実だけでは、stableとは判定しません。

---

## 14. OLDディレクトリを残す理由

historical materialは、repair ancestryとclaim inflationへの戒めとして意図的に保存しています。

旧資料には、次のようなobsolete、unsupported、またはoverstrongな表現が含まれる場合があります。

```text
PH1 = 0 = Ext1
```

または次です。

```text
PH1 = 0 <-> Ext1 = 0
```

これらはv19.0.0のnormative claimではありません。

現在のCoreで許可される読み方は、より限定されています。

```text
eligible regime
+ required artifacts
+ Eval(1, W, tau; F) = 0
    -> Ext1(R(C(tau, W; F)), k) = 0
```

`OLD/`を残す目的は次です。

- 過去にどのclaimを過剰拡張したかを示す。
- 現在のone-way eligible bridgeが、なぜ狭い形になっているかを示す。
- rejected claimを黙って削除せず、修復履歴として残す。
- immutable repair ancestryにより、数学的責任と監査可能性を確保する。

`OLD/`内の資料を、現在のtheorem evidenceとして使用しないでください。

v19.0.0のsourceと、対応するClaim Register entryを使用してください。

---

## 15. AIと自動探索

AK-HPDSTでは、AI systemおよびautomated toolを次に利用できます。

- realization、window、threshold、bridge candidateの提案。
- counterexample探索。
- proof routeのranking。
- formalization candidateの生成。
- map、DAG、manifest、replay recordの作成。
- candidate argumentのcritiqueまたはaudit。

ただし、意味論上の境界は厳格です。

```text
Generation != verification
Transformation != preservation unless checked
Retrieval != verification
Consensus != proof
Compilation != theorem validity
Storage != certification
Replay != mathematical truth
```

AIが生成したstatementをevidenceとして使うには、必要なverifier-side objectへ変換し、数学的検証とaudit checkを通過させる必要があります。

---

## 16. Versioningとcitation discipline

AK-HPDSTの結果を参照する場合、少なくとも次を記録してください。

- theory versionとdocument revision。
- exact source artifact。
- theorem、definition、またはClaim UID。
- complete hypothesisとmonitored scope。
- comparison mode。
- required artifact identity。
- 必要に応じてrepair ancestry。

後から作成されたsummary、README、diagram、software implementationは、canonical sourceに記載されたtheorem statementの代わりにはなりません。

---

## 17. 最終的な位置づけ

AK-HPDST v19.0.0は、次の問いを厳密に扱うための枠組みです。

```text
複雑な数学対象を、より単純なpersistence-based representationへ射影し、
制御されたCollapse処理を行い、
evidence、approximation、computation、proofを混同せずに評価するには、
どのような構造が必要か。
```

中心的な貢献は、「すべての問題がCollapseできる」と主張することではありません。

中心的な貢献は、次の区別を明示し、監査可能にしたことです。

- projectionとpreservation。
- short-bar deletionとstable deletion。
- exact equalityとmetric control。
- persistence vanishingとderived vanishing。
- local profile agreementとtower-level agreement。
- search outputとtheorem evidence。
- Core certificationとexternal mathematical truth。

この分離構造が、v19.0.0の基盤です。
