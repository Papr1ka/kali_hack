<template>
  <main class="auth-registration">
    <header class="auth-header">
      <h1 class="auth-title">AIHire — Ваш личный помощник в поиске работы</h1>
    </header>
    <div class="auth-divider"></div>
    <section class="auth-content">
      <LoginForm />
      <div class="auth-divider-vertical">
        <div class="divider-line"></div>
        <span class="divider-text">или</span>
        <div class="divider-line"></div>
      </div>
      <RegistrationForm />
    </section>
  </main>
</template>

<script>
import LoginForm from './LoginForm.vue';
import RegistrationForm from './RegistrationForm.vue';

export default {
  name: 'AuthRegistrationComponent',
  components: {
    LoginForm,
    RegistrationForm
  }
}
</script>

<style scoped>
.auth-registration {
  background-color: #fff;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  padding: 32px 80px 63px;
}

.auth-header {
  margin-bottom: 30px;
}

.auth-title {
  color: #000;
  text-align: center;
  font: 300 48px Moscow Sans, sans-serif;
}

.auth-divider {
  border-radius: 25px;
  background-color: #d9d9d9;
  height: 8px;
  margin-bottom: 64px;
}

.auth-content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 59px;
  flex-wrap: wrap;
}

.auth-divider-vertical {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: #000;
  font: 300 32px Moscow Sans, sans-serif;
}

.divider-line {
  border-radius: 25px;
  background-color: #d9d9d9;
  width: 16px;
  height: 264px;
}

.divider-text {
  margin: 105px 0;
}

@media (max-width: 991px) {
  .auth-registration {
    padding: 0 20px;
  }

  .auth-title {
    font-size: 40px;
  }

  .auth-content {
    margin-top: 40px;
  }

  .auth-divider-vertical {
    display: none;
  }
}
</style>