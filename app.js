(() => {
  const cards = [...document.querySelectorAll('.card')];
  const input = document.querySelector('#search');
  const buttons = [...document.querySelectorAll('[data-filter]')];
  const pagers = [...document.querySelectorAll('.pagination')];
  const pageSize = 6;
  if (!input) return;
  let category = 'All';
  let currentPage = 1;
  function readUrl() {
    const params = new URLSearchParams(location.search);
    category = buttons.some(b => b.dataset.filter === params.get('category')) ? params.get('category') : 'All';
    input.value = params.get('q') || '';
    const requested = Number(params.get('page'));
    currentPage = Number.isInteger(requested) && requested > 0 ? requested : 1;
  }
  function pageUrl(number) {
    const next = new URL(location.href);
    for (const key of ['category', 'q', 'page']) next.searchParams.delete(key);
    if (category !== 'All') next.searchParams.set('category', category);
    if (input.value.trim()) next.searchParams.set('q', input.value.trim());
    if (number > 1) next.searchParams.set('page', number);
    next.hash = 'projects';
    return next.pathname + next.search + next.hash;
  }
  function render(updateUrl = true) {
    const words = input.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    const matches = cards.filter(card => (category === 'All' || card.dataset.category === category) && words.every(w => card.dataset.search.includes(w)));
    const totalPages = Math.max(1, Math.ceil(matches.length / pageSize));
    currentPage = Math.min(currentPage, totalPages);
    const start = (currentPage - 1) * pageSize;
    cards.forEach(card => { card.hidden = true; });
    matches.slice(start, start + pageSize).forEach(card => { card.hidden = false; });
    buttons.forEach(b => b.setAttribute('aria-pressed', String(b.dataset.filter === category)));
    document.querySelector('#count').textContent = matches.length ? `Showing ${start + 1}–${Math.min(start + pageSize, matches.length)} of ${matches.length} projects` : 'No matching projects';
    document.querySelector('#empty').hidden = matches.length > 0;
    for (const pager of pagers) {
      pager.replaceChildren();
      pager.hidden = totalPages <= 1;
      if (pager.hidden) continue;
      function add(label, number, disabled = false) {
        const item = document.createElement(disabled ? 'span' : 'a');
        item.textContent = label;
        if (disabled) item.className = 'page-disabled';
        else {
          item.href = pageUrl(number);
          item.dataset.page = number;
          if (number === currentPage && /^\d+$/.test(label)) item.setAttribute('aria-current', 'page');
        }
        pager.append(item);
      }
      add('Previous', currentPage - 1, currentPage === 1);
      for (let n = 1; n <= totalPages; n++) add(String(n), n);
      add('Next', currentPage + 1, currentPage === totalPages);
    }
    if (updateUrl) history.replaceState(null, '', pageUrl(currentPage));
  }
  pagers.forEach(pager => pager.addEventListener('click', event => {
    const link = event.target.closest('a[data-page]');
    if (!link || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    currentPage = Number(link.dataset.page);
    history.pushState(null, '', pageUrl(currentPage));
    render(false);
    document.querySelector('#projects').scrollIntoView();
    pagers[0].querySelector('[aria-current="page"]')?.focus({preventScroll: true});
  }));
  buttons.forEach(b => b.addEventListener('click', () => { category = b.dataset.filter; currentPage = 1; render(); }));
  input.addEventListener('input', () => { currentPage = 1; render(); });
  document.querySelector('#reset').addEventListener('click', () => { category = 'All'; input.value = ''; currentPage = 1; render(); input.focus(); });
  window.addEventListener('popstate', () => { readUrl(); render(false); });
  readUrl();
  render(false);
})();
