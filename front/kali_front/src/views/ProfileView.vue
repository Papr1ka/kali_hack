<script>
import InputMask from 'primevue/inputmask'

export default {
  data() {
    return {
      phone: 89999999999,
    }
  },
  components: {
    InputMask,
  },
}
</script>

<template>
  <main class="profile">
    <div class="profile-container">
      <header class="top-nav">
        <nav class="nav-bar">
          <h1 class="nav-item active">Профиль</h1>
          <a href="#" class="nav-item">Подходящие вакансии</a>
          <a href="#" class="nav-item">Мои вакансии</a>
        </nav>
        <div class="logo">AIHire</div>
      </header>
      <section class="profile-content">
        <div class="edit-mode">
          <span class="edit-mode-text">Режим редактирования</span>
          <label class="switch">
            <input type="checkbox" />
            <span class="slider round"></span>
          </label>
        </div>
        <form class="profile-form">
          <div class="form-row">
            <div class="form-group">
              <label for="fullName" class="form-label">ФИО</label>
              <input
                type="text"
                id="fullName"
                class="form-input"
                value="Почтебайло Михаил Петрович"
              />
            </div>
            <div class="form-group">
              <label for="email" class="form-label">Электронная почта</label>
              <input type="email" id="email" class="form-input" value="example@example.com" />
            </div>
          </div>
          <div class="form-row">
            <div class="form-group">
              <label for="telegram" class="form-label">Ссылка в телеграм</label>
              <input type="text" id="telegram" class="form-input" value="@username" />
            </div>
            <div class="form-group">
              <!-- <label for="phone" class="form-label">Номер телефона</label>
              <input type="tel" id="phone" class="form-input" value="8 (ХХХ) ХХХ-ХХ-ХХ" /> -->
              <div class="card flex justify-center">
                <InputMask
                  v-model="phone"
                  mask="8 (999) 999-99-99"
                  placeholder="8 (999) 999-99-99"
                />
              </div>
            </div>
          </div>
        </form>
      </section>
      <aside class="profile-sidebar">
        <div class="profile-picture">
          <div class="profile-picture-inner"></div>
          <div class="profile-picture-badge"></div>
        </div>
        <div class="profile-actions">
          <button class="delete-profile">Удалить профиль</button>

          <button class="logout-button">
            Выйти
            <imgl
              src="https://cdn.builder.io/api/v1/image/assets/TEMP/37543f64421be00d3f200a2120dc5fa659c1fcd067c7067ee6bef4bdaf7c4aa4?placeholderIfAbsent=true&apiKey=64bfb41e968348f18433c05ef76ae6c3"
              alt="Logout icon"
              class="logout-icon"
            />
          </button>
        </div>
        <img
          src="https://cdn.builder.io/api/v1/image/assets/TEMP/58fa4ca33f6669f57e96e2cb5d1ac4c1fd30c80a7dcf113a9839d1087542f278?placeholderIfAbsent=true&apiKey=64bfb41e968348f18433c05ef76ae6c3"
          alt="Profile decoration"
          class="profile-decoration"
        />
      </aside>
      <section class="video-section">
        <h2 class="video-title">Видеовизитка</h2>
        <div class="video-placeholder"></div>
        <div class="video-overlay">
          <p class="video-description">Бла-бла-бла...</p>
          <button class="update-button">
            Обновить
            <img
              src="https://cdn.builder.io/api/v1/image/assets/TEMP/7f3c59662acfc675871af36c299fd3ef4a638c4edbd23a08ef311a00dee526f9?placeholderIfAbsent=true&apiKey=64bfb41e968348f18433c05ef76ae6c3"
              alt="Update icon"
              class="update-icon"
            />
          </button>
        </div>
      </section>
    </div>
  </main>
</template>

<style scoped>
.profile {
  background-color: #fff;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  align-items: flex-end;
  padding: 32px 80px 79px;
}

@media (max-width: 991px) {
  .profile {
    padding: 0 20px;
  }
}

.profile-container {
  z-index: 10;
  display: flex;
  width: 100%;
  max-width: 1232px;
  flex-direction: column;
}

@media (max-width: 991px) {
  .profile-container {
    max-width: 100%;
  }
}

.top-nav {
  display: flex;
  align-items: center;
  gap: 40px 97px;
  font-family:
    Moscow Sans,
    sans-serif;
  font-weight: 300;
  justify-content: flex-start;
  flex-wrap: wrap;
}

@media (max-width: 991px) {
  .top-nav {
    max-width: 100%;
  }
}

.nav-bar {
  align-self: stretch;
  display: flex;
  min-width: 240px;
  align-items: flex-start;
  gap: 40px 64px;
  font-size: 40px;
  color: #000;
  justify-content: center;
  flex-wrap: wrap;
  margin: auto 0;
}

@media (max-width: 991px) {
  .nav-bar {
    max-width: 100%;
  }
}

.nav-item {
  text-align: center;
  text-decoration: none;
  color: inherit;
}

.nav-item.active {
  font-weight: bold;
}

.logo {
  align-self: stretch;
  font-size: 48px;
  color: #5f5f5f;
  white-space: nowrap;
  text-align: center;
  width: 154px;
  margin: auto 0;
}

@media (max-width: 991px) {
  .logo {
    font-size: 40px;
    white-space: initial;
  }
}

.profile-content {
  z-index: 10;
  display: flex;
  margin-top: 54px;
  width: 864px;
  max-width: 100%;
  flex-direction: column;
}

@media (max-width: 991px) {
  .profile-content {
    margin-top: 40px;
  }
}

