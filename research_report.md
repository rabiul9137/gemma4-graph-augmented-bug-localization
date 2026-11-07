\# Graph-Augmented Repository Understanding for Gemma 4 Coding Agents



\## Abstract



Understanding a software repository is an important challenge for AI coding agents, particularly when locating bugs across multiple source files. This preliminary study investigates whether AST-based dependency graph retrieval can improve repository context selection and bug localization compared with full-context retrieval and random file retrieval.



We evaluate three retrieval strategies using Gemma 4 E2B-it: Full Retrieval, Graph Retrieval, and Random Retrieval. The benchmark currently contains three synthetic Python bug-localization tasks. Results show that Graph Retrieval achieved 100% root-cause accuracy, while Full Retrieval achieved 66.67%. Both methods achieved 66.67% accuracy for file, function, and faulty-statement localization. Random Retrieval performed substantially worse on the available valid predictions.



These findings are preliminary and should not be interpreted as conclusive evidence of general superiority. Further evaluation using larger benchmarks and real-world repositories is required.



\## 1. Introduction



Modern software repositories often contain multiple interconnected files. A bug in one file may depend on functions, classes, or modules defined elsewhere.



AI coding agents need relevant repository context to identify the location and cause of software defects.



Providing an entire repository as context may be inefficient, while random file selection may omit important dependencies.



This research explores whether Abstract Syntax Tree (AST)-based dependency graphs can help an AI coding agent select relevant source files for bug localization.



\## 2. Research Question



\*\*Does AST-based dependency graph retrieval improve bug localization compared with full-context retrieval and random file retrieval when using Gemma 4 E2B-it?\*\*



\## 3. Methodology



\### 3.1 Model and Environment



\- Model: Gemma 4 E2B-it

\- Execution platform: Google Colab

\- GPU: NVIDIA Tesla T4

\- Programming language: Python



\### 3.2 Retrieval Strategies



\*\*1. Full Retrieval\*\*



The complete available repository context is provided to the model for bug localization.



\*\*2. Graph Retrieval\*\*



An AST-based dependency graph is constructed from Python source files. Graph traversal using Breadth-First Search (BFS) selects related files to provide repository context.



\*\*3. Random Retrieval\*\*



Source files are selected randomly. Five random seeds are used to examine variation in retrieval results.



\### 3.3 Evaluation Metrics



The experiment evaluates:



\- File Accuracy: Whether the predicted buggy file is correct.

\- Function Accuracy: Whether the predicted function is correct.

\- Statement Accuracy: Whether the predicted faulty statement is correct.

\- Root Cause Accuracy: Whether the predicted explanation identifies the underlying defect.



\## 4. Experimental Results



The current benchmark contains three synthetic bug-localization tasks.



| Retrieval Method | File Accuracy | Function Accuracy | Statement Accuracy | Root Cause Accuracy |

|---|---:|---:|---:|---:|

| Full Retrieval | 66.67% | 66.67% | 66.67% | 66.67% |

| Graph Retrieval | 66.67% | 66.67% | 66.67% | 100.00% |

| Random Retrieval | 6.67% | 6.67% | 6.67% | 0.00% |



\### 4.1 Results Interpretation



Graph Retrieval achieved the highest observed root-cause accuracy in this preliminary experiment.



Both Full Retrieval and Graph Retrieval achieved identical file, function, and statement localization accuracy.



Random Retrieval performed poorly on the available valid predictions. However, some Random Retrieval outputs were missing or invalid. Therefore, its metric denominators differ from those of the other methods.



These results suggest that dependency-aware retrieval is worth investigating further. They do not establish that graph retrieval is universally better than full-context retrieval.



\## 5. Limitations



This study has several limitations:



1\. The benchmark contains only three synthetic Python bug-localization tasks.

2\. The benchmark is too small to support broad statistical conclusions.

3\. Random Retrieval contains missing or invalid predictions, resulting in different valid sample counts.

4\. Results may vary with model versions, prompts, repository structures, and retrieval configurations.

5\. Real-world open-source repository validation has not yet been completed.



\## 6. Conclusion



This preliminary study investigates AST-based dependency graph retrieval for repository understanding and bug localization using Gemma 4 E2B-it.



The initial results show that Graph Retrieval achieved 100% root-cause accuracy across the three evaluated synthetic tasks, compared with 66.67% for Full Retrieval.



Although promising, these results require validation on larger and more diverse benchmarks.



Future work will focus on expanding the benchmark, evaluating real-world repositories, improving retrieval reliability, and investigating the relationship between context selection and bug-localization performance.



\## 7. Reproducibility



The project repository contains the experimental notebook, benchmark task files, scoring results, and supporting documentation.



\*\*GitHub Repository:\*\*  

https://github.com/rabiul9137/gemma4-graph-augmented-bug-localization



\*\*Audited Results:\*\*  

`experiment\_7\_audited\_results.csv`



\*\*Detailed Scoring:\*\*  

`experiment\_7\_detailed\_scoring.csv`



\*\*Original Summary:\*\*  

`experiment\_7\_final\_summary.csv`



\---



\*\*Research Status:\*\* Preliminary experimental study. Further validation is required before making general claims.



