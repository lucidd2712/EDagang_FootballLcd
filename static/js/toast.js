// toast.js
(function () {
  const el = document.getElementById('toast-component');
  const titleEl = document.getElementById('toast-title');
  const msgEl = document.getElementById('toast-message');
  const iconEl = document.getElementById('toast-icon');

  const TYPE_STYLE = {
    success: { cls: ['bg-green-50','border-green-500','text-green-700'], icon: '✅' },
    error:   { cls: ['bg-red-50','border-red-500','text-red-700'],       icon: '⚠️' },
    normal:  { cls: ['bg-white','border-gray-200','text-gray-800'],      icon: '🔔' },
    info:    { cls: ['bg-blue-50','border-blue-500','text-blue-700'],    icon: 'ℹ️' },
  };

  function resetClass() {
    el.classList.remove(
      'bg-green-50','border-green-500','text-green-700',
      'bg-red-50','border-red-500','text-red-700',
      'bg-white','border-gray-200','text-gray-800',
      'bg-blue-50','border-blue-500','text-blue-700',
      'opacity-100','translate-y-0'
    );
  }

  window.showToast = function showToast(title, message, type = 'normal', duration = 2800) {
    if (!el) return;
    const cfg = TYPE_STYLE[type] || TYPE_STYLE.normal;

    resetClass();
    el.classList.add(...cfg.cls);
    iconEl.textContent = cfg.icon;
    titleEl.textContent = title || '';
    msgEl.textContent = message || '';

    // show
    el.classList.remove('opacity-0','translate-y-8');
    el.classList.add('opacity-100','translate-y-0');

    clearTimeout(el._hideTimer);
    el._hideTimer = setTimeout(() => {
      el.classList.remove('opacity-100','translate-y-0');
      el.classList.add('opacity-0','translate-y-8');
    }, duration);
  };
})();
