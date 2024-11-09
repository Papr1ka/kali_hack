<template>
  <section class="profile-container">
    <div class="profile-picture-container">
      <div class="profile-picture"></div>
      <div class="profile-badge"></div>
    </div>
    <nav class="profile-actions">
      <button class="delete-profile" data-layername="удалитьПрофиль">
        Удалить профиль
      </button>
      <div class="logout-container">
        <button class="logout-button" data-layername="выйти">Выйти</button>
        <img src="https://cdn.builder.io/api/v1/image/assets/TEMP/37543f64421be00d3f200a2120dc5fa659c1fcd067c7067ee6bef4bdaf7c4aa4?placeholderIfAbsent=true&apiKey=64bfb41e968348f18433c05ef76ae6c3" alt="Logout icon" class="logout-icon" />
      </div>
    </nav>
    <img src="https://cdn.builder.io/api/v1/image/assets/TEMP/58fa4ca33f6669f57e96e2cb5d1ac4c1fd30c80a7dcf113a9839d1087542f278?placeholderIfAbsent=true&apiKey=64bfb41e968348f18433c05ef76ae6c3" alt="Profile decoration" class="profile-decoration" />
  </section>
</template>

<style scoped>
.profile-container {
  position: relative;
  display: flex;
  max-width: 213px;
  flex-direction: column;
  font-family: 'Moscow Sans', sans-serif;
  font-weight: 300;
  align-items: flex-end;
}

.profile-picture-container {
  position: relative;
  align-self: center;
  margin-bottom: 24px;
}

.profile-picture {
  border-radius: 50%;
  min-height: 200px;
  width: 200px;
  border: 13px solid #000;
}

.profile-badge {
  border-radius: 50%;
  position: absolute;
  min-height: 68px;
  width: 68px;
  right: -4px;
  top: 41px;
  border: 13px solid #000;
}

.profile-actions {
  display: flex;
  width: 100%;
  flex-direction: column;
}

.delete-profile {
  width: 75%;
  font-size: 18px;
  color: #f00;
  background: none;
  border: none;
  cursor: pointer;
  text-align: left;
  padding: 0;
  margin-bottom: 16px;
  margin-left: auto;
}

.logout-container {
  border-radius: 15px;
  background-color: #f00;
  display: flex;
  width: 75%;
  align-items: center;
  justify-content: space-between;
  padding: 4px 8px;
  border: 2px solid #f00;
  margin-left: auto;
}

.logout-button {
  font-size: 24px;
  color: #fff;
  background: none;
  border: none;
  cursor: pointer;
}

.logout-icon {
  width: 25px;
  height: 28px;
  object-fit: contain;
}

.profile-decoration {
  position: absolute;
  width: 162px;
  height: 34px;
  right: 24px;
  top: 132px;
  object-fit: contain;
}
</style>