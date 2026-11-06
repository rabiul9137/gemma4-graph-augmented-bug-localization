\# Graph-Augmented Repository Understanding for Gemma 4 Coding Agents



\## Research Overview



This project investigates whether graph-augmented repository understanding can help Gemma 4 coding agents localize bugs in Python repositories more efficiently than full-context and random file retrieval.



The study uses Gemma 4 E2B-it and a small synthetic benchmark containing three Python bug-localization tasks.



\## Research Question



Can an AST-based dependency graph improve repository context selection and bug localization compared with full-context and random retrieval strategies?



\## Methodology



Three retrieval strategies were evaluated:



1\. \*\*Full Retrieval:\*\* Provides the complete repository context.

2\. \*\*Graph Retrieval:\*\* Uses AST-based import dependency analysis and Breadth-First Search (BFS) to retrieve related files.

3\. \*\*Random Retrieval:\*\* Selects files randomly as a baseline.



The model analyzes the retrieved context and identifies the suspected buggy file, function, and faulty statement.



\## Experimental Setup



\- Model: Gemma 4 E2B-it

\- Platform: Google Colab

\- Hardware: NVIDIA Tesla T4 GPU

\- Programming Language: Python

\- Dependency Analysis: Python AST

\- Graph Traversal: Breadth-First Search (BFS)

\- Benchmark: 3 synthetic Python bug-localization tasks

\- Evaluation: 21 model evaluations across the experiment



\## Preliminary Results



| Metric | Result |

|---|---:|

| Average Graph Context Reduction | 57.33% |

| Full Retrieval File Localization Accuracy | 66.67% |

| Graph Retrieval File Localization Accuracy | 66.67% |

| Graph Retrieval Root-Cause Accuracy | 100% |



These are preliminary results from a small pilot benchmark, not evidence of general performance across real-world repositories.



\## Repository Structure



```text

gemma4-graph-augmented-bug-localization/

├── benchmark\_tasks/

├── Google\_The\_Gemma\_4\_Developer\_Agent\_Paper\_Track.ipynb

├── experiment\_7\_final\_summary.csv

├── experiment\_7\_detailed\_scoring.csv

├── benchmark\_tasks.zip

├── .gitignore

└── README.md

```



\## Files



\- \*\*Notebook:\*\* Experimental workflow and implementation.

\- \*\*Final Summary CSV:\*\* Aggregated experiment results.

\- \*\*Detailed Scoring CSV:\*\* Detailed evaluation records.

\- \*\*Benchmark Tasks:\*\* Synthetic Python repositories used in the experiments.



\## Limitations



\- Only three synthetic bug-localization tasks were evaluated.

\- The sample size is too small to support broad conclusions.

\- Root-cause accuracy was manually scored.

\- Patch correctness and automated patch testing were not evaluated.

\- The results do not establish that graph retrieval is superior to full retrieval.



\## Future Work



\- Expand the benchmark with real-world Python repositories.

\- Evaluate more bug types and repository structures.

\- Increase the number of experimental runs.

\- Automate evaluation and scoring.

\- Evaluate patch generation and automated test execution.

\- Compare graph construction and retrieval strategies.



\## Research Status



\*\*Status:\*\* Preliminary experimental study — ongoing research.



Further experiments and analysis will be added as the research progresses.



\## Author



Rabiul Islam



GitHub: https://github.com/rabiul9137



LinkedIn: https://linkedin.com/in/rabiulislam01/



