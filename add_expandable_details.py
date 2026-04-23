import re

with open('agent_org-main/index_1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS
css_to_add = """
        /* Expandable Details Panel */
        .expandable-details {
            display: none;
            margin-top: 24px;
        }
        .expandable-details.open {
            display: block;
            animation: fadeIn 0.3s ease;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-5px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .details-divider {
            height: 1px;
            background: rgba(255, 255, 255, 0.05);
            margin-bottom: 24px;
        }
        .details-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
        }
        .detail-col {
            display: flex;
            flex-direction: column;
        }
        .detail-row {
            display: flex;
            justify-content: space-between;
            padding: 16px 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.03);
            font-size: 13px;
        }
        .detail-row:last-child {
            border-bottom: none;
        }
        .d-label {
            color: #94A3B8;
        }
        .d-value {
            color: #E2EAF5;
            font-weight: 600;
        }
"""
html = html.replace('/* Commission Card */', css_to_add + '\n        /* Commission Card */')


# 2. Add HTML
html_to_add = """            </div>
            <!-- Expandable Details -->
            <div class="expandable-details" id="agent-details-panel">
                <div class="details-divider"></div>
                <div class="details-grid">
                    <!-- Left Column -->
                    <div class="detail-col">
                        <div class="detail-row">
                            <span class="d-label">开户时间</span>
                            <span class="d-value">2024-12-15 14:30:25</span>
                        </div>
                        <div class="detail-row">
                            <span class="d-label">最后登入时间</span>
                            <span class="d-value">2025-01-14 09:15:42</span>
                        </div>
                        <div class="detail-row">
                            <span class="d-label">姓名</span>
                            <span class="d-value">李经理</span>
                        </div>
                        <div class="detail-row">
                            <span class="d-label">电话</span>
                            <span class="d-value">+86 138 8888 8888</span>
                        </div>
                        <div class="detail-row">
                            <span class="d-label">电子邮件</span>
                            <span class="d-value">leozdfl@example.com</span>
                        </div>
                    </div>
                    <!-- Right Column -->
                    <div class="detail-col">
                        <div class="detail-row">
                            <span class="d-label">QQ</span>
                            <span class="d-value">123456789</span>
                        </div>
                        <div class="detail-row">
                            <span class="d-label">微信</span>
                            <span class="d-value">leozdfl_wx</span>
                        </div>
                        <div class="detail-row">
                            <span class="d-label">Zalo</span>
                            <span class="d-value">+84 90 123 4567</span>
                        </div>
                        <div class="detail-row">
                            <span class="d-label">Facebook</span>
                            <span class="d-value">leozdfl.fb</span>
                        </div>
                        <div class="detail-row">
                            <span class="d-label">WhatsApp</span>
                            <span class="d-value">+86 138 8888 8888</span>
                        </div>
                        <div class="detail-row">
                            <span class="d-label">Line</span>
                            <span class="d-value">leozdfl_line</span>
                        </div>
                        <div class="detail-row">
                            <span class="d-label">Telegram</span>
                            <span class="d-value">@leozdfl</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Unsettled Commission Card -->"""

html = html.replace("""            </div>
        </div>

        <!-- Unsettled Commission Card -->""", html_to_add)


# 3. Add onclick to a tag
html = html.replace('<a href="#" class="view-details-link">', '<a href="#" class="view-details-link" onclick="toggleDetails(event)">')

# 4. Add JS at the end
js_to_add = """<script>
    function toggleDetails(event) {
        event.preventDefault();
        const panel = document.getElementById('agent-details-panel');
        const icon = event.currentTarget.querySelector('i');
        if (panel.classList.contains('open')) {
            panel.classList.remove('open');
            icon.className = 'fas fa-chevron-down';
        } else {
            panel.classList.add('open');
            icon.className = 'fas fa-chevron-up';
        }
    }
</script>
<script src="script.js"></script>"""
html = html.replace('<script src="script.js"></script>', js_to_add)

with open('agent_org-main/index_1.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index_1.html with expandable details.")
