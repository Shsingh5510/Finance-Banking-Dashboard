const dashboardData = {
  metrics: [
    { label: 'Total Balance', value: '$128,460', delta: '+12.4%', trend: 'up', accent: 'blue' },
    { label: 'Monthly Income', value: '$42,800', delta: '+8.1%', trend: 'up', accent: 'green' },
    { label: 'Total Expenses', value: '$18,640', delta: '-3.2%', trend: 'down', accent: 'orange' },
    { label: 'Net Savings', value: '$24,160', delta: '+14.6%', trend: 'up', accent: 'purple' }
  ],
  chart: [
    { month: 'Jan', value: 28 },
    { month: 'Feb', value: 34 },
    { month: 'Mar', value: 30 },
    { month: 'Apr', value: 46 },
    { month: 'May', value: 52 },
    { month: 'Jun', value: 44 },
    { month: 'Jul', value: 59 },
    { month: 'Aug', value: 63 },
    { month: 'Sep', value: 58 },
    { month: 'Oct', value: 68 },
    { month: 'Nov', value: 71 },
    { month: 'Dec', value: 73 }
  ],
  allocations: [
    { label: 'Savings', value: 38, color: '#6EE7B7' },
    { label: 'Investments', value: 28, color: '#60A5FA' },
    { label: 'Payments', value: 22, color: '#A78BFA' },
    { label: 'Cash', value: 12, color: '#FBBF24' }
  ],
  transactions: [
    { name: 'Payroll', category: 'Income', amount: '+$8,200', date: 'Today', status: 'Completed' },
    { name: 'Rent & Utilities', category: 'Bills', amount: '-$2,140', date: 'Yesterday', status: 'Paid' },
    { name: 'Market Buy', category: 'Investment', amount: '-$1,450', date: 'Tue', status: 'Processing' },
    { name: 'Client Payment', category: 'Income', amount: '+$3,600', date: 'Mon', status: 'Completed' },
    { name: 'Groceries', category: 'Daily', amount: '-$420', date: 'Sun', status: 'Paid' }
  ]
};

function renderMetrics() {
  const container = document.getElementById('metrics');
  if (!container) return;

  container.innerHTML = dashboardData.metrics
    .map(
      (metric) => `
        <article class="metric-card ${metric.accent}">
          <div class="metric-header">
            <span>${metric.label}</span>
            <span class="metric-trend ${metric.trend}">${metric.delta}</span>
          </div>
          <h3>${metric.value}</h3>
        </article>
      `
    )
    .join('');
}

function renderTrendChart() {
  const chart = document.getElementById('trend-chart');
  if (!chart) return;

  const maxValue = Math.max(...dashboardData.chart.map((item) => item.value));

  chart.innerHTML = `
    <div class="chart-grid">
      ${dashboardData.chart
        .map(
          (item) => `
            <div class="bar-column">
              <div class="bar-wrap">
                <span class="bar" style="height: ${(item.value / maxValue) * 100}%"></span>
              </div>
              <small>${item.month}</small>
            </div>
          `
        )
        .join('')}
    </div>
  `;
}

function renderPortfolio() {
  const donut = document.getElementById('portfolio-donut');
  const list = document.getElementById('allocation-list');
  if (!donut || !list) return;

  const total = dashboardData.allocations.reduce((sum, item) => sum + item.value, 0);
  let current = 0;

  const gradient = dashboardData.allocations
    .map((item) => {
      const start = current;
      current += item.value;
      const end = current;
      return `${item.color} ${(start / total) * 100}% ${(end / total) * 100}%`;
    })
    .join(', ');

  donut.style.background = `conic-gradient(${gradient})`;

  list.innerHTML = dashboardData.allocations
    .map(
      (item) => `
        <div class="allocation-item">
          <div class="allocation-label">
            <span class="dot" style="background:${item.color}"></span>
            <span>${item.label}</span>
          </div>
          <strong>${item.value}%</strong>
        </div>
      `
    )
    .join('');
}

function renderTransactions() {
  const container = document.getElementById('transactions');
  if (!container) return;

  container.innerHTML = dashboardData.transactions
    .map(
      (transaction) => `
        <div class="transaction-row">
          <div class="transaction-info">
            <div class="avatar">${transaction.name.charAt(0)}</div>
            <div>
              <strong>${transaction.name}</strong>
              <small>${transaction.category}</small>
            </div>
          </div>
          <div class="transaction-meta">
            <span>${transaction.date}</span>
            <em>${transaction.status}</em>
          </div>
          <div class="transaction-amount ${transaction.amount.startsWith('+') ? 'credit' : 'debit'}">
            ${transaction.amount}
          </div>
        </div>
      `
    )
    .join('');
}

renderMetrics();
renderTrendChart();
renderPortfolio();
renderTransactions();
