<template>
  <form class="registration-form">
    <h2 class="form-title">Создайте резюме</h2>
    <div class="form-fields">
      <div class="form-group">
        <label for="fullName" class="visually-hidden">ФИО</label>
        <div class="input-wrapper">
          <img src="https://cdn.builder.io/api/v1/image/assets/TEMP/b8ba0bb14f3cd82af4912565db82addcd615a6bcd94f35416be15cec153e3e15?placeholderIfAbsent=true&apiKey=64bfb41e968348f18433c05ef76ae6c3" alt="" class="input-icon" />
          <input type="text" id="fullName" class="form-input" placeholder="ФИО" />
        </div>
      </div>
      <div class="form-group">
        <label for="email" class="visually-hidden">Электронная почта</label>
        <div class="input-wrapper">
          <img src="https://cdn.builder.io/api/v1/image/assets/TEMP/80c8d248f5566ee96190feacc2ab74277ec31c0ad9ce8ea6ad3cc629420ba882?placeholderIfAbsent=true&apiKey=64bfb41e968348f18433c05ef76ae6c3" alt="" class="input-icon" />
          <input type="email" id="email" class="form-input" placeholder="Электронная почта" />
        </div>
      </div>
      <div class="form-group">
        <label for="password" class="visually-hidden">Пароль</label>
        <div class="input-wrapper">
          <img src="https://cdn.builder.io/api/v1/image/assets/TEMP/4a0760265b0c49c1468ebb962a69b9fdac4fb5c556e907402e1507f16854645a?placeholderIfAbsent=true&apiKey=64bfb41e968348f18433c05ef76ae6c3" alt="" class="input-icon" />
          <input type="password" id="password" class="form-input" placeholder="Пароль" />
          <img src="https://cdn.builder.io/api/v1/image/assets/TEMP/73dc9514b76ef24af6eb9b95e8bec4f6ca3d148a46120887462544cc39cb76c8?placeholderIfAbsent=true&apiKey=64bfb41e968348f18433c05ef76ae6c3" alt="Toggle password visibility" class="toggle-password" />
        </div>
      </div>
    </div>
    <div class="video-upload">
      <h3 class="video-title">Видеовизитка</h3>
      <button type="button" class="upload-button">
        Загрузить
        <img src="https://cdn.builder.io/api/v1/image/assets/TEMP/ce3beafbf04c46a49a794f50a77868f0cae1b6f7394ec163384b88f247017320?placeholderIfAbsent=true&apiKey=64bfb41e968348f18433c05ef76ae6c3" alt="" class="upload-icon" />
      </button>
    </div>
    <button type="submit" class="submit-button">Зарегистрироваться</button>
  </form>
</template>

<script>
export default {
  name: 'RegistrationForm'
}
</script>

<style scoped>
.registration-form {
  width: 470px;
  max-width: 100%;
}

.form-title {
  color: #000;
  text-align: center;
  font: 300 48px Moscow Sans, sans-serif;
  margin-bottom: 80px;
}

.form-fields {
  font-family: Geologica Cursive, sans-serif;
}

.form-group {
  margin-bottom: 42px;
}

.input-wrapper {
  display: flex;
  align-items: center;
  padding: 12px 9px;
}

.input-icon {
  width: 24px;
  height: 24px;
  margin-right: 15px;
}

.form-input {
  flex-grow: 1;
  border: none;
  background: transparent;
  font-size: 20px;
  color: rgba(0, 0, 0, 0.7);
}

.toggle-password {
  width: 36px;
  height: 24px;
  cursor: pointer;
}

.video-upload {
  text-align: center;
  margin-top: 42px;
  margin-bottom: 32px;
}

.video-title {
  font-size: 20px;
  font-weight: 400;
  margin-bottom: 13px;
}

.upload-button {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
  padding: 8px 12px;
  border: none;
  border-radius: 11px;
  background-color: #40f68c;
  font-size: 15px;
  font-weight: 500;
  cursor: pointer;
}

.upload-icon {
  width: 19px;
  height: 19px;
  margin-left: 12px;
}

.submit-button {
  display: block;
  width: 312px;
  max-width: 100%;
  margin: 0 auto;
  padding: 12px 31px;
  border: none;
  border-radius: 10px;
  background: linear-gradient(90deg, #43e97b 0.19%, #38f9d7 99.84%);
  color: #000;
  font-size: 20px;
  font-weight: 600;
  text-align: center;
  cursor: pointer;
}

.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

@media (max-width: 991px) {
  .form-title {
    font-size: 40px;
    margin-bottom: 40px;
  }

  .form-group {
    margin-bottom: 40px;
  }

  .video-upload {
    margin-top: 40px;
  }
}
</style>