function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
  }
  
  function triggerInput(id) {
    document.getElementById(id).click();
  }
  
  function previewImage(input) {
    const file = input.files[0];
    const preview = document.getElementById('preview' + input.id.slice(-1));
    if (file) {
      const reader = new FileReader();
      reader.onload = () => {
        preview.src = reader.result;
        preview.style.display = 'block';
      };
      reader.readAsDataURL(file);
    }
  }
  
  // Retain dark mode setting
  window.onload = () => {
    if (localStorage.getItem('darkMode') === 'true') {
      document.body.classList.add('dark-mode');
    }
  };
  