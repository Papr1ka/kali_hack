<template>
  <form class="login-form">
    <h2 class="form-title">Войдите</h2>
    <div class="form-fields">
      <div class="form-group">
        <label for="email" class="form-label">Электронная почта</label>
        <div class="input-wrapper">
          <img src="https://cdn.builder.io/api/v1/image/assets/TEMP/eaba40305d6860b1729f82298e5fdb002aa29443f820bf374291c77ae3f7361c?placeholderIfAbsent=true&apiKey=64bfb41e968348f18433c05ef76ae6c3" alt="" class="input-icon" />
          <input type="email" id="email" class="form-input" placeholder="example@gmail.com" />
        </div>
      </div>
      <div class="form-group">
        <label for="password" class="form-label">Пароль</label>
        <div class="input-wrapper">
          <img src="https://cdn.builder.io/api/v1/image/assets/TEMP/60e075e76f270028dc05d0ff65f86d88abf6d6a9b3872d50007ef7730669e732?placeholderIfAbsent=true&apiKey=64bfb41e968348f18433c05ef76ae6c3" alt="" class="input-icon" />
          <input type="password" id="password" class="form-input" placeholder="Введите пароль" />
          <img src="https://cdn.builder.io/api/v1/image/assets/TEMP/3312f593b34da5796593b36b146efd9c2129c11130a24d5abfbd72f6dffc0d90?placeholderIfAbsent=true&apiKey=64bfb41e968348f18433c05ef76ae6c3" alt="Toggle password visibility" class="toggle-password" />
        </div>
      </div>
    </div>
    <button type="submit" class="submit-button">Вход</button>
  </form>
</template>

<script>
export default {
  name: 'LoginForm'
}
</script>

<style scoped>
.login-form {
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
  margin-bottom: 18px;
}

.form-label {
  color: rgba(0, 0, 0, 0.75);
  font-size: 16px;
  display: block;
  margin-bottom: 8px;
}

.input-wrapper {
  display: flex;
  align-items: center;
  border-radius: 10px;
  border: 3px solid #000;
  padding: 14px 10px;
  background-color: rgba(255, 255, 255, 0.08);
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
  height: 25px;
  cursor: pointer;
}

.submit-button {
  display: block;
  width: 312px;
  max-width: 100%;
  margin: 109px auto 0;
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

@media (max-width: 991px) {
  .form-title {
    font-size: 40px;
    margin-bottom: 40px;
  }

  .submit-button {
    margin-top: 40px;
  }
}
</style>