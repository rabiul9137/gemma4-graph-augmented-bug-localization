\# Graph-Augmented Repository Understanding for Gemma 4 Coding Agents: A Preliminary Study of Dependency-Aware Bug Localization



\## Abstract



Repository-level bug localization is a challenging task for AI coding agents because software defects may involve dependencies across multiple source files. This preliminary study investigates whether Abstract Syntax Tree (AST)-based dependency graph retrieval can improve bug localization compared with full-context and random retrieval.



We evaluate three retrieval strategies using Gemma 4 E2B-it: Full Retrieval, Graph Retrieval, and Random Retrieval. The initial benchmark consists of three synthetic Python bug-localization tasks. Graph Retrieval achieves 66.67% file, function, and statement accuracy and 100% root-cause accuracy. Full Retrieval achieves 66.67% across all four metrics. Random Retrieval demonstrates substantially lower accuracy among valid predictions, although missing outputs result in different evaluation denominators.



The findings suggest that dependency-aware retrieval is a promising direction for repository understanding. However, the small synthetic benchmark prevents broad conclusions. Larger benchmarks and real-world repository experiments are necessary.



\*\*Keywords:\*\* AI Coding Agents, Repository Understanding, Bug Localization, AST, Dependency Graph, Graph Retrieval, Gemma 4, Code Intelligence.



\## 1. Introduction



AI coding agents increasingly assist developers in understanding, modifying, and debugging software repositories. However, repository-level reasoning remains challenging because relevant information can be distributed across multiple files.



A coding agent must identify relevant source files, understand their dependencies, locate faulty functions, and determine the underlying cause of a defect.



Three possible strategies for selecting repository context are:



1\. Full-context retrieval.

2\. Dependency-aware graph retrieval.

3\. Random file retrieval.



Full-context retrieval provides broad information but may include irrelevant files. Random retrieval does not explicitly consider software dependencies. Graph retrieval uses structural relationships between source files to select potentially relevant context.



This study investigates whether AST-based dependency graph retrieval can improve bug localization with Gemma 4 E2B-it.



\## 2. Research Question



Does AST-based dependency graph retrieval improve repository-level bug localization compared with full-context retrieval and random file retrieval?



\## 3. Methodology



\### 3.1 Experimental Environment



\- Language: Python

\- Model: Gemma 4 E2B-it

\- Platform: Google Colab

\- GPU: NVIDIA Tesla T4

\- Benchmark: Three synthetic Python bug-localization tasks



\### 3.2 Retrieval Approaches



\*\*Full Retrieval:\*\* The available repository context is provided to the model.



\*\*Graph Retrieval:\*\* An AST-based dependency graph represents relationships between Python source files. Breadth-First Search (BFS) is used to select related files for repository context.



\*\*Random Retrieval:\*\* Files are selected randomly using five different random seeds.



\### 3.3 Evaluation Metrics



Four metrics are used:



\- File Accuracy

\- Function Accuracy

\- Faulty Statement Accuracy

\- Root Cause Accuracy



Accuracy is calculated across all evaluation records. Abstentions (Uncertain predictions) and missing metric scores are counted as incorrect predictions (0).



\### 3.4 Experimental Design



The evaluation includes:



\- 3 Full Retrieval evaluations.

\- 3 Graph Retrieval evaluations.

\- 15 Random Retrieval evaluations across five random seeds.



This produces 21 evaluation records in total.



\## 4. Results



| Method | File | Function | Statement | Root Cause |

|---|---:|---:|---:|---:|

| Full Retrieval | 66.67% | 66.67% | 66.67% | 66.67% |

| Graph Retrieval | 66.67% | 66.67% | 66.67% | 100.00% |

| Random Retrieval | 6.67% | 6.67% | 6.67% | 0.00% |



\### 4.1 Discussion



Graph Retrieval and Full Retrieval achieved identical results for file, function, and faulty-statement localization.



Graph Retrieval achieved higher observed root-cause accuracy, with all three evaluations classified as correct.



Random Retrieval achieved substantially lower accuracy among valid predictions. However, random abstentions and missing metric scores were counted as incorrect, so all metrics use the full set of 15 random evaluations.



These results provide preliminary evidence that dependency-aware retrieval may help an AI coding agent reason about repository-level defects.



The results do not establish general superiority of graph retrieval.



\## 5. Limitations



This study has several important limitations:



1\. Only three synthetic Python benchmark tasks were evaluated.

2\. The small benchmark does not support statistically strong generalization.

3\. Random Retrieval produced abstentions or unscored outputs, which are counted as incorrect predictions (0) in the audited evaluation.

4\. Real-world open-source repositories have not yet been evaluated.

5\. The effects of different repository sizes, graph configurations, and context budgets require further investigation.



\## 6. Conclusion



This preliminary study examines AST-based dependency graph retrieval for bug localization using Gemma 4 E2B-it.



The observed results show that Graph Retrieval achieved 100% root-cause accuracy across three synthetic tasks, compared with 66.67% for Full Retrieval. Both approaches achieved the same file, function, and statement accuracy.



The findings motivate further investigation of graph-based repository context selection. However, larger and more realistic experiments are required before drawing general conclusions.



\## 7. Future Work



Future research should investigate:



1\. Expanding the benchmark to at least 15 diverse bug-localization tasks.

2\. Evaluating real-world open-source Python repositories.

3\. Comparing retrieval methods under controlled context-token budgets.

4\. Measuring retrieval precision and recall.

5\. Repeating experiments with multiple random seeds and model runs.

6\. Reporting missing predictions and valid sample counts transparently.

7\. Evaluating whether dependency graph quality affects bug-localization performance.



\## 8. Reproducibility and Research Artifacts



\*\*GitHub Repository:\*\*  

https://github.com/rabiul9137/gemma4-graph-augmented-bug-localization



The repository contains the experimental notebook, benchmark tasks, scoring data, audited results, and preliminary research report.



\## Research Status



Preliminary experimental study. This manuscript is a research draft and has not been peer-reviewed. Additional validation is required before conference or journal submission.