.edit-mode {
  align-self: flex-start;
  display: flex;
  align-items: center;
  gap: 27px;
  justify-content: flex-start;
}

@media (max-width: 991px) {
  .edit-mode {
    max-width: 100%;
  }
}

.edit-mode-text {
  color: #000;
  align-self: stretch;
  margin: auto 0;
  font:
    300 32px/1 Moscow Sans,
    sans-serif;
}

.switch {
  position: relative;
  display: inline-block;
  width: 75px;
  height: 38px;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #000;
  transition: 0.4s;
  border-radius: 19px;
}

.slider:before {
  position: absolute;
  content: '';
  height: 30px;
  width: 30px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  transition: 0.4s;
  border-radius: 50%;
}

input:checked + .slider {
  background-color: #000;
}

input:checked + .slider:before {
  transform: translateX(37px);
}

.profile-form {
  display: flex;
  margin-top: 35px;
  width: 100%;
  flex-direction: column;
  font-family: Geologica, sans-serif;
  font-weight: 700;
}

@media (max-width: 991px) {
  .profile-form {
    max-width: 100%;
  }
}

.form-row {
  display: flex;
  width: 100%;
  align-items: center;
  gap: 40px 160px;
  justify-content: flex-start;
  flex-wrap: wrap;
  margin-bottom: 64px;
}

@media (max-width: 991px) {
  .form-row {
    max-width: 100%;
    margin-bottom: 40px;
  }
}

.form-group {
  border-radius: 10px;
  align-self: stretch;
  display: flex;
  min-width: 240px;
  flex-direction: column;
  flex-grow: 1;
  width: 282px;
  margin: auto 0;
}

.form-label {
  color: rgba(0, 0, 0, 0.75);
  font-size: 24px;
  align-self: flex-start;
  margin-bottom: 8px;
}

.form-input {
  align-self: stretch;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.35);
  font-size: 20px;
  color: #000;
  padding: 10px;
  border: 3px solid rgba(0, 0, 0, 0.7);
  font-family: inherit;
  font-weight: inherit;
}

.profile-sidebar {
  align-self: flex-end;
  position: relative;
  display: flex;
  margin-top: -271px;
  width: 213px;
  max-width: 100%;
  flex-direction: column;
  font-family:
    Moscow Sans,
    sans-serif;
  font-weight: 300;
}

@media (max-width: 991px) {
  .profile-sidebar {
    margin: -200px 10px 0 0;
  }
}

.profile-picture {
  position: relative;
  width: 200px;
  height: 200px;
  margin: 0 auto;
}

.profile-picture-inner {
  border-radius: 50%;
  border: 13px solid #000;
  width: 100%;
  height: 100%;
}

.profile-picture-badge {
  border-radius: 50%;
  position: absolute;
  z-index: 1;
  width: 68px;
  height: 68px;
  right: 0;
  top: 41px;
  border: 13px solid #000;
}

.profile-actions {
  z-index: 0;
  display: flex;
  margin-top: 24px;
  width: 100%;
  flex-direction: column;
}

.delete-profile {
  width: 100%;
  font-size: 24px;
  color: #ff0000;
  background: none;
  border: none;
  cursor: pointer;
  text-align: left;
  padding: 0;
  margin-bottom: 16px;
}

.logout-button {
  border-radius: 15px;
  background-color: #ff0000;
  display: flex;
  width: 100%;
  align-items: center;
  gap: 40px;
  font-size: 32px;
  color: #fff;
  justify-content: space-between;
  padding: 4px 8px;
  border: 2px solid #ff0000;
  cursor: pointer;
}

.logout-icon {
  aspect-ratio: 1.09;
  object-fit: contain;
  width: 35px;
}

.profile-decoration {
  aspect-ratio: 4.76;
  object-fit: contain;
  width: 162px;
  position: absolute;
  z-index: 0;
  max-width: 100%;
  right: 24px;
  top: 132px;
}

.video-section {
  display: flex;
  margin-top: -11px;
  width: 100%;
  max-width: 1232px;
  flex-direction: column;
  color: #000;
}

@media (max-width: 991px) {
  .video-section {
    max-width: 100%;
  }
}

.video-title {
  font:
    700 32px Geologica,
    sans-serif;
  text-align: center;
  margin-bottom: 8px;
}

.video-placeholder {
  background-color: #d9d9d9;
  min-height: 432px;
  width: 768px;
  max-width: 100%;
}

@media (max-width: 991px) {
  .video-placeholder {
    max-width: 100%;
  }
}

.video-overlay {
  align-self: flex-end;
  z-index: 10;
  display: flex;
  margin-top: -432px;
  width: 440px;
  max-width: 100%;
  flex-direction: column;
  font:
    500 18px Geologica Cursive,
    sans-serif;
}

@media (max-width: 991px) {
  .video-overlay {
    margin-top: -200px;
  }
}

.video-description {
  background-color: #d9d9d9;
  padding: 180px 44px 144px;
}

@media (max-width: 991px) {
  .video-description {
    max-width: 100%;
    padding: 100px 20px 110px;
  }
}

.update-button {
  border-radius: 13px;
  background-color: #40f68c;
  align-self: center;
  display: flex;
  margin-top: 8px;
  width: 152px;
  max-width: 100%;
  gap: 11px;
  padding: 9px 14px;
  border: none;
  cursor: pointer;
  font: inherit;
}

.update-icon {
  aspect-ratio: 1;
  object-fit: contain;
  width: 23px;
}
</style>
