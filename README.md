## Infringement URL Analysis (Python & R)

### Objective
To parse and flatten a nested JSON file of infringement reports, extract infringing URLs, resolve their domains to IP addresses and generate meaningful summarizations.

### Key Tasks

- Flattened a nested JSON structure so each row corresponds to a single infringing URL.
- Extracted domain names from URLs.
- Resolved domains to their respective IP addresses.
- Used multiprocessing (4 CPUs) in R to parallelize data processing for performance.
- Created three summary insights from the dataset:
  - Top infringing domains.
  - IP frequency distribution.

### Deliverables

- `url_data_pipeline.py` – Python script for complete data processing pipeline.
- `url_data_analysis_rmarkdown.Rmd` – RMarkdown notebook with equivalent logic and visual summaries.
- `python_output.csv` – Final flattened dataset.
- `rmarkdown_output.csv` – Final flattened dataset of R-based logic.
- `response` – Dataset.
