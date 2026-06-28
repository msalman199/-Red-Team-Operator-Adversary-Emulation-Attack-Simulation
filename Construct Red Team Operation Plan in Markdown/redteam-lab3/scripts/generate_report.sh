#!/bin/bash
# Red Team Report Generator

echo "=== Red Team Report Generator ==="
echo "Generating comprehensive report package..."

# Create report package directory
mkdir -p ~/redteam-lab3/report-package

# Copy all documents
cp ~/redteam-lab3/docs/*.md ~/redteam-lab3/report-package/
cp ~/redteam-lab3/reports/*.md ~/redteam-lab3/report-package/

# Copy all visualizations
cp ~/redteam-lab3/assets/*.png ~/redteam-lab3/report-package/ 2>/dev/null

# Create README
cat > ~/redteam-lab3/report-package/README.md << 'EOF'
# Red Team Assessment Report Package

## Contents
- operation-plan.md: Complete operation plan
- threat-intelligence.md: Threat intelligence analysis
- final-report.md: Executive summary and findings
- *.png: Visual threat heatmaps and analysis charts

## Usage
Review all documents in order:
1. Operation Plan
2. Threat Intelligence
3. Final Report with visualizations
EOF

echo "Report package created at: ~/redteam-lab3/report-package/"
ls -lh ~/redteam-lab3/report-package/
