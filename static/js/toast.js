function showToast(title, message, type = 'normal', duration = 2500) {
  const el = document.getElementById('toast-component');
  const t = document.getElementById('toast-title');
  const m = document.getElementById('toast-message');
  if (!el) return;

  el.classList.remove('bg-green-50','border-green-500','text-green-700',
                      'bg-red-50','border-red-500','text-red-700',
                      'bg-white','border-gray-200','text-gray-800');

  if (type === 'success') {
    el.classList.add('bg-green-50','border-green-500','text-green-700');
    el.style.borderColor = '#22c55e';
  } else if (type === 'error') {
    el.classList.add('bg-red-50','border-red-500','text-red-700');
    el.style.borderColor = '#ef4444';
  } else {
    el.classList.add('bg-white','border-gray-200','text-gray-800');
    el.style.borderColor = '#e5e7eb';
  }

  t.textContent = title || '';
  m.textContent = message || '';

  el.classList.remove('opacity-0','translate-y-8');
  el.classList.add('opacity-100','translate-y-0');

  clearTimeout(el._hideTimer);
  el._hideTimer = setTimeout(() => {
    el.classList.remove('opacity-100','translate-y-0');
    el.classList.add('opacity-0','translate-y-8');
  }, duration);
}
