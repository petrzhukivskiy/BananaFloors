(function () {
  'use strict';
  var key = 'banana-floors-theme';
  var root = document.documentElement;
  var media = window.matchMedia('(prefers-color-scheme: dark)');
  var preference = null;
  try {
    var saved = localStorage.getItem(key);
    if (saved === 'light' || saved === 'dark') preference = saved;
  } catch (error) { /* The toggle also works when browser storage is unavailable. */ }

  function apply(theme) {
    root.dataset.theme = theme;
    root.style.colorScheme = theme;
    var dark = theme === 'dark';
    document.querySelectorAll('[data-theme-toggle]').forEach(function (button) {
      button.hidden = false;
      button.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
      button.title = button.getAttribute('aria-label');
      button.querySelector('[data-theme-label]').textContent = dark ? 'Light' : 'Dark';
    });
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.content = dark ? '#141516' : '#ffd84d';
  }

  // Runs in the head, before the page paints, to avoid a bright flash.
  apply(preference || (media.matches ? 'dark' : 'light'));
  function initialize() {
    apply(root.dataset.theme);
    document.querySelectorAll('[data-theme-toggle]').forEach(function (button) {
      button.addEventListener('click', function () {
        preference = root.dataset.theme === 'dark' ? 'light' : 'dark';
        apply(preference);
        try { localStorage.setItem(key, preference); } catch (error) { /* Session still works. */ }
      });
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initialize);
  else initialize();
  function followSystem() { if (!preference) apply(media.matches ? 'dark' : 'light'); }
  if (media.addEventListener) media.addEventListener('change', followSystem);
  else if (media.addListener) media.addListener(followSystem);
  window.addEventListener('storage', function (event) {
    if (event.key !== key && event.key !== null) return;
    preference = event.newValue === 'dark' || event.newValue === 'light' ? event.newValue : null;
    apply(preference || (media.matches ? 'dark' : 'light'));
  });
}());
