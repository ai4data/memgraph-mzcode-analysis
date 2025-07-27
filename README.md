# Memgraph Graph Database Tutorial with SSIS Northwind

This repository contains a comprehensive tutorial for learning graph databases using Memgraph and the SSIS Northwind dataset. The tutorial demonstrates how traditional ETL systems can be analyzed and understood through graph database concepts.

## Background

### What is Metazcode?
Metazcode is a tool that analyzes legacy ETL systems (like SSIS packages) and converts them into graph representations. It extracts metadata, data lineage, dependencies, and business logic from complex ETL workflows and stores them in graph databases for better analysis and migration planning.

### Why Graph Databases?
Graph databases excel at representing and querying complex relationships between data entities. For ETL systems, this means:
- **Data Lineage Tracking**: Follow data from source to destination across multiple transformations
- **Dependency Analysis**: Understand how packages, operations, and tables depend on each other
- **Impact Analysis**: Quickly identify what's affected when making changes
- **Migration Planning**: Visualize system complexity and plan modernization efforts

### Why Memgraph?
Memgraph is a high-performance graph database that:
- Uses Cypher query language (same as Neo4j)
- Provides real-time analytics capabilities
- Supports materialized views for fast querying
- Integrates well with Python for data analysis

## Dataset: SSIS Northwind

The tutorial uses the classic Northwind database implemented as SSIS (SQL Server Integration Services) packages. This provides a realistic but manageable example of:
- Multiple ETL packages with interdependencies
- Data transformations and business logic
- Source-to-target data flows
- Connection management

## Tutorial Structure

### 📚 Jupyter Notebooks

#### `01_getting_started.ipynb`
**Purpose**: Introduction to graph databases and Memgraph basics
- Connect to Memgraph database
- Verify SSIS Northwind data is loaded
- Understand basic graph concepts (nodes, relationships, properties)
- Explore analytics-ready features and materialized views
- Basic Cypher queries for data exploration

#### `02_exploring_ssis_structure.ipynb`
**Purpose**: Deep dive into SSIS components represented as graph structures
- Analyze SSIS packages (pipelines) and their operations
- Understand data flow relationships (READS_FROM, WRITES_TO)
- Identify shared resources and potential bottlenecks
- Explore package dependencies and execution order
- Visualize system complexity with charts and graphs

#### `03_analytics_ready_features.ipynb`
**Purpose**: Leverage pre-computed analytics for fast insights
- Work with materialized views for performance
- Access pre-computed SQL operations catalog
- Analyze cross-package dependencies efficiently
- Explore data lineage and business rules catalogs
- Compare performance: materialized views vs raw queries
- Build simple migration assessment tools

#### `04_advanced_queries.ipynb`
**Purpose**: Master complex Cypher queries and analysis patterns
- Complex path analysis for data lineage tracking
- Advanced aggregation queries for system complexity
- Pattern matching to identify ETL patterns and anti-patterns
- Performance optimization techniques
- Custom analytics functions for reusable analysis
- Network data preparation for visualization tools

#### `05_migration_analysis.ipynb`
**Purpose**: Practical migration planning and risk assessment
- Comprehensive migration complexity assessment
- Execution sequence planning based on dependencies
- Risk analysis and mitigation strategies
- Target platform compatibility analysis (Azure Data Factory, AWS Glue, etc.)
- Data lineage impact assessment
- Generate migration reports and recommendations

### 🐍 Python Scripts

Converted versions of the notebooks are also available as standalone Python scripts:
- `01_getting_started.py`
- `02_exploring_ssis_structure.py`
- Additional conversions available on request

### 🛠️ Utility Scripts

- `debug_metadata.py`: Debug script for examining metadata structure
- `test-connection.py`: Connection testing utility

## Prerequisites

### Software Requirements
- **Memgraph Database**: Running instance (Docker recommended)
- **Python 3.11+**: With virtual environment support
- **Jupyter Notebook**: For interactive exploration (optional)

### Data Requirements
- SSIS Northwind dataset analyzed and loaded into Memgraph using metazcode
- Analytics-ready optimization applied for materialized views

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start Memgraph
```bash
# Using Docker
docker run -p 7687:7687 -p 7444:7444 memgraph/memgraph

# Or using docker-compose (if available)
docker-compose up -d
```

### 3. Load SSIS Data (if not already done)
```bash
# Using metazcode with Memgraph backend
METAZCODE_DB_BACKEND=memgraph python -m metazcode full --path data/ssis/ssis_northwind
```

### 4. Start Learning
```bash
# Option 1: Jupyter Notebooks (Interactive)
jupyter notebook

# Option 2: Python Scripts (Direct execution)
python 01_getting_started.py
```

## Learning Path

### For Graph Database Beginners
1. Start with `01_getting_started.ipynb` to understand basic concepts
2. Work through `02_exploring_ssis_structure.ipynb` to see real-world applications
3. Explore `03_analytics_ready_features.ipynb` for performance insights

### For ETL/Migration Engineers
1. Begin with `01_getting_started.ipynb` for context
2. Focus on `04_advanced_queries.ipynb` for analysis techniques
3. Deep dive into `05_migration_analysis.ipynb` for practical applications

### For Data Engineers
1. Review all notebooks in sequence
2. Experiment with custom queries and analysis
3. Adapt patterns to your own ETL systems

## Key Concepts Covered

- **Graph Database Fundamentals**: Nodes, relationships, properties
- **Cypher Query Language**: From basic to advanced patterns
- **Data Lineage**: Tracking data flow through complex systems
- **Dependency Analysis**: Understanding system interconnections
- **Performance Optimization**: Materialized views and query tuning
- **Migration Planning**: Risk assessment and execution strategies
- **Analytics-Ready Systems**: Pre-computed insights for fast analysis

## Troubleshooting

### Common Issues

**Connection Failed**
- Ensure Memgraph is running on localhost:7687
- Check firewall settings
- Verify credentials (default: empty username/password)

**No Data Found**
- Confirm SSIS Northwind data was loaded with metazcode
- Check that analytics-ready optimization was applied
- Verify database backend was set to Memgraph

**Query Errors**
- Some functions (like JSON_EXTRACT) may not be available in all Memgraph versions
- Use Python JSON parsing as fallback
- Check Cypher syntax compatibility

### Getting Help

1. Check the troubleshooting sections in each notebook
2. Review the debug scripts for data validation
3. Consult Memgraph documentation for Cypher syntax
4. Verify metazcode configuration and data loading

## Contributing

This tutorial is designed for learning and can be adapted for:
- Different ETL systems (beyond SSIS)
- Other graph databases (Neo4j, Amazon Neptune)
- Custom analysis patterns and use cases

Feel free to extend the examples and share improvements!

## License

This tutorial is provided for educational purposes. Please respect the licenses of the underlying tools (Memgraph, metazcode) when using in production environments.