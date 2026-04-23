import re

# Read statistical_reports.html
with open('agent_org-main/statistical_reports.html', 'r', encoding='utf-8') as f:
    stat_html = f.read()

# Extract everything up to the end of topbar
# We'll use regex to find the closing div of topbar
topbar_end_match = re.search(r'(<div class="topbar">.*?</button>.*?<div class="topbar-title">.*?<i class="fas fa-chart-bar"></i>.*?<span>统计报表</span>.*?</div>.*?</div>)', stat_html, re.DOTALL)

if topbar_end_match:
    header_part = stat_html[:topbar_end_match.end()]
    
    # Change topbar title to Home
    header_part = header_part.replace('<i class="fas fa-chart-bar"></i>', '<i class="fas fa-home"></i>')
    header_part = header_part.replace('<span>统计报表</span>', '<span>首页</span>')
    
    # Add content-area div
    header_part += '\n    <div class="content-area" style="overflow-y: auto; flex-direction: column;">\n'
else:
    # Fallback if regex fails
    lines = stat_html.split('\n')
    header_lines = []
    for line in lines:
        header_lines.append(line)
        if '<div class="topbar-title">' in line:
            # Skip the next two lines (i, span, /div) and add our own
            pass
    header_part = "FAILED"

if header_part != "FAILED":
    # Read index.html
    with open('agent_org-main/index.html', 'r', encoding='utf-8') as f:
        idx_html = f.read()
    
    # Extract container and settings-dropdown
    container_match = re.search(r'(<div class="container">.*</div>\s*<div id="settings-dropdown"[^>]*>.*?</ul>\s*</div>)', idx_html, re.DOTALL)
    
    if container_match:
        content_part = container_match.group(1)
        
        # Assemble
        final_html = header_part + content_part + '\n    </div>\n</div>\n<script src="script.js"></script>\n</body>\n</html>'
        
        # Change title
        final_html = final_html.replace('<title>统计报表 - Casino 后台</title>', '<title>首页 - Casino 后台</title>')
        
        # Change active nav item
        final_html = final_html.replace('<div class="nav-item active" onclick="window.location.href=\'statistical_reports.html\'">', '<div class="nav-item" onclick="window.location.href=\'statistical_reports.html\'">')
        final_html = final_html.replace('<div class="nav-item" onclick="window.location.href=\'index_1.html\'">', '<div class="nav-item active" onclick="window.location.href=\'index_1.html\'">')
        
        # Also need to make sure styles.css is included because container needs it
        if '<link rel="stylesheet" href="styles.css">' not in final_html:
            final_html = final_html.replace('</style>', '</style>\n    <link rel="stylesheet" href="styles.css">')
            
        with open('agent_org-main/index_1.html', 'w', encoding='utf-8') as f:
            f.write(final_html)
        print("Successfully generated index_1.html with sidebar.")
    else:
        print("Could not find container in index.html")
        import shutil
        shutil.copy('agent_org-main/index.html', 'agent_org-main/index_1.html')
        print("Fallback: Copied index.html to index_1.html")
else:
    print("Could not parse statistical_reports.html")
    import shutil
    shutil.copy('agent_org-main/index.html', 'agent_org-main/index_1.html')
    print("Fallback: Copied index.html to index_1.html")

