# AK-HPDST v21.0.0

## AK高次元射影構造理論  
## AK High-Dimensional Projection Structural Theory

> 複雑な数学的対象を制御された「構造的な影」へ射影し、有限観測を証明可能な有限証拠へ変換し、実際の有限図式を再構成・大域化し、最後に証明された強度だけを元の数学領域へReturnするための、型付き数学フレームワーク。

**著者:** Atsushi Kobayashi  
**理論バージョン:** v21.0.0  
**リリーステーマ:** Finite Globalization, Unified Bridge Calculus, and Certificate Complexity  
**主要数学アーキテクチャ:** `Core-P + Core-DG`  
**ステータス:** v21.0.0 正典・source-controlled research corpus / Final Claim Register収録  
**リポジトリ形式:** 全文PDF。最初に読むための独立したKernel Paperを収録

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21831104.svg)](https://doi.org/10.5281/zenodo.21831104)

---

## はじめに読むもの

最短で全体像をつかむ場合は、次の順序を推奨します。

1. [Kernel Paper](<AK_HPDST_v21_0_0_Kernel_Paper_Projection_Reaudited(1).pdf>)  
   v21の数学的エッセンスを約50ページに圧縮した独立論文です。
2. [Main Chapters 1--10](<AK_HPDST_v21_0_0_Part1_Main.pdf>)  
   v21の一般理論・定理・型・Bridge/Returnの正典です。
3. [Final Claim Register](<AK_HPDST_v21_0_0_Appendix_Part12_Claim_Register.pdf>)  
   定理ID、所有権、migration、source binding、使用可能強度を管理します。

**最初の数学的読解にはKernel Paperを推奨します。**  
ただし、v21の完全な定理文、仮定、証明、Interface、Validation、運用境界については、Mainおよび各Appendixが正典です。

---

## 目次

- [1. AK-HPDSTとは何か](#1-ak-hpdstとは何か)
- [2. v20とv21の違い](#2-v20とv21の違い)
- [3. 最短の入口 Kernel Paper](#3-最短の入口-kernel-paper)
- [4. Dual-Coreアーキテクチャ](#4-dual-coreアーキテクチャ)
- [5. P2DG Interface](#5-p2dg-interface)
- [6. v21におけるCollapse](#6-v21におけるcollapse)
- [7. 有限観測と有限証明は違う](#7-有限観測と有限証明は違う)
- [8. 有限証明には明確なno-go境界がある](#8-有限証明には明確なno-go境界がある)
- [9. finite-to-infinite reduction](#9-finite-to-infinite-reduction)
- [10. record globalizationとobject globalization](#10-record-globalizationとobject-globalization)
- [12. Unified Bridgeとtyped Return](#12-unified-bridgeとtyped-return)
- [16. v21 Kernelで数学的に際立つ結果](#16-v21-kernelで数学的に際立つ結果)
- [19. Known-Theorem Recovery](#19-known-theorem-recovery)
- [22. AI・探索・proof engineering](#22-ai探索proof-engineering)
- [27. v21が主張しないこと](#27-v21が主張しないこと)
- [33. Repository Guide](#33-repository-guide)
- [34. 推奨読解ルート](#34-推奨読解ルート)
- [41. 最終的な位置づけ](#41-最終的な位置づけ)

---

## 1. AK-HPDSTとは何か

AK-HPDSTは、数学の多くの領域に共通して現れる次の構造的問題を扱います。

```text
高次元・非局所・無限・複雑な数学対象を、
制御可能な数学的shadowへ射影し、

有限証拠によって必要な性質を認証し、

失われていない構造を実際の数学対象として再構成・大域化し、

証明された強度だけを元の数学領域へ戻せるか？
```

v21の基本経路は次です。

```text
high-dimensional source X
    |
    | typed / purpose-faithful structural projection
    v
structured shadow F_X = R_AK(X)
    |
    | persistence / filtration / finite observation
    v
finite Collapse certificate
    |
    | P2DG reconstruction
    v
actual finite diagram
    |
    | coherence + effective descent
    v
global mathematical object
    |
    | typed Bridge / Return
    v
source-domain conclusion E_sigma(X)
```

AKにおける **projection（射影）** は構造的な意味です。

必ずしも、

```text
線形射影
幾何学的な低次元化
topological dimensionの減少
global faithful functor
```

を意味しません。

有効なAK射影には、少なくとも次を宣言する必要があります。

```text
source class
source側で知りたいfeature
observable / shadow
variance
coefficient
使用する含意の方向
information-loss profile
preservation / reflection theorem
failure boundary
```

したがって、射影された対象は元の対象そのものではありません。

それは、

```text
目的に対して制御された structured shadow
```

です。

AK理論の中心的な非対称性は次です。

```text
Projectionは構造的な影を取り出す。

Returnだけが、
認証された結論を元のsource domainへ戻す。
```

この

```text
Projection
    -> Collapse
    -> Reconstruction / Globalization
    -> Return
```

が、AK高次元射影構造理論の根本概念です。

---

## 2. v20とv21の違い

v20は主として、

```text
finite proof compression
higher obstruction transport
finite-to-infinite reduction
typed external Return
```

を整備したreleaseでした。

v21は、v20の完全なlower baselineを保守的に継承した上で、第二の数学Coreを追加し、**有限証拠から実際の有限数学構造、さらに大域対象へ進む経路**を正面から構築します。

v21のstable architectureは、

```text
Core-P + Core-DG
```

です。

ただし `+` は、

```text
二つのCoreが型付きInterfaceで連携する
```

という意味です。

次を意味しません。

```text
Core-P = Core-DG

Core-PからCore-DGが自動的に再構成される

Core-DGからCore-Pが自動的に復元される

categorical product / coproduct / equivalence
```

v21の主要鎖は、

```text
persistent certificate
    -> finite diagram
    -> global object
    -> external Return
```

です。

**各矢印は独立した定理を必要とします。**

概念的には、

```text
v20:
有限の認証済み証拠
    -> 外部数学へのproof transport

v21:
有限の認証済み証拠
    -> exact finite mathematical structure
    -> effective globalization
    -> target-relative external Return
```

への進化です。

---

## 3. 最短の入口: Kernel Paper

v21全体は非常に大きいため、最初に次を読むことを推奨します。

```text
AK_HPDST_v21_0_0_Kernel_Paper_Projection_Reaudited(1).pdf
```

Kernel PaperではAK理論を、

```text
source
-> structural projection
-> repaired finite certificate
-> finite diagram reconstruction
-> finite diagrammatic globalization
-> typed Return
```

として整理しています。

また、現在のv21 Kernelの中で数学的に重要な結果を抽出しています。

主なものは、

- hard threshold deletionに対するsharp threshold-gap stability
- reduced image上のexact zero separation
- family-relative finite certificate complexity
- exact lower boundとfinite-detection no-go
- endpoint-complete persistenceのfinite Mobius reconstruction
- coordinate rank-query modelでのexact query complexity
- finite-state inverse limit reconstruction
- `lim^1 = 0` の有限認証
- projective generatorによるzero reflection
- cone detection
- finite Morita reconstruction
- finite Alexandrov realization
- effective finite descent
- target-relative Bridge / Return composition
- reject / undefinedのcausal localization

です。

推奨順序は、

```text
README
  -> Kernel Paper
  -> Main Chapters 1--10
  -> Foundation / DG
  -> HT / UB
  -> source-specific appendices
```

です。

---

## 4. Dual-Coreアーキテクチャ

### 4.1 Core-P: Persistence Certificate Core

Core-Pは、v20で修復されたPersistence Coreをv21で保守的に継承・強化したものです。

stableな標準scopeは、

```text
field上のconstructible one-parameter persistence
finite-dimensional monitored data
```

です。

filtered object `F`、homological degree `n`、window `W`、threshold `tau` に対し、標準評価順序は、

```text
P_n(F)
  -> Window_W(P_n(F))
  -> T_bar_tau(Window_W(P_n(F)))
```

です。

簡易表記では、

```text
B(n,W;F) = Window_W(P_n(F))

Eval(n,W,tau;F) = T_bar_tau(B(n,W;F))
```

となります。

順序は固定されています。

```text
persistence
    -> window
    -> hard threshold deletion
```

Core-Pには次が含まれます。

- constructible persistenceとbarcode decomposition
- hard finite-bar threshold deletion
- sharp threshold-gap-safe transport
- repaired zero / nonzero certification
- finite detector soundness
- finite detector completeness
- certificate complexity
- lower bounds
- higher obstruction / Ext edge
- actual morphismに基づくType IV diagnostics
- transient defect separation
- detector atlas
- overlap / coverage / Restart
- finite-state / Noetherian / theorem-certified finite-to-infinite reduction

### thresholdに関する重要境界

hard positive-threshold deletionは、一般には、

```text
global exact Serre localization
globally non-expansive endofunctor
universally functorial exact operation
```

ではありません。

安全なmetric transportは概略、

```text
d_B(B,C) <= epsilon

かつ

B,Cのどのfinite barの長さも
[tau - epsilon, tau + epsilon]
に入らない

なら

d_B(T_bar_tau(B), T_bar_tau(C)) <= epsilon
```

という二側threshold-gap条件のもとで成立します。

gap条件は実装上の便宜ではなく、定理の仮定です。

---

### 4.2 Core-DG: Finite Diagram and Globalization Core

Core-DGはv21でstable Coreへ追加された主要数学層です。

標準scopeは、

```text
finite small category / finite poset
finite-dimensional diagram over a field
bounded complex
actual natural transformation
actual chain map
finite projective generator
finite-dimensional Morita algebra
finite Alexandrov space
effective finite descent
```

です。

finite category `P` と field `k` に対して、

```text
Diag_P(k) = Fun(P, Vect_fd(k))
```

を考えます。

Core-DGでは、

- finite category presentation
- relations
- variance
- abelian finite-diagram category
- representable projectives
- finite projective generator
- Yoneda reconstruction
- derived zero reflection
- coneによるmorphism-isomorphism detection
- finite Morita reconstruction
- finite Alexandrov realization
- strict finite sheaf descent
- strict bounded-complex descent
- separately certified derived descent
- global zero / isomorphism certificate
- model-relative global certificate complexity

を扱います。

重要な原則は、

```text
same objectwise data
    != same diagram

equal rank table
    != actual morphisms

objectwise isomorphism
    != natural isomorphism

pairwise overlap equivalence
    != cocycle

descent readiness
    != effective descent
```

です。

Core-DGは、このような「暗黙に同一視されやすい構造差」を数学的に分離するために存在します。

---

## 5. P2DG Interface

v21では、Persistence dataとfinite categorical structureを同一視しません。

Persistence-to-Diagram Interface、略して `P2DG` を独立した定理-bearing handoffとして扱います。

必要に応じてP2DG recordは、

```text
finite grid / category
objects
actual morphisms
relations
variance
coefficients
endpoint conventions
exactness profile
reflection profile
information-preservation profile
terminal policy
supported conclusion strengths
artifacts
prohibited stronger readings
```

を保持します。

endpoint-completeなfinite one-parameter persistence classでは、適切なfinite gridに制限することで、finite linear-quiver representationへ移すことができます。

complete rank table

```text
r(i,j) = rank(V_i -> V_j)
```

からinterval multiplicityをfinite Mobius inversionで復元できます。

coordinate rank-query modelでは、comparable pairsすべてのrankを読むことが、unrestricted interval-multiplicity familyのexact reconstructionに必要十分です。

しかし、

```text
rank table != arbitrary enriched diagram

barcode != natural transformation

scalar probe != morphism reconstruction
```

です。

morphismやcategory structureまで戻す場合には、enriched probeとactual relation dataが必要です。

---

## 6. v21におけるCollapse

AK-HPDSTにおける **Collapse** は、一つの万能scalarではありません。

また単に、

```text
何かが0になった
```

という一種類の主張でもありません。

Collapse型の結論には、例えば次があります。

```text
repaired persistence zero
finite detector zero
higher Ext obstruction zero
kernel defect zero
cokernel defect zero
terminal Type IV zero
transient defect absence
diagram-probe zero
descent-coherence success
global object zero
source-domain predicate
```

これらは自動的に同一ではありません。

例えば、

```text
repaired persistence zero
    != automatically Ext zero

terminal Type IV clean
    != full kernel/cokernel zero

local repaired zero
    != global object zero

global internal zero
    != external theorem
```

です。

一つのstageから別のstageへ強い結論を移すには、独立したpromotion theoremが必要です。

この型付きCollapse calculusは、v21の重要な特徴です。

---

## 7. 有限観測と有限証明は違う

AKの中心原則の一つは、

```text
finite data != finite certificate
```

です。

有限個の、

- rank
- value
- sample
- endpoint
- bar
- local object
- overlap map
- numerical approximation

が得られたからといって、それだけでglobal statementの証明にはなりません。

finite certificate modelでは、少なくとも、

```text
information model
query model
encoding model
verification model
```

を宣言します。

概略、

```text
M = (I, Q, E, V)
```

です。

またv21では、証明コストを一つの数値へ潰しません。

典型的には、

```text
cost(Pi) = (q, b, t, a)
```

として、

```text
q = query count
b = encoding / bit size
t = verification work
a = artifact footprint
```

を区別します。

有限のachievable familyでは、最小certificateは単一最小値ではなくPareto frontierとして表現されます。

例えば、

```text
query数は少ないがartifactが大きい

artifactは小さいがverification costが高い
```

というtrade-offをそのまま保持できます。

---

## 8. 有限証明には明確なno-go境界がある

AK-HPDSTは、

```text
どんな無限問題にも有限certificateが存在する
```

とは仮定しません。

例えば、retained barのbirthが任意に右へ移動できるfamilyでは、有限回で停止するdetectorは、最後に観測した位置より右で初めて現れるbarを見逃せます。

したがって、

```text
uncontrolled right-unbounded birth family
    -> no uniform finite exact detector
```

です。

有限から無限へ進むには、例えば次の追加構造が必要です。

```text
finite-state reduction
eventual constancy
Noetherian stabilization
global support bound
compactness
recurrence theorem
derived-limit theorem
certified apex agreement
```

長く安定して見えるfinite prefixは、それだけではinfinite theoremではありません。

---

## 9. finite-to-infinite reduction

v21は、

```text
finite observation
finite certificate
finite pattern
actual infinite target
```

を区別します。

typed finite-state inverse towerでは、適切な仮定のもとでstable partを有限transition dataから復元できます。

代表的には、

```text
inverse_limit(V_n) ~= stable_image(T^e)

lim^1(V_n) = 0
```

です。

重要なのは式だけではありません。

完全なrouteでは、

```text
actual tower
bonding maps
variance
period / state record
stable-image witness
derived-limit conditions
apex
apex comparison map
apex-agreement theorem
```

を識別する必要があります。

これにより、

```text
多数のfinite layerが一致した
```

ことを、

```text
infinite targetが証明された
```

と誤読することを防ぎます。

---

## 10. record globalizationとobject globalization

v21は二種類のglobalizationを明確に区別します。

### Record globalization

local certificate recordをまとめ、global record-level predicateを証明することです。

ここでは、

```text
cover
overlap
coverage
Restart
consistency
```

などを使います。

### Object globalization

実際のglobal mathematical objectを構成することです。

こちらには、

```text
actual local objects
actual transition / overlap maps
cocycle
必要ならhigher coherence
effectivity theorem
target equivalence strength
```

が必要です。

つまり、

```text
glued evidence != descended object
```

です。

この区別はv20からv21への本質的な強化です。

---

## 11. Finite MoritaとAlexandrov globalization

finite category `P` に対して、linearized representablesの直和

```text
G_P = direct_sum_{p in P} P_p
```

をfinite projective generatorとして用います。

これにより、

- zero reflection
- cone detection
- enriched reconstruction
- finite Morita equivalence

を扱います。

finite posetについては、diagramをupper Alexandrov space上のsheafとして実現します。

actual overlap mapsとstrict cocycleがあれば、finite object descentとbounded-complex descentを行えます。

ただし、

```text
finite-dimensional category algebra
    != automatically semisimple

zero reflection
    != automatically thick generation

pairwise local isomorphism
    != descent datum
```

です。

---

## 12. Unified Bridgeとtyped Return

genericなBridge / Return calculusの正典はMain Chapter 9であり、Appendix HTがその研究spineとexpanded proofを担います。

一つのrouteは、単なる文章上の含意列ではありません。

typed proof DAGとして、各nodeが少なくとも、

```text
input type
output type
hypotheses
variance
coefficients
comparison mode
supported target strengths
failure route
artifacts
```

を持ちます。

完全routeは概略、

```text
source
  -> realization
  -> Core-P
  -> optional P2DG
  -> Core-DG
  -> optional spectral / derived / tower transfer
  -> descent / rigidity
  -> final target-specific Return
```

です。

最終Returnは、**必要なすべてのcomponentが支える強度以下**でのみ有効です。

Return targetの例は、

```text
predicate
numerical invariant
barcode / object class
actual object
actual morphism
exact sequence
quasi-isomorphism
derived equivalence
pseudo-isomorphism
determinant
ideal
regularized / partial target
```

です。

一般に、

```text
weaker Return
    -> stronger Return
```

は成立しません。

強度を上げるには、rigidity、conservativity、reconstruction、comparisonなどの独立定理が必要です。

---

## 13. Returnはprojectionの自動逆写像ではない

非常に重要な点です。

```text
Return != automatic inverse of projection
```

AK projectionは情報を意図的に捨てることがあります。

それでも、目的とするsource predicateについて十分である可能性があります。

したがって、

```text
source predicateをReturnできる
```

ことと、

```text
source object全体を復元できる
```

ことは別です。

例えば、

```text
predicate Return
    != source-object reconstruction

determinant Return
    != module reconstruction

local-system Return
    != constant-object Return

derived equivalence
    != preferred presentation
```

です。

v21ではReturn targetそのものが定理の一部です。

---

## 14. failure semanticsとnon-compensation

atomic verifier statusは、

```text
pass
reject
undefined
not_invoked
```

です。

意味は異なります。

```text
pass:
    invokedされた全義務が満たされた

reject:
    well-typedな必要条件が偽であることが確認された

undefined:
    必要な証拠、型、source identity、theorem edgeが欠けている

not_invoked:
    immutable scope上、その条件を使用していない
```

target-indexed Bridge resultは別の型です。

```text
reject
undefined
obstructed
partial_return
regularized_return
return
```

数学的に証明されたnonzero obstructionは、missing evidenceではありません。

また、

```text
別条件の成功
大きなmetric reserve
AI agentの多数一致
大量のsearch coverage
successful compilation
successful replay
manifest closure
```

によって、欠けた数学的矢印を補うことはできません。

これが **non-compensation principle** です。

---

## 15. Proof-DAG sovereignty

v21のtheorem-bearing routeはdependency-completeなtarget sliceとして管理されます。

finite dependencyではacyclic proof DAGを用います。

countable / infinite dependencyでは、追加で、

```text
well-founded rank
```

または、

```text
separately certified finite-to-infinite reduction
```

が必要です。

workflow graphにcycleがあるというだけでは数学的意味は与えられません。

数学的cycleには、

```text
induction
coinduction
recursion
fixed-point theorem
mutual recursion theorem
```

などの独立した意味付けが必要です。

v21では、最終的にfailしたというだけでなく、必要な `reject` / `undefined` nodeのうち最も上流にあるcausal blockerを局在化する仕組みも導入しています。

---

## 16. v21 Kernelで数学的に際立つ結果

v21の数学的内容を評価する際の主要landmarkです。

### 16.1 Sharp threshold-gap repair

hard threshold deletionはglobally non-expansiveではありません。

しかしthreshold境界の両側に必要なgapがある場合、bottleneck stabilityが回復します。

さらに、そのgap条件が必要であることをcounterexampleで確認します。

### 16.2 Exact zero separation

`tau`-reduced image上では、thresholdとbottleneck errorによってrepaired zero / nonzeroを分離できます。

### 16.3 Family-relative certificate complexity

有限証明complexityは、定理の絶対的な数値ではなく、information / query / verifier modelに相対的に定義されます。

finite achievable familyではPareto frontierを持ちます。

### 16.4 Private-witness lower bounds

互いに独立したprivate witnessを持つfamilyでは、exact deterministic certificationに必要なquery lower boundを構成できます。

### 16.5 Right-unbounded finite-detection no-go

任意に右側へ遅れて初めて現れるfeatureを許すuncontrolled familyには、uniform finite detectorは存在しません。

### 16.6 Finite Mobius reconstruction

endpoint-complete finite persistenceはcomplete rank tableからfinite Mobius inversionで復元できます。

### 16.7 Exact rank-query count

`m + 1` 個のgrid verticesに対して、coordinate rank-query modelで必要十分なquery数は、

```text
N_m = (m + 1)(m + 2) / 2
```

です。

### 16.8 Finite-state inverse-limit reconstruction

typed finite-state inverse towerはstable imageから再構成でき、declared hypothesesのもとで `lim^1 = 0` とfinite apex-agreement testを得ます。

### 16.9 Generator--cone--Morita package

actual finite diagramsに対して、

```text
projective generator
    -> zero reflection

cone
    -> isomorphism detection

enriched probe
    -> finite Morita reconstruction
```

を接続します。

### 16.10 Effective finite descent

actual local objects、actual maps、cocycle、effectivity theoremから、finite Alexandrov model上のglobal objectおよびbounded complexを構成します。

### 16.11 Typed end-to-end Return

source-domain conclusionは、要求されたtargetに必要なすべての数学nodeが、正しい型と強度で成立した場合にのみReturnされます。

---

## 17. Appendix HT: Higher Transfer and Unified Bridge Composition

Appendix HTはMain Chapter 9周辺のresearch spineです。

次の五つのtransfer familyを統合しています。

```text
HC = homological compression

PE = persistence--Ext /
     finite reconstruction and enhancement

SS = spectral-sequence transfer

RL = inverse/direct systems and derived limits

IW/Return = target-specific Return architecture
```

役割は、

```text
Core-P / Core-DG
    = 何が数学的にcertifyされたか

HT
    = そのcertified informationを
      より大きな数学構造へどうtransportするか
```

です。

HTでは、

- homological compression下のprotected persistence
- finite persistence / Ext reconstruction
- finite-quiver reconstruction
- enhanced morphism Return
- spectral-sequence page-to-abutment transfer
- extension ambiguity
- inverse system / derived limit
- coefficient / base-change route
- regularized Return
- target-relative strength
- unified defect stack
- composable Bridge DAG

などを扱います。

HTは強力なresearch-spineですが、内部に存在するすべてのconstructionが自動的にstable Coreへ昇格するわけではありません。

---

## 18. Appendix UB: reusable componentsと12のvalidation case

Appendix UBは、再利用可能なBridge componentとvalidated Return portfolioです。

含まれる主なcomponentは、

- finite-generator / conservative realization
- coefficient / base change / completion
- finite-state reduction
- Noetherian reduction
- descent
- Kunneth
- duality
- coherence
- rigidity
- determinant / Fitting-facing component
- source-specific adapters

です。

12のsource-bound validation familyは、概ね、

```text
finite rank reconstruction
enriched projective-probe reconstruction
finite / periodic Tachikawa lanes
Galois--Leopoldt defect reconstruction
finite Alexandrov descent
finite-state inverse limits
Iwasawa / p-adic analytic interfaces
Serrin compactness / continuation
certified regulator calculation
regular one-variable Iwasawa finite layers
singular / Bockstein Iwasawa finite layers
```

を含みます。

Validation successは、使用したtheoremをuniversal theoremへ昇格させません。

各caseは、

```text
source class
hypotheses
target
Return strength
```

の範囲でのみ有効です。

---

## 19. Known-Theorem Recovery

AK-HPDSTは、**Known-Theorem Recovery** と **new theorem** を明確に分けます。

Recovery trackでは、既知のbenchmark conclusionをproof constructionから隔離します。

routeを独立に閉じた後でのみ、

```text
正しいknown theoremを
正しいstrengthでReturnできたか
```

を比較します。

v21 Final Claim Registerには、二つのexact-strength recovery trackが登録されています。

### Iwasawa growth

登録されたReturnは、declared precursor packageに相対的なIwasawa characteristic-growth clauseです。

概略、

```text
c_n = mu * p^n + lambda * n + constant
```

をcertified tail上で回収します。

これは一般Iwasawa main conjectureの証明ではありません。

### Fixed-exponent Serrin criterion

PDE側のrecoveryは、declared Leray--Hopf regimeにおける固定指数のstrict-subcritical implicationです。

```text
u in L^6_t L^6_x
    -> interior regularity
```

を回収します。

これはcriterion-level recoveryであり、3次元Navier--Stokesのunconditional global regularityを意味しません。

---

## 20. v21 Main validation portfolio

Main Chapter 10ではpositive caseとnegative caseの両方を使ってarchitectureを検証します。

v21 Main validation gateは、

```text
V1  v20 regression at exact registered strength

V2  finite persistence reconstruction

V3  enriched finite-diagram reconstruction

V4  finite object-level and strict derived descent

V5  finite-state inverse-limit and apex Return

V6  complete external Return using Core-P + Core-DG

V7  model-relative certificate upper / lower bounds

V8  mandatory negative / no-go boundaries

V9  artifact / replay / proof-DAG / manifest consistency
```

です。

Main-bodyでは `V1--V9` がそれぞれdeclared strengthでpassしています。

ただしこれは、

```text
AKのすべてのpossible routeがcompleteである
```

ことも、

```text
named open problemが解かれた
```

ことも意味しません。

---

## 21. Negative validationも数学である

v21では、counterexampleとprohibited upgradeを副次的なものではなく、理論の主要出力として扱います。

例えば、

```text
incomplete generator data
    -> no full reconstruction

pairwise local agreement
    -> no higher coherence automatically

finite prefix agreement
    -> no infinite-target theorem

local zero
    -> no global zero without retained-feature coverage

synthetic algebraic duality
    -> no source-semantic Bridge automatically

predicate Return
    -> no source-object reconstruction
```

などです。

AK-HPDSTは成功routeだけを探す理論ではありません。

```text
なぜその強い結論には到達できないのか
```

を、数学的に特定する理論でもあります。

---

## 22. AI・探索・proof engineering

AK-HPDST v21には専用のSearch / Platform layerがあります。

対象は、

- human mathematician
- AI system
- proof assistant
- theorem search
- counterexample search
- route search
- proof-DAG construction
- proof storage
- semantic replay
- reproducible execution

です。

platformは、

```text
source lanes
adapters
routes
targets
fallbacks
consumers
backends
```

の幅を広げることができます。

しかし、

```text
pipeline width != theorem strength
```

です。

AIに関する基本境界は、

```text
generation != verification

consensus != proof

search success != theorem

self-review != independent verification

formal wiring != source-faithful interpretation

successful execution != mathematical truth

replay != mathematical proof
```

です。

AI-generated objectは、exact verifier-side schemaへ変換され、必要な数学的obligationを満たして初めてtheorem evidenceになります。

---

## 23. AI支援数学においてAKアーキテクチャが有効な理由

現代の数学AIは、

```text
candidate lemma
possible realization
counterexample
formalization draft
proof route
numerical evidence
source match
```

を大量に生成できます。

しかし重要なのは、generated stepがもっともらしいかどうかだけではありません。

AKでは次を確認します。

```text
source / target typeは正しいか

含意方向は正しいか

必要なsemanticsは保存されているか

finite observationはclaimed targetに対してcompleteか

benchmark informationがpremiseへ逆流していないか

invariantをobjectへ暗黙昇格していないか

local dataをglobal dataへ暗黙昇格していないか

finite evidenceをinfinite theoremへ暗黙昇格していないか
```

AK-HPDSTのAI上の位置づけは、

```text
AI automatically solves mathematics
```

ではなく、

```text
AI searches and proposes.

Typed mathematics determines
what the evidence actually proves.
```

です。

---

## 24. statusとresult sort

v21には複数のstatus系があります。

混同しないことが重要です。

### Atomic verifier status

```text
pass
reject
undefined
not_invoked
```

### P2DG readiness

```text
ready
incomplete
inconsistent
not_invoked
```

### Handoff readiness

例:

```text
descent_input_ready
bridge_input_ready
```

これらは次のtheorem nodeを呼べるinput readinessであり、theorem conclusionではありません。

### Type IV diagnostic status

```text
not_invoked
undefined
certified_zero
obstructed
```

### Target-indexed Bridge result

```text
reject
undefined
obstructed
partial_return
regularized_return
return
```

### Workflow / repository state

```text
compilation
review
migration
registration
replay
publication
package release
```

は別のlifecycleです。

あるfieldのfavorable tokenを、別のfieldへコピーしてはいけません。

---

## 25. v21の重要な「非同一化」

以下はv21を読む上での恒久的な原則です。

```text
registration != proof

finite observation != finite certificate

soundness != completeness

persistence profile != finite diagram

rank data != actual morphism

record globalization != object globalization

objectwise isomorphism != natural isomorphism

pairwise overlap equivalence != cocycle

descent readiness != descent effectivity

finite prefix != infinite reduction

terminal defect zero != full defect zero

determinant / ideal Return != object Return

pseudo-isomorphism != isomorphism

derived equivalence != preferred presentation

realization != Return

validation != theorem premise

AI output != proof

replay != mathematical truth

package integrity != theorem validity
```

これらの多くは単なる運用ruleではありません。

v21には、それぞれを支える数学的境界、counterexample、またはnonpromotion theoremがあります。

---

## 26. v21で現在できること

明示されたsource classと仮定の範囲で、v21は次を扱えます。

- source structureからtyped Core-readable shadowを構成する
- constructible one-parameter persistenceを解析する
- repaired hard-threshold evaluationを行う
- finite detectorでzero / nonzeroをcertifyする
- model-relative certificate upper / lower boundを与える
- uncontrolled familyにuniform finite detectorが存在しないことを証明する
- endpoint-complete finite persistenceを再構成する
- rank dataからinterval multiplicityを復元する
- enriched probeからactual finite diagramを復元する
- finite projective generatorでzero objectを検出する
- coneでmorphismのisomorphismを検出する
- finite Morita reconstructionを行う
- finite-poset diagramをAlexandrov sheafとして実現する
- strict finite object / bounded-complex descentを行う
- actual coherenceとeffectivityがある場合にlocal dataをglobal objectへ大域化する
- selected finite-state inverse limitを有限certificationする
- homological / spectral / tower / coefficient / descent / rigidity componentをtyped Bridge DAGとして合成する
- complete routeが支える強度だけをReturnする
- missing evidenceや数学的failureを局在化する
- arithmetic / representation-theoretic / PDE / categoricalなsource-specific routeをvalidationする
- AI、proof assistant、proof store、semantic replayを数学的authorityと分離して利用する

---

## 27. v21が主張しないこと

AK-HPDST v21.0.0単体は、次を証明していません。

- Riemann hypothesis
- Birch and Swinnerton-Dyer conjecture
- ABC conjecture
- general Iwasawa main conjecture
- general Leopoldt conjecture
- general Tachikawa conjecture
- unconditional 3D Navier--Stokes regularity
- Clay-level Navier--Stokes result
- general Langlands correspondence
- homological mirror symmetry
- general Fukaya-category equivalence
- unrestricted multiparameter persistence classification
- arbitrary stack / hypersheaf descent
- unrestricted `(infinity,1)`-categorical globalization
- arbitrary unbounded-derived reconstruction
- every infinite familyに対するuniversal finite detector
- persistent homologyとExt群のuniversal equivalence

また、

```text
PH_n = 0 <-> Ext^n = 0
```

を無条件では主張しません。

必要なrealization、eligibility、reflection、Return theoremがある場合にのみ、指定された方向・強度で使用できます。

同様に、

```text
successful AK internal certificate
    != automatically external theorem
```

です。

---

## 28. Technical Extension layer

Technical Extension Appendices H--Nは、stable Coreの周囲にある制御された研究拡張です。

主な領域は、

- spectral indicators
- discretization / continuum transfer
- measurement-level stability
- controlled commutation
- Mirror / Transfer comparison
- quantale / defect-ledger semantics
- derived extension
- dg structure
- sheaf / stack
- multiparameter extension
- stable / higher-categorical discipline

です。

ただし、

```text
derived
stack
stable
coherent
infinity-categorical
hypercomplete
```

と書かれているだけでstable Coreへ昇格するわけではありません。

Core-facing theorem evidenceとして使用するには、明示的なextraction / transport theoremが必要です。

---

## 29. Problem Interface layer

Problem Interface Appendixは、外部数学領域をgeneric AK architectureへ接続します。

v21のproblem-facing routeは概略、

```text
R_PI =
(
  source semantics,
  realization,
  Core-facing object / predicate,
  external target,
  selected route,
  assumptions,
  defects,
  artifacts
)
```

です。

現在のsource-facing領域には、

- finite abelian p-groups
- cyclotomic / Iwasawa structure
- congruence / p-adic profile
- Mirror / categorical comparison
- Fukaya-facing extension
- normalization / resolution-assisted route
- Navier--Stokes exploration / soundness / proof-first program

があります。

source-specific theoremはsource-specificのままです。

別familyへ再利用するには、完全なtyped contractを保存するsubstitution theoremが必要です。

---

## 30. Search / Platform layer

Appendices U--Zはproof engineering platformを構成します。

```text
U  Agent Semantics

V  Hunter / Mapper / Lifter Search Protocols

W  Bridge Programs

X  Validity Map and Global Certificate DAG

Y  AI Platform and Proof Store

Z  Execution and Reproducibility Schema
```

v21 synchronizationではさらに、

- semantic field map
- target-local route slice
- route resilience
- compatible packet amalgamation
- proof-store snapshot safety
- deterministic parallel execution
- cache admission
- content-addressed proof closure
- semantic replay
- infrastructure non-compensation

などを強化しています。

---

## 31. Companion layer

Companionは、既にownerが存在する数学結果を運用schemaへ投影する層です。

主に、

- problem-interface calibration
- route assembly
- execution
- storage
- replay
- audit
- release handoff

のtemplateを提供します。

基本原則は、

```text
Companion completeness
    != mathematical completeness
```

です。

templateやpacketやexecutionが完全でも、Main / Appendixの数学ownerに存在しないtheoremは生成されません。

---

## 32. Claim Registerとcanonical authority

Final Claim Registerは、

```text
AK_HPDST_v21_0_0_Appendix_Part12_Claim_Register.pdf
```

です。

役割は、

- canonical identity
- migration
- source binding
- admissible use
- target strength
- failure semantics
- theorem ownership
- release closure

の管理です。

Claim Registerはregistrationによって数学を強化しません。

大まかなauthorityは、

```text
Main Chapters 1--10
    -> generic theorem statementsのcanonical owner

Foundation A--G
    -> Core-P expanded proofs / schemas

Appendix DG
    -> Core-DG / descent expanded proofs

Appendix HT
    -> higher-transfer / Return research spine

Appendix UB
    -> reusable components / validated cases

Appendix CM
    -> compact corollaries / consumer contracts

Appendix TB
    -> toy theorems / counterexamples / regressions

Technical Extension H--N
    -> bounded extension mathematics

Problem Interface MS/NS
    -> source-specific interfaces / Returns

Search / Platform U--Z
    -> proof infrastructure

Companion
    -> operational projection / handoff

Claim Register
    -> identity / admissible-use governance
```

です。

source間に不一致がある場合、audited repairが行われるまでは、

```text
weakest source-supported type-correct reading
```

を採用します。

---

## 33. Repository Guide

v21 repositoryは現在PDFベースです。

```text
.
|-- README.md
|-- README_JA.md
|
|-- AK_HPDST_v21_0_0_Part1_Main.pdf
|     Main Chapters 1--10
|
|-- AK_HPDST_v21_0_0_appendix_Part2_Foundation_Core_P_Verification_Appendices (1).pdf
|     Foundation Appendices A--G
|
|-- AK_HPDST_v21_0_0_appendix_Part3_appendix_DG.pdf
|     Finite Diagram and Globalization Foundation
|
|-- AK_HPDST_v21_0_0_Appendeix_Part4_appendix_HT.pdf
|     Higher Transfer, Unified Bridge Composition, and Typed Return
|
|-- AK_HPDST_v21_0_0_Appendix_Part5_Appendix_UB.pdf
|     Universal Bridge Component Library and Validated Return Portfolio
|
|-- AK_HPDST_v21_0_0_Appendix_Part6_Appendix_CM.pdf
|     Core Corollary, Implementation Lemma, and Consumer-Contract Library
|
|-- AK_HPDST_v21_0_0_Appendix_Part7_Appendix_TB.pdf
|     Toy Bridge, Counterexample, and Regression Portfolio
|
|-- AK_HPDST_v21_0_0_Appendix_Part8_Technical_Extension_Appendices.pdf
|     Technical Extension Appendices H--N
|
|-- AK_HPDST_v21_0_0_Appendix_Part9_Problem_Interface_Appendices.pdf
|     Problem Interface Appendices MS / NS
|
|-- AK_HPDST_v21_0_0_Appendix_Part10_Search_Platform_Appendices.pdf
|     Search / Platform Appendices U--Z
|
|-- AK_HPDST_v21_0_0_Appendix_Part11_Companion.pdf
|     Calibration / execution / reproducibility / release handoff
|
|-- AK_HPDST_v21_0_0_Appendix_Part12_Claim_Register.pdf
|     Final Claim Register
|
`-- AK_HPDST_v21_0_0_Kernel_Paper_Projection_Reaudited(1).pdf
      standalone mathematical kernel / recommended entry point
```

filenameは現在のrelease packageに合わせています。

ただしcanonical theorem identityはfilenameの見た目ではなく、source documentとClaim Registerによって管理されます。

---

## 34. 推奨読解ルート

### 34.1 最短のconceptual route

```text
1. README
2. Kernel Paper
3. Main Chapter 1
4. Main Chapters 7, 9, 10
5. Claim Register
```

AK理論とは何か、v21で何が変わったかを最短で理解するrouteです。

### 34.2 Mathematical Kernel route

```text
1. Kernel Paper
2. Main Chapters 2--7
3. Foundation Appendices A--G
4. Appendix DG
5. Main Chapter 9
```

Persistence、certificate、reconstruction、Morita、descent、Returnを数学的に追うrouteです。

### 34.3 Bridge / advanced homological route

```text
1. Kernel Paper
2. Main Chapters 4--9
3. Appendix DG
4. Appendix HT
5. Appendix UB
```

### 34.4 Arithmetic / Iwasawa route

```text
1. Kernel Paper
2. Main Chapters 3--5 and 9
3. Appendix HT
4. Appendix UB
5. Problem Interface MS
6. Main Chapter 10
7. Claim Register
```

### 34.5 Navier--Stokes route

```text
1. Main Chapter 9
2. Problem Interface NS
3. Appendix UBの該当validation
4. Main Chapter 10
5. Claim Register
```

### 34.6 AI / proof-platform route

```text
1. Main Chapters 1 and 8
2. Main Chapter 9
3. Search / Platform Appendices U--Z
4. Companion
5. Claim Register
```

---

## 35. 小さな概念例

あるprogramがpersistence profileの有限個の点を評価し、すべて0だったとします。

AK-HPDSTは、それだけでは、

```text
repaired profile = 0
```

とは結論しません。

次を確認します。

```text
どのprofile stageをsampleしたか？

threshold deletionの前か後か？

endpoint / right-germ conventionは正しいか？

retained barがsampleを全て避ける可能性はないか？

sourceはdeclared familyに属しているか？

coverageは独立に証明されているか？

そのfamilyにuniform finite detectorは存在するか？

certificateを許されたstrengthだけで使用しているか？
```

これらが定理によって閉じたとき、zero-looking observationは初めてtheorem-bearing zero certificateになります。

さらにそのcertificateからdiagramを再構成する場合、

```text
actual mapsは復元されたか？

category relationsはすべて含まれているか？

varianceは固定されているか？

objectwise reconstructionなのか
fully faithful reconstructionなのか？
```

を確認します。

globalizationする場合には、

```text
overlap mapsはactual mapsか？

cocycleはあるか？

effectivityは証明されているか？
```

を確認します。

最後にsourceへReturnする前に、

```text
source realizationは
要求するfeatureを本当にpreserve / reflectするか？

requested Return strengthに十分なrigidityがあるか？

final source-domain Return theoremが存在するか？
```

を確認します。

この一連の流れが、v21におけるhigh-dimensional projection structural analysisの実践的意味です。

---

## 36. Return strengthが重要な理由

あるprojectionがpersistent homologyの一つのdegreeしか観測していないとします。

二つのsource objectがdegree-zero persistenceでは同じでも、degree oneでは異なることがあります。

この場合、

```text
observed predicate Return = valid
```

であっても、

```text
full source-object reconstruction
filtered quasi-isomorphism
derived equivalence
```

は導けません。

これは文章上の違いではありません。

**information-loss boundaryの違い**です。

そのためv21では、Return targetとstrengthをtheorem statementの一部として保持します。

---

## 37. Design philosophy

AK-HPDSTはtheorem promotionについて意図的に保守的です。

### Explicit information loss

projectionがglobally faithfulでなくても構いません。

問題は、declared targetに対して十分かどうかです。

### Exact local structure before globalization

local valueやobject classは、actual mapやcoherenceの代用にはなりません。

### Finite proof only through a theorem

finite computationはsoundness / completeness / reconstruction theoremによって初めてfinite proofになります。

### No hidden infinite extrapolation

infinite conclusionにはfinite-to-infinite theoremが必要です。

### Return is target-relative

routeは、最も弱いnecessary componentが支えるstrengthを超えてReturnしません。

### Counterexamples are structural information

強い含意が失敗したなら、その失敗はload-bearing hypothesisを特定します。

### AI is an agent, not theorem authority

AIはsearch、proposal、transformation、formalization assistを行えます。

theorem strengthを決めるのは数学的routeです。

---

## 38. 現在のstable mathematical scope

v21 stable kernelが最も強いのは、概ね次の領域です。

```text
one-parameter constructible persistence over a field

finite certificate models

finite categories / finite posets

finite-dimensional diagrams

bounded complexes

finite projective generators

finite Morita reconstruction

finite Alexandrov descent

certified finite-state / Noetherian reductions

typed Bridge / Return composition
```

このstable scopeの外側には、controlled research interfaceとして、

```text
non-field coefficients
spectral sequences
dg / A_infinity structures
sheaves / stacks
multiparameter extraction
higher coherence
Iwasawa theory
p-adic analysis
Mirror / Fukaya-facing structures
PDE compactness / continuation
```

があります。

これらは自動的にstable-Core theoremではありません。

---

## 39. v21以降の研究方向

v21はfinite globalizationとtyped Return architectureを大きく閉じました。

一方で、次のより深い問題を露出させました。

もはや中心課題は単に、

```text
shadowをどうcertifyするか？
```

ではありません。

より本質的には、

```text
どのprojectionがtargetに必要な情報を保存するのか？

何が失われるのか？

失われた情報を補うために
どのadditional probeが必要なのか？

どのstrengthでsourceへReturnできるのか？
```

です。

これは将来的なProjection--Return / observability理論につながります。

v21 corpus内のsuccessor directionには、

- finite-state certificate compiler
- machine-checkable homotopy-coherent descent
- controlled Noetherian base上のfinite Morita
- compatible partial Returnのuniform calculus
- determinant / Fitting-ideal Return
- higher Bockstein reconstruction
- source-specific rigidity
- Iwasawa information-preservation
- p-adic L-function Return
- analytic / categorical applicationの拡張

などがあります。

これらはv21で完成済みの主張ではなく、後続研究programです。

---

## 40. Citation / source discipline

AK-HPDST v21.0.0のtheoremを引用する場合、可能な限り次を記録してください。

```text
theory version
source PDF
chapter / appendix
theorem / definition number
Claim UID
complete hypotheses
source / target types
comparison mode
detector stage
Return target / strength
source bindings
required artifacts
```

README、要約、diagram、生成説明、後続implementationはcanonical theorem statementの代用ではありません。

Final Claim Registerはidentityとadmissible useを管理しますが、

```text
registration != proof
```

です。

数学的sourceとproofが最終的な根拠です。

---

## 41. 最終的な位置づけ

AK-HPDST v21.0.0は、一つの問いに要約できます。

```text
複雑な数学対象を
制御されたshadowへ射影し、

有限のcertified evidenceへ圧縮し、

actual mathematical structureとして再構成し、

coherenceを捏造することなくglobalizeし、

証明した以上のことを言わずに
元の数学領域へReturnするにはどうすればよいか？
```

v21の回答はDual-Core architectureです。

```text
Core-P
    = robust finite persistence certification

        +

Core-DG
    = exact finite diagram reconstruction
      and finite globalization
```

これらを、

```text
finite-to-infinite reduction
higher transfer
coherence
rigidity
typed Bridge composition
target-relative Return
proof-DAG verification
source / claim governance
```

によって接続します。

AK-HPDST v21.0.0は、最終的には次のように位置づけられます。

```text
高次元・複雑・非局所なsource structureを
目的相対的なstructured shadowへ射影し、

有限証拠とactual mathematical structureを区別しながら
再構成・大域化し、

source-domain truthへ戻るために必要な
数学的矢印を一つずつ明示する
finite-proof and structural-projection architecture
```

そして、その中心原則は次です。

```text
A projected shadow may reveal the structure.

Only a proved Return carries the theorem home.
```

日本語で言えば、

```text
射影された影は、構造を明らかにすることができる。

しかし、その結論を元の数学対象へ持ち帰るのは、
証明されたReturnだけである。
```
