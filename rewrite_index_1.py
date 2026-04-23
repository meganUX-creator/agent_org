import re

with open('agent_org-main/index_1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find <div class="content-area" ...>
start_match = re.search(r'(<div class="content-area"[^>]*>)', html)
if not start_match:
    print("Could not find content-area")
    exit(1)

start_pos = start_match.end()

# The end is the closing tags
end_match = re.search(r'(    </div>\n</div>\n<script src="script.js"></script>\n</body>\n</html>)', html)
if not end_match:
    print("Could not find end tags")
    exit(1)

end_pos = end_match.start()

new_content = """
    <style>
        .dashboard-container {
            padding: 24px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            background: #0B1120;
            min-height: 100%;
        }
        .dash-card {
            background: #1E293B;
            border-radius: 12px;
            padding: 24px;
            border: 1px solid rgba(255,255,255,0.05);
        }
        
        /* Top Info Card */
        .info-card {
            padding: 24px 30px;
        }
        .info-grid {
            display: grid;
            grid-template-columns: 1fr 1fr 2fr;
            row-gap: 24px;
            column-gap: 40px;
        }
        .info-item {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .info-label {
            font-size: 13px;
            color: #94A3B8;
        }
        .info-value {
            font-size: 15px;
            color: #E2EAF5;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .text-bold { font-weight: 600; }
        .text-large { font-size: 24px; font-weight: 700; }
        .text-white { color: #FFFFFF; }
        .text-dim { color: #64748B; font-size: 14px; }
        .status-pill {
            display: inline-flex;
            align-items: center;
            padding: 2px 10px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 600;
        }
        .status-pill.status-normal {
            background: rgba(34, 197, 94, 0.15);
            color: #4ADE80;
            border: 1px solid rgba(34, 197, 94, 0.2);
        }
        .view-details-link {
            color: #38BDF8;
            font-size: 14px;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: color 0.2s;
        }
        .view-details-link:hover {
            color: #7DD3FC;
        }
        
        /* Commission Card */
        .commission-card {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 20px 30px;
        }
        .comm-title {
            font-size: 15px;
            font-weight: 600;
            color: #E2EAF5;
        }
        .comm-amount {
            font-size: 26px;
            font-weight: 700;
            color: #F59E0B;
            display: flex;
            align-items: center;
            gap: 12px;
            letter-spacing: 0.5px;
        }
        .comm-amount i {
            font-size: 16px;
            color: #64748B;
            cursor: pointer;
            transition: color 0.2s;
        }
        .comm-amount i:hover { color: #E2EAF5; }
        
        .btn-primary {
            background: #3B82F6;
            color: #FFFFFF;
            border: none;
            padding: 10px 24px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.2s;
        }
        .btn-primary:hover {
            background: #60A5FA;
        }
        
        /* Filter Row */
        .filter-row-dash {
            display: flex;
            align-items: center;
            gap: 16px;
        }
        .date-picker-wrap, .dropdown-wrap {
            background: #1E293B;
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 8px;
            padding: 10px 16px;
            display: flex;
            align-items: center;
            gap: 12px;
            color: #E2EAF5;
            font-size: 13px;
            cursor: pointer;
            transition: border-color 0.2s;
        }
        .date-picker-wrap:hover, .dropdown-wrap:hover {
            border-color: rgba(255,255,255,0.2);
        }
        .date-picker-wrap i, .dropdown-wrap i {
            color: #64748B;
        }
        .btn-search {
            padding: 10px 24px;
        }
        
        /* Metrics Grids */
        .metrics-grid-2 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }
        .metrics-grid-3 {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 20px;
        }
        
        .metric-card-large {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }
        .mc-icon-wrap {
            width: 44px;
            height: 44px;
            background: rgba(59, 130, 246, 0.15);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #3B82F6;
            font-size: 20px;
        }
        .metric-card-small {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        .mc-label {
            font-size: 13px;
            color: #94A3B8;
        }
        .mc-value {
            font-size: 28px;
            font-weight: 700;
            color: #FFFFFF;
            letter-spacing: 0.5px;
        }
    </style>

    <div class="dashboard-container">
        <!-- Top Info Card -->
        <div class="dash-card info-card">
            <div class="info-grid">
                <div class="info-item">
                    <div class="info-label">状态</div>
                    <div class="info-value"><span class="status-pill status-normal">正常</span></div>
                </div>
                <div class="info-item">
                    <div class="info-label">代理账号</div>
                    <div class="info-value text-bold">leozdfl</div>
                </div>
                <div class="info-item" style="grid-column: span 2; text-align: right; grid-row: 1 / span 2; justify-content: flex-start;">
                    <div class="info-label" style="margin-bottom: 10px;">当前额度</div>
                    <div class="info-value text-large text-white" style="justify-content: flex-end;">¥96,840,000.00</div>
                </div>
                
                <div class="info-item">
                    <div class="info-label">占返比</div>
                    <div class="info-value text-bold text-white">45% <i class="far fa-question-circle text-dim"></i></div>
                </div>
                <div class="info-item">
                    <div class="info-label">有效投注比</div>
                    <div class="info-value text-bold text-white">8% <i class="far fa-question-circle text-dim"></i></div>
                </div>
                <div class="info-item" style="grid-column: span 2; text-align: right; align-self: end;">
                    <a href="#" class="view-details-link" style="justify-content: flex-end;">查看详细信息 <i class="fas fa-chevron-down" style="font-size: 12px;"></i></a>
                </div>
            </div>
        </div>

        <!-- Unsettled Commission Card -->
        <div class="dash-card commission-card">
            <div class="comm-left">
                <div class="comm-title">未结算佣金</div>
            </div>
            <div class="comm-middle">
                <div class="comm-amount">123,456,789.00 <i class="fas fa-sync-alt"></i></div>
            </div>
            <div class="comm-right">
                <button class="btn-primary">立即结算</button>
            </div>
        </div>

        <!-- Date Filter Row -->
        <div class="filter-row-dash">
            <div class="date-picker-wrap">
                <i class="far fa-calendar-alt"></i>
                <span>2025-12-31 00:00:00 - 2025-12-31 23:59:59</span>
            </div>
            <div class="dropdown-wrap">
                <span>今日</span>
                <i class="fas fa-chevron-down" style="margin-left: 10px;"></i>
            </div>
            <button class="btn-primary btn-search">查询</button>
        </div>

        <!-- Main Metrics Cards -->
        <div class="metrics-grid-2">
            <div class="dash-card metric-card-large">
                <div class="mc-icon-wrap"><i class="fas fa-user-friends"></i></div>
                <div class="mc-label">代理总数</div>
                <div class="mc-value">0</div>
            </div>
            <div class="dash-card metric-card-large">
                <div class="mc-icon-wrap"><i class="far fa-credit-card"></i></div>
                <div class="mc-label">玩家总数</div>
                <div class="mc-value">0</div>
            </div>
        </div>

        <!-- Sub Metrics Cards -->
        <div class="metrics-grid-3">
            <div class="dash-card metric-card-small">
                <div class="mc-label">投注金额</div>
                <div class="mc-value">0.00</div>
            </div>
            <div class="dash-card metric-card-small">
                <div class="mc-label">总输赢</div>
                <div class="mc-value">0.00</div>
            </div>
            <div class="dash-card metric-card-small">
                <div class="mc-label">有效投注</div>
                <div class="mc-value">0.00</div>
            </div>
            <div class="dash-card metric-card-small">
                <div class="mc-label">有效投注佣金</div>
                <div class="mc-value">0.00</div>
            </div>
            <div class="dash-card metric-card-small">
                <div class="mc-label">占成盈亏</div>
                <div class="mc-value">0.00</div>
            </div>
            <div class="dash-card metric-card-small">
                <div class="mc-label">应得佣金</div>
                <div class="mc-value">0.00</div>
            </div>
        </div>
    </div>
"""

final_html = html[:start_pos] + "\n" + new_content + "\n" + html[end_pos:]

with open('agent_org-main/index_1.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Updated index_1.html with new dashboard layout.")
