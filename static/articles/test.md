# A Quick Refresher on Logic and Proofs

I was a terrible student for a large part of my life and that part included when I was expected to learn many important math concepts. 

In an attempt to rectify that gap I've been reading a textbook on discrete math (whoopie.)

Below is a brief summarization of the Logic and Proofs section and what I thought was important.

## Basic Propositional Logic

A **proposition** is a declarative sentence that is either true or false. Propositonal logic allows us to evaluate the truthfullness of **compound propositions** or series of declarative sentences joined by **logical operators**.

Propositional variables are usually denoted with the letters *p, q, r, ...* .

Basic logical operators:

| Operator | Name | Meaning | Example |
| -------- | ---- | ------- | ------- |
| ¬ | negation operator | NOT | ¬p |
| ∧ | conjunction | AND | p ∧ q |
| ∨ | disjunction | OR | p ∨ q |
| ⊕ | exclusive or | XOR | p ⊕ q |
| → | conditional statement | if _ then _ | p → q |
| ↔ | biconditional statement | if and only if _ then _ | p ↔ q |

## Propositional Equivalences

To be able to substitute propositions we need to be able to establish their equivalence.

A **tautology** is a compound proposition that is always true no matter its values.

A **contradiction** is one that is always false no matter its values.

A **contingency** is everything else (all the interesting ones).

Basic logical equivalences:

| Equivalence | Name |
| ----------- | ---- |
| p ∧ T ≡ p<br>p ∨ F ≡ p | Identity laws |
| p ∨ T ≡ T<br>p ∧ F ≡ F | Domination laws |
| p ∨ p ≡ p<br>p ∧ p ≡ p | Idempotent laws |
| ¬(¬p) ≡ p | Double negation law |
| p ∨ q ≡ q ∨ p<br>p ∧ q ≡ q ∧ p | Commutative laws |
| (p ∨ q) ∨ r ≡ p ∨ (q ∨ r)<br>(p ∧ q) ∧ r ≡ p ∧ (q ∧ r) | Associative laws |
| p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)<br>p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r) | Distributive laws |
| ¬(p ∧ q) ≡ ¬p ∨ ¬q<br>¬(p ∨ q) ≡ ¬p ∧ ¬q | De Morgan's laws |
| p ∨ (p ∧ q) ≡ p<br>p ∧ (p ∨ q) ≡ p | Absorption laws |
| p ∨ ¬p ≡ T<br>p ∧ ¬p ≡ F | Negation laws |

Logical equivalences involving conditional statements:

| Equivalence |
| ----------- |
| p → q ≡ ¬p ∨ q |
| p → q ≡ ¬q → ¬p |
| p ∨ q ≡ ¬p → q |
| p ∧ q ≡ ¬(p → ¬q) |
| ¬(p → q) ≡ p ∧ ¬q |
| (p → q) ∧ (p → r) ≡ p → (q ∧ r) |
| (p → r) ∧ (q → r) ≡ (p ∨ q) → r |
| (p → q) ∨ (p → r) ≡ p → (q ∨ r) |
| (p → r) ∨ (q → r) ≡ (p ∧ q) → r |

Logical equivalences involving biconditional statements:

| Equivalence |
| ----------- |
| p ↔ q ≡ (p → q) ∧ (q → p) |
| p ↔ q ≡ ¬p ↔ ¬q |
| p ↔ q ≡ (p ∧ q) ∨ (¬p ∧ ¬q) |
| ¬(p ↔ q) ≡ p ↔ ¬q |

## Predicates and Quantifiers


