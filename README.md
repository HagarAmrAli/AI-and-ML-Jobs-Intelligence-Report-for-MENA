# AI-and-ML-Jobs-Intelligence-Report-for-MENA
Below is a `README.md` file for the CLI-based version of the multi-agent system for generating an intelligence report on AI and Machine Learning job trends in the MENA region (without Streamlit). The README provides an overview, setup instructions, usage details, and other relevant information in English, as per the previous implementation's language.

---

# AI & ML Jobs Intelligence Report for MENA Region

A multi-agent system designed to analyze job trends for AI and Machine Learning roles in the MENA region and generate a customized PDF report. The system collects job data, extracts structured information, analyzes trends, and produces a professional report with visualizations, all through a command-line interface (CLI).

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Extending the System](#extending-the-system)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Project Overview
This project implements a multi-agent system to:
1. Collect job listings for AI/ML roles in the MENA region (currently simulated with mock data).
2. Extract structured data (job titles, skills, and locations).
3. Analyze trends to identify the top 10 job titles, required skills, and geographic distribution.
4. Generate a professional PDF report with tables and visualizations.

The system uses a CLI for user input, allowing users to specify countries and a time period for analysis. It is designed to be extensible for real web scraping and scalable data processing.

## Features
- **Multi-Agent Architecture**:
  - `WebSearchAgent`: Simulates fetching job listings (extendable for real scraping).
  - `DataExtractionAgent`: Extracts job titles, skills, and countries.
  - `TrendAnalysisAgent`: Analyzes data to identify trends and generate visualizations.
  - `ReportWriterAgent`: Creates a PDF report with tables and charts.
- **CLI Interface**: Configure countries and time period via command-line arguments.
- **Visualizations**: Bar charts for top jobs, skills, and geographic distribution.
- **Output**: Professional PDF report saved in the `reports` directory.

## Project Structure
```
├── main.py                        # Main script to orchestrate agents and handle CLI input
├── agents/
│   ├── web_search_agent.py       # Agent for collecting job listings
│   ├── data_extraction_agent.py  # Agent for extracting structured data
│   ├── trend_analysis_agent.py   # Agent for analyzing trends and generating plots
│   └── report_writer_agent.py    # Agent for generating PDF report
├── reports/
│   └── MENA_AI_Jobs_Report.pdf   # Generated PDF report
├── requirements.txt              # Required Python libraries
├── README.md                     # Project documentation
```

## Requirements
- Python 3.8 or higher
- Libraries listed in `requirements.txt`:
  ```
  pandas==2.2.2
  requests==2.32.3
  beautifulsoup4==4.12.3
  matplotlib==3.9.2
  seaborn==0.13.2
  reportlab==4.2.2
  numpy==2.0.2
  ```

## Setup Instructions
1. **Clone or Download the Project**:
   Download the project files to a directory, e.g., `C:\Users\YourName\ai-ml-jobs-mena`.

2. **Set Up a Python Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Navigate to the project directory and install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create the `reports` Directory** (optional):
   The system automatically creates the `reports` directory, but you can create it manually if needed:
   ```bash
   mkdir reports
   ```

## Usage
Run the main script using the CLI to generate the report. The script accepts optional arguments for countries and time period.

### Default Run
Use default settings (countries: Egypt, Saudi Arabia, UAE; time period: 6 months):
```bash
python main.py
```

### Custom Run
Specify countries and time period:
```bash
python main.py --countries Egypt UAE Qatar Jordan --time-period 12
```

### Available Options
- `--countries`: List of MENA countries (space-separated). Options: Egypt, Saudi Arabia, UAE, Qatar, Jordan, Lebanon, Morocco. Default: Egypt, Saudi Arabia, UAE.
- `--time-period`: Time period in months (1-12). Default: 6.

### Example Output
```
AI & ML Jobs Intelligence Report for MENA Region
Selected Countries: Egypt, UAE, Qatar, Jordan
Time Period: 12 months

Starting analysis...
Fetching job listings...
Extracting job details...
Analyzing job trends...
Generating PDF report...

Report generated successfully at: reports/MENA_AI_Jobs_Report.pdf
```

The generated PDF report (`MENA_AI_Jobs_Report.pdf`) is saved in the `reports` directory and includes:
- Top 10 AI/ML job titles with counts.
- Top required skills with frequencies.
- Geographic distribution of jobs by country.
- Visualizations (bar charts) for each analysis.

## Extending the System
- **Real Web Scraping**: Replace mock data in `web_search_agent.py` with actual scraping using `BeautifulSoup` or `Selenium` for platforms like LinkedIn, Bayt, or Wuzzuf. Handle authentication and rate limits as needed.
- **Database Integration**: Store job listings in a database (e.g., SQLite) for scalability.
- **Additional Analysis**: Add agents for sentiment analysis, salary trends, or real-time data updates.
- **Input Validation**: Enhance `main.py` to validate CLI inputs (e.g., check for empty country lists).

## Troubleshooting
- **ModuleNotFoundError**:
  Ensure all dependencies are installed:
  ```bash
  pip install -r requirements.txt
  ```
  Verify the Python environment:
  ```bash
  python --version
  pip list
  ```
- **FileNotFoundError**:
  If errors occur when saving plots or the PDF, ensure write permissions in the project directory. Create the `reports` directory manually if needed:
  ```bash
  mkdir reports
  ```
- **Plotting Issues**:
  If visualizations fail, ensure Matplotlib uses the `Agg` backend. Add to `trend_analysis_agent.py`:
  ```python
  import matplotlib
  matplotlib.use('Agg')
  ```
- **Permissions**: Run the command prompt as an administrator if you encounter permission errors.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details (if applicable).

---


