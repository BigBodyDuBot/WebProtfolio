(() => {
  const cards = [...document.querySelectorAll('.card')];
  const input = document.querySelector('#search');
  const buttons = [...document.querySelectorAll('[data-filter]')];
  if (!input) return;
  const params = new URLSearchParams(location.search);
  let category = buttons.some(b => b.dataset.filter === params.get('category')) ? params.get('category') : 'All';
  input.value = params.get('q') || '';
  function filter(updateUrl = true) {
    const words = input.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    let count = 0;
    for (const card of cards) {
      const matches = (category === 'All' || card.dataset.category === category) && words.every(w => card.dataset.search.includes(w));
      card.hidden = !matches;
      count += Number(matches);
    }
    buttons.forEach(b => b.setAttribute('aria-pressed', String(b.dataset.filter === category)));
    document.querySelector('#count').textContent = `${count} of ${cards.length} projects`;
    document.querySelector('#empty').hidden = count > 0;
    if (updateUrl) {
      const next = new URL(location.href);
      next.searchParams.delete('category'); next.searchParams.delete('q');
      if (category !== 'All') next.searchParams.set('category', category);
      if (input.value.trim()) next.searchParams.set('q', input.value.trim());
      history.replaceState(null, '', next);
    }
  }
  buttons.forEach(b => b.addEventListener('click', () => { category = b.dataset.filter; filter(); }));
  input.addEventListener('input', () => filter());
  document.querySelector('#reset').addEventListener('click', () => { category = 'All'; input.value = ''; filter(); input.focus(); });
  filter(false);
})();
