with open('agent_org-main/index_1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add a style block after styles.css to reset the body for the sidebar layout
fix_style = """
    <style>
        body {
            padding: 0 !important;
            justify-content: flex-start !important;
            align-items: stretch !important;
        }
        .container {
            margin: 20px auto !important;
        }
    </style>
"""

html = html.replace('<link rel="stylesheet" href="styles.css">', '<link rel="stylesheet" href="styles.css">' + fix_style)

with open('agent_org-main/index_1.html', 'w', encoding='utf-8') as f:
    f.write(html)
