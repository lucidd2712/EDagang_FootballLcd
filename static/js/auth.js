function getCookie(name){
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return decodeURIComponent(parts.pop().split(';').shift());
  return null;
}
const CSRF = getCookie('csrftoken');

async function ajaxPost(url, form) {
  const res = await fetch(url, { method:'POST', headers:{ 'X-CSRFToken': CSRF }, body: new FormData(form) });
  const data = await res.json().catch(()=>({}));
  return {ok: res.ok, data};
}

document.addEventListener('DOMContentLoaded', ()=>{
  const loginForm = document.querySelector('form[action=""]#login-form') || document.querySelector('form[action=""]');
  if (loginForm && document.title.includes('Login')) {
    loginForm.addEventListener('submit', async (e)=>{
      e.preventDefault();
      const {ok, data} = await ajaxPost('/api/auth/login/', loginForm);
      if (ok) {
        showToast('Welcome back', data.username || '', 'success');
        // redirect tanpa reload penuh halaman utama? tetap redirect normal:
        window.location.href = '/';
      } else {
        showToast('Login failed', data.message || 'Invalid credentials', 'error', 3500);
      }
    });
  }

  const registerForm = document.querySelector('form[action=""]');
  if (registerForm && document.title.includes('Register')) {
    registerForm.addEventListener('submit', async (e)=>{
      e.preventDefault();
      const {ok, data} = await ajaxPost('/api/auth/register/', registerForm);
      if (ok) {
        showToast('Account created', data.username || '', 'success');
        window.location.href = '/login/';
      } else {
        const err = data.errors ? JSON.stringify(data.errors) : (data.message || 'Registration failed');
        showToast('Register failed', err, 'error', 4000);
      }
    });
  }

  const logoutLink = document.querySelector('a[href="/logout/"]');
  if (logoutLink) {
    logoutLink.addEventListener('click', async (e)=>{
      e.preventDefault();
      const res = await fetch('/api/auth/logout/', {method:'POST', headers:{'X-CSRFToken': CSRF}});
      if (res.ok) {
        showToast('Logged out','See you!', 'success');
        window.location.href = '/login/';
      } else {
        showToast('Error','Failed to logout','error');
      }
    });
  }
});
