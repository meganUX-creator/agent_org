document.addEventListener('DOMContentLoaded', () => {
    // Current breadcrumb path
    let breadcrumbPath = ['leozdfl'];
    const breadcrumbContainer = document.getElementById('breadcrumb');

    // Save initial table data for Level 0
    const initialOrgHTML = document.getElementById('org-table-body').innerHTML;
    const initialMembersHTML = document.getElementById('members-table-body').innerHTML;
    const initialOrgCount = document.getElementById('tab-count-org').textContent;
    const initialMembersCount = document.getElementById('tab-count-members').textContent;

    // View Mode Switching (Breadcrumb vs Tree)
    const btnModeBreadcrumb = document.getElementById('btn-mode-breadcrumb');
    const btnModeTree = document.getElementById('btn-mode-tree');
    const viewModeBreadcrumb = document.getElementById('view-mode-breadcrumb');
    const viewModeTree = document.getElementById('view-mode-tree');

    if (btnModeBreadcrumb && btnModeTree) {
        btnModeBreadcrumb.addEventListener('click', () => {
            btnModeBreadcrumb.classList.add('active');
            btnModeTree.classList.remove('active');
            viewModeBreadcrumb.style.display = 'block';
            viewModeTree.style.display = 'none';
        });

        btnModeTree.addEventListener('click', () => {
            btnModeTree.classList.add('active');
            btnModeBreadcrumb.classList.remove('active');
            viewModeBreadcrumb.style.display = 'none';
            viewModeTree.style.display = 'block';
        });
    }

    // Tree View Logic (Selection and Toggle)
    document.addEventListener('click', (e) => {
        // Toggle Expand/Collapse
        if (e.target.classList.contains('toggle-icon')) {
            const node = e.target.closest('.tree-node');
            const children = node.querySelector('.node-children');
            if (children) {
                const isHidden = children.style.display === 'none';
                children.style.display = isHidden ? 'block' : 'none';
                e.target.classList.toggle('fa-chevron-right', !isHidden);
                e.target.classList.toggle('fa-chevron-down', isHidden);
            }
            return; // Don't trigger selection if only toggling
        }

        // Select node
        const nodeHeader = e.target.closest('.node-header');
        if (nodeHeader) {
            document.querySelectorAll('.tree-node').forEach(node => node.classList.remove('active'));
            nodeHeader.parentElement.classList.add('active');

            // Update Right Side Info
            const accountName = nodeHeader.querySelector('span').textContent;
            const detailAccount = document.querySelector('.tree-detail .account-name');
            const detailUid = document.querySelector('.tree-detail .uid-tag');
            
            if (detailAccount) detailAccount.textContent = accountName;
            if (detailUid) detailUid.textContent = `UID: ${Math.floor(Math.random() * 899999) + 100000}`;
            
            // Sync table data with actual hierarchy children
            const listBody = document.querySelector('.detail-list-body');
            const nodeChildrenDiv = nodeHeader.parentElement.querySelector('.node-children');
            let mockRows = '';

            if (nodeChildrenDiv) {
                // Get direct child tree-nodes
                const subNodes = Array.from(nodeChildrenDiv.children).filter(child => child.classList.contains('tree-node'));
                subNodes.forEach(sub => {
                    const subName = sub.querySelector('.node-header span').textContent;
                    const balance = (Math.random() * 50000 + 1000).toFixed(2);
                    const ratio = Math.floor(Math.random() * 30 + 15);
                    mockRows += `
                        <div class="detail-item">
                            <div class="item-account">
                                <span>${subName}</span>
                            </div>
                            <div class="item-balance highlight-green">${parseFloat(balance).toLocaleString('en-US', {minimumFractionDigits: 2})}</div>
                            <div class="item-ratio">${ratio}%</div>
                        </div>
                    `;
                });
            }

            if (!mockRows) {
                mockRows = '<div style="padding: 100px 20px; text-align: center; color: var(--text-muted); opacity: 0.6;">無下級組織數據</div>';
            }
            
            if (listBody) {
                listBody.innerHTML = mockRows;
                listBody.style.opacity = '0.4';
                setTimeout(() => listBody.style.opacity = '1', 80);
            }
        }
    });

    // Detail Tab Selection
    document.querySelectorAll('.detail-tab').forEach(tab => {
        tab.addEventListener('click', () => {
            tab.parentElement.querySelectorAll('.detail-tab').forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
        });
    });

    function renderBreadcrumbs() {
        breadcrumbContainer.innerHTML = '';
        
        const MAX_VISIBLE = 5;
        let itemsToRender = [];
        
        if (breadcrumbPath.length <= MAX_VISIBLE) {
            itemsToRender = breadcrumbPath.map((item, index) => ({ item, index }));
        } else {
            itemsToRender = [
                { item: breadcrumbPath[0], index: 0 },
                { item: '...', index: -1 },
                { item: breadcrumbPath[breadcrumbPath.length - 3], index: breadcrumbPath.length - 3 },
                { item: breadcrumbPath[breadcrumbPath.length - 2], index: breadcrumbPath.length - 2 },
                { item: breadcrumbPath[breadcrumbPath.length - 1], index: breadcrumbPath.length - 1 }
            ];
        }

        itemsToRender.forEach((obj, idx) => {
            const { item, index } = obj;
            const isLast = idx === itemsToRender.length - 1;
            
            const span = document.createElement('span');
            span.classList.add('breadcrumb-item');
            
            if (index === 0 && item === 'leozdfl') {
                span.innerHTML = `${item} <span class="admin-badge">總代理</span>`;
            } else {
                span.textContent = item;
            }
            
            if (item === '...') {
                // Not clickable dots
            } else if (isLast) {
                span.classList.add('current');
            } else {
                span.classList.add('clickable');
                span.addEventListener('click', () => {
                    breadcrumbPath = breadcrumbPath.slice(0, index + 1);
                    renderBreadcrumbs();
                    loadDataForLevel();
                });
            }
            
            breadcrumbContainer.appendChild(span);
            
            if (!isLast) {
                const icon = document.createElement('i');
                icon.className = 'fas fa-chevron-right breadcrumb-separator';
                breadcrumbContainer.appendChild(icon);
            }
        });
    }

    function loadDataForLevel() {
        const level = breadcrumbPath.length - 1;
        const orgBody = document.getElementById('org-table-body');
        const membersBody = document.getElementById('members-table-body');
        const orgCount = document.getElementById('tab-count-org');
        const membersCount = document.getElementById('tab-count-members');

        if (level === 0) {
            orgBody.innerHTML = initialOrgHTML;
            membersBody.innerHTML = initialMembersHTML;
            orgCount.textContent = initialOrgCount;
            membersCount.textContent = initialMembersCount;
        } else {
            // Generate dummy subordinate data
            const currentUser = breadcrumbPath[level];
            const numSubAgents = Math.floor(Math.random() * 5) + 1;
            const numSubMembers = Math.floor(Math.random() * 8) + 2;
            
            orgCount.textContent = `(${numSubAgents})`;
            membersCount.textContent = `(${numSubMembers})`;

            let orgHTML = '';
            for(let i=1; i<=numSubAgents; i++) {
                // Generate more distinct sub-account names (e.g., AG_mas_1234)
                const prefix = currentUser.substring(0, 3).toUpperCase();
                const randomId = Math.floor(Math.random() * 9000) + 1000;
                const distinctName = `AG_${prefix}_${randomId}`;
                
                orgHTML += `
                    <tr>
                        <td>${distinctName} <i class="fas fa-cog settings-icon" title="設定"></i></td>
                        <td class="balance">${(Math.random() * 10000).toFixed(2)}</td>
                        <td>10.00%</td>
                        <td>0.50%</td>
                        <td class="date-time">2024-03-01<br>10:00:00</td>
                        <td class="date-time highlight-blue">2024-03-25<br>09:15:00</td>
                        <td><span class="status-pill status-normal">正常</span></td>
                        <td class="actions">
                            <button class="btn-primary">進入下級 (${Math.floor(Math.random()*3)})</button>
                        </td>
                    </tr>`;
            }
            orgBody.innerHTML = orgHTML;

            let membersHTML = '';
            for(let i=1; i<=numSubMembers; i++) {
                const prefix = currentUser.substring(0, 3).toUpperCase();
                const randomId = Math.floor(Math.random() * 9000) + 1000;
                const distinctMemName = `MEM_${prefix}_${randomId}`;
                
                membersHTML += `
                    <tr>
                        <td>${distinctMemName} <i class="fas fa-cog settings-icon" title="設定"></i></td>
                        <td class="balance">${(Math.random() * 5000).toFixed(2)}</td>
                        <td>5.00%</td>
                        <td>0.20%</td>
                        <td class="date-time">2024-02-15<br>14:30:00</td>
                        <td class="date-time highlight-blue">2024-03-24<br>20:45:11</td>
                        <td><span class="status-pill status-normal">離線</span></td>
                    </tr>`;
            }
            membersBody.innerHTML = membersHTML;

            // Update Total Count in Pagination Bar
            const totalCountSpan = document.getElementById('total-count');
            if (totalCountSpan) {
                const total = numSubAgents + numSubMembers;
                totalCountSpan.textContent = total;
            }
        }
    }

    renderBreadcrumbs();

    const tabs = document.querySelectorAll('.tab');
    const orgContent = document.getElementById('tab-content-org');
    const membersContent = document.getElementById('tab-content-members');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            
            if (tab.id === 'tab-org') {
                orgContent.style.display = 'block';
                membersContent.style.display = 'none';
            } else {
                orgContent.style.display = 'none';
                membersContent.style.display = 'block';
            }
        });
    });

    // Handle "進入下級" button clicks (only for organization table)
    document.addEventListener('click', (e) => {
        if (e.target && e.target.classList.contains('btn-primary') && e.target.textContent.includes('進入下級')) {
            const row = e.target.closest('tr');
            if (row) {
                // Get clean username text from the first cell (ignores icon)
                const usernameCell = row.cells[0];
                const usernameText = usernameCell.innerText.trim();
                
                breadcrumbPath.push(usernameText);
                renderBreadcrumbs();
                loadDataForLevel();
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        }
    });

    // Handle Page Size Dropdown
    const pageSizeToggle = document.getElementById('page-size-toggle');
    const pageSizeMenu = document.getElementById('page-size-menu');
    const currentPageSizeSpan = document.getElementById('current-page-size');
    const pageSizeOptions = document.querySelectorAll('.page-size-option');

    if (pageSizeToggle) {
        pageSizeToggle.addEventListener('click', (e) => {
            e.stopPropagation();
            pageSizeMenu.classList.toggle('show');
        });

        pageSizeOptions.forEach(option => {
            option.addEventListener('click', (e) => {
                pageSizeOptions.forEach(opt => opt.classList.remove('active'));
                option.classList.add('active');
                currentPageSizeSpan.textContent = option.textContent;
            });
        });
    }

    // Handle Settings Dropdown & Global Clicks
    const dropdown = document.getElementById('settings-dropdown');
    document.addEventListener('click', (e) => {
        const isIcon = e.target.classList.contains('settings-icon');
        const isInsideSettings = dropdown ? dropdown.contains(e.target) : false;
        const isInsidePageSize = pageSizeToggle ? pageSizeToggle.contains(e.target) : false;

        if (isIcon) {
            e.stopPropagation();
            const rect = e.target.getBoundingClientRect();
            const isVisible = dropdown.style.display === 'block';
            
            // Close other menu
            pageSizeMenu.classList.remove('show');

            if (isVisible) {
                dropdown.style.display = 'none';
            } else {
                dropdown.style.display = 'block';
                dropdown.style.top = `${rect.bottom + window.scrollY + 8}px`;
                dropdown.style.left = `${rect.right - 220 + window.scrollX}px`;
            }
        } else {
            if (!isInsideSettings && dropdown) dropdown.style.display = 'none';
            if (!isInsidePageSize && pageSizeMenu) pageSizeMenu.classList.remove('show');
        }
    });
});
